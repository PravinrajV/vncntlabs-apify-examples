#!/usr/bin/env bash
# Run vncntlabs/pagespeed-vs-competitors (needs APIFY_TOKEN).
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
RUN=$(curl -s -X POST "https://api.apify.com/v2/acts/vncntlabs~pagespeed-vs-competitors/runs?token=$APIFY_TOKEN&waitForFinish=300" \
  -H 'Content-Type: application/json' \
  -d '{"keywords":["custom t shirt printing"],"yourUrl":"https://www.printful.com/","topN":3,"country":"United States","device":"mobile"}')
echo "$RUN" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; print(d["id"], d["status"])'
