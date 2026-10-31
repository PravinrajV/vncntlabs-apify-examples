// 13: Google search results: the top 10 organic results and People Also Ask for one query.
// Actor: https://apify.com/vncntlabs/google-serp-scraper
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { queries: ['how to sell on etsy'], country: 'US', resultsPerQuery: 10, fastMode: true };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/google-serp-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'organic') {
        console.log(String(row.position ?? '').padStart(3), '|', row.domain ?? '-', '|', row.title);
    } else if (row.type === 'serp') {
        console.log(row.query, '|', row.status, '| features:', (row.serpFeatures ?? []).join(', '));
        for (const q of row.peopleAlsoAsk ?? []) console.log('    PAA:', q.question);
    }
}
