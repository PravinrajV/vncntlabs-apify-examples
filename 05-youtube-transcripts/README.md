# 05: YouTube transcripts with timestamps

Get the transcript of any YouTube video, from links, IDs or a keyword search: full text, timestamped segments, caption
language, title and channel. Actor: [YouTube Transcript Scraper](https://apify.com/vncntlabs/youtube-transcript-scraper).

| File | What it does | Cost at list price (Oct 23, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Transcripts of 2 videos by link and by ID, printing the first timestamped lines | $0.01 |
| `curl.sh` | Top 5 videos for a keyword search (Shorts skipped), full text only | up to $0.025 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per transcript delivered, $0.008 per transcript with fast mode on, no start fee. Videos without captions,
missing or private videos are returned with a status row and are not charged. Check the Store page for current prices.

Each video row has `status` (`ok`, `no_captions`, `not_found`, `unavailable`, `error`), `title`, `channelName`, `language`,
`transcript` (full text), `wordCount` and, with `includeSegments` on, `segments` as `{start, duration, end, text}` in seconds.
