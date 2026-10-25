#!/bin/bash
for i in $(seq 1 34); do f=$(ls $HOME/mnt/Downloads | grep -E "__OPUS55_V3_1__v[0-9]+\.png$" | head -1); if [ -n "$f" ]; then sleep 2; echo "FOUND $f"; exit 0; fi; sleep 5; done; echo "NOTYET"
