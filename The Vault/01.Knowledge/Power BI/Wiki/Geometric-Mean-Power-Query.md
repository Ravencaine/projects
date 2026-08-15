---
created: 2026-08-08
updated: 2026-08-08
source: Calculating Geometric Mean in Power BI
note_type: pattern
tags: [power-bi, power-query, geometric-mean, list-product]
---

# Geometric Mean in Power Query

Power Query has no built-in geometric mean function. Implement it in two steps: (1) compute the product of all values, then (2) raise to power `1/n`.

## Implementation Steps

### Step 1 — Group By to get product and count

Using the **Group By** dialog:

1. Group by the identifier column (e.g., `PlayerID`)
2. Add two aggregations:
   - `Count` → operation: `Count Rows`
   - `Product` → operation: `All Rows` (keep rows for the custom column)

### Step 2 — Custom Column: List.Product

Add a custom column:

```
= List.Product([AllRows][Value])
```

This multiplies all `Value` rows together for each group.

### Step 3 — Custom Column: Number.Power

Add a second custom column:

```
= Number.Round(
    Number.Power([Product], 1 / [Count]),
    2
)
```

- `1 / [Count]` = the *n*th root (nth root = power of 1/n)
- `Number.Round(..., 2)` rounds to 2 decimal places

## Result

Each row now has its group's geometric mean pre-calculated. No DAX required — purely Power Query.

## Prerequisites

- No zero or negative values in the `Value` column
- All values must be positive numbers

## Related

- [[Geometric-Mean-Formula]] — the underlying math
- [[Geometric-Mean-Zero-Negative-Limitation]] — prerequisite limitation
- [[Geometric-Mean-Multi-Reviewer-Rankings]] — ranking use case for this pattern
