#!/usr/bin/env bash
# A report takes about 3-6 minutes on the standard queue (add "fast": true for the priority queue).
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
API=https://api.apify.com/v2
RUN=$(curl -s -X POST "$API/acts/vncntlabs~kdp-category-finder/runs?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' -d '{"keyword":"gardening journal","yourBsr":60000}')
ID=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['id'])" <<<"$RUN")
while :; do
  R=$(curl -s "$API/actor-runs/$ID?token=$APIFY_TOKEN&waitForFinish=60")
  ST=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['status'])" <<<"$R")
  [[ "$ST" == "READY" || "$ST" == "RUNNING" ]] || break
done
echo "status: $ST"
KV=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['defaultKeyValueStoreId'])" <<<"$R")
curl -s "$API/key-value-stores/$KV/records/OUTPUT?token=$APIFY_TOKEN" | python3 -c "
import json,sys; o=json.load(sys.stdin)
for p in o['top3']: print(p['pick'], p['path'], '|', p['label'], '|', p['reason'])"
