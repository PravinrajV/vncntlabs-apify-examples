#!/usr/bin/env bash
# 06: content-research reports for 2 keywords, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/seo-content-bundle
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~seo-content-bundle/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"keywords":["best running shoes for flat feet","how to start a podcast"],"country":"United States","transcripts":2}'
