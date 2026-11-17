"""Run vncntlabs/amazon-offers-monitor and print one verdict per ASIN plus the plain-English summary."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/amazon-offers-monitor").call(run_input={
    "asins": ["1661264107", "B07YHZR726"],
    "monitorName": "my-books",          # keep the same name on every run
    "allowedSellers": ["My Author Store"],
    "floorPrice": 9.99,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "asin":
        print(item["asin"], item.get("verdict"), "|", item.get("whatChanged"))
        for issue in item.get("openIssues") or []:
            print("   still open:", issue)
print(client.key_value_store(run["defaultKeyValueStoreId"]).get_record("OUTPUT")["value"]["summary"])
