// Run vncntlabs/kdp-category-finder and print your 3 best relevant, winnable KDP categories.
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor("vncntlabs/kdp-category-finder").call({
  keyword: "gardening journal",
  yourBsr: 60000,
});
const { value: out } = await client.keyValueStore(run.defaultKeyValueStoreId).getRecord("OUTPUT");
console.log("Snapshot read at", out.readAt);
for (const p of out.top3) console.log(`${p.pick}. ${p.path}\n   ${p.label}: ${p.reason}`);
if (out.top3Note) console.log(out.top3Note);
