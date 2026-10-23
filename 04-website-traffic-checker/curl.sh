#!/usr/bin/env bash
# Tutorial 04: bulk mode, one traffic row per domain (good for scoring a lead or competitor list).
# Actor: https://apify.com/vncntlabs/domain-seo-data
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~domain-seo-data/run-sync-get-dataset-items?maxTotalChargeUsd=0.10" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"mode":"bulk","domains":["plausible.io","usefathom.com","simpleanalytics.com"],"countries":["US"],"includeAuthority":true}'
