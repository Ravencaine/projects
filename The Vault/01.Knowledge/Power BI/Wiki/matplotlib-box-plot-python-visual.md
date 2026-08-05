---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [matplotlib, box-plot, python-visual, pandas, power-bi]
---

# matplotlib Box Plot in Python Visual

Creating a box plot using matplotlib inside Power BI's Python Visual to visualise summary statistics.

## Purpose

Unlike the native Power BI scatter chart, a true box plot (showing Q1, median, Q3, whiskers, and outliers) requires matplotlib in the Python Visual.

## Structure

```python
import matplotlib.pyplot as plt
import pandas as pd

# Prepare data — drop nulls
df = dataset[['Healthy life expectancy at birth']].dropna()

# Create box plot
plt.boxplot(df['Healthy life expectancy at birth'],
            showmeans=True,
            showfliers=True)

plt.ylabel('Healthy life expectancy at birth')
plt.title('Box Plot of Healthy Life Expectancy')
plt.show()
```

## Key Parameters

| Parameter | Effect |
|-----------|--------|
| `showmeans=True` | Display the mean (triangle) alongside the median (line) |
| `showfliers=True` | Display outlier points beyond whiskers |

## Notes

- The box shows the **IQR** (middle 50% of data)
- **Mean ≠ Median** in the box plot reveals skew: if mean < median → left-skewed; mean > median → right-skewed
- Whiskers extend to 1.5 × IQR; points beyond are outliers
- Use with `dataset[['Column']].dropna()` to avoid null errors

## Related

- [[matplotlib-histogram-python-visual]]
- [[box-plot-anatomy]]
- [[box-plot-visual]]
