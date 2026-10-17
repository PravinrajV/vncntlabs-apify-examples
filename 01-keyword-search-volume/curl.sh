#!/usr/bin/env bash
# Tutorial 01: one synchronous HTTP call (works the same from n8n, Make or Zapier).
# Actor: https://apify.com/vncntlabs/keyword-search-volume
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~keyword-search-volume/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"keywords":["teacher gift","pickleball paddle"],"sources":["google"],"location":"United States"}'
