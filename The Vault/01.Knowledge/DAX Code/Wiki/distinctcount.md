---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# DISTINCTCOUNT

## Signature

```dax
DISTINCTCOUNT(<column>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<column>` | The column to count distinct (unique) values from. |

## Returns

A number representing the count of distinct values in the column.

## Examples

```dax
-- Count unique customers who made a purchase
DISTINCTCOUNT('Sales'[CustomerKey])

-- Distinct count in a measure with filters
CALCULATE(DISTINCTCOUNT('Sales'[ProductKey]), 'Sales'[Amount] > 0)
```

## Notes

- Counts **unique values INCLUDING BLANK**: blank is treated as a distinct value.
- Use `DISTINCTCOUNTNOBLANK` to exclude blank from the count.
- The **only** argument is a column — pass a table expression (like `DISTINCTCOUNT(FILTER(...))`) using `DISTINCTCOUNTNOBLANK` or `COUNTROWS(DISTINCT(...))` instead.
- **Not supported** in DirectQuery mode for calculated columns or row-level security (RLS) rules.
- Useful for metrics like "unique customers," "distinct products sold," etc.

## Related

- [[distinct]] — returns the distinct values as a table (not a count)
- [[countrows]] — counts rows; often used alongside distinct value analysis
- [[values]] — returns all distinct values including blank (table context)
