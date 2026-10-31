#!/usr/bin/env bash
# 13: top 20 Google results for 2 local queries in Columbus, Ohio on mobile, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/google-serp-scraper
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~google-serp-scraper/run-sync-get-dataset-items?timeout=300" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"queries":["best pizza near me","emergency plumber"],"country":"US","location":"Columbus,Ohio,United States","device":"mobile","resultsPerQuery":20}'
