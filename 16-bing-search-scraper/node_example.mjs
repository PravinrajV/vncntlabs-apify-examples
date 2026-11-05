#!/usr/bin/env node
/** 16: Bing search results. Actor: vncntlabs/bing-search-scraper
 *  Run: APIFY_TOKEN=... node node_example.mjs [input.json] */
import { ApifyClient } from "apify-client";
import { readFileSync } from "node:fs";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let runInput = { queries: ["how to sell on etsy"], country: "US", resultsPerQuery: 10, fastMode: false };
if (process.argv[2]) runInput = JSON.parse(readFileSync(process.argv[2], "utf8"));

const run = await client.actor("vncntlabs/bing-search-scraper").call(runInput);
for await (const row of client.dataset(run.defaultDatasetId).iterateItems()) {
  if (row.type === "organic") {
    console.log(String(row.position ?? "").padStart(3), "|", row.domain || "-", "|", row.title);
  } else if (row.type === "serp") {
    console.log(row.query, "|", row.status, "| features:", (row.serpFeatures || []).join(", "));
    for (const q of row.relatedSearches || []) {
      console.log("    related:", typeof q === "string" ? q : q.query || q.title);
    }
  }
}
