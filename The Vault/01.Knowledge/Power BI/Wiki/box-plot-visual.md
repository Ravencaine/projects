---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-bi, visual, box-plot, distribution, outliers]
---

# Box Plot Visual

Visualises six summary statistics simultaneously: minimum, Q1, mean, median, Q3, and maximum.

## Signature

Power BI: Python Visual with matplotlib (native box plot visual not available in standard Power BI).

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Data column | Numeric field | The variable to summarise |
| Show means | boolean | Overlay the mean (triangle) on the median |
| Show outliers | boolean | Display points beyond 1.5 × IQR |

## Returns

A box-and-whisker plot showing the full distribution shape.

## Notes

- No native box plot visual in standard Power BI — use the **Python Visual with matplotlib**
- Power BI does have a built-in **Key Influencers** visual that incorporates some distribution analysis
- The box plot is essential for EDA: immediately reveals skew, outliers, and normality

## Related

- [[box-plot-anatomy]]
- [[matplotlib-box-plot-python-visual]]
- [[outlier-detection-box-plot]]
