# 06: SEO content research for a keyword

One keyword in, one content-research report out: Google search volume, CPC, difficulty and intent, the Google top 10 with
People Also Ask and AI Overview, the top YouTube videos and transcripts of the top 3. Actor:
[SEO Content Research](https://apify.com/vncntlabs/seo-content-bundle).

| File | What it does | Cost at list price (Oct 23, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | One report, printing the summary, the top 3 Google results and the transcript lengths | $0.05 |
| `curl.sh` | Reports for 2 keywords as one synchronous HTTP call | $0.10 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.05 per report, or $0.08 per report with `fastMode` on (charged instead of the standard price), no start fee.
Reports whose keyword, Google or YouTube data failed are not charged. Check the Store page for current prices.

Each report row has `status`, `summary` (search volume, difficulty, intent, CPC, top domains, People Also Ask count, AI
Overview and featured snippet flags), `keywordData` (with 12 months of `monthlySearches`), `serp` (`organic`,
`peopleAlsoAsk`, `relatedSearches`, `aiOverview`, ...), `youtubeVideos` and `transcripts` (`title`, `channelName`, `wordCount`,
`transcript`).
