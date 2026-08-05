---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Data Cleaning Checklist Before Creating Dashboards 12 Essential Steps That Save Hours of Rework.md
note_type: pattern
tags: [power-bi, pattern, data-quality, hidden-page, monitoring, trust, refresh]
---

# Data Quality Page Pattern

A hidden Power BI tab that monitors data health metrics, catching data corruption and quality issues before end users encounter them. The most important quality control mechanism that never appears in the final dashboard.

## Purpose

When the underlying database changes, this page surfaces the impact immediately. Stakeholders stop asking "is this data right?" — you can answer before they ask.

## What to Include

Quick counts and metrics for every critical field:

| Metric | What It Detects |
|---|---|
| Total rows imported | Unexpected jumps or drops in data volume |
| Blank/NULL count per critical field | Missing data creeping in |
| Duplicate record count | New data sources introducing duplicates |
| Max/Min date | Stale data, future dates, or system migration gaps |
| Distinct count per key field | Unexpected new categories or entities |

## How to Build It

1. Create a new report page
2. Set page visibility to **Off** (right-click tab → Hide)
3. Add KPI cards or a small Matrix showing the metrics above
4. Use `Table.SelectRows` counts or direct column statistics

## Refresh Status Indicator (Bonus)

Add a single card at the top corner of every report page:

```
Data Last Refreshed: July 30, 2026 – 09:15 AM IST
```

Implementation in Power Query — create a new blank query and enter:
```m
= DateTime.LocalNow()
```

Set to hidden in the model. Reference it in a measure for display.

This single card eliminates "is this data current?" questions entirely.

## Key Principle

A dashboard is only as trustworthy as its worst unvalidated number. A data quality page makes trust-building automatic and permanent.

## Related

- [[power-query-data-cleaning-checklist]] — `pattern`
- [[pre-dashboard-cleaning-checklist-reference]] — `reference`
