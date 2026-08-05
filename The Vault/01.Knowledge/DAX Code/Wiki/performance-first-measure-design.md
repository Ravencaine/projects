---
created: 2026-08-01
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use (and How to Validate Them in Your Model).md"
note_type: atomic
tags: [dax, performance, var, iterator, sumx, calculate, storage-engine, formula-engine, intermediate]
---

# Performance-First Measure Design: Variables and Iterator Awareness

Correct DAX that takes 4 minutes to calculate might as well be wrong. Lift expensive calculations out of iterators.

## Pattern 1: Lift Expensive Measures Out of Iterators

```c
-- SLOW: calculates AvgFrequency and RetentionYears for every customer
Customer Lifetime Value =
SUMX(
    VALUES(Customer[CustomerID]),
    CALCULATE(
        SUM(Sales[Amount]) *
        (1 + [Average Order Frequency]) *
        [Predicted Retention Years]
    )
)
```

```c
-- FAST: calculate expensive measures once, then iterate cheaply
Customer Lifetime Value =
VAR AvgFrequency = [Average Order Frequency]
VAR RetentionYears = [Predicted Retention Years]
VAR MultiplierConstant = 1 + AvgFrequency

VAR Result =
    SUMX(
        VALUES(Customer[CustomerID]),
        CALCULATE(SUM(Sales[Amount])) * MultiplierConstant * RetentionYears
    )
RETURN Result
```

**Before:** 3 min 47 sec | **After:** 4.2 sec — 54x faster.

## Pattern 2: Push Filters to CALCULATE, Not Inside Iterators

```c
-- SLOW: iterator filters every row one by one
Result =
SUMX(
    FILTER(Sales, Sales[Amount] > 1000),
    Sales[Quantity]
)

-- FAST: Storage Engine filters before iteration
Result =
CALCULATE(
    SUMX(Sales, Sales[Quantity]),
    Sales[Amount] > 1000
)
```

CALCULATE with a filter argument pushes the filter to the Storage Engine (fast). FILTER inside SUMX forces Formula Engine evaluation per row (slow).

## Pattern 3: Avoid Iterators When Aggregation Works

```c
-- SLOW: row-by-row iteration
Slow Profit =
SUMX(
    Sales,
    Sales[Quantity] * (Sales[Price] - Sales[Cost])
)

-- FAST: let the engine aggregate
Fast Profit =
SUM(Sales[Quantity]) * AVERAGE(Sales[Price] - Sales[Cost])

-- FASTEST: pre-calculate in a calculated column
-- Extended Price = Sales[Quantity] * Sales[UnitPrice]
-- Then: SUM(Sales[Extended Price])
```

Trade-off: calculated columns increase model size but dramatically speed up frequently-used calculations on large fact tables.

## Pattern 4: Materialize Filter Context Early

```c
-- SLOW: context changes inside iterator
Slow Version =
SUMX(
    Products,
    CALCULATE([Sales], USERELATIONSHIP(Sales[ProductKey], Products[ProductKey]))
)

-- FAST: capture context once, then iterate
Fast Version =
VAR FilteredSales =
    CALCULATETABLE(
        Sales,
        USERELATIONSHIP(Sales[ProductKey], Products[ProductKey])
    )
RETURN
    SUMX(FilteredSales, Sales[Amount])
```

## Pattern 5: Pre-Aggregate with Calculated Columns (When Appropriate)

For calculations used across 10+ measures on large fact tables:
```c
-- Calculated column
Extended Price = Sales[Quantity] * Sales[UnitPrice]

-- Measure
Measure = SUM(Sales[Extended Price])
```

Model size increases; query speed improves dramatically. Appropriate for facts with 10M+ rows.

## Related

- [[defensive-dax-error-handling]] — VAR for correctness alongside performance
- [[context-transition-architecture]] — context transition performance cost
- [[dax-studio-performance-validation]] — how to measure and validate performance
