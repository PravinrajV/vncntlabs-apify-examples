"""Tutorial 03: Google Trends with an absolute monthly-search estimate (pickleball vs padel).
Actor: https://apify.com/vncntlabs/google-trends-search-volume
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "keywords": ["pickleball, padel"], "locations": ["United States"],
    "timeframe": "past_12_months", "absoluteVolume": True,
}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/google-trends-search-volume").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "keyword":
        print(row["keyword"], row["estimatedMonthlySearches"], row["estimateConfidence"])
    else:
        print("share of search:", row["shareOfSearchPct"])
