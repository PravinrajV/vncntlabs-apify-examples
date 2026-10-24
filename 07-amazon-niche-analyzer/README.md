# 07: Amazon niche research for books, Kindle and t-shirts

One niche keyword in, one niche report out: Amazon search volume, the price and review spread of the top 20 results, Best
Sellers Rank and publish dates of the top product pages, the self-published share and a USPTO trademark screen. Actor:
[Amazon Book & T-Shirt Niche Analyzer](https://apify.com/vncntlabs/amazon-book-tshirt-niche-analyzer).

| File | What it does | Cost at list price (Oct 23, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | One paperback niche, printing demand, competition and trademark risk | $0.15 |
| `curl.sh` | 2 t-shirt niches as one synchronous HTTP call | $0.30 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.15 per niche report, no start fee. Failed or empty searches are not charged. Check the Store page for current prices.

Each niche row has `status`, `amazonSearchVolume`, `totalResults`, `signals` (`demand`, `competition`, `selfPublishedShare`
and the basis for each label), `searchStats` (price, rating and review spread of the top 20), `productStats` (Best Sellers
Rank median, publish dates, publishers), `trademark` (`risk`, `flaggedPhrases`, `classesChecked`) and `products`.
The trademark screen is not legal advice, and the tool does not estimate sales. Not affiliated with Amazon.
