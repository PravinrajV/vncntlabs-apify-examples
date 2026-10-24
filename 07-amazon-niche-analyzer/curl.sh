#!/usr/bin/env bash
# 07: niche reports for 2 t-shirt niches on amazon.com, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~amazon-book-tshirt-niche-analyzer/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"niches":["pickleball dad","retired teacher"],"productType":"t-shirt","marketplace":"US"}'
