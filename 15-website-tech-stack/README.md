# 15: Website tech stack lookup and find-by-technology

See which CMS, ecommerce platform, analytics, CDN and marketing tools a website runs, or find domains that use a given technology (Shopify, Printful, Klaviyo...). Actor: [Website Tech Stack Checker](https://apify.com/vncntlabs/website-tech-stack).

| File | What it does | Cost |
|---|---|---|
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |
| `python_example.py` | Lookup five domains | ~$0.105 |
| `node_example.mjs` | Find 10 Shopify domains | ~$0.085 |
| `curl.sh` | Same lookup via curl | ~$0.105 |

Data is from DataForSEO's Domain Analytics Technologies index, not a live crawl of the sites you enter.
