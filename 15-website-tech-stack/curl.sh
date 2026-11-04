#!/usr/bin/env bash
# Tutorial 15: lookup tech stacks via curl.
# Actor: https://apify.com/vncntlabs/website-tech-stack
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~website-tech-stack/run-sync-get-dataset-items?maxTotalChargeUsd=0.25" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"mode":"lookup","domains":["printful.com","bonfire.com","prodigi.com","shopify.com","klaviyo.com"]}'
