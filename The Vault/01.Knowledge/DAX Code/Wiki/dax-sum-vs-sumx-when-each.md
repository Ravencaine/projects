---
created: 2026-08-01
updated: 2026-08-02
source: "Why I Stopped Writing “Best Practice” DAX Posts (And What I Write Instead).md"
note_type: atomic
tags: [dax, sum, sumx, iterator, cardinality, performance, row-by-row]
---

# SUM vs SUMX — When Each Applies

## The Misleading "Best Practice"

"Always use SUM instead of SUMX — SUMX is slower because it iterates row-by-row."

## When SUM Is Correct

\`\`\`c
Total Quantity = SUM(FactSales[Quantity])
\`\`\`

Simple column aggregation. No row-by-row calculation needed.

## When SUM Is Wrong

\`\`\`c
-- WRONG: looks plausible, runs fine, produces garbage
Incorrect Revenue =
    SUM(FactSales[Quantity]) * SUM(FactSales[UnitPrice])
-- Result: Total Quantity × Total UnitPrice = mathematically wrong
\`\`\`

## When SUMX Is the Only Correct Choice

\`\`\`c
-- CORRECT: row-by-row multiplication, then sum
Revenue =
SUMX(
    FactSales,
    FactSales[Quantity] * FactSales[UnitPrice]
)
\`\`\`

SUMX is non-negotiable for: `row × row → aggregate`. Any case where you need to multiply columns before summing.

## Performance Rule of Thumb

| Scenario | Recommendation |
|----------|----------------|
| 50K–500K rows, simple sum | SUM |
| 500K+ rows, row-by-row calc | SUMX (still correct, just test) |
| 50M+ rows, row-by-row calc | Test both; consider pre-aggregating in Power Query |
| Any row-by-row multiplication | SUMX only |

The "SUMX is slow" advice only applies above certain data volumes. Below that threshold, correctness beats micro-optimization.

## The Pattern That Fails Without Context

"Best practice" readers learn "SUMX is slow, avoid it." They encounter a pricing calculation and write:

\`\`\`c
Incorrect Revenue = SUM(Quantity) * SUM(UnitPrice)
\`\`\`

This runs without error. The number looks plausible. Nobody catches it until Finance asks why Q3 revenue is 300× higher than Q2.

Seen in 6 different client environments. Each time, developer was following "best practice." Each time, error sat undetected for months.
