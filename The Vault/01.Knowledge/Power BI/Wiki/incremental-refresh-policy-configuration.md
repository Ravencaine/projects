---
created: 2026-08-13
source: Incremental Refresh in Power BI — Explained Simply
source_url: https://medium.com/write-a-catalyst/incremental-refresh-in-power-bi-explained-simply-1b7daff5f5cb
note_type: pattern
tags: [power-bi, incremental-refresh, configuration, policy]
---

# Incremental Refresh Policy Configuration

Step-by-step setup for Incremental Refresh on a Power BI semantic model.

## Prerequisites

- A date/time column in the table (used as the partition key — must be a datetime column, not just a date)
- Premium capacity (Pro requires XMLA endpoint for incremental refresh via deployment pipelines)
- The table must be in **Import mode** or **Composite model**

## Components

- **Range start column** — the datetime column that defines the refresh window
- **Range end column** — optional; used for range boundaries
- **Store rows in the last N** — number of days/periods to keep in the fast partition
- **Refresh rows in the last N** — how many days to look back for changes (detect changes)

## Structure

### Step 1 — Enable Incremental Refresh
1. Right-click the table in the Fields pane → **Incremental refresh and real-time**
2. Power BI creates two hidden parameters: `RangeStart` and `RangeEnd`
3. Apply a filter on the date column: `DateColumn >= RangeStart AND DateColumn < RangeEnd`

### Step 2 — Configure Policy
- **Store rows in the last N days**: how much historical data to keep in the import
- **Refresh rows in the last N days**: how far back to detect changes on each refresh

### Step 3 — Publish and Refresh
```text
First publish    → full historical load (one-time)
Subsequent runs  → only N-day window refreshed
```

## Example

```m
// Power Query filter applied to the date column
Table.SelectRows(
    Source,
    each [OrderDate] >= RangeStart and [OrderDate] < RangeEnd
)
```

## Gotcha

The `RangeStart`/`RangeEnd` parameters are automatically injected by Power BI — do not set their values manually. The filter must be applied in Power Query, not in the model relationships.

## Related

- [[What-Is-Incremental-Refresh]]
- [[Incremental-Refresh-vs-Full-Refresh]]
