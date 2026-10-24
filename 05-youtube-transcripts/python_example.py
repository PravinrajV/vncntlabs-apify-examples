"""05: YouTube transcripts with timestamps, from video links or a keyword search.
Actor: https://apify.com/vncntlabs/youtube-transcript-scraper
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "videos": ["https://www.youtube.com/watch?v=jNQXAC9IVRw", "dQw4w9WgXcQ"],
    "includeSegments": True,
}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/youtube-transcript-scraper").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row.get("type") == "keyword":  # one summary row per keyword search
        print("search:", row["keyword"], row["videosQueued"], "videos")
        continue
    print(row["videoId"], row["status"], row.get("title"))
    for seg in (row.get("segments") or [])[:3]:  # first 3 timestamped lines
        print(f"  {seg['start']:>7.2f}s  {seg['text']}")
