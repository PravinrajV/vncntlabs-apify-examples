"""Run vncntlabs/google-ai-mode-scraper and print share of voice plus each answer's sources."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/google-ai-mode-scraper").call(run_input={
    "prompts": [
        "best print on demand company for etsy",
        "printful vs printify",
        "best print on demand for t-shirts",
    ],
    "brandDomain": "printful.com",
    "competitorDomains": ["printify.com", "gooten.com"],
    "country": "United States",
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "share_of_voice":
        print("snapshot", item.get("snapshotAt"))
        for row in item.get("domains") or []:
            print(row.get("domain"), "cited", row.get("citedPromptRate"), "avg position", row.get("avgCitationPosition"))
        print("competitor-only prompts:", item.get("promptsCompetitorNamedNotYou"))
    elif item.get("type") == "answer":
        sources = ", ".join((s.get("domain") or "") for s in (item.get("sources") or [])[:5])
        print(item.get("prompt"), "->", sources)
