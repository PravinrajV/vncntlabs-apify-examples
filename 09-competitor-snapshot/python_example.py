"""09: One-row competitor snapshots: traffic, top keywords, organic competitors and backlink profile per domain.
Actor: https://apify.com/vncntlabs/domain-seo-data (mode "snapshot")
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"mode": "snapshot", "domains": ["monzo.com", "revolut.com"], "countries": ["GB"]}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/domain-seo-data").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row.get("type") != "snapshot":
        continue
    print(row["domain"], row["country"], row["status"])
    print("  organic traffic", row.get("organicTraffic"), "| keywords", row.get("organicKeywords"),
          "| traffic value $", row.get("organicTrafficValueUsd"))
    print("  domain rank", row.get("domainRank"), "| referring domains", row.get("referringDomains"))
    print("  top keyword:", row.get("topKeyword"), "| top competitors:", row.get("topCompetitorList"))
