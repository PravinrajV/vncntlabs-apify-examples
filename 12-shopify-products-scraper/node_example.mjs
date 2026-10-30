// 12: Shopify store products: the newest products with price and discount.
// Actor: https://apify.com/vncntlabs/shopify-products-scraper
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { startUrls: [{ url: 'https://www.allbirds.com' }], maxProductsPerStore: 10, sortBy: 'newest' };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/shopify-products-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'store') {
        console.log(row.store, row.status, '| products read', row.productsScanned, '| returned', row.productsDelivered,
            '| median price', row.priceMedian, row.currency ?? '');
    } else if (row.type === 'product') {
        console.log(String(row.price ?? '-').padStart(8), row.discountPercent ? `-${row.discountPercent}%` : '    ', '|',
            row.title, '|', row.available ? 'in stock' : 'sold out', '|', (row.publishedAt ?? '').slice(0, 10));
    }
}
