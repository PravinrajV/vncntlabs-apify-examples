# 09: Competitor snapshot, one row per domain

Size up a shortlist of competitors in one call: each domain becomes one row with its organic traffic, keyword count and
traffic value, its top 20 keywords by traffic, its top 10 organic competitors with keyword overlap, and its backlink profile.
Actor: [Domain SEO Data](https://apify.com/vncntlabs/domain-seo-data), `mode: "snapshot"`.

| File | What it does | Cost at list price |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Snapshots for 2 domains in the UK | $0.26 now, $0.24 from Nov 9, 2026 |
| `curl.sh` | Snapshots for 3 domains in the US, one synchronous HTTP call | $0.39 now, $0.36 from Nov 9, 2026 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: until November 9, 2026 a snapshot is charged as its parts (about $0.13). From November 9 it is one flat
`competitor-snapshot` event of $0.12. Snapshot mode uses the first selected country only. Check the Store page for
current prices.
