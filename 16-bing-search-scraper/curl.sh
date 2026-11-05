#!/usr/bin/env bash
# 16: Bing Search Scraper. Needs APIFY_TOKEN.
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
ACTOR=vncntlabs/bing-search-scraper
INPUT='{"queries":["how to sell on etsy"],"country":"US","resultsPerQuery":10,"fastMode":false}'
RUN=$(curl -sS -X POST "https://api.apify.com/v2/acts/${ACTOR}/runs?token=${APIFY_TOKEN}&waitForFinish=120" \
  -H 'Content-Type: application/json' -d "$INPUT")
echo "$RUN" | python3 -c 'import json,sys; r=json.load(sys.stdin)["data"]; print(r["id"], r["status"])'
DS=$(echo "$RUN" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["defaultDatasetId"])')
curl -sS "https://api.apify.com/v2/datasets/${DS}/items?token=${APIFY_TOKEN}&format=json" | python3 -m json.tool | head -80
