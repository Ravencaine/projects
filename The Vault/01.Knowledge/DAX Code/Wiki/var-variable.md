---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, variable]
---

# VAR (Variables)

Defines a named variable that stores an intermediate result within a DAX expression.

## Signature

```dax
VAR <name> = <expression>
RETURN <result_expression>
```

## Parameters

| Term | Definition |
|------|------------|
| `name` | Variable name (no spaces, not case-sensitive) |
| `expression` | Any DAX expression evaluated once |
| `result_expression` | The final expression using the variable(s) |

## Examples

```dax
-- Store intermediate calculations
Profit Margin :=
VAR TotalSales = SUM(Sales[Amount])
VAR TotalProfit = SUM(Sales[Profit])
RETURN
    DIVIDE(TotalProfit, TotalSales)

-- Reuse a filtered table
Top Products :=
VAR TopRows =
    TOPN(10, ALLSELECTED(Product), [Sales], DESC)
RETURN
    COUNTROWS(TopRows)

-- Multiple variables
YoY Comparison :=
VAR SalesThisYear = [Sales]
VAR SalesLastYear = CALCULATE([Sales], SAMEPERIODLASTYEAR('Date'[Date]))
VAR Difference = SalesThisYear - SalesLastYear
RETURN
    DIVIDE(Difference, SalesLastYear)
```

## Notes

- Variables are evaluated **once** when the expression is first evaluated — not recalculated per row
- This makes them both **faster** (no repeated computation) and **correct** (stable values in row context)
- Variable names are case-insensitive but must be unique within an expression
- Variables capture the value in the current filter context — they are NOT evaluated in row context
- Prefer VAR over EARLIER for storing outer-row-context values
- Variables can hold tables or scalar values
- Multiple VAR statements can be chained before RETURN

## Related

- [[earlier]]
- [[dax-context]]
- [[use-variables-in-dax-formulas]]
