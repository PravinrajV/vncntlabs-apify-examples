#!/usr/bin/env bash
# 09: competitor snapshots for 3 domains in the US, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/domain-seo-data (mode "snapshot")
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~domain-seo-data/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"mode":"snapshot","domains":["ahrefs.com","semrush.com","moz.com"],"countries":["US"]}'
