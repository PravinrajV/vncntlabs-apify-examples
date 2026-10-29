// 11: Keyword gap: Google keywords your competitors rank for and you don't.
// Actor: https://apify.com/vncntlabs/keyword-gap-finder
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { yourDomain: 'gelato.com', competitors: ['printify.com'], maxKeywords: 10 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/keyword-gap-finder').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'competitor') {
        console.log(row.competitor, row.status, '| keywords found', row.totalKeywords, '| returned', row.keywordsDelivered);
    } else if (row.type === 'keyword') {
        console.log(String(row.searchVolume ?? 0).padStart(8), '| KD', row.keywordDifficulty, '|', row.keyword, '|',
            `${row.bestCompetitor} #${row.bestPosition}`, '| you:', row.yourPosition ?? '-');
    }
}
