// Tutorial 01: bulk Google + Amazon keyword search volume.
// Actor: https://apify.com/vncntlabs/keyword-search-volume
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = {
    keywords: ['teacher gift', 'coloring book for adults', 'pickleball paddle'],
    sources: ['google', 'amazon'],
    location: 'United States',
    trademarkCheck: true,
};
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/keyword-search-volume').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    console.log(row.keyword, row.googleSearchVolume, row.amazonSearchVolume, row.cpcUsd);
}
