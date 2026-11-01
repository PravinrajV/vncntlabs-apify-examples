// 14: business emails, phones and social profiles for 3 print-on-demand websites.
// Actor: https://apify.com/vncntlabs/website-contact-scraper
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { websites: ['printful.com', 'bonfire.com', 'prodigi.com'], maxPagesPerSite: 5 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/website-contact-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'website') {
        const socials = Object.keys(row.socialProfiles ?? {}).sort().join(', ') || '-';
        console.log(row.domain, '|', row.status, '|', row.email ?? '-', '|', row.phone ?? '-', '|', socials);
    } else {
        console.log('skipped:', row.input, '|', row.skipReason);
    }
}
