// Run vncntlabs/amazon-offers-monitor and print one verdict per ASIN plus the plain-English summary.
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor("vncntlabs/amazon-offers-monitor").call({
  asins: ["1661264107", "B07YHZR726"],
  monitorName: "my-books", // keep the same name on every run
  allowedSellers: ["My Author Store"],
  floorPrice: 9.99,
});
for await (const item of client.dataset(run.defaultDatasetId).iterateItems()) {
  if (item.type === "asin") {
    console.log(item.asin, item.verdict, "|", item.whatChanged);
    for (const issue of item.openIssues || []) console.log("   still open:", issue);
  }
}
const out = await client.keyValueStore(run.defaultKeyValueStoreId).getRecord("OUTPUT");
console.log(out.value.summary);
