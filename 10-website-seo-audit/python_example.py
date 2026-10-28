"""10: Website SEO audit: broken pages, broken links and on-page issues for a whole site.
Actor: https://apify.com/vncntlabs/website-seo-audit
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"websites": ["books.toscrape.com"], "maxPagesPerSite": 10}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/website-seo-audit").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "site":
        print(row["site"], row["status"], "| score", row.get("onpageScore"), "| pages", row.get("pagesCrawled"),
              "| broken pages", row.get("brokenPages"), "| broken links", row.get("brokenLinks"))
        for issue in (row.get("issues") or [])[:5]:
            print("  ", issue.get("pagesAffected") or "site-wide", "|", issue["issue"], "->", issue.get("howToFix"))
    elif row["type"] == "broken-link":
        print("  broken link", row["linkFrom"], "->", row["linkTo"], row.get("targetStatusCode"))
    elif row.get("issues"):
        print("  page", row.get("statusCode"), row["url"], "|", ", ".join(row["issues"][:3]))
