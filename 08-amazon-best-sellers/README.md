# 08: Amazon Best Sellers, New Releases and Movers & Shakers

Ranked products from Amazon's charts for any category on 11 marketplaces: rank, ASIN, title, price, rating, reviews count
and author or brand line, up to 100 per chart, with subcategories, rank changes since the last run and optional full product
details. Actor: [Amazon Best Sellers, New Releases & Movers Scraper](https://apify.com/vncntlabs/amazon-best-sellers).

| File | What it does | Cost at list price (Oct 25, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Top 10 Best Sellers and top 10 Hot New Releases in Books on amazon.com | about $0.045 (20 products + start) |
| `curl.sh` | Top 20 in Kitchen on amazon.de plus 3 subcategories, one synchronous HTTP call | about $0.165 (80 products + start) |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.002 per product, $0.005 per product with full details (instead of, not on top of), plus $0.005 per run start.
Empty charts are not charged. Amazon's Movers & Shakers chart is sometimes empty across the store; those rows come back
with `status: empty` at no charge. Check the Store page for current prices. Not affiliated with Amazon.
