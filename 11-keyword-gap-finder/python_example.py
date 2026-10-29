"""11: Keyword gap: Google keywords your competitors rank for and you don't.
Actor: https://apify.com/vncntlabs/keyword-gap-finder
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"yourDomain": "gelato.com", "competitors": ["printify.com"], "maxKeywords": 10}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/keyword-gap-finder").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "competitor":
        print(row["competitor"], row["status"], "| keywords found", row.get("totalKeywords"),
              "| returned", row.get("keywordsDelivered"))
    elif row["type"] == "keyword":
        print(f'{row["searchVolume"] or 0:>8} | KD {row.get("keywordDifficulty")} | {row["keyword"]} | '
              f'{row["bestCompetitor"]} #{row["bestPosition"]} | you: {row.get("yourPosition") or "-"}')
