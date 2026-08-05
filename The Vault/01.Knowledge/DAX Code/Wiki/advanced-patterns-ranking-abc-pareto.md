---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, patterns, ranking, abc-analysis, pareto, running-total, beginner, churn]
---

# Advanced Patterns: Ranking, ABC Analysis, and Pareto

Combining DAX building blocks into real-world analytical patterns.

## Pattern 1: Running Total

```dax
Running Total Revenue =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALLSELECTED(Date),
        Date[Date] <= MAX(Date[Date])
    )
)
```

For each date row, FILTER keeps all dates up to and including that date. The measure accumulates over time.

**Result:**
```
Date       | Revenue  | Running Total
Jan 1      | $5,000   | $5,000
Jan 2      | $7,200   | $12,200
Jan 3      | $4,100   | $16,300
```

## Pattern 2: Product Ranking

```dax
Product Rank =
RANKX(
    ALLSELECTED(Products),
    [Total Revenue]
)
```

Ranks products by revenue within the current visual context. ALLSELECTED respects whatever the user has filtered.

**Show only top 5:**

```dax
Top 5 Product Revenue =
IF(
    [Product Rank] <= 5,
    [Total Revenue],
    BLANK()
)
```

## Pattern 3: ABC Analysis

Classify customers (or products) by revenue contribution:
- **A:** Top 20% of customers → 80% of revenue
- **B:** Next 30% → 15% of revenue
- **C:** Remaining 50% → 5% of revenue

```dax
Customer Category =
VAR CustomerRevenue = [Total Revenue]
VAR AllRevenue = CALCULATE([Total Revenue], ALLSELECTED(Customers))
VAR PercentOfTotal = DIVIDE(CustomerRevenue, AllRevenue)
VAR CumulativePercent =
    CALCULATE(
        DIVIDE([Total Revenue], AllRevenue),
        FILTER(
            ALLSELECTED(Customers),
            [Total Revenue] >= CustomerRevenue
        )
    )
RETURN
    SWITCH(
        TRUE(),
        CumulativePercent <= 0.80, "A - High Value",
        CumulativePercent <= 0.95, "B - Medium Value",
        "C - Low Value"
    )
```

## Pattern 4: Pareto (80/20) Analysis

```dax
Cumulative Revenue % =
VAR CurrentProductRevenue = [Total Revenue]
VAR AllRevenue = CALCULATE([Total Revenue], ALLSELECTED(Products))
VAR ProductsWithHigherOrEqualRevenue =
    FILTER(
        ALLSELECTED(Products),
        [Total Revenue] >= CurrentProductRevenue
    )
RETURN
    DIVIDE(
        CALCULATE([Total Revenue], ProductsWithHigherOrEqualRevenue),
        AllRevenue
    )
```

This computes each product's cumulative share of total revenue when sorted descending. Products contributing to the first 80% get a "Top 80%" label.

## Pattern 5: Dynamic Segmentation with Slicers

Let users define "high value" dynamically:

```dax
// Step 1: Create disconnected parameter table
Revenue Threshold =
GENERATESERIES(10000, 100000, 10000)
// Values: 10000, 20000, ..., 100000

// Step 2: Measure to read selected threshold
Selected Threshold =
SELECTEDVALUE('Revenue Threshold'[Value], 50000)

// Step 3: Use it
Customer Segment =
IF(
    [Total Revenue] >= [Selected Threshold],
    "High Value",
    "Standard"
)
```

Users move a slicer on the parameter table — the segmentation updates live.

## Pattern 6: Churn Analysis

Customers who purchased last year but not this year:

```dax
Churned Customers =
VAR CustomersLastYear =
    CALCULATETABLE(
        VALUES(Orders[CustomerID]),
        DATEADD(Date[Date], -1, YEAR)
    )
VAR CustomersThisYear =
    VALUES(Orders[CustomerID])
RETURN
    COUNTROWS(
        EXCEPT(CustomersLastYear, CustomersThisYear)
    )
```

EXCEPT finds IDs in last year's list but not this year's.

## Pattern 7: New vs Returning Customers

```dax
Customer Type =
VAR FirstOrderDate =
    CALCULATE(
        MIN(Orders[OrderDate]),
        ALLEXCEPT(Orders, Orders[CustomerID])
    )
VAR CurrentPeriodStart = MIN(Date[Date])
RETURN
    IF(
        FirstOrderDate >= CurrentPeriodStart,
        "New Customer",
        "Returning Customer"
    )
```

## Related

- [[iterator-functions-sumx]] — SUMX used in the running total pattern
- [[logical-functions-switc]] — SWITCH TRUE pattern used in ABC classification
- [[filter-functions-all-allselected]] — ALLSELECTED used in ranking and Pareto
