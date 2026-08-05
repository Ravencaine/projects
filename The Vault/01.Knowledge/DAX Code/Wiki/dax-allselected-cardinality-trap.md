---
created: 2026-08-01
updated: 2026-08-02
source: "Why I Stopped Writing “Best Practice” DAX Posts (And What I Write Instead).md"
note_type: atomic
tags: [dax, allselected, cardinality, performance, filter-context, cross-join]
---

# ALLSELECTED Cardinality Trap

## The "Best Practice" That Breaks Production

Widely-shared advice: use ALLSELECTED for "flexible" measures that respond to user filters while keeping calculations "stable."

\`\`\`c
Flexible Revenue =
CALCULATE(
    SUMX(
        FactSales,
        FactSales[Quantity] * FactSales[UnitPrice]
    ),
    ALLSELECTED(DimProduct[ProductCategory]),
    ALLSELECTED(DimDate[Year]),
    ALLSELECTED(DimCustomer[Region])
)
\`\`\`

## Why It Breaks at Scale

ALLSELECTED with multiple dimensions creates a cross-join context that grows exponentially:

| Model | Dimensions | Combinations |
|-------|-----------|---------------|
| Demo (12 cats × 8 yrs × 23 regions) | Low cardinality | Manageable |
| Production (12 cats × 8 yrs × 23 regions) | Low cardinality | ~2,200 combos |
| Large (45,000 SKUs × 6 yrs × 340 stores) | High cardinality | 91,800,000 combos |

Every visual triggers N×M×P DAX queries simultaneously → timeouts.

## Real Case

- Original: 47 seconds per visual
- Fix: Remove ALLSELECTED from 2 of 3 contexts, replace with VALUES() where cardinality is controlled
- Result: 1.2 seconds

## When ALLSELECTED Is Safe

- Single dimension with controlled cardinality
- Dimensions known to have < ~100 distinct values in user-facing filters
- Context combinations can be calculated and bounded

## Rule

ALLSELECTED is not "remove this filter." It's "remove visible filters and create a new context from current selection." Multiple ALLSELECTED dimensions = explicit cross-join.

Always ask: **what is the cardinality of each dimension under ALLSELECTED?**
