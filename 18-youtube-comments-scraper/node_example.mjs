import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('vncntlabs/youtube-comments-scraper').call({
  videos: ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'jNQXAC9IVRw'],
  maxCommentsPerVideo: 20,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items.filter((i) => i.type === 'comment')) {
  console.log(item.videoId, item.position, item.likes, (item.text || '').slice(0, 80));
}
