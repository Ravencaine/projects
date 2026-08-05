---


title: "VAR (Return Variable)"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, variable]
note_type: pattern
description: "VAR — declares a named variable inside a DAX expression. Improves readability and performance by avoiding repeated subexpression evaluation. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# VAR

Declares a named variable (intermediate result) inside a DAX expression. The variable holds its computed value for reuse within the same expression.

## Syntax

```
VAR <name> = <expression>
RETURN <result_expression>
```

## Why Variables Matter

1. **Performance**: if an expression is used multiple times, computing it once and storing it avoids redundant evaluation
2. **Readability**: complex nested expressions become self-documenting
3. **Debugging**: intermediate values can be inspected

## Example

```dax
Profit Margin :=
VAR TotalSales = SUM( 'Sales'[Amount] )
VAR TotalCost  = SUM( 'Sales'[Cost] )
VAR Profit     = TotalSales - TotalCost
RETURN
    DIVIDE( Profit, TotalSales )
```

## Rules

- Variables are **immutable**: once set, cannot be reassigned within the same expression
- A variable can reference other variables declared earlier
- Variables are evaluated in the **filter context** at the point of declaration
- Variable names cannot conflict with column names in the same scope

## Common Pattern: Reuse FILTER Results

```dax
-- Without VAR: FILTER runs twice
CustomerCount :=
COUNTROWS(
    FILTER( Customer, [Sales] > 1000 )
)
-- With VAR: FILTER runs once
VAR HighValueCustomers = FILTER( Customer, [Sales] > 1000 )
RETURN COUNTROWS( HighValueCustomers )
```

## Related Functions

- `DIVIDE` — often paired with VAR for safe division
- `CALCULATE` — variables work inside CALCULATE as well

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
