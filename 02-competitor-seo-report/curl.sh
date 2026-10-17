#!/usr/bin/env bash
# Tutorial 02: the full report input from the article, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/domain-seo-data
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~domain-seo-data/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"domains":["backlinko.com"],"mode":"report","countries":["US"],"maxKeywords":15,"maxCompetitors":5,"includeBacklinks":true,"includeAuthority":true}'
