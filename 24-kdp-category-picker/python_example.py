"""Run vncntlabs/kdp-category-finder and print your 3 best relevant, winnable KDP categories."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/kdp-category-finder").call(run_input={
    "keyword": "gardening journal",   # your niche, as a reader would search Amazon Books
    "yourBsr": 60000,                 # optional: your current or expected Best Sellers Rank
})
out = client.key_value_store(run["defaultKeyValueStoreId"]).get_record("OUTPUT")["value"]
print("Snapshot read at", out["readAt"])
for p in out["top3"]:
    print(f"{p['pick']}. {p['path']}\n   {p['label']}: {p['reason']}")
if out.get("top3Note"):
    print(out["top3Note"])
