---
created: 2026-08-08
updated: 2026-08-08
source: ABC Analysis in Power BI The Chart That Shows Your 8020 Instantly
note_type: snippet
tags: [power-bi, visual-calculations, chart-formatting, stacked-columns]
---

# ABC Group Thresholds as Stacked Columns

Use three stacked column series with IF/BLANK logic to create coloured threshold bands behind a Pareto line.

## Formula Set

```
Group A = IF([Running Sum] <= 0.4, 0.4, BLANK())
Group B = IF([Running Sum] > 0.4 && [Running Sum] <= 0.8, 0.8, BLANK())
Group C = IF([Running Sum] > 0.8, 1.0, BLANK())
```

Each column returns a fixed threshold value only for items within its bucket; returns `BLANK()` otherwise (blank = no bar drawn).

## Formatting to Create Bands

1. Put all three series on **Column Y-axis:** they stack automatically
2. **Format → Columns → Layout**:
   - **Overlap** = 100% (series stack into one band)
   - **Space between categories** = 0% (removes gaps)
3. Use **Flip overlap** button to split the single band into three separate bands
4. Assign distinct fill colours per series

## Result

Three semi-transparent coloured bands at 0–40%, 40–80%, 80–100% — appear as shaded ABC zones behind the Pareto line.

## Related

- [[ABC-Classification-Chart-Visual-Calculations]] — full chart context
- [[Visual-Calculations-RUNNINGSUM-ORDER-BY]] — threshold values derived from running sum
