# VNCNT Labs Apify examples

Minimal, runnable code for three tutorials on pulling SEO and search data through the Apify API. Each folder has the same call
four ways: curl, Python (`apify-client`), Node.js (`apify-client`) and, where the tutorial uses it, an n8n workflow. The `mcp/`
folder connects Claude, ChatGPT or Cursor to the same Actors through Apify's MCP server.

| Folder | Tutorial | Apify Actor |
|---|---|---|
| [`01-keyword-search-volume`](01-keyword-search-volume) | Bulk Google + Amazon keyword search volume ([tutorial](https://dev.to/vncntlabs/bulk-google-amazon-keyword-search-volume-for-about-3-per-1000-keywords-api-n8n-claude-f87)) | [Keyword Search Volume](https://apify.com/vncntlabs/keyword-search-volume) |
| [`02-competitor-seo-report`](02-competitor-seo-report) | A competitor SEO report for any domain (tutorial coming soon) | [Domain SEO Data](https://apify.com/vncntlabs/domain-seo-data) |
| [`03-google-trends-volume`](03-google-trends-volume) | Google Trends with real monthly-search numbers (tutorial coming soon) | [Google Trends with Search Volume](https://apify.com/vncntlabs/google-trends-search-volume) |

## Setup

You need an Apify account and an API token (Apify Console > Settings > API & Integrations).

```bash
export APIFY_TOKEN=your_apify_token_here   # or copy .env.example to .env and load it; never commit it

pip install -r requirements.txt             # Python 3.10+
npm install                                 # Node 18+
```

Every example reads the token from the `APIFY_TOKEN` environment variable. Nothing in this repo contains a real token.

## Run

```bash
# Python
python 01-keyword-search-volume/python_example.py
# Node
node 01-keyword-search-volume/node_example.mjs
# curl (synchronous: returns the dataset rows as JSON)
./01-keyword-search-volume/curl.sh
```

Each Python and Node script uses the tutorial's input by default. Pass a JSON file to use your own input:

```bash
python 02-competitor-seo-report/python_example.py my-input.json
```

`test-inputs/` holds the smallest useful input for each Actor (1 keyword, 1 domain, 1 term). `scripts/smoke_test.sh` runs
all six Python and Node examples with them.

**Note for Python:** `apify-client` 3.x returns a `Run` object, so the dataset ID is `run.default_dataset_id`. Code written
for 1.x/2.x uses `run["defaultDatasetId"]` instead.

## n8n

Import `01-keyword-search-volume/n8n-workflow.json` (Workflows > Import from file). Then create a **Header Auth** credential
with name `Authorization` and value `Bearer <your token>`, and select it on the HTTP Request node. Each keyword becomes one n8n item.

## Claude, ChatGPT, Cursor (MCP)

| File | Use it when |
|---|---|
| `mcp/remote-oauth.json` | Your client supports remote MCP servers. You sign in to Apify in the browser, and no token goes in the file. |
| `mcp/remote-bearer.json` | You'd rather use a token. Clients that expand environment variables read `${APIFY_TOKEN}`. Otherwise, paste your token. |
| `mcp/local-stdio.json` | Your client only supports local servers (needs Node 18+). Replace the placeholder token. |

Each config loads only the three Actors above plus Apify's Actor-search tools. Then ask something like
*"Get US Google and Amazon search volume for these 40 keywords and sort by volume per KD point."*

## Costs

All three Actors are pay-per-event, and you pay only for results returned. Current prices are on each Actor's Store page,
and you can cap a run with `maxTotalChargeUsd` (Keyword Search Volume input) or the maximum charge setting on any run.

## License

MIT, see [LICENSE](LICENSE). The data comes from the Actors' providers under their terms. Not affiliated with Google or Amazon.
