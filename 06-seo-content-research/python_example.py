"""06: SEO content research report for a keyword (volume, Google top 10, People Also Ask, YouTube transcripts).
Actor: https://apify.com/vncntlabs/seo-content-bundle
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"keywords": ["how to make sourdough starter"], "country": "United States", "transcripts": 3}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/seo-content-bundle").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["keyword"], row["status"])
    s = row.get("summary") or {}
    print("  volume", s.get("searchVolume"), "| KD", s.get("keywordDifficulty"), "|", s.get("searchIntent"),
          "| AI Overview", s.get("hasAiOverview"))
    for r in ((row.get("serp") or {}).get("organic") or [])[:3]:
        print("  google:", r.get("position"), r.get("domain"), r.get("title"))
    for q in ((row.get("serp") or {}).get("peopleAlsoAsk") or [])[:3]:
        print("  asks:", q.get("question") if isinstance(q, dict) else q)
    for t in row.get("transcripts") or []:
        print("  transcript:", t["title"], "-", t.get("wordCount"), "words")
