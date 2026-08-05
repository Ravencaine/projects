---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX - The Power of Variables (VAR).md"
note_type: atomic
tags: [dax, var, table-variable, topn, summarize, calculatetable, intermediate]
---

# Table Variables in DAX

DAX `VAR` can hold **table expressions**: not just scalar values. Table variables are evaluated once and then referenced repeatedly, making complex table operations efficient and readable.

## What Makes a Table Variable

Any expression that returns a table can be stored in a `VAR`:

```dax
VAR <table_variable> = <table_expression>
```

Examples: `SUMMARIZE`, `TOPN`, `FILTER`, `CALCULATETABLE`, `VALUES`, `ALL`, `DISTINCT`.

## Pattern: TOPN + CALCULATETABLE

The source article's example — find the top 5 customers by revenue:

```dax
Top 5 Customers =
VAR TopCustomers =
    TOPN (
        5,
        SUMMARIZE (
            Sales,
            Sales[Customer],
            "TotalSales", SUM ( Sales[Revenue] )
        ),
        [TotalSales],
        DESC
    )
RETURN
CALCULATETABLE (
    Sales,
    TopCustomers
)
```

`SUMMARIZE` builds the ranking table once. `CALCULATETABLE` then filters the Sales table to only those customers.

## Why Table Variables Matter

1. **Efficiency:** the table expression is evaluated once, not every time it's referenced
2. **Readability:** the intermediate table has a named variable instead of a nested wall of code
3. **Composability:** the table variable can be used in multiple contexts (CALCULATETABLE, FILTER, SUMMARIZE again)

## Common Table Variable Patterns

### Pattern: Filtered Segment

```dax
VAR HighValueCustomers =
    FILTER (
        SUMMARIZE (
            Sales,
            Sales[Customer],
            "TotalSales", SUM ( Sales[Revenue] )
        ),
        [TotalSales] > 10000
    )
RETURN
CALCULATETABLE ( Sales, HighValueCustomers )
```

### Pattern: Ranked Table

```dax
VAR RankedProducts =
    ADDMISSINGITEMS (
        'Product'[Product],
        SUMMARIZE (
            Sales,
            Sales[Product],
            "Revenue", SUM ( Sales[Revenue] )
        ),
        'Product'[Product]
    )
```

### Pattern: Date Table Reference

```dax
VAR AllDates = VALUES ( 'Date'[Date] )
VAR FiscalYearDates =
    FILTER ( AllDates, 'Date'[FiscalYear] = 2025 )
RETURN
CALCULATE (
    [Total Sales],
    FiscalYearDates
)
```

## Table Variables and Filter Context

Table variables capture the filter context **at the point of definition**: not at the point of use in `RETURN`. This matters when the `RETURN` expression wraps the variable in `CALCULATE`, `FILTER`, or `SUMMARIZE`.

```dax
VAR CustomerTable = VALUES ( Sales[Customer] )
RETURN
CALCULATETABLE (
    'Product',
    CustomerTable   -- filtered by the current filter context
)
```

## Limitations of Table Variables

- Table variables cannot be used in a `RETURN` that expects a scalar (error if `RETURN` is a table but the measure context expects a scalar — use `COUNTROWS`, `SUMX`, etc.)
- A table variable is **not** a materialised table in memory — it is a virtual table evaluated when referenced
- Very large table variables can still consume significant memory during evaluation

## Related

- [[var-syntax-and-pattern]] — scalar VAR syntax
- [[var-calculate-filter-composition]] — combining table VAR with CALCULATE
- [[iterator-functions-sumx]] — row-level iteration over tables (related evaluation pattern)
