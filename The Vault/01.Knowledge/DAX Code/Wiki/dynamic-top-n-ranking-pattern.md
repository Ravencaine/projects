---
created: 2026-07-30
updated: 2026-08-02
source: Dynamic Ranking in DAX How I Built a Top 5 Dashboard That Actually Worked.md
note_type: pattern
tags: [dax, ranking, top-n, rankx, pattern]
---

# Dynamic Top N Ranking Pattern

Control what the ranking universe is by choosing exactly which filters ALL() removes.

## Purpose

Display the top N items (customers, products, regions) dynamically within any filter context — without the ranking universe shifting unexpectedly when users interact with slicers.

## Components

- `RANKX()` — ranks each item within a specified table/column set
- `ALL()` / `ALLSELECTED()` — controls what the ranking universe includes
- `IF()` + `BLANK()` — hides non-top-N rows cleanly

## Structure

```dax
Customer Rank =
RANKX (
    ALL ( Customers[CustomerName] ),   -- ranking universe
    [Total Sales],                     -- measure to rank by
    ,                                  -- ties: default (skip rank)
    DESC                               -- highest = rank 1
)

Top N Sales =
IF (
    [Customer Rank] <= 5,
    [Total Sales],
    BLANK ()
)
```

## Example

Rank customers globally regardless of any slicer filter on Product Category:

```dax
Customer Rank Global =
RANKX (
    ALL ( Customers[CustomerName] ),
    [Total Sales],
    ,
    DESC
)
```

Combined with a dynamic Top N visual:

```dax
Top 5 Customer Sales =
IF (
    [Customer Rank Global] <= 5,
    [Total Sales],
    BLANK ()
)
```

## Variations

| Scenario | Rank Universe |
|----------|--------------|
| Global top N (ignores all filters) | `ALL( Table[Column] )` |
| Top N within current slicer selection | `ALLSELECTED( Table[Column] )` |
| Top N within a specific dimension | `ALL( DimProduct[Category] )` then partition |

**Using CALCULATE to restore specific filters:**

```dax
Customer Rank By Category =
RANKX (
    ALL ( Customers[CustomerName] ),
    CALCULATE ( [Total Sales], REMOVEFILTERS ( 'Product'[Category] ) ),
    ,
    DESC
)
```

This ranks customers within their category while still respecting other active filters.

## Performance Note

On large datasets, RANKX re-evaluates for every row context. Wrap in VAR to cache intermediate results:

```dax
Customer Rank Optimized =
VAR BaseTable = ALL ( Customers[CustomerName] )
VAR SalesValue = [Total Sales]
RETURN
    RANKX ( BaseTable, SalesValue, , DESC )
```

This stores the base table and measure value once, avoiding repeated evaluation. Reported ~30% performance improvement.

## Related

- [[rankx]] — core function
- [[all]] — ALL vs ALLSELECTED for ranking universe control
- [[top-n-parameter-slicer-pattern]] — user-driven Top N via slicer
- [[top-n-others-union-pattern]] — Top N + Others aggregate bar
- [[use-selectedvalue-instead-of-values]] — reading the N value from a slicer
