"""Run vncntlabs/youtube-video-details and print title / views / subscribers."""
import os, json
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/youtube-video-details").call(run_input={
    "videos": [
        "https://www.youtube.com/watch?v=jNQXAC9IVRw",
        "https://youtu.be/dQw4w9WgXcQ",
    ],
    "maxVideos": 10,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") != "video":
        continue
    print(item.get("status"), item.get("videoId"), item.get("title"),
          "views", item.get("views"), "subs", item.get("subscribers"))
