// Run vncntlabs/aso-keyword-research and print the iOS keyword field plus scored keyword rows.
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor("vncntlabs/aso-keyword-research").call({
  app: "571800810",
  store: "app_store",
  mode: "app_keywords",
  limit: 20,
});
for await (const item of client.dataset(run.defaultDatasetId).iterateItems()) {
  if (item.type === "listing") {
    console.log("app", item.appTitle, "field", item.iosKeywordField);
    console.log("android terms", item.androidTerms);
  } else if (item.type === "keyword") {
    console.log(item.keyword, "vol", item.estimatedVolume, "rank", item.yourRank,
      "score", item.opportunityScore, "noise", item.noiseFlag, "last", item.lastChecked);
  }
}
