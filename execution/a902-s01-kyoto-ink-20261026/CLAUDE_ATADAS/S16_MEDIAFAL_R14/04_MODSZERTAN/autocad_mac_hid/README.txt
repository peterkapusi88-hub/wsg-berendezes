Local AutoCAD for Mac bridge — 2026-10-28

Installed location:
/Users/peterkapusi/Library/Application Support/ChatGPTAutoCAD

MCP server name: autocad-mac
Configuration registered using the ChatGPT/Codex CLI. Desktop clients sharing
the same local host use this configuration. Refresh/restart the MCP connection
if its tools do not appear in an existing chat.

CONNECT (in the AutoCAD command line):
(load "/Users/peterkapusi/Library/Application Support/ChatGPTAutoCAD/bridge.lsp")
CHATGPT

Accept the file-loading prompt for this exact local file if AutoCAD requests it.
This installation does not turn off secure loading or alter trusted paths.

DISCONNECT:
Press Esc in AutoCAD, or call autocad_disconnect from the assistant.
Run CHATGPT again to reconnect. Load bridge.lsp in each new drawing/session.

DESIGN AND LIMITS:
This is an AutoLISP command-line session, not a background ObjectARX plugin.
While connected, AutoCAD's command line is reserved for the bridge. Disconnect
for manual drawing work. Commands execute inside AutoCAD, without screenshots,
mouse clicks, external model APIs, or cloud licensing. Idle polling uses local
DELAY calls, not AI calls or tokens.

The private installation directory holds session and request/result files.
MCP requests are serialized with a local file lock. A new session rejects stale
requests; each request checks the full active drawing path. Never retry an
unknown or timed-out operation without inspecting the actual drawing.
Mutating calls use an AutoCAD UNDO group. An error can leave partial edits;
there is no automatic rollback, and Undo does not undo file writes or saves.
Do not use interactive prompts or change/close documents from eval calls.
autocad_eval_lisp is a powerful code-execution tool: use only for authorized work.

VALIDATION:
Six automated Python tests cover MCP initialization/tool discovery, Unicode
responses, target drawing checks, stale connections, in-flight requests,
and timeout handling. AutoLISP structure checked for balanced parentheses.
These tests do not replace the live AutoCAD connection check.

RECOVERY AFTER AN AUTOCAD CRASH:
Do not replay an uncertain operation. Inspect the drawing first. Once AutoCAD
has stopped running the bridge, stale session/request/running files may need
to be archived before reconnecting. Keep result.txt as evidence of completion.

UNINSTALL:
Disconnect in AutoCAD. Remove the autocad-mac MCP entry using the MCP settings
or `codex mcp remove autocad-mac`. Delete the dedicated ChatGPTAutoCAD folder
only after confirming that the connection is no longer running.
