#!/bin/bash
# Télécharge les fichiers allbsd de Cremona (ecdata) pour les conducteurs < 500 000.
set -u
BASE=https://raw.githubusercontent.com/JohnCremona/ecdata/master
mkdir -p allbsd
for k in $(seq 0 49); do
  lo=$((k*10000)); hi=$((lo+9999))
  name=$(printf "allbsd.%05d-%d" $lo $hi)
  [ $k -eq 0 ] && name="allbsd.00000-09999"
  [ -s allbsd/$name ] && continue
  for t in 1 2 3 4; do
    curl -sf --max-time 300 -o allbsd/$name "$BASE/allbsd/$name" && break
    sleep $((t*3))
  done
  echo "$name $(wc -l < allbsd/$name 2>/dev/null)"
done
