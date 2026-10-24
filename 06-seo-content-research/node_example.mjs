// 06: SEO content research report for a keyword (volume, Google top 10, People Also Ask, YouTube transcripts).
// Actor: https://apify.com/vncntlabs/seo-content-bundle
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { keywords: ['how to make sourdough starter'], country: 'United States', transcripts: 3 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/seo-content-bundle').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    const s = row.summary || {};
    console.log(row.keyword, row.status, '| volume', s.searchVolume, '| KD', s.keywordDifficulty, '|', s.searchIntent);
    for (const r of (row.serp?.organic || []).slice(0, 3)) console.log('  google:', r.position, r.domain, r.title);
    for (const t of row.transcripts || []) console.log('  transcript:', t.title, '-', t.wordCount, 'words');
}
