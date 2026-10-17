// Tutorial 02: competitor SEO report for any domain (traffic, keywords, competitors, backlinks).
// Actor: https://apify.com/vncntlabs/domain-seo-data
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { domains: ['backlinko.com'], countries: ['US'], maxKeywords: 15, maxCompetitors: 5 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/domain-seo-data').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
const overview = items.find((r) => r.type === 'domain');
console.log(overview.organicTraffic, overview.domainRank, overview.referringDomains);
