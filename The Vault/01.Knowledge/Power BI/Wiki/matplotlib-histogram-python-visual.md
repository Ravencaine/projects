---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [matplotlib, histogram, python-visual, pandas, power-bi]
---

# matplotlib Histogram in Python Visual

Creating a histogram using Python's matplotlib library inside Power BI's Python Visual.

## Purpose

matplotlib gives finer control over bin size, axis ranges, and styling than Power BI's built-in Grouping approach.

## Structure

```python
import matplotlib.pyplot as plt

# Define bin edges (0 to 10 in steps of 1)
bins = list(range(0, 11, 1))

# Create histogram
plt.hist(dataset['Life Ladder'], bins=bins, width=0.8)

# Labels and title
plt.xlabel('Life Ladder')
plt.ylabel('Number of countries')
plt.title('Life Ladder Distribution 2019')

plt.show()
```

## Example

Finer bin detail (0 to 10 in steps of 0.5):

```python
bins = [x * 0.5 for x in range(0, 21)]
plt.hist(dataset['Life Ladder'], bins=bins, width=0.4)
plt.xlabel('Life Ladder')
plt.ylabel('Number of countries')
plt.show()
```

## Notes

- Power BI passes the selected table as `dataset` (pandas DataFrame)
- All column names from the visual's fields appear as DataFrame columns
- `plt.show()` renders the plot as a static image in the report
- Use `dataset[['Column']].dropna()` to handle nulls

## Related

- [[matplotlib-box-plot-python-visual]]
- [[box-plot-visual]]
- [[python-visual-in-power-bi]]
