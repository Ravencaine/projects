---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, group-by, aggregation, summarize]
---

# Group By

Aggregate rows into summary rows — sum, average, count per group.

## Purpose

Reduce row count by grouping on categorical columns and computing aggregates. Common first step for building summary fact tables.

## Components

- `Table.Group`

## Structure

```m
Table.Group(
    Source,
    {"GroupCol1", "GroupCol2"},
    {
        {"AggregatedColName", each List.Sum([Column]), type number},
        {"CountRows", each Table.RowCount(_), Int64.Type}
    }
)
```

## Example

```m
// Total revenue and order count per region
Table.Group(
    Source,
    {"Region"},
    {
        {"TotalRevenue", each List.Sum([Revenue]), type number},
        {"OrderCount", each Table.RowCount(_), Int64.Type}
    }
)
```

## Aggregation Functions

| Function | Returns |
|----------|--------|
| `List.Sum` | Sum |
| `List.Average` | Average |
| `List.Count` | Count of non-null values |
| `List.Max` | Maximum |
| `List.Min` | Minimum |
| `Table.RowCount` | Total row count including nulls |

## Related

- [[Remove-Duplicates]] — deduplicate before grouping
- [[Unpivot-Columns]] — reshape wide data before aggregating
- [[Merge-Queries]] — enrich grouped result with lookup tables
