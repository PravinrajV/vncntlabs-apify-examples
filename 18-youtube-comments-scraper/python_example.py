"""Run vncntlabs/youtube-comments-scraper and print the top comments with likes."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/youtube-comments-scraper").call(run_input={
    "videos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "jNQXAC9IVRw"],
    "maxCommentsPerVideo": 20,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "comment":
        print(item["videoId"], item["position"], item.get("likes"), (item.get("text") or "")[:80])
