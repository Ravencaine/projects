---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, relationship, filter]
---

# RELATEDTABLE

Evaluates a table expression in a context modified by the given filters. Equivalent to `CALCULATETABLE` with no logical expression.

## Syntax

```dax
RELATEDTABLE(<tableName>)
```

## Parameters

| Term | Definition |
|------|------------|
| `tableName` | The name of an existing table using standard DAX syntax. It cannot be an expression. |

## Return Value

A table of values.

## Remarks

`RELATEDTABLE` changes the context in which the data is filtered and evaluates the expression in the new context. It is a shortcut for `CALCULATETABLE` with no logical expression.

- Use `RELATEDTABLE` to fetch related rows from the many side of a relationship
- Unlike `RELATED`, which returns a scalar value, `RELATEDTABLE` returns a table
- `RELATEDTABLE` is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules
- Equivalent to: `CALCULATETABLE(<tableName>)` with no filter conditions

## Example

```dax
-- Count orders for the current row's product (many-side)
COUNTROWS(RELATEDTABLE('InternetSales_USD'))
```

## Related

- [[related]] — fetch a scalar value from the one-side of a relationship
- [[calculatetable]] — more general form with explicit filter expressions
- [[calculate]] — modifies filter context for scalar expressions
