---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, measure, use-cases, beginner, aggregation]
---

# DAX Measure Use Cases

Measures are for numbers that change based on report context — anything that aggregates, compares, or computes a ratio where the result should differ depending on what is filtered. These are the situations where a measure (not a calculated column) is the right choice.

## Use Case 1: Basic Aggregation

Any sum, average, count, minimum, or maximum.

```dax
Total Sales = SUM(Sales[SalesAmount])
Average Order Value = AVERAGE(Orders[OrderAmount])
Order Count = COUNTROWS(Orders)
Distinct Customers = DISTINCTCOUNT(Orders[CustomerID])
```

The foundational measure type. Every report needs these.

## Use Case 2: Dynamic Comparison (YoY, MoM, vs Target)

Comparisons that adapt to whatever time period or dimension is selected.

```dax
Sales YoY % =
VAR CurrentYear = SUM(Sales[SalesAmount])
VAR PreviousYear =
    CALCULATE(
        SUM(Sales[SalesAmount]),
        DATEADD(Calendar[Date], -1, YEAR)
    )
RETURN
DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0)
```

When sliced by region, this shows regional YoY. When sliced by product, this shows per-product YoY. The same measure adapts automatically.

## Use Case 3: Ratio or Percentage

Any proportion calculation where the denominator is an aggregate.

```dax
% of Total Sales =
DIVIDE(
    SUM(Sales[SalesAmount]),
    CALCULATE(SUM(Sales[SalesAmount]), ALL(Products)),
    0
)
```

This computes each product's share of total sales — the percentage changes based on the product filter, which is exactly what you want.

## Use Case 4: % of Total with Correct Totals

The measure form of this ensures correct totals (unlike the [[calculated-column-vs-measure-total-sums|column trap]]):

```dax
Margin % =
DIVIDE(
    SUM(Sales[Revenue]) - SUM(Sales[Cost]),
    SUM(Sales[Revenue]),
    0
)
```

At the total row: uses total revenue and cost → correct total margin %. At each category row: uses category totals → correct category margin %.

## Use Case 5: KPIs and Single Values

```dax
Total Customers = DISTINCTCOUNT(Sales[CustomerID])
Revenue Target = SUM(Targets[TargetAmount])
Achievement % = DIVIDE([Total Sales], [Revenue Target], 0)
```

Card visuals, KPI gauges, and trend indicators — all measures.

## Use Case 6: Conditional Aggregation

Aggregations that apply different logic based on conditions.

```dax
Total Revenue =
SUMX(
    Sales,
    IF(Sales[Channel] = "Online",
        Sales[Quantity] * Sales[UnitPrice] * 0.95,   // 5% discount for online
        Sales[Quantity] * Sales[UnitPrice]
    )
)
```

SUMX iterates row-by-row; IF applies per-row logic; SUMX sums the results. This is the pattern for conditional calculations in measures.

## The Common Thread

Every measure:
- Aggregates multiple rows into one value
- Reacts to filter context (changes based on what's selected in the report)
- Does not store data — computes on demand
- Can be referenced by other measures

## Related

- [[measure-filter-context]] — why measures evaluate the way they do
- [[implicit-measure-trap]] — why these should always be explicit
- [[calculated-column-vs-measure-decision-tree]] — confirming the measure choice
