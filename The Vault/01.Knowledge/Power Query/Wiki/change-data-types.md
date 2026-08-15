---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, data-types, type-conversion]
---

# Change Data Types

Convert columns to the correct type — text, number, date, etc. Required before building accurate visuals.

## Purpose

Power Query infers types at import time, often incorrectly (text vs number, text vs date). Wrong types cause incorrect aggregations, broken visuals, and silent calculation errors.

## Components

- `Table.TransformColumnTypes`

## Structure

```m
Table.TransformColumnTypes(
    Source,
    {
        {"ColumnName", type text},
        {"NumericCol", type number},
        {"DateCol", type date}
    }
)
```

## Example

```m
Table.TransformColumnTypes(
    Source,
    {
        {"CustomerID", type text},
        {"Revenue", type number},
        {"OrderDate", type date}
    }
)
```

## Common Type Literals

| Type | M literal |
|------|-----------|
| Text | `type text` |
| Whole number | `type number` |
| Decimal | `type number` |
| Date | `type date` |
| DateTime | `type datetime` |
| Boolean | `type logical` |

## Gotcha

If the column contains errors or mismatched values before conversion, `Table.TransformColumnTypes` throws an error. Clean with [[Replace-Values]] first.

## Related

- [[Replace-Values]] — remove non-numeric tokens before numeric conversion
- [[Trim-and-Clean-Text]] — remove corrupt characters before text conversion
