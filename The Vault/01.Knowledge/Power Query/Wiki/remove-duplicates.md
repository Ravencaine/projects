---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, remove-duplicates]
---

# Remove Duplicates

Remove rows that appear more than once based on one or more columns.

## Purpose

Eliminate redundant records before analysis. Critical before building relationships — duplicate keys cause cardinality warnings and incorrect joins.

## Components

- `Table.Distinct`

## Structure

```m
Table.Distinct(Source, {"Column1", "Column2"})
```

Without column specification, `Table.Distinct` removes fully identical rows across all columns.

## Example

```m
// Remove duplicate CustomerID rows, keep all other columns
Table.Distinct(Source, {"CustomerID"})
```

## Variations

| Scope | M equivalent |
|-------|-------------|
| All columns identical | `Table.Distinct(Source)` |
| Specific columns | `Table.Distinct(Source, {"Col1", "Col2"})` |
| UI: Home → Remove Rows → Remove Duplicates | Same as `Table.Distinct` |

## Related

- [[Group-By]] — aggregation after deduplication
