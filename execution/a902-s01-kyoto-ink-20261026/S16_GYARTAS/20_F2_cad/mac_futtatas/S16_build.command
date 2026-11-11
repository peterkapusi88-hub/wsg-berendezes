#!/bin/bash
# S16 R15 – teljes felépítés AutoCAD parancssori motorral (AcCoreConsole), háttérben, képernyő nélkül.
# Használat: a ~/CAD/S16_R15 mappába másolva Finderből megnyitni. Billentyűzet-bemenet nélkül, 900 s időkorláttal.
D="$HOME/CAD/S16_R15"; LOG="$D/futtatas_build.log"; T=900
cd "$D" || exit 1
mkdir -p "$D/readback"
BIN="/Applications/Autodesk/AutoCAD 2027/AutoCAD 2027.app/Contents/Helpers/AcCoreConsole.app/Contents/MacOS/AcCoreConsole"
{
  echo "== $(date)"
  "$BIN" -s "$D/S16_R15_build.scr" -isolate s16r15build /private/tmp/s16r15build < /dev/null &
  PID=$!
  ( sleep $T; if kill -0 $PID 2>/dev/null; then echo "== IDOTULLEPES ($T s) - leallitas"; kill $PID; fi ) &
  W=$!
  wait $PID; RC=$?
  kill $W 2>/dev/null
  echo "== kilepesi kod: $RC"
  ls -la "$D/readback" "$D"/*.dwg 2>&1
} > "$LOG" 2>&1
echo "KESZ - naplo: $LOG"
