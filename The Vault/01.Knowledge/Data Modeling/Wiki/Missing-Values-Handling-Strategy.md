---
created: 2026-08-05
updated: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: atomic
tags: [data-cleaning, missing-values, blank, power-query, data-quality]
---

# Missing Values: Handling Strategy

Blank cells are dangerous because they silently fail — no error, no warning, just a blank cell that breaks average calculations, distorts models, and hides upstream pipeline failures.

## Why Blanks Are Dangerous

Blanks do not just look ugly in a matrix visual — they actively:

- **Skew averages:** `AVERAGE` ignores blanks in numerator but may count them in the denominator in some aggregations
- **Break slicers and filters:** blank values create unexpected "blank" groups in slicers
- **Reduce model accuracy:** forecasting and ML models trained on data with blanks produce biased predictions
- **Hide pipeline failures:** blank Customer Name or Product Category usually means an upstream join or extract failure

## The Decision Framework

For every blank, ask two questions:

1. **Why is this missing?** Check the upstream data source or pipeline.
2. **Should this row be kept or dropped?**

| Situation | Action |
|-----------|--------|
| Transaction with missing optional fields | Keep; replace blanks with `"Unknown"` or `"N/A"` |
| Customer dimension row with no matching transactions | Investigate — may be a failed join |
| Numeric measure with blanks (no sales for this period) | Keep; use `IF(ISBLANK(...), 0, ...)` in measures |
| Row where the key identifier is blank | Drop — the row cannot be uniquely identified |

## Power Query Handling

| Transform | When to use |
|-----------|------------|
| **Fill Down** | Forward-fill time series gaps (e.g., account balance carries forward) |
| **Fill Up** | Back-fill values from the next row |
| **Replace Errors** | Convert errors to null, then decide |
| **Remove Rows with Errors** | Drop rows where a critical column failed to parse |
| **Replace Nulls** | Replace nulls with a default value (`"Unknown"`, `0`, `-1`) |

## The Rule

> When you see a blank: don't ignore it. Ask *"Why is this missing? Can it be replaced, or should this row be dropped?"*

Blanks usually point to a broken pipeline upstream — fix the root cause, not just the symptom.

## Related

- [[Duplicate-Records-Detection-Removal]]
- [[Dashboard-Health-Checklist]]
