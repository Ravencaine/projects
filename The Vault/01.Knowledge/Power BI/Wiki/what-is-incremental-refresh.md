---
created: 2026-08-13
source: Incremental Refresh in Power BI — Explained Simply
source_url: https://medium.com/write-a-catalyst/incremental-refresh-in-power-bi-explained-simply-1b7daff5f5cb
note_type: atomic
tags: [power-bi, incremental-refresh, semantic-model, data-refresh]
---

# What Is Incremental Refresh

Incremental Refresh loads only the changed or new data from a source instead of reloading the entire dataset on every refresh.

## Purpose

Avoids re-fetching millions of historical rows on every refresh. Instead, the semantic model processes only recent or changed partitions — reducing refresh time from minutes/hours to seconds.

## How It Works

1. Define a **date/time column** as the partition key (typically an order date or transaction date)
2. Set a **lookback window** — how many periods to keep in the hot/fast partition
3. Set a **lookforward window** — how far ahead to monitor for new data
4. On each refresh, Power BI processes only the relevant window; historical data is untouched

## Key Concepts

| Term | Meaning |
|------|---------|
| Incremental refresh | Refreshes only a sliding window of data |
| Full refresh | Reloads the entire dataset |
| Range start / range end | Date boundaries that define partitions |
| Partition | A chunk of data filtered by date range |

## When to Use

- Large fact tables (100M+ rows)
- Slowly changing dimensions with frequent updates
- Any dataset where full refresh takes more than a few minutes

## Related

- [[Incremental-Refresh-Policy-Configuration]]
- [[Incremental-Refresh-vs-Full-Refresh]]
