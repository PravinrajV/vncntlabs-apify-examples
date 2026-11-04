// Tutorial 15: find domains that use Shopify.
// Actor: https://apify.com/vncntlabs/website-tech-stack
import { ApifyClient } from 'apify-client';

const client = new ApifyClient();
const run = await client.actor('vncntlabs/website-tech-stack').call({
  mode: 'find',
  technologies: ['Shopify'],
  limit: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (item.type === 'domain' && item.status === 'ok') {
    console.log(item.domain, item.ecommerce, item.cdn);
  }
}
