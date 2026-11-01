# 14: Business emails, phones and social profiles from a list of websites

Give it websites (domains or full URLs, up to 1,000 per run) and it returns one row per site with the business
emails, phone numbers, social profiles (Facebook, Instagram, X, LinkedIn, YouTube, TikTok, Pinterest, Threads, Etsy,
Amazon), the contact page and contact form, and the page each email was found on. It reads the homepage plus the
pages where contacts usually live (contact, impressum, about, wholesale, press): 5 pages per site by default
(`maxPagesPerSite`, 1 to 20, same price).
Actor: [Website Contact Scraper](https://apify.com/vncntlabs/website-contact-scraper).

| File | What it does | Cost at list price (Nov 1, 2026) |
|---|---|---|
| `python_example.py` / `node_example.mjs` | Contacts for 3 print-on-demand websites | about $0.011 |
| `curl.sh` | Contacts for 5 websites as one synchronous HTTP call | about $0.015 |
| `mcp.json` | Loads only this Actor into Claude, ChatGPT or Cursor through Apify's MCP server (OAuth sign-in) | per run |

```bash
export APIFY_TOKEN=your_apify_token_here
pip install -r ../requirements.txt   # apify-client 3.x
python python_example.py             # or: python python_example.py my-input.json
node node_example.mjs
./curl.sh
```

Prices: $0.005 per run and $0.002 per website where at least one business email or phone number was found ($2 per
1,000). Websites with nothing found, blocked or dead websites and skipped inputs aren't charged. Check the Store page
for current prices.

Rows have a `type` field: `website` (one per site) or `skipped` (inputs that weren't valid, such as social media
links, with a `skipReason`). `status` is `ok`, `no-contacts`, `blocked`, `unreachable`, `robots-disallowed`,
`suppressed` (the business opted out) or `error`. Only emails on the website's own domain are returned; free-mail and
personal-looking addresses are dropped, and EU, EEA, UK and Swiss websites get role addresses only. The crawler
follows robots.txt. If you contact anyone, follow the rules that apply to you (GDPR, PECR, CAN-SPAM, CASL).
