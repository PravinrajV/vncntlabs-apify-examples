# 21 · PageSpeed vs Competitors

Keyword in, ranking pages audited, app-level blame. Enter a keyword and your URL. The Actor finds Google's top organic pages, runs Lighthouse on each of them and on your page in the same run with the same device, and names the apps that slow you down versus the pages that outrank you.

- **Actor:** [`vncntlabs/pagespeed-vs-competitors`](https://apify.com/vncntlabs/pagespeed-vs-competitors)
- **Price:** $0.005 start, $0.01 per page audited, $0.02 per keyword compared. Failed, blocked and unresolvable pages are free.
- **Site:** https://vncntlabs.com/tools/pagespeed-vs-competitors/

This is lab data from one Lighthouse run per page. Scores drift. Google ranks on field data; speed is one ranking factor, not the explanation. Licensed DataForSEO SERP and On-Page Lighthouse APIs. Not affiliated with Google or Lighthouse.

## Quick start

```bash
export APIFY_TOKEN=...   # your Apify token
python python_example.py
# or
node node_example.mjs
# or
bash curl.sh
```

## MCP

```json
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/pagespeed-vs-competitors" } } }
```
