"""Run vncntlabs/aso-keyword-research and print the iOS keyword field plus scored keyword rows."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/aso-keyword-research").call(run_input={
    "app": "571800810",
    "store": "app_store",
    "mode": "app_keywords",
    "limit": 20,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "listing":
        print("app", item.get("appTitle"), "field", item.get("iosKeywordField"))
        print("android terms", item.get("androidTerms"))
    elif item.get("type") == "keyword":
        print(item.get("keyword"), "vol", item.get("estimatedVolume"),
              "rank", item.get("yourRank"), "score", item.get("opportunityScore"),
              "noise", item.get("noiseFlag"), "last", item.get("lastChecked"))
