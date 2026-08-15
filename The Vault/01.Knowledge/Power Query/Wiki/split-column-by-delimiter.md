---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, split-column, text-transformation]
---

# Split Column by Delimiter

Break a single column into multiple columns based on a delimiter (e.g., split `"FirstName LastName"` into two columns).

## Purpose

Many data exports concatenate multiple fields into one column. Splitting exposes individual fields for filtering, grouping, and joining.

## Components

- `Table.SplitColumn`

## Structure

```m
Table.SplitColumn(
    Source,
    "ColumnName",
    Splitter.SplitTextByDelimiter(","),  // or other splitter
    {"NewCol1", "NewCol2"}
)
```

## Example

```m
// Split "FirstName LastName" into two columns
Table.SplitColumn(
    Source,
    "FullName",
    Splitter.SplitTextByEachDelimiter({" "}, QuoteStyle.None),
    {"FirstName", "LastName"}
)

// Split by comma (common for CSV-like fields)
Table.SplitColumn(
    Source,
    "Categories",
    Splitter.SplitTextByDelimiter(","),
    {"Category1", "Category2", "Category3"}
)
```

## Variations

| Splitter | Use case |
|----------|---------|
| `Splitter.SplitTextByDelimiter(",")` | Comma-separated values |
| `Splitter.SplitTextByEachDelimiter({" ", "-"})` | Multiple delimiters |
| `Splitter.SplitTextByPositions({3, 7})` | Fixed-width split |
| UI: Transform → Split Column → By Delimiter | Calls `Table.SplitColumn` |

## Related

- [[Trim-and-Clean-Text]] — clean delimiters before splitting
- [[Replace-Values]] — standardise inconsistent delimiters first
