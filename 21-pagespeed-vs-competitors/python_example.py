"""Run vncntlabs/pagespeed-vs-competitors and print the verdict plus page scores."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("vncntlabs/pagespeed-vs-competitors").call(run_input={
    "keywords": ["custom t shirt printing"],
    "yourUrl": "https://www.printful.com/",
    "topN": 3,
    "country": "United States",
    "device": "mobile",
})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("type") == "summary":
        print(item.get("verdict"))
        for row in item.get("askYourDeveloper") or []:
            print("ask", row.get("name"), "ms", row.get("estimatedSavingsMainThreadMs"),
                  "KB", row.get("estimatedSavingsKB"))
        print("yourPerformance", item.get("yourPerformance"),
              "median", item.get("medianPerformance"),
              "lcpGapMs", item.get("lcpGapMs"))
    elif item.get("type") == "page":
        print("page", item.get("rank"), item.get("url"),
              "perf", item.get("performance"),
              "lcp", item.get("lcpMs"),
              "status", item.get("status"))
