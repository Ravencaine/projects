---
title: "Iterators in DAX: SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context"
source: "https://medium.com/write-your-world/iterators-in-dax-sumx-averagex-rankx-and-how-they-use-row-filter-context-711bfa11297a"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2025-09-26
created: 2026-07-27
description: "Understanding iterators is the key to mastering DAX. Let’s break down how SUMX, AVERAGEX, and RANKX work with row context, filter context, and context transition — with visuals and examples."
Processed: "Unprocessed"
---
## Understanding iterators is the key to mastering DAX. Let’s break down how SUMX, AVERAGEX, and RANKX work with row context, filter context, and context transition — with visuals and examples.

## Introduction: Why Iterators Matter

If you’ve ever compared `SUM(Sales[Revenue])` with `SUMX(Sales, Sales[Quantity] * Sales[Price])`, you’ve already seen the difference between **aggregators** and **iterators**.

Iterators — the functions ending in **X** (SUMX, AVERAGEX, RANKX, MAXX, MINX, etc.) — are among the most important tools in DAX.

But they confuse learners because they:

- Create **row context** while looping over a table.
- Often trigger **context transition** when CALCULATE is involved.
- Can give very different results from non-X functions.

In this blog, we’ll take a deep dive into **iterators**, focusing on SUMX, AVERAGEX, and RANKX — three of the most useful ones.

## Part 1 — Aggregators vs Iterators

**Aggregators (e.g., SUM, AVERAGE):**

- Work directly on a column.
- Example:
```c
SUM(Sales[Revenue])
```

👉 Adds up all rows in the filtered context.

**Iterators (e.g., SUMX, AVERAGEX):**

- Loop row by row, create **row context**, then aggregate results.
- Example:
```c
SUMX(Sales, Sales[Quantity] * Sales[Price])
```

👉 For each row in Sales, calculate `Quantity * Price`, then sum it up.

![](99.System/Attachments/1!PuldY6_sVCYmQ7mXtBCqAw.png.webp)

Side-by-side comparison of SUM vs SUMX

## Part 2 — SUMX in Action

`SUMX` is the most common iterator. It’s essential when:

- Your data model doesn’t have a pre-calculated column.
- You want to calculate derived values like profit, margin, or weighted average.

Example:

```c
Total Profit =
SUMX(
 Sales,
 Sales[Revenue] — Sales[Cost]
)
```
- Creates row context (one row at a time).
- Evaluates expression `(Revenue – Cost)` for each row.
- Aggregates (sums) the results.

⚡ Without SUMX, you’d need to create a calculated column `Profit = Revenue - Cost`, then sum it — less efficient.

## Part 3 — AVERAGEX for Weighted Calculations

`AVERAGEX` works similarly, but averages the row-by-row results.

Example: Weighted Average Price:

```c
Weighted Avg Price =
AVERAGEX(
 Sales,
 Sales[Revenue] / Sales[Quantity]
)
```
- Loops over each row, computes Revenue ÷ Quantity.
- Averages across all rows.

📌 **Key Use Case:** Useful in retail or finance where simple averages don’t make sense.

![](99.System/Attachments/1!6X7ueSLGav_ghsT5eaEMPA.png.webp)

AVERAGE gives a simple mean, while AVERAGEX calculates a weighted average

## Part 4 — RANKX for Ranking

`RANKX` adds a different flavor — it assigns a rank based on an expression.

Example: Ranking customers by sales:

```c
Customer Rank =
RANKX(
 ALL(Customer),
 SUM(Sales[Revenue])
)
```
- `ALL(Customer)` removes customer filter (so you rank across all customers).
- `SUM(Sales[Revenue])` is evaluated per customer.
- RANKX loops and assigns a rank.

⚠️ Without ALL, each customer would always be ranked “1” (because they only see themselves).

![](99.System/Attachments/1!pJPX07IIDM97I6HImOVANg.png.webp)

Leaderboard chart: Top 5 customers ranked by revenue.

## Part 5 — Context Transition Inside Iterators

Here’s the tricky part:

- Iterators create **row context**.
- But row context alone cannot filter other tables.
- When CALCULATE is involved inside an iterator, it triggers **context transition** — converting row context into filter context.

Example:

```c
ProfitX =
SUMX(
 Sales,
 CALCULATE( Sales[Revenue] — Sales[Cost] )
)
```
- CALCULATE forces context transition.
- Row context becomes filter context.
- Expression reevaluates with those filters.

📌 This is why iterators + CALCULATE are so powerful, but also confusing for learners.

![](99.System/Attachments/1!O0y6v2uodA8SalsU4ut_bA.png.webp)

Flow diagram: Row Context → CALCULATE → Filter Context

## Part 6 — When to Use Iterators vs Calculated Columns

- ✅ Use Iterators when you want **dynamic calculations** in measures.
- ✅ Use Calculated Columns when the derived value is static and reusable.
- ⚠️ Avoid Iterators on very large tables unless necessary — they can be expensive.

## Best Practices

- Start with a simple aggregator (`SUM`, `AVERAGE`) whenever possible.
- Move to iterators (`SUMX`, `AVERAGEX`, `RANKX`) when you need per-row logic.
- Always check performance — iterators loop row by row, which can be costly.
- Use `ALL`, `ALLEXCEPT`, or `REMOVEFILTERS` inside RANKX for correct ranking logic.

## Key Takeaways

- Iterators (`SUMX`, `AVERAGEX`, `RANKX`) loop through tables row by row.
- They create **row context** and often require **context transition**.
- They are essential for dynamic calculations like profit, weighted averages, and ranking.
- Choosing between aggregators and iterators depends on business logic and performance.

## Closing Thought

If CALCULATE is the “king” of DAX, then iterators are the “workers” that actually get the job done row by row.

👉 Mastering SUMX, AVERAGEX, and RANKX will make your Power BI models far more powerful, flexible, and accurate.