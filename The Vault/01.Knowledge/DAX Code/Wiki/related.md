---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, relationship]
---

# RELATED

## Signature

```dax
RELATED(<column>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<column>` | A column from the related table to retrieve the value from. |

## Returns

The value in the specified column for the related row.

## Examples

```dax
-- In a Sales calculated column, fetch the product's color
RELATED('Product'[Color])

-- In a Sales calculated column, fetch the year from the Date table
RELATED('Date'[Year])
```

## Notes

- Requires **row context**: typically used inside a calculated column or row-level expression.
- Follows the **active relationship** from the many-side table to the one-side table.
- Works in calculated columns and inside `CALCULATE` filter arguments.
- **Cannot** fetch from the many-side of a one-to-many relationship (the relationship must go from the current table outward).
- For **inactive relationships**, use `USERELATIONSHIP` instead.

## Related

- [[relatedtable]] — returns a table of all rows related to the current row
- [[userexplicitrelationship]] — activates an inactive relationship
- [[calculate]] — context for where RELATED often appears
