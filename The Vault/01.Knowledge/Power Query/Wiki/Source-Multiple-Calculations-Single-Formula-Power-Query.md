---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Create Multiple Calculations Using A Single Formula in Power Query(.pbix included).md"
source_url: "https://medium.com/microsoft-power-bi/easily-create-multiple-calculations-using-a-single-formula-in-power-query-pbix-included-e4c71b1e6835"
author: "[[Shashanka Shekhar]]"
site: https://medium.com/@shashanka.shekhar02
published: 2026-07-30
source_type: article
kb_routing: Power Query
tags: [power-query, custom-column, record, multiple-columns, beginner]
level: Beginner
---

# Multiple Calculations from a Single Formula in Power Query

Shashanka Shekhar · Medium · 2026-07-30

## What this article covers

Power Query Custom Column can return a **record:** a single M value containing multiple named fields. Expanding the record creates multiple columns from one formula. Instead of writing separate Custom Column steps for Cost, ProfitPct, and Comm, write one record literal and expand it.

## Key technique

```c
[
    Cost = [Sales] - [Profit],
    ProfitPct = [Profit] / [Sales],
    Comm = 0.1 * [Profit]
]
```

Each `Key = Value` pair becomes a column after expansion.

## Benefits

- **Efficiency:** one step instead of three
- **Consistency:** uniform logic across derived columns
- **Scalability:** extend to new columns by adding pairs
- **Optimization:** fewer transformation steps in the query

## Example data

Sales Rep: Varsha, Veronica, Ramesh, James, Rajat
Sales: 10,400–14,200 | Profit: 3,040–5,720

## Steps

1. Add Column → Custom Column
2. Enter record syntax with required calculations
3. Rename column (e.g., "Multiple Column")
4. Click expand icon (left side) to create individual columns
5. Close & Apply

After Close & Apply, expanded columns appear in the Data pane under an **Invoked Function** table.

## Level

Beginner
