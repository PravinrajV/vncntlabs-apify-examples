// 05: YouTube transcripts with timestamps, from video links or a keyword search.
// Actor: https://apify.com/vncntlabs/youtube-transcript-scraper
// Run:   APIFY_TOKEN=... node node_example.mjs [input.json]
import { readFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
let input = {
    videos: ['https://www.youtube.com/watch?v=jNQXAC9IVRw', 'dQw4w9WgXcQ'],
    includeSegments: true,
};
if (process.argv[2]) input = JSON.parse(readFileSync(process.argv[2], 'utf8')); // optional: your own input file

const run = await client.actor('vncntlabs/youtube-transcript-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) {
    if (row.type === 'keyword') { console.log('search:', row.keyword, row.videosQueued, 'videos'); continue; }
    console.log(row.videoId, row.status, row.title);
    for (const seg of (row.segments || []).slice(0, 3)) console.log(`  ${seg.start.toFixed(2)}s  ${seg.text}`);
}
