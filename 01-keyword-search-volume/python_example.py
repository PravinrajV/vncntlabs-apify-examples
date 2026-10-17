"""Tutorial 01: bulk Google + Amazon keyword search volume.
Actor: https://apify.com/vncntlabs/keyword-search-volume
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "keywords": ["teacher gift", "coloring book for adults", "pickleball paddle"],
    "sources": ["google", "amazon"],
    "location": "United States",
    "trademarkCheck": True,
}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/keyword-search-volume").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["keyword"], row.get("googleSearchVolume"), row.get("amazonSearchVolume"), row.get("cpcUsd"))
