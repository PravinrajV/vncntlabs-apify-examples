"""05: transcripts of the top 5 YouTube results for a keyword, cut into ~60-second chunks for RAG.
Actor: https://apify.com/vncntlabs/youtube-transcript-scraper
Run:   APIFY_TOKEN=... python rag_chunks.py   (about $0.025 at list price)"""
import os
from decimal import Decimal

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "keywords": ["chatgpt tutorial for beginners"],
    "maxVideosPerKeyword": 5,
    "excludeShorts": True,
}

# max_total_charge_usd caps what this run can cost you (pay-per-event)
run = client.actor("vncntlabs/youtube-transcript-scraper").call(
    run_input=run_input, max_total_charge_usd=Decimal("0.05")
)

chunks = []
for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["type"] != "transcript" or row["status"] != "ok":
        continue  # skips the keyword summary row and videos without captions
    print(f"#{row['searchRank']} {row['title']} ({row['channelName']}): "
          f"{row['wordCount']:,} words, {row['videoDurationSeconds'] // 60} min")

    # about 60 seconds of speech per chunk, with a link that opens the video there
    text, start = [], None
    for seg in row["segments"]:
        start = seg["start"] if start is None else start
        text.append(seg["text"])
        if seg["end"] - start >= 60:
            chunks.append({"url": f"{row['url']}&t={int(start)}s", "text": " ".join(text)})
            text, start = [], None
    if text:
        chunks.append({"url": f"{row['url']}&t={int(start)}s", "text": " ".join(text)})

print(len(chunks), "chunks ready to embed")
print(chunks[0]["url"], chunks[0]["text"][:80])
