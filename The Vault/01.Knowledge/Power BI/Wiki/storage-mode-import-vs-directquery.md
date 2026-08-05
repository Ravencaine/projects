---
created: 2026-08-01
updated: 2026-08-02
source: "Power Query or DAX Make the Right Choice Every Time.md"
note_type: atomic
tags: [power-bi, storage-mode, import, directquery, beginner, performance]
---

# Storage Mode: Import vs DirectQuery

Before choosing Power Query or DAX, understand how data gets into Power BI — which is determined by storage mode.

## Import Mode (Default)

Data is compressed and loaded into Power BI's in-memory cache. Query speed is fast (data is in RAM).

- **Power Query:** ✅ Available — transform data before it loads
- **DAX:** ✅ Available — measures calculate against in-memory data
- **Refresh:** Scheduled or on-demand; full reload or incremental

Best for: small to medium datasets, fast interactive queries, most standard Power BI reports.

## DirectQuery Mode

Power BI connects to the data source and queries it in real time. No data is stored in the Power BI model.

- **Power Query:** ❌ Not available — cannot transform data before query
- **DAX:** ✅ Available — measures run as queries against the source
- **Refresh:** Real-time or near-real-time data

Best for: very large datasets, regulatory environments requiring live data, scenarios where Import would be impractical.

## The Power Query Limitation in DirectQuery

DirectQuery means Power BI sends DAX queries directly to the source database. Power Query's transformations happen during the Import phase — and in DirectQuery there is no Import phase.

If you're in DirectQuery, all data shaping must happen:
1. In the source database (SQL views, transformations)
2. In DAX measures (limited)

## Which Storage Mode Does Power Query Require?

**Power Query only works in Import mode.** If you need Power Query transformations, you cannot use DirectQuery — you must use Import mode (or Dual/Simple storage modes if you need a hybrid).

## Choosing Between Import and DirectQuery

| Factor | Import | DirectQuery |
|--------|--------|-------------|
| Dataset size | Up to ~1GB compressed | No practical limit |
| Query speed | Fastest (in-memory) | Slower (source query) |
| Power Query | ✅ | ❌ |
| Real-time data | ❌ (refresh lag) | ✅ |
| Complexity | Simpler | More complex |

## Related

- [[power-query-vs-dax-core-difference]] — what PQ and DAX each do; PQ requires Import
- [[power-query-vs-dax-model-size-performance]] — performance tradeoffs by storage mode
