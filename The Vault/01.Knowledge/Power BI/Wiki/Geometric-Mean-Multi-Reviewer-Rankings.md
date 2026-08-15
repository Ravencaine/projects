---
created: 2026-08-08
updated: 2026-08-08
source: Calculating Geometric Mean in Power BI
note_type: pattern
tags: [power-bi, geometric-mean, ranking, statistics, multi-reviewer]
---

# Geometric Mean for Multi-Reviewer Rankings

When multiple reviewers/judges rank the same set of subjects (players, products, candidates), the **geometric mean** is the preferred aggregation over arithmetic mean — because it reduces the disproportionate influence of extreme outlier scores.

## Problem with Arithmetic Mean in Rankings

If a player receives scores of 20 and 80 from two judges:

- Arithmetic mean: (20 + 80) / 2 = **50**
- But the 20 is an extreme outlier — the arithmetic mean doesn't penalise it enough

## Why Geometric Mean Works Better

Using the same example:

- Geometric mean: √(20 × 80) = √1600 = **40**

The geometric mean of 40 is closer to the range of realistic scores, because it factors in the **multiplicative gap** between the two values rather than treating them as independent additions.

## Practical Setup in Power BI

### Data Model

| PlayerID | Reviewer | Score |
|----------|----------|-------|
| 1 | Judge 1 | 70 |
| 1 | Judge 2 | 20 |
| 1 | Judge 3 | 65 |
| 2 | Judge 1 | 55 |
| 2 | Judge 2 | 58 |
| ... | ... | ... |

### Power Query Steps

1. **Group By** on `PlayerID`
2. Add custom column `Product = List.Product([AllRows][Score])`
3. Add custom column `Count = Table.RowCount([AllRows])`
4. Add custom column `Geometric Mean = Number.Round(Number.Power([Product], 1/[Count]), 2)`

Result: one row per player with their geometric mean score across all reviewers.

## Key Insight

> Geometric mean naturally down-weights extreme scores because it works on **multiplicative relationships:** a judge's 20 combined with 80 produces a mean of 40, not 50.

## Related

- [[Geometric-Mean-Formula]] — underlying formula
- [[Geometric-Mean-Power-Query]] — implementation steps
- [[Geometric-Mean-Zero-Negative-Limitation]] — prerequisite: all scores must be > 0
