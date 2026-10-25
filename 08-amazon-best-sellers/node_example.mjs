// 08: Amazon Best Sellers, Hot New Releases and Movers & Shakers for any category.
// Actor: https://apify.com/vncntlabs/amazon-best-sellers
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { categories: ['books'], listTypes: ['bestsellers', 'new-releases'], maxItemsPerList: 10 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/amazon-best-sellers').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'list') console.log('==', row.marketplace, row.listType, row.category, row.status, row.productsDelivered, 'products');
    else console.log(`  #${row.rank} ${row.asin} ${row.priceText ?? ''}  ${row.title.slice(0, 70)}`);
}
