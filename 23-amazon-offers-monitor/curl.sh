#!/usr/bin/env bash
# A run takes about 2-3 minutes (the data provider answers each ASIN in 1-2 minutes, in parallel).
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
API=https://api.apify.com/v2
RUN=$(curl -s -X POST "$API/acts/vncntlabs~amazon-offers-monitor/runs?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"asins":["1661264107","B07YHZR726"],"monitorName":"my-books","floorPrice":9.99}')
ID=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['id'])" <<<"$RUN")
while :; do
  R=$(curl -s "$API/actor-runs/$ID?token=$APIFY_TOKEN&waitForFinish=60")
  ST=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['status'])" <<<"$R")
  [[ "$ST" == "READY" || "$ST" == "RUNNING" ]] || break
done
echo "status: $ST"
KV=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['defaultKeyValueStoreId'])" <<<"$R")
DS=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['defaultDatasetId'])" <<<"$R")
curl -s "$API/key-value-stores/$KV/records/OUTPUT?token=$APIFY_TOKEN" | python3 -c "import json,sys; print(json.load(sys.stdin)['summary'])"
curl -s "$API/datasets/$DS/items?token=$APIFY_TOKEN&clean=1&view=changes" | python3 -m json.tool | head -60
