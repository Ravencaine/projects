---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: pattern
tags: [powerbi, pattern, chart, label, conditional-formatting]
---

# Dummy Measures for Label Background

A workaround technique that splits a single measure into multiple "dummy" series — each handling one conditional branch — so each can be styled independently in the chart.

## Purpose

Power BI does not yet expose an `fx` button for data label background color. This technique achieves the same result by placing the same metric in multiple series, then using `IF` to make each series show the value only for its branch. The chart's native per-series background formatting then applies to whichever series is visible at each data point.

## Components

1. **Base measure:** the underlying metric (e.g. `Turnover Rate Variance`)
2. **Positive dummy:** `IF(metric < 0, metric)` — shows the value only for negative rows
3. **Negative dummy:** `IF(metric >= 0, metric)` — shows the value only for positive rows
4. **Both dummies** added to the chart's Values field well
5. **Per-series formatting:** set background color on each dummy independently

## Structure

```
Base Metric: Turnover Rate Variance
     ├→ Turnover Variance_Positive = IF([Variance] < 0, [Variance])
     │   → Format: light green background
     └→ Turnover Variance_Negative = IF([Variance] >= 0, [Variance])
         → Format: light red background
```

## Example

```dax
// Two series on the chart — only one fires per row
Turnover Variance_Positive =
    IF(
        [Turnover Rate Variance] < 0,
        [Turnover Rate Variance]
    )

Turnover Variance_Negative =
    IF(
        [Turnover Rate Variance] >= 0,
        [Turnover Rate Variance]
    )
```

In the Format pane: *Data labels → Series → Turnover_Variance_Positive → Background: light green*. Same for Negative with light red.

**Critical:** set the bar/column color of all series to the same color so the bar fills look seamless — only the label background changes.

## Variations

- Three-way split: add a `Neutral` series for `= 0` cases with no special formatting
- Use with font color (not just background) by formatting the Label Font Color property per series
- Works on any chart that supports per-series data labels: bar, column, line, area

## Related

- [[label-font-color-switch]]
- [[variance-arrow-label]]
- [[Conditional-Data-Label-Background-Formatting]]
