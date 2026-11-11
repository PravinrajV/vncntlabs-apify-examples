"""Run vncntlabs/trustpilot-company-comparison and print the side-by-side snapshot."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/trustpilot-company-comparison").call(run_input={
    "mode": "compare",
    "companies": ["printful.com", "printify.com", "gooten.com"],
    "maxReviewsPerCompany": 20,
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "sideBySide":
        print(item.get("summary"))
        for row in item.get("table") or []:
            print(row.get("domain"), "worse", row.get("gettingWorse"),
                  "last", row.get("lowStarShareLast30"), "prior", row.get("lowStarSharePrior30"),
                  "velocity", row.get("reviewsPerWeek"), "sample", row.get("sampleSize"))
    elif item.get("type") == "comparison":
        print(item.get("domain"), item.get("status"), "TrustScore", item.get("trustScore"),
              "gettingWorse", item.get("gettingWorse"))
