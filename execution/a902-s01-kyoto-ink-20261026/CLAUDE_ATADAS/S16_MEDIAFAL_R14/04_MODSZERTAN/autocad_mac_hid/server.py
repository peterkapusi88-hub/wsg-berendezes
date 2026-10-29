#!/usr/bin/env python3
"""Local, dependency-free MCP stdio client for the AutoLISP bridge."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parent


def atomic_write(path, text):
    temp = path.with_name(path.name + '.tmp-python')
    with open(temp, 'w', encoding='utf-8') as f:
        os.chmod(temp, 0o600)
        f.write(text)
    os.replace(temp, path)


def lisp_string(text):
    if '\x00' in text:
        raise ValueError('NUL is not allowed')
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"').replace('\r', '\\r').replace('\n', '\\n').replace('\t', '\\t') + '"'


def status():
    try:
        p = ROOT / 'session.txt'
        lines = p.read_text(encoding='utf-8').splitlines()
        age = max(0, time.time() - p.stat().st_mtime)
        if len(lines) < 3:
            raise ValueError('Incomplete session file')
        return {'connected': age < 8, 'session': lines[0], 'drawing': lines[1],
                'autocad_version': lines[2], 'heartbeat_age_seconds': round(age, 2),
                'busy': (ROOT / 'running.txt').exists()}
    except (OSError, ValueError):
        return {'connected': False, 'hint': 'In AutoCAD load bridge.lsp and run CHATGPT.'}


def evaluate(code, drawing, mutation=True, timeout=30):
    if not isinstance(code, str) or not code.strip() or len(code) > 100000:
        raise ValueError('Supply a nonempty AutoLISP expression, at most 100000 characters')
    if not isinstance(drawing, str) or not drawing:
        raise ValueError('expected_drawing is required; obtain its exact value from status')
    with open(ROOT / 'request.lock', 'a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        current = status()
        if not current['connected']:
            raise RuntimeError('AutoCAD is disconnected. Run CHATGPT in AutoCAD.')
        if current['drawing'] != drawing:
            raise RuntimeError('Active drawing differs from expected_drawing; nothing submitted')
        if (ROOT / 'running.txt').exists() or (ROOT / 'request.txt').exists():
            raise RuntimeError('An earlier request is pending or has unknown outcome. Do not retry it.')
        request_id = uuid.uuid4().hex
        request = [request_id, current['session'], drawing, 'write' if mutation else 'read', code]
        atomic_write(ROOT / 'request.txt', '(' + ' '.join(map(lisp_string, request)) + ')\n')
        deadline = time.monotonic() + min(max(timeout, 1), 120)
        while time.monotonic() < deadline:
            try:
                lines = (ROOT / 'result.txt').read_text(encoding='utf-8').splitlines()
                if len(lines) >= 3 and lines[0] == request_id:
                    return {'ok': lines[1] == 'ok', 'request_id': request_id,
                            'drawing': drawing, 'autolisp_result': '\n'.join(lines[2:])}
            except OSError:
                pass
            time.sleep(.05)
        # Withdraw only requests which have not been claimed; never replay a timeout.
        queued = ROOT / 'request.txt'
        try:
            if request_id in queued.read_text(encoding='utf-8'):
                queued.unlink()
        except FileNotFoundError:
            pass
        raise TimeoutError('No completion received; execution outcome may be unknown. Do not retry automatically. Inspect status and drawing first.')


INFO = '(list (cons "drawing" (strcat (getvar "DWGPREFIX") (getvar "DWGNAME"))) (cons "units" (getvar "INSUNITS")) (cons "tilemode" (getvar "TILEMODE")) (cons "current_layer" (getvar "CLAYER")) (cons "modified" (getvar "DBMOD")))'
TOOLS = [
    {'name': 'autocad_status', 'description': 'Check the local AutoCAD connection and exact active drawing path. Always call before editing.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False},
     'annotations': {'readOnlyHint': True, 'openWorldHint': False}},
    {'name': 'autocad_drawing_info', 'description': 'Read drawing name, units, current layer and modification state without editing.',
     'inputSchema': {'type': 'object', 'properties': {'expected_drawing': {'type': 'string'}}, 'required': ['expected_drawing'], 'additionalProperties': False},
     'annotations': {'readOnlyHint': True, 'openWorldHint': False}},
    {'name': 'autocad_eval_lisp', 'description': 'Execute one complete AutoLISP expression directly in the active Mac AutoCAD drawing. Batch work with progn; return concise values. No COM/ActiveX on Mac. Use command-s for complete noninteractive commands. May modify drawings and files. Never save, erase or overwrite unless authorized. Mutations form one undo group; errors can leave partial edits. Do not change documents or run interactive input. Never retry an unknown outcome automatically.',
     'inputSchema': {'type': 'object', 'properties': {'code': {'type': 'string'}, 'expected_drawing': {'type': 'string'}, 'timeout_seconds': {'type': 'number', 'minimum': 1, 'maximum': 120}}, 'required': ['code', 'expected_drawing'], 'additionalProperties': False},
     'annotations': {'readOnlyHint': False, 'destructiveHint': True, 'idempotentHint': False, 'openWorldHint': False}},
    {'name': 'autocad_disconnect', 'description': 'Release AutoCAD command line for manual work. Reconnect by running CHATGPT in AutoCAD.',
     'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False},
     'annotations': {'readOnlyHint': False, 'destructiveHint': False, 'openWorldHint': False}}
]


def call_tool(name, args):
    if name == 'autocad_status':
        return status()
    if name == 'autocad_drawing_info':
        return evaluate(INFO, args['expected_drawing'], mutation=False)
    if name == 'autocad_eval_lisp':
        return evaluate(args['code'], args['expected_drawing'], timeout=args.get('timeout_seconds', 30))
    if name == 'autocad_disconnect':
        atomic_write(ROOT / 'stop.txt', 'stop\n')
        return {'stop_requested': True}
    raise ValueError('Unknown tool: ' + name)


def serve():
    for raw in sys.stdin:
        msg = None
        try:
            msg = json.loads(raw)
            if not isinstance(msg, dict):
                raise ValueError('Expected JSON object')
            method = msg.get('method')
            if 'id' not in msg:
                continue
            if method == 'initialize':
                result = {'protocolVersion': msg.get('params', {}).get('protocolVersion', '2024-11-05'),
                          'capabilities': {'tools': {}}, 'serverInfo': {'name': 'local-autocad-mac', 'version': '1.0.0'},
                          'instructions': 'Local AutoCAD for Mac bridge. Check autocad_status first. Only operate on the user-authorized drawing; pass its exact path. Do not modify or save without task authorization. Batch AutoLISP calls for efficiency. Esc or autocad_disconnect releases manual control. Timeouts must never be replayed automatically.'}
            elif method == 'ping':
                result = {}
            elif method == 'tools/list':
                result = {'tools': TOOLS}
            elif method == 'tools/call':
                try:
                    params = msg['params']
                    value = call_tool(params['name'], params.get('arguments', {}))
                    result = {'content': [{'type': 'text', 'text': json.dumps(value, ensure_ascii=False)}], 'isError': value.get('ok') is False}
                except Exception as error:
                    result = {'content': [{'type': 'text', 'text': str(error)}], 'isError': True}
            else:
                print(json.dumps({'jsonrpc': '2.0', 'id': msg['id'], 'error': {'code': -32601, 'message': 'Method not found'}}), flush=True)
                continue
            print(json.dumps({'jsonrpc': '2.0', 'id': msg['id'], 'result': result}, ensure_ascii=False), flush=True)
        except Exception as error:
            print(json.dumps({'jsonrpc': '2.0', 'id': msg.get('id') if isinstance(msg, dict) else None,
                              'error': {'code': -32600, 'message': str(error)}}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--status', action='store_true')
    parser.add_argument('--info', action='store_true')
    options = parser.parse_args()
    if options.status:
        print(json.dumps(status(), ensure_ascii=False))
    elif options.info:
        print(json.dumps(evaluate(INFO, status().get('drawing'), mutation=False), ensure_ascii=False))
    else:
        serve()
