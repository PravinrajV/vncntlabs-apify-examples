"""12: Shopify store products: the newest products with price and discount.
Actor: https://apify.com/vncntlabs/shopify-products-scraper
Run:   APIFY_TOKEN=... python python_example.py [input.json]"""
import json
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {"startUrls": [{"url": "https://www.allbirds.com"}], "maxProductsPerStore": 10, "sortBy": "newest"}
if len(sys.argv) > 1:  # optional: pass your own input file
    run_input = json.load(open(sys.argv[1]))

run = client.actor("vncntlabs/shopify-products-scraper").call(run_input=run_input)
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] == "store":
        print(row["store"], row["status"], "| products read", row["productsScanned"], "| returned",
              row["productsDelivered"], "| median price", row.get("priceMedian"), row.get("currency") or "")
    elif row["type"] == "product":
        disc = f"-{row['discountPercent']}%" if row.get("discountPercent") else ""
        print(f"{row.get('price')!s:>8} {disc:>5} | {row['title']} | "
              f"{'in stock' if row.get('available') else 'sold out'} | {(row.get('publishedAt') or '')[:10]}")
