// Tutorial 03: Google Trends with an absolute monthly-search estimate (pickleball vs padel).
// Actor: https://apify.com/vncntlabs/google-trends-search-volume
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = {
    keywords: ['pickleball, padel'],
    locations: ['United States'],
    timeframe: 'past_12_months',
    absoluteVolume: true,
};
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/google-trends-search-volume').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'keyword') console.log(row.keyword, row.estimatedMonthlySearches, row.estimateConfidence);
    else console.log('share of search:', row.shareOfSearchPct);
}
