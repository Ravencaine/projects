---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, fill-down, fill-up, forward-fill]
---

# Fill Down / Up

Propagate the last known value into blank (null) cells — common in Excel-style pivoted data.

## Purpose

Handle sparse data where a category label appears once at the top of a group and nulls fill the rest. Common after unpivoting or importing from report grids.

## Components

- `Table.FillDown`
- `Table.FillUp`

## Structure

```m
// Fill nulls downward (carry last value down)
Table.FillDown(Source, {"Column1", "Column2"})

// Fill nulls upward (carry next value up)
Table.FillUp(Source, {"Column1", "Column2"})
```

## Example

```m
// Fill Region down to cover each block of rows
Table.FillDown(Source, {"Region"})

// Fill upward for sparse monthly data where future values backfill
Table.FillUp(Source, {"ForecastValue"})
```

## Variations

| Direction | M function | Use case |
|-----------|------------|---------|
| Down | `Table.FillDown` | Category labels at top of group |
| Up | `Table.FillUp` | Values that backfill from below |
| UI: Transform → Fill → Down | `Table.FillDown` | Same |
| UI: Transform → Fill → Up | `Table.FillUp` | Same |

## Related

- [[Unpivot-Columns]] — common source of nulls that need filling
- [[Group-By]] — alternative for structured aggregation
