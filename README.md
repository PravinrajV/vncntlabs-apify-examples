# VNCNT Labs Apify examples

Minimal, runnable code for calling VNCNT Labs tools through the Apify API. The numbered folders have the same call four ways: curl, Python (`apify-client`), Node.js (`apify-client`) and, where the tutorial uses it, an n8n workflow. The `mcp/` folder connects Claude, ChatGPT, Cursor or VS Code to the same tools through Apify's MCP server.

## All 26 tools

Every tool runs the same way: send its input as JSON and get rows back. The example folders cover six tools in depth. For the rest, use the generic call below with the input from the tool's input schema page.

| Tool | Group | Price | Example |
|---|---|---|---|
| [Keyword Search Volume](https://apify.com/vncntlabs/keyword-search-volume) | SEO & Search Data | $0.003 per Google keyword ($0.004 Amazon, + $0.05 per batch) | [01-keyword-search-volume](01-keyword-search-volume) |
| [Keyword Research Tool](https://apify.com/vncntlabs/keyword-ideas) | SEO & Search Data | $0.002 per keyword idea (+ $0.02 per seed/ASIN) | curl below |
| [Website Traffic Checker](https://apify.com/vncntlabs/domain-seo-data) | SEO & Search Data | $0.02 per domain overview ($0.001 per ranked keyword) | [04-website-traffic-checker](04-website-traffic-checker) |
| [Google Trends Scraper & API with Search Volume](https://apify.com/vncntlabs/google-trends-search-volume) | SEO & Search Data | $0.01 per keyword report (+ $0.015 per volume lookup) | [03-google-trends-volume](03-google-trends-volume) |
| [AI Visibility Tracker](https://apify.com/vncntlabs/ai-search-visibility-tracker) | SEO & Search Data | $0.03 per AI answer | curl below |
| [Google Maps Rank Tracker](https://apify.com/vncntlabs/google-maps-rank-tracker) | SEO & Search Data | $0.006 per grid point | curl below |
| [Google Ads Transparency Scraper](https://apify.com/vncntlabs/google-ads-transparency) | SEO & Search Data | $0.001 per ad (+ $0.004 per advertiser) | curl below |
| [Google News Scraper & API](https://apify.com/vncntlabs/google-news-scraper) | SEO & Search Data | $0.0015 per article | curl below |
| [SEO Content Research](https://apify.com/vncntlabs/seo-content-bundle) | SEO & Search Data | $0.05 per report ($0.08 fast mode) | [06-seo-content-research](06-seo-content-research) |
| [Google Rank Tracker](https://apify.com/vncntlabs/google-rank-tracker) | SEO & Search Data | $0.003 per keyword check | curl below |
| [Backlink Checker & Bulk Domain Authority](https://apify.com/vncntlabs/backlink-checker) | SEO & Search Data | $0.0004 per backlink ($0.002 per domain metrics) | curl below |
| [Trademark Checker](https://apify.com/vncntlabs/pod-trademark-checker) | Seller Tools | $0.003 per phrase checked ($0.01 per listing) | curl below |
| [Google Shopping Scraper](https://apify.com/vncntlabs/google-shopping-scraper) | Seller Tools | $0.002 per product ($0.01 with all offers) | curl below |
| [AI Image Upscaler for Print](https://apify.com/vncntlabs/print-ready-upscaler) | Seller Tools | $0.06 per image ($0.10 over 40 MP) | curl below |
| [PNG to SVG Converter](https://apify.com/vncntlabs/png-to-svg-vectorizer) | Seller Tools | $0.02 per image | curl below |
| [Amazon Book & T-Shirt Niche Analyzer](https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer) | Seller Tools | $0.15 per niche report | [07-amazon-niche-analyzer](07-amazon-niche-analyzer) |
| [Amazon Product Scraper](https://apify.com/vncntlabs/amazon-product-scraper) | Seller Tools | $0.001 per product ($0.003 with ASIN details) | curl below |
| [Google Images Scraper + Google Lens Reverse Image Search](https://apify.com/vncntlabs/google-images-scraper) | Seller Tools | $0.0004 per image ($0.004 per reverse search) | curl below |
| [YouTube Transcript Scraper](https://apify.com/vncntlabs/youtube-transcript-scraper) | YouTube Data | $0.005 per transcript ($0.008 fast mode; videos without captions free) | [05-youtube-transcripts](05-youtube-transcripts) |
| [YouTube Search & Comments Scraper](https://apify.com/vncntlabs/youtube-search-scraper) | YouTube Data | $0.0005 per video (+ $0.001 per search page) | curl below |
| [Local Business Leads from Google Maps](https://apify.com/vncntlabs/local-business-leads) | Local & Market Data | $0.002 per lead | curl below |
| [Google Maps, Trustpilot & Tripadvisor Reviews Scraper](https://apify.com/vncntlabs/review-monitor) | Local & Market Data | $0.0005 per review (+ $0.001 per business) | curl below |
| [Google Play & App Store Reviews Scraper](https://apify.com/vncntlabs/app-reviews-scraper) | Local & Market Data | $0.0001 per Google Play review ($0.00015 App Store) | curl below |
| [Google Jobs Scraper & API](https://apify.com/vncntlabs/google-jobs-scraper) | Local & Market Data | $0.002 per job | curl below |
| [Google Hotels Scraper](https://apify.com/vncntlabs/google-hotels-scraper) | Local & Market Data | $0.002 per hotel | curl below |
| [eBay, Etsy & Amazon FBA Fee Calculator (MCP + API)](https://apify.com/vncntlabs/shoptrueprofit-fee-mcp) | Fee & Profit | $0.005 per fee calculation | curl below |

Prices are from each tool's Store page on Oct 24, 2026. The Store page is always the current source.

## Example folders

| Folder | Tutorial | Apify Actor |
|---|---|---|
| [`01-keyword-search-volume`](01-keyword-search-volume) | Bulk Google + Amazon keyword search volume ([tutorial](https://dev.to/vncntlabs/bulk-google-amazon-keyword-search-volume-for-about-3-per-1000-keywords-api-n8n-claude-f87)) | [Keyword Search Volume](https://apify.com/vncntlabs/keyword-search-volume) |
| [`02-competitor-seo-report`](02-competitor-seo-report) | A competitor SEO report for any domain (tutorial coming soon) | [Domain SEO Data](https://apify.com/vncntlabs/domain-seo-data) |
| [`03-google-trends-volume`](03-google-trends-volume) | Google Trends with real monthly-search numbers (tutorial coming soon) | [Google Trends with Search Volume](https://apify.com/vncntlabs/google-trends-search-volume) |
| [`04-website-traffic-checker`](04-website-traffic-checker) | Website traffic checker: Google traffic, competitor keywords and SEO competitors for any domain ([tutorial](https://dev.to/vncntlabs/website-traffic-checker-api-plausibleios-google-traffic-competitor-keywords-and-backlinks-for-412j)) | [Domain SEO Data](https://apify.com/vncntlabs/domain-seo-data) |
| [`05-youtube-transcripts`](05-youtube-transcripts) | YouTube transcripts with timestamps from links, keyword searches or channels (tutorial coming soon) | [YouTube Transcript Scraper](https://apify.com/vncntlabs/youtube-transcript-scraper) |
| [`06-seo-content-research`](06-seo-content-research) | An SEO content-research report per keyword: volume, Google top 10, People Also Ask and YouTube transcripts (tutorial coming soon) | [SEO Content Research](https://apify.com/vncntlabs/seo-content-bundle) |
| [`07-amazon-niche-analyzer`](07-amazon-niche-analyzer) | Amazon niche research for low-content books, Kindle and print-on-demand t-shirts (tutorial coming soon) | [Amazon Book & T-Shirt Niche Analyzer](https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer) |

## Setup

You need an Apify account and an API token (Apify Console > Settings > API & Integrations).

```bash
export APIFY_TOKEN=your_apify_token_here   # or copy .env.example to .env and load it; never commit it

pip install -r requirements.txt             # Python 3.10+
npm install                                 # Node 18+
```

Every example reads the token from the `APIFY_TOKEN` environment variable. Nothing in this repo contains a real token.

## Any tool with curl

Replace `TOOL` with a slug from the table (for example `backlink-checker`) and the body with that tool's input:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/vncntlabs~TOOL/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"targets": ["example.com"]}'
```

Each tool's fields are at `https://apify.com/vncntlabs/TOOL/input-schema`. Sync calls wait up to 300 seconds; for bigger jobs start a run with `POST /v2/acts/vncntlabs~TOOL/runs` and read the dataset when it finishes.

## Run the folder examples

```bash
python 01-keyword-search-volume/python_example.py
node 01-keyword-search-volume/node_example.mjs
./01-keyword-search-volume/curl.sh
```

Each script uses the tutorial's input by default. Pass a JSON file to use your own:

```bash
python 02-competitor-seo-report/python_example.py my-input.json
```

`test-inputs/` holds the smallest useful input for each folder. `scripts/smoke_test.sh` runs all the Python and Node examples with them.

**Note for Python:** `apify-client` 3.x returns a `Run` object, so the dataset ID is `run.default_dataset_id`. Code written for 1.x/2.x uses `run["defaultDatasetId"]` instead.

## n8n

Import `01-keyword-search-volume/n8n-workflow.json` (Workflows > Import from file). Then create a **Header Auth** credential with name `Authorization` and value `Bearer <your token>`, and select it on the HTTP Request node.

## Claude, ChatGPT, Cursor, VS Code (MCP)

The tools are grouped into five hosted MCP servers. Add one URL as a streamable HTTP server and sign in to Apify in the browser, or send your token as a Bearer header.

| Server | Tools | URL |
|---|---|---|
| SEO & Search Data | 11 | `https://mcp.apify.com/?tools=vncntlabs/keyword-search-volume,vncntlabs/keyword-ideas,vncntlabs/domain-seo-data,vncntlabs/google-trends-search-volume,vncntlabs/ai-search-visibility-tracker,vncntlabs/google-maps-rank-tracker,vncntlabs/google-ads-transparency,vncntlabs/google-news-scraper,vncntlabs/seo-content-bundle,vncntlabs/google-rank-tracker,vncntlabs/backlink-checker` |
| Seller Tools | 8 | `https://mcp.apify.com/?tools=vncntlabs/pod-trademark-checker,vncntlabs/keyword-ideas,vncntlabs/google-shopping-scraper,vncntlabs/print-ready-upscaler,vncntlabs/png-to-svg-vectorizer,vncntlabs/amazon-book-tshirt-niche-analyzer,vncntlabs/amazon-product-scraper,vncntlabs/google-images-scraper` |
| YouTube Data | 3 | `https://mcp.apify.com/?tools=vncntlabs/youtube-transcript-scraper,vncntlabs/youtube-search-scraper,vncntlabs/seo-content-bundle` |
| Local & Market Data | 5 | `https://mcp.apify.com/?tools=vncntlabs/local-business-leads,vncntlabs/review-monitor,vncntlabs/app-reviews-scraper,vncntlabs/google-jobs-scraper,vncntlabs/google-hotels-scraper` |
| Fee & Profit | 1 | `https://mcp.apify.com/?tools=vncntlabs/shoptrueprofit-fee-mcp` |

To mix tools, put any `vncntlabs/<tool>` names in one `?tools=` list.

| File | Use it when |
|---|---|
| `mcp/remote-oauth.json` | Your client supports remote MCP servers. You sign in to Apify in the browser, and no token goes in the file. |
| `mcp/remote-bearer.json` | You'd rather use a token. Clients that expand environment variables read `${APIFY_TOKEN}`. Otherwise, paste your token. |
| `mcp/local-stdio.json` | Your client only supports local servers (needs Node 18+). Replace the placeholder token. |
| `gemini-extension.json` | Gemini CLI: `gemini extensions install https://github.com/PravinrajV/vncntlabs-apify-examples` |
| `.claude-plugin/` | Claude Code: `/plugin marketplace add PravinrajV/vncntlabs-apify-examples`, then `/plugin install vncntlabs-tools@vncntlabs` |

Then ask something like *"Get US Google and Amazon search volume for these 40 keywords and sort by volume per KD point."*

## Costs

Every tool is pay per event, and you pay only for results returned, on your own Apify account. You can cap any run with the maximum charge setting (`maxTotalChargeUsd`).

## License

MIT, see [LICENSE](LICENSE). The data comes from the tools' providers under their terms. Not affiliated with Google, Amazon, YouTube, Etsy, eBay or the USPTO.
