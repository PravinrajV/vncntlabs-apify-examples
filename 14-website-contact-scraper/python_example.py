"""14: business emails, phones and social profiles for 3 print-on-demand websites.
Actor: https://apify.com/vncntlabs/website-contact-scraper
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"websites": ["printful.com", "bonfire.com", "prodigi.com"], "maxPagesPerSite": 5}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/website-contact-scraper").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "website":
        socials = ", ".join(sorted((row.get("socialProfiles") or {}).keys())) or "-"
        print(f"{row['domain']} | {row['status']} | {row.get('email') or '-'} | {row.get('phone') or '-'} | {socials}")
    else:
        print("skipped:", row.get("input"), "|", row.get("skipReason"))
