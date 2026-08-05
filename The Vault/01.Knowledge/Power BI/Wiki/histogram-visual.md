---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-bi, visual, histogram, binning, distribution]
---

# Histogram Visual

A bar chart that groups numerical data into bins to show the frequency distribution of a variable.

## Signature

Power BI visual: Stacked Column Chart / Bar Chart with data binned via Grouping.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Axis | Binned numerical field | Created by grouping the original column into buckets |
| Values | Count of records | `Count of [Row Identifier]` |

## Returns

A frequency distribution showing how many observations fall into each bin.

## Examples

Create a histogram of Life Ladder scores (range 0–10):

1. Right-click Life Ladder → Group
2. Bin type: Bin Count, Number of bins: 10
3. Create a Stacked Column Chart
4. Axis: Life Ladder (bin groups)
5. Values: Count of Country Name

## Notes

- A histogram groups **continuous numerical data** into bins
- A bar chart is for **categorical** data — the distinction matters
- Bin size affects insight: too few bins hides detail; too many creates noise
- Power BI's Grouping feature creates the bins; rename the group field for clarity
- matplotlib's `plt.hist()` in Python Visual offers more control over bin edges

## Related

- [[histogram-versus-bar-chart]]
- [[distribution-shapes-normal-right-skewed-left-skewed]]
- [[matplotlib-histogram-python-visual]]
