---
created: 2026-08-02
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: atomic
tags: [powerbi, percentile, bucketing, data-visualization]
---

# Percentile Bucketing Concept

Dividing a dataset into equally sized groups based on data distribution rather than fixed numerical thresholds.

## Definition

Instead of static ranges (e.g. "$0–10K", "$10K–25K"), data is divided into percentile-based buckets where each bin represents an equal proportion of records. For quintiles (5 buckets):

- Bin 1: first 20% of records (smallest values)
- Bin 2: next 20%
- ...
- Bin 5: last 20%

Each bucket holds the same *number* of records — but the dollar width of each bucket varies dynamically based on the actual distribution.

## Key Properties

- **Context-aware:** When users filter the data (e.g. one department), percentiles are recomputed for that subset — bins always reflect the current distribution.
- **Fair comparison:** Each bar always represents the same proportion of the filtered dataset, enabling fair comparison across segments.
- **Adaptable shape:** Bin dollar ranges shift automatically when the underlying data changes.

## PERCENTILEX.INC vs PERCENTILEX.EXC

- `PERCENTILEX.INC`: Inclusive — 0th and 100th percentiles are defined (includes min and max values). Use this when bins must span the full data range including extremes.
- `PERCENTILEX.EXC`: Exclusive — 0th and 100th percentiles are undefined; calculation is between extremes only.

## Related

- [[dynamic-percentile-threshold-measures]]
- [[quintile-bucket-min-max-amount]]
- [[bucket-count-total-via-filter-allselected]]
- [[dynamic-bin-bar-chart-from-percentile-buckets]]
