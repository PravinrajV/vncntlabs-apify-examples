# 13: Google search results (organic rankings, People Also Ask, AI Overviews and local pack)

Give it search queries and it returns one row per organic result (position, title, URL, domain, snippet, sitelinks)
and one `serp` row per query with People Also Ask, related searches, the AI Overview text and its sources, the
featured snippet, the local pack, ads, videos, top stories and the top domains. Pick any country, an optional city,
a language and `desktop` or `mobile`, and how many results you want (`resultsPerQuery`, 1 to 100).
Actor: [Google SERP Scraper](https://apify.com/vncntlabs/google-serp-scraper).

| File | What it does | Cost at list price (Oct 31, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Top 10 results and People Also Ask for one query, in fast mode | about $0.008 |
| `curl.sh` | Top 20 results for 2 local queries in Columbus, Ohio on mobile, as one synchronous HTTP call | about $0.013 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per run and $0.002 per results page (up to 10 organic results for one query, $2 per 1,000 pages).
Fast mode adds $0.0012 per page. Queries Google has no results for, and searches that fail, aren't charged. Check the
Store page for current prices.

Fast mode runs usually finish in about 30 seconds. Standard mode can take 1 to 5 minutes because searches wait in a
queue, so the curl call allows the full 300 seconds. Rows have a `type` field: `serp` (one per query), `organic` (one
per result) or `skipped` (inputs that weren't valid). Not affiliated with Google.
