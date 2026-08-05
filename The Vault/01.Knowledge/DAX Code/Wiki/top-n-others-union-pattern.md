---
created: 2026-07-30
updated: 2026-08-02
source: Dynamic Ranking in DAX How I Built a Top 5 Dashboard That Actually Worked.md
note_type: pattern
tags: [dax, ranking, top-n, union, others, pattern]
---

# Top N + Others Union Pattern

Combine a Top N group and an "Others" group into a single bar chart row, using `UNION` to stack two virtual tables.

## Purpose

Stakeholders want to see the top N performers plus a single "Others" row that aggregates everyone outside the Top N — without changing the underlying data model. The pattern uses `UNION` to create a virtual two-row table from a measure.

## Components

- `RANKX()` — assigns each item a rank
- `CALCULATE()` + `FILTER()` — aggregates only the Top N items
- `UNION()` — stacks two virtual rows into one result
- `ROW()` — constructs each virtual row for the union
- `VAR` — stores intermediate values for clarity and performance

## Structure

```dax
Top N vs Others =
VAR RankedMeasure = [Customer Rank]          -- existing rank measure
VAR N = [Selected TopN]                     -- from parameter table
VAR TopNSales =
    CALCULATE (
        [Total Sales],
        FILTER ( ALL ( Customers[CustomerName] ), [Customer Rank] <= N )
    )
VAR AllSales = [Total Sales]
VAR OthersSales = AllSales - TopNSales
RETURN
    UNION (
        ROW ( "Segment", "Top " & N, "Sales", TopNSales ),
        ROW ( "Segment", "Others",   "Sales", OthersSales )
    )
```

Use this measure in a card or table visual that shows two rows.

## How It Works

1. `TopNSales` uses `CALCULATE` + `FILTER` to sum only rows where rank ≤ N
2. `AllSales` is the grand total (ignoring the rank filter)
3. `OthersSales = AllSales − TopNSales`
4. `UNION` + `ROW` creates a two-row virtual table for the visual

## Variations

**Hardcoded N (no parameter table):**

```dax
Top 5 vs Others =
VAR Top5Sales = CALCULATE ( [Total Sales], FILTER ( ALL ( Customers[CustomerName] ), [Customer Rank] <= 5 ) )
VAR OthersSales = [Total Sales] - Top5Sales
RETURN
    UNION (
        ROW ( "Segment", "Top 5", "Sales", Top5Sales ),
        ROW ( "Segment", "Others", "Sales", OthersSales )
    )
```

**With percentage share:**

```dax
Top N vs Others with Pct =
VAR TopNSales = CALCULATE ( [Total Sales], FILTER ( ALL ( Customers[CustomerName] ), [Customer Rank] <= [Selected TopN] ) )
VAR AllSales = [Total Sales]
VAR OthersSales = AllSales - TopNSales
RETURN
    UNION (
        ROW ( "Segment", "Top " & [Selected TopN], "Sales", TopNSales, "Share", DIVIDE ( TopNSales, AllSales ) ),
        ROW ( "Segment", "Others", "Sales", OthersSales, "Share", DIVIDE ( OthersSales, AllSales ) )
    )
```

## Related

- [[dynamic-top-n-ranking-pattern]] — base ranking pattern
- [[top-n-parameter-slicer-pattern]] — parameter-driven N value
- [[union-intersect-except]] — UNION mechanics
- [[calculate]] — CALCULATE + FILTER for Top N aggregation
