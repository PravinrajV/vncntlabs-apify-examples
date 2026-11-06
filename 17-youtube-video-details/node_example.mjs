import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('vncntlabs/youtube-video-details').call({
  videos: [
    'https://www.youtube.com/watch?v=jNQXAC9IVRw',
    'https://youtu.be/dQw4w9WgXcQ',
  ],
  maxVideos: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items.filter((i) => i.type === 'video')) {
  console.log(item.status, item.videoId, item.title, 'views', item.views, 'subs', item.subscribers);
}
