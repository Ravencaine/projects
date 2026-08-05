---
created: 2026-07-27
updated: 2026-08-02
source: "Stop Building Slow Power BI Reports: A Data Pro's Checklist"
source_url: "https://medium.com/@foodarchitects/stop-building-slow-power-bi-reports-a-data-pros-checklist-53990dbe770c"
note_type: pattern
tags: [incremental-refresh, append-only, large-tables, power-bi]
---

# Incremental Refresh Pattern

A Power BI configuration that limits refresh scope to recent partitions — dramatically reducing refresh time for append-only large tables like GA4 event data, daily sales feeds, and log data.

## Purpose

A table with 5 years of daily appends (1.8 million rows) refreshing fully on every schedule takes progressively longer as data accumulates. Incremental refresh partitions the table and only refreshes the recent partitions, leaving historical data untouched.

## When to Use

- Append-only tables: new rows are added, existing rows are never modified (GA4, POS sales, server logs)
- Large tables where full refresh takes > 30 minutes
- Scenarios where historical data never changes (only recent data is "live")

## Configuration

1. Right-click the table in Power BI → Incremental Refresh
2. Set **Store rows in the last** N days — historical partition boundary
3. Set **Refresh rows in the last** N days — how far back to look for new rows on each refresh
4. Enable the policy

## Structure

```
Table partitions:
  Partition 1: Historical (2020-01-01 to 2025-06-30) — never refreshed
  Partition 2: Recent (2025-07-01 to today)           — refreshed on schedule

On each scheduled refresh:
  → Only Partition 2 is touched
  → New rows appended to Partition 2
  → Partition 1 is locked and never re-queried
```

## Common Sources That Suit Incremental Refresh

- Google Analytics 4 (daily snapshot appends)
- POS sales systems
- Server/application logs
- IoT sensor data
- ERP transaction logs

## Related

- [[import-vs-directquery-performance]] — Import mode is required for incremental refresh
- [[column-pruning-bravo]] — prune unused columns before enabling incremental refresh to reduce partition size
