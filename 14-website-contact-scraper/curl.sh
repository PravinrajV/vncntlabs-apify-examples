#!/usr/bin/env bash
# 14: business emails, phones and social profiles for 5 websites, as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/website-contact-scraper
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~website-contact-scraper/run-sync-get-dataset-items?timeout=300" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"websites":["printful.com","bonfire.com","prodigi.com","moz.com","ahrefs.com"],"maxPagesPerSite":5}'
