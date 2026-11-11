// Run vncntlabs/trustpilot-company-comparison and print the side-by-side snapshot.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('vncntlabs/trustpilot-company-comparison').call({
  mode: 'compare',
  companies: ['printful.com', 'printify.com', 'gooten.com'],
  maxReviewsPerCompany: 20,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (item.type === 'sideBySide') {
    console.log(item.summary);
    for (const row of item.table || []) {
      console.log(row.domain, 'worse', row.gettingWorse, 'velocity', row.reviewsPerWeek, 'sample', row.sampleSize);
    }
  } else if (item.type === 'comparison') {
    console.log(item.domain, item.status, 'TrustScore', item.trustScore, 'gettingWorse', item.gettingWorse);
  }
}
