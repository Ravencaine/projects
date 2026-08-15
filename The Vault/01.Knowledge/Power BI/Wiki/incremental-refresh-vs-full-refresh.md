---
created: 2026-08-13
source: Incremental Refresh in Power BI — Explained Simply
source_url: https://medium.com/write-a-catalyst/incremental-refresh-in-power-bi-explained-simply-1b7daff5f5cb
note_type: pattern
tags: [power-bi, incremental-refresh, full-refresh, comparison]
---

# Incremental Refresh vs Full Refresh

Side-by-side comparison of the two refresh strategies in Power BI semantic models.

## Comparison

| Dimension | Incremental Refresh | Full Refresh |
|-----------|--------------------|--------------------|
| Data loaded | Sliding window (recent rows only) | Entire dataset |
| Refresh time | Fast (seconds/minutes) | Slow (minutes/hours) |
| Premium requirement | Required | Not required (Pro supports full refresh) |
| XMLA endpoint | Required for Pro deployments | Not required |
| Historical data | Retained in model (archived partition) | Retained in model |
| First publish | Full historical load | Full load |
| Detect changes | Tracks via change detection column | Not applicable |

## When to Choose Incremental Refresh

- Table has 1M+ rows
- Refresh window needs to complete in under 5 minutes
- Data source has a datetime column suitable as a partition key
- Data changes are append-only (new rows) or have a reliable modified date

## When to Choose Full Refresh

- Small dataset (under 100K rows)
- No suitable datetime partition key
- Data changes require full recalculation
- Pro workspace without XMLA access

## Change Detection Column

For incremental refresh to detect modifications to existing rows (not just new rows), add a **change detection column** — a timestamp or version column Power BI can query to identify updated rows:

```sql
SELECT * FROM Orders
WHERE ModifiedDate >= DATEADD(day, -30, GETDATE())
```

Without a change detection column, only new rows are added on each refresh.

## Related

- [[What-Is-Incremental-Refresh]]
- [[Incremental-Refresh-Policy-Configuration]]
