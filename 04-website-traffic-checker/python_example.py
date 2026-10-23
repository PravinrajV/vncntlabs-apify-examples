"""Tutorial 04: check a website's Google traffic, the keywords it ranks for and its SEO competitors.
Actor: https://apify.com/vncntlabs/domain-seo-data
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "mode": "report",
    "domains": ["plausible.io"],
    "countries": ["US"],
    "maxKeywords": 10,
    "maxCompetitors": 3,
    "includeBacklinks": True,
}
if len(sys.argv) > 1:  # optional: pass your own input file
    with open(sys.argv[1]) as f:
        run_input = json.load(f)

# max_total_charge_usd caps what this run can cost you (pay-per-event)
run = client.actor("vncntlabs/domain-seo-data").call(
    run_input=run_input, max_total_charge_usd=Decimal("0.25")
)
rows = list(client.dataset(run.default_dataset_id).iterate_items())  # apify-client 3.x: Run object

for d in (r for r in rows if r["type"] == "domain"):
    print(f"{d['domain']} ({d['country']}): ~{d['organicTraffic']:,.0f} organic visits/month, "
          f"{d['organicKeywords']:,} keywords, {d['top10']:,} in the top 10, "
          f"domain rank {d.get('domainRank') or 'n/a'}, referring domains {d.get('referringDomains') or 'n/a'}")

print("\nTop keywords by estimated traffic:")
for k in (r for r in rows if r["type"] == "keyword"):
    print(f"  #{k['position']:>3}  {k['keyword']:<32} vol {k['searchVolume']:>7,}  {k['url']}")

print("\nSEO competitors:")
for c in (r for r in rows if r["type"] == "competitor"):
    print(f"  {c['competitor']:<20} {c['sharedKeywords']:>5} shared keywords ({c['sharedKeywordsPct']}%)")
