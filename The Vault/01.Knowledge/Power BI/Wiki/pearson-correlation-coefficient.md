---
created: 2026-08-02
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: atomic
tags: [powerbi, statistics, correlation, pearson, analytics]
---

# Pearson Correlation Coefficient

A measure of linear correlation between two variables, ranging from -1 to +1. Used as the basis for the DAX-only correlation matrix in Power BI.

## Definition

$$r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2} \cdot \sqrt{\sum(y_i - \bar{y})^2}}$$

## Interpretation

| Value | Meaning |
|-------|---------|
| +1 | Perfect positive correlation — as one variable increases, the other always increases |
| 0 | No linear relationship |
| -1 | Perfect negative correlation — as one variable increases, the other always decreases |

## Interpretation Guidelines (Bucketed)

| Range | Label |
|-------|-------|
| \|r\| < 0.10 | Very weak / none |
| 0.30 – 0.49 | Low positive / negative |
| 0.50 – 0.69 | Medium positive / negative |
| 0.70 – 1.00 | High positive / negative |

## DAX Implementation

See [[pearson-correlation-measure]] for the full DAX implementation used in the correlation matrix pattern.

## Related

- [[pearson-correlation-measure]]
- [[dax-correlation-matrix-power-bi]]
