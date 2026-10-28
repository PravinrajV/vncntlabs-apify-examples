#!/usr/bin/env bash
# 10: spot-check 2 single pages (no crawl) as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/website-seo-audit
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~website-seo-audit/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"pageUrls":["https://books.toscrape.com/","https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"]}'
