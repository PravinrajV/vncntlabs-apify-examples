#!/usr/bin/env bash
# 08: top 20 Best Sellers in Kitchen on amazon.de and its first 3 subcategories, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/amazon-best-sellers
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~amazon-best-sellers/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"categories":["kitchen"],"marketplace":"DE","maxItemsPerList":20,"includeSubcategories":true,"maxSubcategories":3}'
