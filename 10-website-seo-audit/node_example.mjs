// 10: Website SEO audit: broken pages, broken links and on-page issues for a whole site.
// Actor: https://apify.com/vncntlabs/website-seo-audit
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = { websites: ['books.toscrape.com'], maxPagesPerSite: 10 };
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/website-seo-audit').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'site') {
        console.log(row.site, row.status, '| score', row.onpageScore, '| pages', row.pagesCrawled,
            '| broken pages', row.brokenPages, '| broken links', row.brokenLinks);
        for (const i of (row.issues || []).slice(0, 5)) console.log('  ', i.pagesAffected || 'site-wide', '|', i.issue);
    } else if (row.type === 'broken-link') {
        console.log('  broken link', row.linkFrom, '->', row.linkTo, row.targetStatusCode);
    } else if ((row.issues || []).length) {
        console.log('  page', row.statusCode, row.url, '|', row.issues.slice(0, 3).join(', '));
    }
}
