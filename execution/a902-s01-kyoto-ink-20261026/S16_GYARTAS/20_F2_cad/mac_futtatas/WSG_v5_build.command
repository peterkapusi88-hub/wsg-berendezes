#!/bin/bash
# WSG A-902 – S16 (R15B) és R16 (J) v5 DWG felépítése egymás után, AcCoreConsole-lal, időkorláttal.
BIN="/Applications/Autodesk/AutoCAD 2027/AutoCAD 2027.app/Contents/Helpers/AcCoreConsole.app/Contents/MacOS/AcCoreConsole"
run() {  # $1 mappa  $2 scr  $3 readback  $4 kulcs
  D="$HOME/CAD/$1"; LOG="$D/futtatas_$4.log"; T=1800
  mkdir -p "$D/$3"; cd "$D" || return
  {
    echo "== $(date)"
    "$BIN" -s "$D/$2" -isolate "$4" "/private/tmp/$4" < /dev/null &
    PID=$!
    ( sleep $T; if kill -0 $PID 2>/dev/null; then echo "== IDOTULLEPES ($T s)"; kill $PID; fi ) &
    W=$!
    wait $PID; RC=$?
    kill $W 2>/dev/null
    echo "== kilepesi kod: $RC"; echo "== readback: $(ls "$D/$3" | wc -l)"
    ls -la "$D"/*.dwg 2>&1
  } > "$LOG" 2>&1
  echo "KESZ $4 - naplo: $LOG"
}
run S16_R15 S16_R15B_build.scr readback_S16_R15B_v5 s16r15bv5
run R16_J R16_J_build.scr readback_R16_J_v5 r16jv5
echo "MINDKETTO KESZ" > "$HOME/CAD/S16_R15/WSG_v5_KESZ.txt"
