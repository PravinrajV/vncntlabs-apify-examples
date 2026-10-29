# 11: Keyword gap (competitor keywords you don't rank for)

Give it your domain and up to 5 competitors and it returns one row per Google keyword they rank for and you don't, with
monthly search volume, CPC, keyword difficulty, intent, how many competitors rank for it and each competitor's position
and URL. `mode: "behind"` returns keywords where a competitor outranks you, and `mode: "shared"` returns every keyword you
share. Actor: [Keyword Gap Finder](https://apify.com/vncntlabs/keyword-gap-finder).

| File | What it does | Cost at list price (Oct 29, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Compares one domain with one competitor and prints the top 10 missing keywords | $0.035 |
| `curl.sh` | Keywords where 2 competitors outrank you, as one synchronous HTTP call | up to $0.065 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per run, $0.02 per competitor compared and $0.001 per keyword returned ($1 per 1,000). Competitors with
no ranking data aren't charged. Check the Store page for current prices.

Runs usually finish in under 10 seconds. Rows have a `type` field: `keyword`, `competitor` (one summary per competitor)
or `skipped` (inputs that weren't valid domains). Branded searches for your competitors are left out by default
(`excludeBrandedKeywords`). Positions and volumes are estimates from DataForSEO Labs. Not affiliated with Google.
