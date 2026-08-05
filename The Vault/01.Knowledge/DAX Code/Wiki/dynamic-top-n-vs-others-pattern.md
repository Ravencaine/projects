---
created: 2026-07-27
updated: 2026-08-02
source: "Dynamic Ranking in DAX: How I Built a Top 5 Dashboard That Actually Worked"
note_type: pattern
tags: [dax, ranking, top-n, others, union, pareto]
---

# Dynamic Top N vs Others Pattern

Uses DAX UNION() + ROW() to combine "Top N" and "Others" into a single two-row virtual table — useful for Pareto charts and segment comparisons.

## Purpose

Show the top N items and all remaining items as "Others" in the same visual, without splitting into two separate charts.

## Components

- UNION() — combines two virtual tables
- ROW() — constructs single-row virtual tables
- CALCULATE() + FILTER() — computes Top N sales
- TopN parameter measure

## Structure

```dax
Sales Top N vs Others =
VAR TopN Sales =
    CALCULATE (
        [Total Sales],
        FILTER ( Customers, [Customer Rank] <= [Selected TopN] )
    )
VAR All Sales = [Total Sales (All Customers)]
RETURN
    UNION (
        ROW ( "Segment", "Top N",  "Sales", TopN Sales ),
        ROW ( "Segment", "Others", "Sales", All Sales - TopN Sales )
    )
```

## Related

- [[dynamic-top-n-ranking-pattern]]
