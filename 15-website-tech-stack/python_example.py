"""Tutorial 15: look up the tech stack of a few competitor domains.
Actor: https://apify.com/vncntlabs/website-tech-stack
"""
from apify_client import ApifyClient

client = ApifyClient()  # uses APIFY_TOKEN from env
run = client.actor("vncntlabs/website-tech-stack").call({
    "mode": "lookup",
    "domains": ["printful.com", "bonfire.com", "prodigi.com", "shopify.com", "klaviyo.com"],
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "domain" and item.get("status") == "ok":
        print(item["domain"], "ecom=", item.get("ecommerce"), "cdn=", item.get("cdn"),
              "analytics=", item.get("analytics"), "techs=", item.get("technologyCount"))
