#!/usr/bin/env bash
# 11: keywords where 2 competitors outrank you, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/keyword-gap-finder
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~keyword-gap-finder/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"yourDomain":"gelato.com","competitors":["printify.com","printful.com"],"mode":"behind","maxKeywords":20}'
