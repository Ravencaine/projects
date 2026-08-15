---
created: 2026-08-09
updated: 2026-08-09
source: "Data Analysis Expressions (DAX) in Power BI.md"
note_type: atomic
tags: [dax, virtual-table, debugging, calculated-table, iterator, summarize]
---

# Virtual Table Debugging via Calculated Tables

When a virtual table expression (FILTER, SUMMARIZE, ADDCOLUMNS, etc.) produces unexpected results inside a measure, create a physical calculated table in Power BI Desktop to inspect its output directly.

## Technique

1. Identify the virtual table expression in your measure
2. Copy the table expression (without CALCULATE wrapping)
3. In Power BI Desktop: **Modeling** → **New table**
4. Paste the expression and name it
5. Inspect the resulting table to verify row count, columns, and values

## Example

```dax
-- Problem: this measure returns wrong numbers
Some Measure =
CALCULATE(
    [Sales Amount],
    FILTER(
        SUMMARIZE(Sales, 'Date'[Year], Product[Category]),
        [Sales Amount] > 1000
    )
)

-- Debug step: create this as a calculated table
DebugTable =
SUMMARIZE(Sales, 'Date'[Year], Product[Category])
```

Inspect DebugTable — check row count, columns, and which rows have [Sales Amount] > 1000 before adding the FILTER condition.

## Common Virtual Table Patterns to Debug

| Pattern | Use when |
|---------|---------|
| `FILTER(table, condition)` | Checking which rows survive the filter |
| `SUMMARIZE(...)` | Verifying grouping columns and granularity |
| `ADDCOLUMNS(...)` | Confirming calculated column values |
| `CALCULATETABLE(...)` | Checking pre-filtered table before aggregation |
| `UNION(...)` | Confirming row counts across combined tables |

## When to Use

- Virtual table produces fewer/more rows than expected
- Measure returns unexpected values
- SUMMARIZE grouping is not producing the expected granularity
- Debugging complex CALCULATE with multiple filter arguments

## Why It Works

Virtual tables exist only during measure evaluation and are invisible. Creating a physical table materializes the same logic so you can see exactly what the engine sees — same expression, same context, visible output.

## Related

- [[calculate]] — CALCULATE and filter context
- [[filter-context-vs-row-context]] — context understanding
- [[dax-debugging-tocsv]] — outputting intermediate results
