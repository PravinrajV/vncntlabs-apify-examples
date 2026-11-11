# 20 · Trustpilot Company Comparison

Compare 2-5 Trustpilot companies side by side: 1-2 star trend, a getting-worse flag, weekly velocity, reply rate, TrustScore and raw reviews.

- **Actor:** [`vncntlabs/trustpilot-company-comparison`](https://apify.com/vncntlabs/trustpilot-company-comparison)
- **Price:** $0.005 start, $0.001 per comparison row or search hit, $0.0005 per raw review. Not found, failed, empty and already-seen rows are free.
- **Site:** https://vncntlabs.com/tools/trustpilot-company-comparison/

Licensed DataForSEO data, no scraping of trustpilot.com. Not affiliated with Trustpilot. Reply rate and reply lag are also available from other Store tools; this Actor's difference is the side-by-side row, the getting-worse flag, weekly velocity, snapshot date and sample size.

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
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/trustpilot-company-comparison" } } }
```
