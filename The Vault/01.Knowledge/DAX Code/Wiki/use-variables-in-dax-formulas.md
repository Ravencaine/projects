---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: pattern
tags: [dax, pattern, variables]
---

# Use Variables to Improve DAX Formulas

Variables (VAR) store intermediate results, improve performance, readability, and reliability of DAX formulas.

## Purpose

Complex DAX formulas often repeat the same expression multiple times. Variables eliminate repetition, make formulas self-documenting, and can improve performance by avoiding redundant calculations.

## Components

- `VAR` — declares a named variable and assigns it the result of an expression
- `RETURN` — specifies the final expression that uses the variable(s)

## Structure

```dax
MeasureName :=
VAR VariableName1 = <expression1>
VAR VariableName2 = <expression2>
RETURN
    <final expression using variables>
```

## Example

```dax
Sales YoY Change :=
VAR SalesCurrentYear = [Total Sales]
VAR SalesPriorYear = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN
    DIVIDE(SalesCurrentYear - SalesPriorYear, SalesPriorYear)
```

### Variable as Documentation

```dax
High Margin Products :=
VAR AvgMargin = AVERAGE('Product'[Margin])
RETURN
    COUNTROWS(
        FILTER('Product', 'Product'[Margin] > AvgMargin)
    )
```

### Debug with Variables

```dax
-- Temporarily return a variable to inspect its value during development
VAR Result = CALCULATE([Sales], 'Product'[Color] = "Red")
RETURN
    Result  -- switch between Result and intended RETURN expression to debug
```

## Benefits

1. **Performance**: expression is evaluated once instead of N times
2. **Readability**: meaningful variable names explain intent
3. **Debugging**: return individual variables to inspect intermediate values
4. **Maintainability**: change the expression in one place, not N

## Related

- [[var-variable]] — function
- [[calculate]] — function
