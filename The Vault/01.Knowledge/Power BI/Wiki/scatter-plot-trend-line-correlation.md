---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [scatter-plot, trend-line, correlation, positive, negative]
---

# Scatter Plot + Trend Line for Correlation Detection

Adding a trend line to a scatter plot quantifies the direction and strength of a relationship between two variables.

## Purpose

Scatter plots reveal relationships. The trend line summarises whether the relationship is positive, negative, or absent.

## Components

1. **Scatter plot**: X and Y numeric fields
2. **Trend line**: Analytics pane → Add → Trend Line

## Trend Line Interpretation

| Slope direction | Correlation | Interpretation |
|-----------------|-------------|----------------|
| ↗ Upward | **Positive** | Higher X → higher Y |
| ↘ Downward | **Negative** | Higher X → lower Y |
| Flat | **None / weak** | No clear relationship |

## Example

Scatter plot: Life Ladder vs Healthy Life Expectancy

- Upward-sloping cloud → positive correlation
- Adding a trend line confirms: countries with higher life expectancy score higher on the Life Ladder

## Why It Matters

The trend line helps distinguish real patterns from visual noise. A scattered cloud without a clear slope means no learnable relationship exists for ML models.

## Related

- [[scatter-plot-visual]]
- [[correlation-does-not-imply-causation]]
