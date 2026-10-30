#!/usr/bin/env bash
# 12: products 2 Shopify stores published in the last 30 days, newest first, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/shopify-products-scraper
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~shopify-products-scraper/run-sync-get-dataset-items?timeout=290" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"startUrls":[{"url":"https://kith.com"},{"url":"https://www.allbirds.com"}],"publishedWithinDays":30,"sortBy":"newest","maxProductsPerStore":50}'
