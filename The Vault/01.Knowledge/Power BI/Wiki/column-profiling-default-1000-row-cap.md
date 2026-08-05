---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [column-profiling, 1000-rows, data-quality, power-query, false-negative]
---

# Column Profiling Default 1000-Row Cap

By default, Power BI only profiles the first 1,000 rows — real data quality issues elsewhere in the dataset are invisible.

## Expected Behaviour

You enable Column Profile on a column and see summary statistics that appear clean and complete.

## Actual Behaviour

The statistics are calculated only against the first 1,000 rows of your dataset. If errors, empty rows, or distribution anomalies exist in rows 1,001 onward, they are completely hidden from the profiling results.

## Why It Happens

Performance optimisation. Profiling large datasets is computationally expensive, so Power BI defaults to a 1,000-row sample.

## How to Handle It

1. Check the **status bar** at the bottom of Power Query Editor
2. If it says "Column profiling based on top 1,000 rows", click it
3. Change to **"Column profiling based on entire dataset"**
4. **Warning**: for large tables, this may cause a significant delay

## Related

- [[data-profiling-column-quality-distribution-profile]]
- [[garbage-in-garbage-out]]
