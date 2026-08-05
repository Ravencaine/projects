---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNTROWS

## Signature

```dax
COUNTROWS([<table>])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<table>` | *(Optional)* A table name or table expression. Defaults to the home table if omitted. |

## Returns

A whole number representing the count of rows in the table.

Returns **BLANK** when the table is empty.

## Examples

```dax
-- Count all rows in the Sales table
COUNTROWS('Sales')

-- Count rows where Amount exceeds 1000
COUNTROWS(FILTER('Sales', 'Sales'[Amount] > 1000))

-- Count related child rows (e.g., orders per customer)
COUNTROWS(RELATEDTABLE('Orders'))
```

## Notes

- Counts rows in a table — the standard way to count records in DAX.
- Defaults to the **home table** if no argument is provided (useful inside row-level contexts).
- Returns **BLANK** when the table is empty — handle this in measures that depend on it.
- Preferred over `COUNT` for counting rows rather than column values.
- Commonly paired with `FILTER` or `RELATEDTABLE` for conditional or related row counts.

## Related

- [[count]] — counts non-blank values in a column (different purpose)
- [[use-countrows-instead-of-count]] — guidance on when to prefer COUNTROWS
- [[relatedtable]] — returns the many-side table related to the current row context
