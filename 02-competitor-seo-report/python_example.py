"""Tutorial 02: competitor SEO report for any domain (traffic, keywords, competitors, backlinks).
Actor: https://apify.com/vncntlabs/domain-seo-data
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "domains": ["backlinko.com"], "countries": ["US"], "maxKeywords": 15, "maxCompetitors": 5,
}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/domain-seo-data").call(run_input=run_input)
rows = list(client.dataset(run.default_dataset_id).iterate_items())
overview = next(r for r in rows if r["type"] == "domain")
print(overview.get("organicTraffic"), overview.get("domainRank"), overview.get("referringDomains"))
