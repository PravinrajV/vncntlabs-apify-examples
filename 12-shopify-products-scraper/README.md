# 12: Shopify store products (prices, stock, variants and new launches)

Give it one or more Shopify store URLs and it returns one row per product with price, compare-at price, discount,
stock, variants and options, product type, tags, vendor, image and publish date, plus a free summary row per store
(currency, product count, median price, share on sale, top product types and tags, launches in the last 7 and 30 days).
Filter by keyword, `publishedWithinDays`, `onlyOnSale` or `onlyInStock`, and sort by `newest` or `discount`.
Actor: [Shopify Products Scraper](https://apify.com/vncntlabs/shopify-products-scraper).

| File | What it does | Cost at list price (Oct 30, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Lists the 10 newest products from one store with price and discount | $0.01 |
| `curl.sh` | Products 2 stores published in the last 30 days, as one synchronous HTTP call | up to $0.055 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per run and $0.0005 per product returned ($0.50 per 1,000). Store summary rows, products your filters
leave out, and stores that block requests, are password-protected or aren't on Shopify aren't charged. Check the Store
page for current prices.

Small runs usually finish in under 10 seconds. Rows have a `type` field: `product`, `store` (one summary per store) or
`skipped` (inputs that weren't valid). Data comes from each store's public product feed. Not affiliated with Shopify.
