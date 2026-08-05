---
created: 2026-08-01
updated: 2026-08-02
source: "The DAX concepts that actually save you time in Power BI.md"
note_type: atomic
tags: [dax, functions, fundamentals, beginner, reference]
---

# DAX Functions: The 8 That Cover 80% of Real Work

A curated shortlist from Daniel Olatunji's experience — the functions he reaches for on almost every project.

## DIVIDE

Division that handles zero denominator safely. Always use this instead of `/`.

```c
Margin = DIVIDE([Profit], [Revenue], 0)  -- returns 0 when Revenue = 0
Margin = [Profit] / [Revenue]             -- returns INF when Revenue = 0
```

**Always use DIVIDE** when the denominator could be zero. One empty category can crash an entire visual without it.

## Iterators: SUMX, AVERAGEX, MINX, MAXX, etc.

Iterators walk through a table **row by row**, applying a calculation to each row before aggregating.

Use when the calculation needs to happen **per row** before summing:
```c
// Quantity × Unit Price per row, then sum
Revenue = SUMX(Sales, Sales[Quantity] * Sales[Unit Price])
```

Plain `SUM` can't do row-by-row multiplication — it aggregates columns independently.

## ALL / ALLSELECTED

**`ALL`** removes all filters on a table or column — the building block of percent-of-total measures:

```c
Percent of Total =
DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales)))
```

**`ALLSELECTED`** keeps slicer filters but removes visual-level context — the trick behind subtotal rows that still show 100%.

## RELATED

Pulls a value from a related table into the **current row context**: useful in calculated columns:

```c
// Inside Sales table, referencing Customer table
Customer City = RELATED(Customer[City])
```

Requires an active relationship between the tables.

## SWITCH

Replaces long chains of nested IFs with a readable branch:

```c
// 5 nested IFs — painful to read and maintain
Grade =
IF(Score >= 90, "A",
IF(Score >= 80, "B",
IF(Score >= 70, "C",
IF(Score >= 60, "D", "F"))))

// SWITCH — clean and debuggable
Grade =
SWITCH(
    TRUE(),
    Score >= 90, "A",
    Score >= 80, "B",
    Score >= 70, "C",
    Score >= 60, "D",
    "F"
)
```

## Time Intelligence: SAMEPERIODLASTYEAR, DATESYTD, DATEADD, TOTALYTD, TOTALQTD

All require a **marked, continuous date table** to work correctly.

```c
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
Sales YTD = TOTALYTD([Total Sales], 'Calendar'[Date])
Sales QTD = TOTALQTD([Total Sales], 'Calendar'[Date])
```

Without a proper date table, these functions give wrong or blank results.

## RANKX

Dynamic ranking that updates as filters change — exactly what you want for top-N visuals:

```c
Product Rank =
RANKX(
    ALL(Product[Product Name]),
    [Total Sales],
    ,
    DESC,
    DENSE
)
```

Keeps accurate rank no matter what the user filters by.

## Related

- [[measures-vs-calculated-columns]] — when to use measures (where most of these live)
- [[calculate-context-transition-core]] — CALCULATE underpins ALL, SAMEPERIODLASTYEAR, etc.
- [[var-dax-reading-complexity]] — VAR with these functions = readable formulas
