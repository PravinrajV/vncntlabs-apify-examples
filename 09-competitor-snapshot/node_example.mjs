// 09: One-row competitor snapshots: traffic, top keywords, organic competitors and backlink profile per domain.
// Actor: https://apify.com/vncntlabs/domain-seo-data (mode "snapshot")
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { mode: 'snapshot', domains: ['monzo.com', 'revolut.com'], countries: ['GB'] };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/domain-seo-data').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items.filter((r) => r.type === 'snapshot')) {
    console.log(row.domain, row.country, row.status);
    console.log('  organic traffic', row.organicTraffic, '| keywords', row.organicKeywords, '| traffic value $', row.organicTrafficValueUsd);
    console.log('  domain rank', row.domainRank, '| referring domains', row.referringDomains);
    console.log('  top keyword:', row.topKeyword, '| top competitors:', row.topCompetitorList);
}
