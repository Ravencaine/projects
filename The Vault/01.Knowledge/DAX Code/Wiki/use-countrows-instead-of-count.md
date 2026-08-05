---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: pattern
tags: [dax, pattern, countrows, count]
---

# Use COUNTROWS Instead of COUNT

When counting rows in a table, prefer COUNTROWS over COUNT.

## Purpose

COUNTROWS counts the number of rows in a table (or table expression), which is more semantically correct and safer than COUNT, which counts non-blank values in a column.

## Components

- `COUNTROWS` — counts rows in a table
- `COUNT` — counts non-blank values in a column (does not support Boolean values)
- `COUNTA` — counts non-blank values in a column (supports Boolean values)
- `COUNTBLANK` — counts BLANK values in a column

## Structure

```dax
-- WRONG: COUNT on column
Number of Orders := COUNT('Sales'[OrderID])

-- CORRECT: COUNTROWS on table
Number of Orders := COUNTROWS('Sales')
```

## Example

```dax
-- Count rows in a filtered table
Orders Last 30 Days :=
COUNTROWS(
    FILTER(
        'Sales',
        'Sales'[OrderDate] >= TODAY() - 30
    )
)

-- Count rows in a related table
Products Ordered :=
COUNTROWS(RELATEDTABLE('Sales'))
```

## When to Use Each

| Function | Use when |
|----------|---------|
| `COUNTROWS` | Counting rows in a table — preferred |
| `COUNT` | Counting non-blank values in a single column (no Boolean support) |
| `COUNTA` | Counting non-blank values in a column (Boolean support) |
| `COUNTBLANK` | Counting BLANK values in a column |

## Related

- [[countrows]] — function
- [[count]] — function
- [[counta]] — function
- [[countblank]] — function
