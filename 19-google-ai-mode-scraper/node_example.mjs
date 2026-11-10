import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('vncntlabs/google-ai-mode-scraper').call({
  prompts: [
    'best print on demand company for etsy',
    'printful vs printify',
    'best print on demand for t-shirts',
  ],
  brandDomain: 'printful.com',
  competitorDomains: ['printify.com', 'gooten.com'],
  country: 'United States',
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (item.type === 'share_of_voice') {
    console.log('snapshot', item.snapshotAt);
    for (const row of item.domains || []) {
      console.log(row.domain, 'cited', row.citedPromptRate, 'avg position', row.avgCitationPosition);
    }
    console.log('competitor-only prompts:', item.promptsCompetitorNamedNotYou);
  } else if (item.type === 'answer') {
    const sources = (item.sources || []).slice(0, 5).map((s) => s.domain || '').join(', ');
    console.log(item.prompt, '->', sources);
  }
}
