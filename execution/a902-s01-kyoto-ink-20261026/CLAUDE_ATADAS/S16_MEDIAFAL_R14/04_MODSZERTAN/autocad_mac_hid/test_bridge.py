import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest

spec = importlib.util.spec_from_file_location('bridge', Path(__file__).with_name('server.py'))
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.original_root = bridge.ROOT
        bridge.ROOT = Path(self.temp.name)
        self.drawing = '/drawings/test.dwg'
        (bridge.ROOT / 'session.txt').write_text('session-1\n' + self.drawing + '\n26.0\n')

    def tearDown(self):
        bridge.ROOT = self.original_root
        self.temp.cleanup()

    def test_wrong_drawing_never_submitted(self):
        with self.assertRaisesRegex(RuntimeError, 'differs'):
            bridge.evaluate('(entdel (entlast))', '/wrong.dwg')
        self.assertFalse((bridge.ROOT / 'request.txt').exists())

    def test_stale_connection_rejected(self):
        os.utime(bridge.ROOT / 'session.txt', (1, 1))
        with self.assertRaisesRegex(RuntimeError, 'disconnected'):
            bridge.evaluate('(+ 1 2)', self.drawing)

    def test_unknown_previous_request_never_replayed(self):
        (bridge.ROOT / 'running.txt').write_text('earlier request')
        with self.assertRaisesRegex(RuntimeError, 'unknown outcome'):
            bridge.evaluate('(+ 1 2)', self.drawing)

    def test_reply_correlation_and_unicode(self):
        def adapter():
            p = bridge.ROOT / 'request.txt'
            deadline = time.monotonic() + 3
            while not p.exists() and time.monotonic() < deadline:
                time.sleep(.01)
            request_id = p.read_text().split('"')[1]
            p.rename(bridge.ROOT / 'running.txt')
            bridge.atomic_write(bridge.ROOT / 'result.txt', request_id + '\nok\n"árvíztűrő"\n')
            (bridge.ROOT / 'running.txt').unlink()
        worker = threading.Thread(target=adapter)
        worker.start()
        value = bridge.evaluate('(strcat "árvíz" "tűrő")', self.drawing, mutation=False)
        worker.join()
        self.assertTrue(value['ok'])
        self.assertEqual(value['autolisp_result'], '"árvíztűrő"')

    def test_timeout_removes_only_unclaimed_request(self):
        with self.assertRaises(TimeoutError):
            bridge.evaluate('(+ 1 2)', self.drawing, timeout=1)
        self.assertFalse((bridge.ROOT / 'request.txt').exists())

    def test_mcp_handshake_and_errors(self):
        messages = [
            {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2025-06-18'}},
            {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
            {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
            {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'invalid', 'arguments': {}}}
        ]
        run = subprocess.run([sys.executable, str(Path(__file__).with_name('server.py'))],
                             input='\n'.join(map(json.dumps, messages)) + '\n', text=True, capture_output=True, check=True)
        replies = [json.loads(x) for x in run.stdout.splitlines()]
        self.assertEqual(len(replies), 3)
        self.assertEqual(replies[0]['result']['protocolVersion'], '2025-06-18')
        self.assertEqual(len(replies[1]['result']['tools']), 4)
        self.assertTrue(replies[2]['result']['isError'])


if __name__ == '__main__':
    unittest.main()
