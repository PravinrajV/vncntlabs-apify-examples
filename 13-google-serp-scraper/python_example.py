"""13: Google search results: the top 10 organic results and People Also Ask for one query.
Actor: https://apify.com/vncntlabs/google-serp-scraper
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"queries": ["how to sell on etsy"], "country": "US", "resultsPerQuery": 10, "fastMode": True}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/google-serp-scraper").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "organic":
        print(f"{row.get('position')!s:>3} | {row.get('domain') or '-'} | {row.get('title')}")
    elif row["type"] == "serp":
        print(row["query"], "|", row["status"], "| features:", ", ".join(row.get("serpFeatures") or []))
        for q in row.get("peopleAlsoAsk") or []:
            print("    PAA:", q.get("question"))
