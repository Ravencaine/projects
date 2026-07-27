---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, fundamentals, column-reference, measure-reference, syntax]
---

# Column and Measure References

Article - 09/20/2022

## Column References

### Fully Qualified

`Table[Column]` — includes the table name. Always required when:
- Column names are ambiguous
- Writing measures (fully qualified is best practice)
- The formula is outside the table's context

### Unqualified

`[Column]` — omits the table name. Can be used when:
- In a calculated column on the same table
- No ambiguity exists

### In Measures

Measures must be fully qualified in most contexts:
```dax
[Sales Amount]           -- within the same measure table
'Sales'[Sales Amount]     -- from another table
```

## Measure References

Measures are model-level objects. They must be referenced by name (or fully qualified by table name).

### Scope of Measures

A measure is evaluated in the current **filter context** — it has no row context unless called from within one (e.g., inside CALCULATE in a calculated column, where context transition occurs).

### Circular References

Measures cannot reference themselves. DAX will return an error if you try to create a measure that references itself.

## Column References in Calculated Columns

In a calculated column, you can reference columns without qualification when they belong to the same table:

```dax
-- Both columns on the same table - unqualified is fine
Revenue = Quantity * Price

-- Column from another table - use RELATED
Tax = Revenue * RELATED('TaxRate'[Rate])
```

## Related

- [[dax-syntax]]
- [[dax-context]]
- [[measures-vs-calculated-columns]]
