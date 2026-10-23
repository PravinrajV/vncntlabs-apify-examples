# 04: Website traffic checker, competitor keywords and SEO competitors

Code for the dev.to tutorial on checking a site's Google organic traffic, the keywords it ranks for and the domains it
competes with in search. Actor: [Domain SEO Data](https://apify.com/vncntlabs/domain-seo-data).

| File | What it does | Cost at list price (Oct 23, 2026) |
|---|---|---|
| `python_example.py` | Report mode for `plausible.io`: overview, 10 keywords, 3 competitors, backlink profile | about $0.097 |
| `curl.sh` | Bulk mode for 3 domains, one traffic row each | about $0.064 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
./curl.sh
```

Prices: $0.005 per run start, $0.02 per domain overview, $0.001 per ranked keyword, $0.004 per competitor,
$0.05 per backlink profile. Bulk mode: $0.003 per domain plus $0.05 per batch of up to 1,000 domains.
Domains with no search data are not charged in report mode. Check the Store page for current prices.

Traffic is DataForSEO's estimate of Google organic clicks, not total visits from all channels.
