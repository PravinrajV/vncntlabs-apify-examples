#!/usr/bin/env bash
set -euo pipefail
: "${APIFY_TOKEN:?set APIFY_TOKEN}"
RUN=$(curl -s -X POST "https://api.apify.com/v2/acts/vncntlabs~youtube-video-details/runs?token=$APIFY_TOKEN&waitForFinish=120" \
  -H 'Content-Type: application/json' \
  -d '{"videos":["https://www.youtube.com/watch?v=jNQXAC9IVRw","https://youtu.be/dQw4w9WgXcQ"],"maxVideos":10}')
DS=$(python3 -c "import json,sys; print(json.load(sys.stdin)['data']['defaultDatasetId'])" <<<"$RUN")
curl -s "https://api.apify.com/v2/datasets/$DS/items?token=$APIFY_TOKEN&clean=1" | python3 -m json.tool | head -80
