# 10: Website SEO audit (broken links and on-page issues)

Give it a domain and it crawls the site, then returns one row per page (status code, title, meta description, H1, word
count, load time and the issues found), one site report with every issue grouped and a fix for each, and one row per
broken link with the page it sits on. You can also pass single page URLs to check without a crawl. Actor:
[Website SEO Audit](https://apify.com/vncntlabs/website-seo-audit).

| File | What it does | Cost at list price (Oct 28, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Crawls 10 pages of a test site and prints the site report, broken links and the pages with issues | $0.035 |
| `curl.sh` | Checks 2 single pages without a crawl, as one synchronous HTTP call | $0.011 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per run plus $0.003 per page audited ($3 per 1,000 pages). Sites that can't be crawled and page URLs that fail to load are not charged.
Check the Store page for current prices.

Crawls take about 2 to 3 seconds per page, so 100 pages is roughly 4 to 6 minutes. For bigger sites use
`python_example.py` or the Node script rather than `curl.sh`, since the synchronous endpoint stops waiting after 300 seconds.

Rows have a `type` field: `page`, `site` or `broken-link`. Site rows include `onpageScore`, `pagesCrawled`, `brokenPages`,
`brokenLinks`, `duplicateTitles`, `hasSitemap`, `hasRobotsTxt`, `httpsRedirect` and `issues` (each with `pagesAffected`,
`exampleUrls` and `howToFix`). Not affiliated with Google.
