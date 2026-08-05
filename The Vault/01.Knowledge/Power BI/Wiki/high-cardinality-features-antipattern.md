---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [high-cardinality, antipattern, feature-engineering, model-limitation]
---

# High-Cardinality Features — Model Anti-Pattern

A column with too many distinct values — or only unique values — carries no learnable pattern for ML models.

## Definition

**Cardinality** = the number of distinct values in a column.

**High-cardinality** = a column where most or all values are unique. Examples: customer account numbers, email addresses, timestamps with second-level precision, free-text fields.

ML models cannot extract meaningful patterns from high-cardinality features because each value appears too rarely to establish a relationship with the target variable.

## Key Points

- **High distinct count** relative to row count = high cardinality
- Customer IDs, email addresses, product codes: do not use as model features
- A column with the same number of distinct values as rows = **zero cardinality**: every value is unique
- Fix: aggregate to a lower granularity (e.g., customer region instead of customer ID) or remove the column

## Why It Matters

Including high-cardinality features wastes model capacity and can cause overfitting. The model memorises specific values instead of learning generalisable patterns.

## Related

- [[garbage-in-garbage-out]]
- [[feature-engineering-versus-selection-versus-importance]]
- [[summary-statistics-power-bi]]
