"""11: Keyword gap across two competitors, with a word filter (code from the dev.to article, tested Nov 10, 2026).
Actor: https://apify.com/vncntlabs/keyword-gap-finder
Run:   APIFY_TOKEN=... python two_competitors.py"""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/keyword-gap-finder").call(run_input={
    "yourDomain": "gelato.com",
    "competitors": ["printify.com", "printful.com"],
    "maxKeywords": 20,
    "excludeKeywordsContaining": ["wix"],
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "competitor":
        print(row["competitor"], row["status"], "| gap size", row.get("totalKeywords"))
    elif row["type"] == "keyword":
        print(row["searchVolume"], row["keywordDifficulty"], row["keyword"], row["positions"])
