#!/usr/bin/env bash
# Run vncntlabs/trustpilot-company-comparison (needs APIFY_TOKEN).
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
RUN=$(curl -s -X POST "https://api.apify.com/v2/acts/vncntlabs~trustpilot-company-comparison/runs?token=$APIFY_TOKEN&waitForFinish=180" \
  -H 'Content-Type: application/json' \
  -d '{"mode":"compare","companies":["printful.com","printify.com","gooten.com"],"maxReviewsPerCompany":20}')
echo "$RUN" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; print(d["id"], d["status"])'
