# 20 · ASO Keyword Research

Paste an App Store id or a Google Play package and get every keyword that app ranks for, with estimated volume (DataForSEO), rank, last-checked date, an opportunity score, and a ready-to-paste iOS keyword field.

- **Actor:** [`vncntlabs/aso-keyword-research`](https://apify.com/vncntlabs/aso-keyword-research)
- **Price:** $0.005 start, $0.02 per app lookup, $0.001 per keyword row. Unknown apps and empty results are free.
- **Site:** https://vncntlabs.com/tools/aso-keyword-research/

Volume is DataForSEO's monthly estimate, not Apple popularity and not a live rank. Each row carries a last-checked date. US English store only.

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
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/aso-keyword-research" } } }
```
