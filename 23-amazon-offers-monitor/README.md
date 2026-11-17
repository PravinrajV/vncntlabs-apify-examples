# 23 · Amazon Offers & Hijacker Monitor

Daily check of who sells your ASINs. Each run compares with the previous run of the same monitor and gives one verdict per ASIN: ACT (possible unauthorized new-condition seller, confirmed Buy Box change to one, or a new-condition price below your floor), WATCH (new used seller, Buy Box price move, likely Buy Box change) or OK. The first run of a monitor saves a baseline and never alerts.

- **Actor:** [`vncntlabs/amazon-offers-monitor`](https://apify.com/vncntlabs/amazon-offers-monitor)
- **Price:** $0.005 per run + $0.01 per ASIN checked. ASINs with no offer data are free.

Flags are data, not legal findings. Verify any unknown seller with a test buy. Not affiliated with Amazon.

## Quick start

```bash
export APIFY_TOKEN=...   # your Apify token
python python_example.py   # run it twice: the first run is the baseline
# or
node node_example.mjs
# or
bash curl.sh
```

Keep `monitorName` the same on every run (schedule a saved task daily). Add `alertWebhookUrl` (Slack, Discord, Zapier, Make) to get a message only when something changed.

## MCP

```json
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/amazon-offers-monitor" } } }
```
