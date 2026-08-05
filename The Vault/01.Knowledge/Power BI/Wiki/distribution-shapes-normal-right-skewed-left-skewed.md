---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [distribution, normal, skewed, right-skewed, left-skewed, mean, median]
---

# Distribution Shapes: Normal, Right-Skewed, Left-Skewed

The relationship between mean and median reveals the shape of a distribution.

## Definitions

| Shape | Condition | Visual clue in box plot |
|-------|-----------|------------------------|
| **Normal / Symmetrical** | Mean ≈ Median | Box centred, mean ≈ median |
| **Right-skewed** | Mean > Median | Box shifted left of mean; long right whisker |
| **Left-skewed** | Mean < Median | Box shifted right of mean; long left whisker |

## Key Points

- **Right-skewed**: positive tail extends right — most values are low, few are very high (e.g., income distribution)
- **Left-skewed**: negative tail extends left — most values are high, few are very low (e.g., exam scores with a floor)
- **Normal**: mean and median are close; bell-shaped histogram
- Skewness affects which imputation strategy to use: for right-skewed data, median is more appropriate than mean

## How to Detect

1. **Box plot**: compare mean (triangle) to median (line in box)
2. **Histogram**: look at which direction the tail extends
3. **Summary statistics**: compare mean vs median values
4. **Y-axis starting at zero**: always check axis starts at 0 to avoid misleading scale

## Related

- [[box-plot-anatomy]]
- [[summary-statistics-power-bi]]
- [[handling-missing-data-strategies]]
