---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# SUMX

## Signature

```dax
SUMX(<table>, <expression>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<table>` | The table to iterate over. |
| `<expression>` | The expression evaluated per row to produce the value to sum. |

## Returns

A decimal number representing the sum of the evaluated expression across all rows.

## Examples

```dax
-- Sum of quantity multiplied by price per row
SUMX('Sales', 'Sales'[Quantity] * 'Sales'[Price])

-- With a filter applied via CALCULATE
SUMX(
    CALCULATE('Sales', 'Sales'[Region] = "West"),
    'Sales'[Quantity] * 'Sales'[Price]
)
```

## Notes

- **Iterator function** — loops over table rows, introducing row context for each iteration.
- The `<expression>` is evaluated in row context — column references refer to the current row.
- Use when the sum requires a **row-level calculation** (e.g., Quantity × Price).
- BLANK rows in the expression result are **skipped** — not treated as zero.
- Logical values and text in the expression result are **ignored**.
- For simple column totals without row-level computation, prefer `SUM`.

## Related

- [[sum]] — simple column sum without row-level computation
- [[calculate]] — often used to pre-filter the table before iteration
- [[filter]] — used to narrow the iterated table
