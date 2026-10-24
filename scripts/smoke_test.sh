#!/usr/bin/env bash
# Runs every Python and Node example once against the live Actors with the tiny inputs in test-inputs/
# (1 keyword / 1 domain / 1 term / 1 niche), so a full pass costs well under $1 at list price.
# Needs: APIFY_TOKEN, `pip install -r requirements.txt`, `npm install`.
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
for d in 01-keyword-search-volume 02-competitor-seo-report 03-google-trends-volume; do
  echo "== $d (python)"; "$PY" "$d/python_example.py" "test-inputs/$d.json"
  echo "== $d (node)";   node "$d/node_example.mjs"   "test-inputs/$d.json"
done
echo "== 04-website-traffic-checker (python)"
"$PY" 04-website-traffic-checker/python_example.py test-inputs/04-website-traffic-checker.json
echo "== 05-youtube-transcripts (python)"
"$PY" 05-youtube-transcripts/python_example.py test-inputs/05-youtube-transcripts.json
echo "== 05-youtube-transcripts (node)"
node 05-youtube-transcripts/node_example.mjs test-inputs/05-youtube-transcripts.json
for d in 06-seo-content-research 07-amazon-niche-analyzer; do
  echo "== $d (python)"; "$PY" "$d/python_example.py" "test-inputs/$d.json"
  echo "== $d (node)";   node "$d/node_example.mjs"   "test-inputs/$d.json"
done
echo "all examples passed"
