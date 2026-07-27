---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, query]
---

# EVALUATE

Executes a DAX query and returns a result table.

## Signature

```dax
EVALUATE <table_expression>
```

## Examples

```dax
-- Return all products
EVALUATE 'Product'

-- Return filtered table
EVALUATE
FILTER('Product', 'Product'[List Price] > 100)

-- Grouped aggregation
EVALUATE
SUMMARIZECOLUMNS(
    'Product'[Category],
    'Date'[Year],
    "Total Sales", SUM(Sales[Amount])
)
ORDER BY 'Product'[Category], 'Date'[Year]
```

## EVALUATE Options

| Keyword | Purpose |
|---------|---------|
| `ORDER BY` | Sort results |
| `START AT` | Specify the starting value for ORDER BY |
| `DEFINE` | Define local measures, variables, tables |
| `TOPNSKIP` | Skip N rows then return top M |
| `EVALUATEANDLOG` | Return result and log to profiler |

## Notes

- EVALUATE is the primary keyword for DAX queries in DAX Studio, Power BI, and SSMS
- A query can include multiple EVALUATE statements, each returning a separate result set
- DEFINE creates measures that are local to the query — useful for testing without polluting the model
- EVALUATEANDLOG is for profiling and debugging — returns the value and logs it

## Related

- [[dax-queries]]
- [[summarizecolumns]]
