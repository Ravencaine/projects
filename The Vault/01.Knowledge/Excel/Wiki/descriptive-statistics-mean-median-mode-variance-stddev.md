---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: reference
tags: [excel, statistics, reference, descriptive]
---

# Descriptive Statistics: Mean, Median, Mode, Variance, Standard Deviation

Reference for the five core descriptive statistics output by the Analysis ToolPak — what each measures and how to interpret it.

## Quick Reference

| Statistic | Excel Function | What It Measures |
|-----------|----------------|-----------------|
| **Mean** | `AVERAGE(range)` | Arithmetic average: sum of values divided by count |
| **Median** | `MEDIAN(range)` | Middle value: 50% of values are above and below |
| **Mode** | `MODE(range)` | Most frequent value in the dataset |
| **Variance** | `VAR.P(range)` | Average of squared deviations from the mean — measures spread |
| **Std Dev** | `STDEV.P(range)` | Square root of variance — same unit as the original data |

## Definitions

### Mean (Arithmetic Average)
Add all values, divide by the count. Sensitive to outliers — a single extreme value pulls the mean significantly.

```
Mean = (Σ values) / N
```

### Median (Middle Value)
Sort all values; the median is the value at position N/2. Not affected by outliers — more representative of a typical value in skewed distributions.

### Mode (Most Frequent)
The value that appears most often. Can be multimodal (two or more modes) or no mode at all if all values are unique. Most useful for categorical or discrete data.

### Variance
Measures how spread out the data is. Computed as: average of (each value minus the mean) squared.

```
Variance = Σ(value - mean)² / N
```

### Standard Deviation
Square root of variance. Returns to the original unit of measurement. A small standard deviation means values cluster tightly around the mean.

```
StdDev = √Variance
```

## The Normal Distribution

In a perfectly normal (bell curve) distribution:
- Mean = Median = Mode (all at the center)
- ~68.27% of values fall within ±1 standard deviation
- ~95.45% of values fall within ±2 standard deviations
- ~99.73% of values fall within ±3 standard deviations

## Notes

- `AVERAGE` ignores blank cells and text; `AVERAGEA` treats text as 0
- `AVERAGEIF` / `AVERAGEIFS` compute the mean conditionally
- `MEDIAN` automatically sorts internally — no need to pre-sort the data
- Variance has two Excel variants: `VAR.P` (population) and `VAR.S` (sample) — use the sample variant when the data is a sample of a larger population

## Related

- [[excel-analysis-toolpak-descriptive-statistics-histogram]] — how to generate these via the ToolPak
- [[dax-68-95-99-rule]] — interpreting standard deviation against the normal distribution
- [[scatter-chart-with-r-squared-trendline]] — R-squared as a measure of how well a regression line fits the data
