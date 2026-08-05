---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [summary-statistics, mean, median, mode, standard-deviation, data-profile]
---

# Summary Statistics in Power BI

Six core statistics that describe a numerical column's distribution and quality.

## Definition

| Statistic | What it measures |
|-----------|-----------------|
| **Count** | Total number of rows |
| **Non-Null Count** | Rows with a value |
| **Null Count** | Rows with no value (empty) |
| **Min / Max** | Range boundaries |
| **Mean** | Arithmetic average |
| **Median** | Middle value (50th percentile) |
| **Standard Deviation** | Spread of values around the mean |
| **Distinct** | Number of unique values |
| **Unique** | Values appearing only once |

## Key Points

- **Mean vs Median** reveals skew:
  - Mean ≈ Median → normally distributed
  - Mean > Median → right-skewed
  - Mean < Median → left-skewed
- **Null Count** + **Empty %** in Column Quality tells you whether missing data is a problem
- **Distinct** + **Unique** together flag high-cardinality columns (e.g., customer IDs) that are not useful for ML
- Standard deviation tells you whether values cluster tightly or are widely spread

## Related

- [[distribution-shapes-normal-right-skewed-left-skewed]]
- [[high-cardinality-features-antipattern]]
- [[data-profiling-column-quality-distribution-profile]]
