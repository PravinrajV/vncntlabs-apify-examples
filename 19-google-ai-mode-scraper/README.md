# 19 · Google AI Mode Scraper

Get a dated snapshot of what Google AI Mode answered for your prompts, the sites it cited, and competitor share of voice.

- **Actor:** [`vncntlabs/google-ai-mode-scraper`](https://apify.com/vncntlabs/google-ai-mode-scraper)
- **Price:** $0.005 per answer delivered + $0.005 start fee. Empty or failed answers are free.
- **Site:** https://vncntlabs.com/tools/google-ai-mode-scraper/

AI Mode answers vary between runs. Each row is a snapshot, not a claim about what Google says in general. For scheduled checks across ChatGPT, Gemini, AI Mode, AI Overviews and Perplexity, use the [AI Visibility Tracker](https://apify.com/vncntlabs/ai-search-visibility-tracker).

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
{ "mcpServers": { "apify": { "url": "https://mcp.apify.com?tools=vncntlabs/google-ai-mode-scraper" } } }
```
