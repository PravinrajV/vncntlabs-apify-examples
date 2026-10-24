"""07: Amazon niche report for low-content books, Kindle or print-on-demand t-shirts.
Actor: https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"niches": ["fishing log book"], "productType": "paperback", "marketplace": "US"}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/amazon-book-tshirt-niche-analyzer").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    sig, st, ps, tm = (row.get(k) or {} for k in ("signals", "searchStats", "productStats", "trademark"))
    print(row["niche"], row["status"], "| Amazon volume", row.get("amazonSearchVolume"), "| results", row.get("totalResults"))
    print("  demand", sig.get("demand"), "| competition", sig.get("competition"), "| self-published", sig.get("selfPublishedShare"))
    print("  price median", st.get("priceMedian"), "| reviews median", st.get("reviewsMedian"), "| BSR median", ps.get("bsrMedian"))
    print("  trademark risk", tm.get("risk"), tm.get("flaggedPhrases"))
