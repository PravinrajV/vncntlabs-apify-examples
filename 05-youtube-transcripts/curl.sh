#!/usr/bin/env bash
# 05: transcripts of the top 5 videos for a keyword (Shorts skipped), as one synchronous HTTP call.
# Actor: https://apify.com/vncntlabs/youtube-transcript-scraper
# Run:   APIFY_TOKEN=... ./curl.sh
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN first}"
curl -sS -X POST "https://api.apify.com/v2/acts/vncntlabs~youtube-transcript-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"keywords":["python tutorial for beginners"],"maxVideosPerKeyword":5,"excludeShorts":true,"includeSegments":false}'
