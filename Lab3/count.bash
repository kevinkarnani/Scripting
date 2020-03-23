#!/bin/bash

for f in $(ls); do
  if [[ -f $f ]]; then
    echo -n "$f"
    cat "$f" | wc -wl
  fi
done
