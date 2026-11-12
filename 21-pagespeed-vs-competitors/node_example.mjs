// Run vncntlabs/pagespeed-vs-competitors and print the verdict plus page scores.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('vncntlabs/pagespeed-vs-competitors').call({
  keywords: ['custom t shirt printing'],
  yourUrl: 'https://www.printful.com/',
  topN: 3,
  country: 'United States',
  device: 'mobile',
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (item.type === 'summary') {
    console.log(item.verdict);
    for (const row of item.askYourDeveloper || []) {
      console.log('ask', row.name, 'ms', row.estimatedSavingsMainThreadMs, 'KB', row.estimatedSavingsKB);
    }
    console.log('yourPerformance', item.yourPerformance, 'median', item.medianPerformance, 'lcpGapMs', item.lcpGapMs);
  } else if (item.type === 'page') {
    console.log('page', item.rank, item.url, 'perf', item.performance, 'lcp', item.lcpMs, 'status', item.status);
  }
}
