---
created: 2026-08-01
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use (and How to Validate Them in Your Model).md"
note_type: atomic
tags: [dax, context-transition, calculate, all, allexcept, filter-context, row-context, architecture, intermediate]
---

# Context Transition Architecture

Every CALCULATE creates a context transition — row context becomes filter context. Explicit naming makes transitions intentional, not accidental.

## The Problem

```c
Customer % of Total =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), ALL(Sales))
)
```

Works in a table. Then in a card visual with one region filtered → shows 100% for every region. Then in a calculated column → errors.

Root cause: context transitions happen whether you control them or not.

## The Pattern: Explicit Context Control

```c
-- Base measure (respects current filter context)
_Sales = SUM(Sales[Amount])

-- Controlled context removal — named explicitly
_Sales All Customers = CALCULATE([_Sales], ALL(Customer))

-- Selective removal — remove ALL customers, restore region filter
_Sales All Except Region =
CALCULATE(
    [_Sales],
    ALL(Sales),
    VALUES(Region[Region])
)

-- Final ratio with VAR for clarity
Customer % of Total =
VAR CurrentSales = [_Sales]
VAR TotalSales = [_Sales All Customers]
RETURN
    DIVIDE(CurrentSales, TotalSales, 0)
```

Every context transition is intentional and named.

## Context Transition Options

| Function | What it does | When to use |
|----------|-------------|-------------|
| `ALL()` | Removes all filters | Grand total denominator |
| `ALLEXCEPT()` | Removes filters except specified | All-of-category-but-per-row |
| `REMOVEFILTERS()` | Removes filters, no return value | Same as ALL in modern DAX |
| `KEEPFILTERS()` | Adds filter, doesn't overwrite | When intersection matters |
| `VALUES()` | Returns current filter values | Restore specific filters |
| `ALLSELECTED()` | Returns user-applied filters | Visual-level totals |

## Validation Test 1: The Three Visual Test

Take any measure with ALL/ALLEXCEPT/REMOVEFILTERS:

1. Put in a table visual with row details
2. Put in a card visual with one filter applied
3. Put in a matrix with row and column dimensions

If numbers change unexpectedly → context transitions are accidental.

## Validation Test 2: DAX Studio Query Analysis

```c
EVALUATE
ADDCOLUMNS(
    VALUES(Customer[CustomerName]),
    "Sales", [_Sales],
    "Total Sales", [_Sales All Customers],
    "% of Total", [Customer % of Total]
)
ORDER BY [% of Total] DESC
```

Check:
- "Total Sales" column = same value for every row
- Sum of "% of Total" ≈ 100%
- Removing VALUES() wrapper returns correct totals

## Validation Test 3: The Calculated Column Test

```c
Test Column = [Your Measure]
```

If it errors or returns BLANK consistently → measure relies on external filter context rather than managing its own. Measures that work in visuals but not in calculated columns have uncontrolled transitions.

## Common Trap: Uncontrolled Sales per Employee

```c
-- WRONG: denominator changes with filter context
Sales per Employee =
DIVIDE(
    SUM(Sales[Amount]),
    DISTINCTCOUNT(Employee[EmployeeID])
)
```

In a table by employee name → each row = total sales / 1 = meaningless.
In a bar chart by department → total dept sales / distinct employees in current filter context (changes with slicers).

```c
-- RIGHT: denominator is explicit and controlled
_Employee Count All =
CALCULATE(
    DISTINCTCOUNT(Employee[EmployeeID]),
    ALL(Employee)
)

Sales per Employee =
DIVIDE([_Sales], [_Employee Count All], 0)
```

## Related

- [[measure-branching-naming-conventions]] — context transitions within branching hierarchy
- [[defensive-dax-error-handling]] — BLANK() vs ERROR() when context yields no data
- [[performance-first-measure-design]] — context transition performance cost
