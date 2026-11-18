# 24 · KDP Category Picker

Pick accurate KDP categories you can win. Give a niche keyword (or up to 5 comparable books) and get your 3 best
relevant categories first: the category path to click in KDP's picker, the #1 and #10 Best Sellers Rank, where your
BSR would land, a label (badge within reach, top 10 within reach, out of reach) and a one-line reason. The full
category table follows. Categories only count when at least 2 similar books already sit in them, and anything that
isn't a selectable book category is labelled, never recommended.

- **Actor:** [`vncntlabs/kdp-category-finder`](https://apify.com/vncntlabs/kdp-category-finder)
- **Price:** $0.15 per report. Reports with no books, no BSR data or no checked category are free.
- **Pairs with:** [`07-amazon-niche-analyzer`](../07-amazon-niche-analyzer) (is the niche worth it?) first, then this.

BSR is a snapshot. For the range over several days, add `"trackName": "my-book"` and schedule the same input daily
for 3-7 days. Not affiliated with Amazon or KDP.

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
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/kdp-category-finder" } } }
```
