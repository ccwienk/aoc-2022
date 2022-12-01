#!/usr/bin/env bash

own_dir="$(dirname "${BASH_SOURCE[0]}")"
echo "$own_dir"

for d in $(seq -w 01 24); do
  tgt_dir="${own_dir}/${d}"
  mkdir -p "${tgt_dir}"
  cp "${own_dir}/util.py" "${tgt_dir}/util.py"
done
