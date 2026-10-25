"""08: Amazon Best Sellers, Hot New Releases and Movers & Shakers for any category.
Actor: https://apify.com/vncntlabs/amazon-best-sellers
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"categories": ["books"], "listTypes": ["bestsellers", "new-releases"], "maxItemsPerList": 10}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/amazon-best-sellers").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "list":
        print("==", row["marketplace"], row["listType"], row.get("category"), row["status"], row["productsDelivered"], "products")
    else:
        print(f'  #{row["rank"]:>3} {row["asin"]} {row.get("priceText") or "":>10}  {row["title"][:70]}')
