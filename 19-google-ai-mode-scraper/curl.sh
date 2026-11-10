#!/usr/bin/env bash
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
RUN=$(curl -s -X POST "https://api.apify.com/v2/acts/vncntlabs~google-ai-mode-scraper/runs?token=$APIFY_TOKEN&waitForFinish=180" \
  -H 'Content-Type: application/json' \
  -d '{"prompts":["best print on demand company for etsy","printful vs printify","best print on demand for t-shirts"],"brandDomain":"printful.com","competitorDomains":["printify.com","gooten.com"],"country":"United States"}')
DS=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['defaultDatasetId'])" <<<"$RUN")
curl -s "https://api.apify.com/v2/datasets/$DS/items?token=$APIFY_TOKEN&clean=1" | python3 -m json.tool | head -80
