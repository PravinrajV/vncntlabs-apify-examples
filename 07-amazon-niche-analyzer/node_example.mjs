// 07: Amazon niche report for low-content books, Kindle or print-on-demand t-shirts.
// Actor: https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { niches: ['fishing log book'], productType: 'paperback', marketplace: 'US' };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/amazon-book-tshirt-niche-analyzer').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    const sig = row.signals || {}, st = row.searchStats || {}, ps = row.productStats || {}, tm = row.trademark || {};
    console.log(row.niche, row.status, '| Amazon volume', row.amazonSearchVolume, '| results', row.totalResults);
    console.log('  demand', sig.demand, '| competition', sig.competition, '| price median', st.priceMedian,
        '| reviews median', st.reviewsMedian, '| BSR median', ps.bsrMedian, '| trademark', tm.risk);
}
