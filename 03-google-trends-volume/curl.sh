#!/usr/bin/env bash
# Tutorial 03: the article's full run input, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/google-trends-search-volume
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~google-trends-search-volume/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"keywords":["pickleball, padel"],"locations":["United States"],"timeframe":"past_12_months","absoluteVolume":true,"includeRegions":true,"includeRelatedQueries":true,"maxRelatedItems":10,"maxRegions":10}'
