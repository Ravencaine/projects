---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: pattern
tags: [error-bars, boxplot, distribution, power-bi]
---

# Error Bar Boxplot

Build a full boxplot (min, Q1, median, Q3, max, average) using a line and stacked column chart combined with error bars — no custom visual.

## Purpose

Power BI has no native boxplot visual. This pattern recreates the full distribution display using only native chart types and error bars: stacked columns build the IQR box, error bars draw the whiskers, and layered markers show min/max/avg.

## Components

- Line and stacked column chart
- 3 invisible stacked column series (PERCENTILE 25 spacer, IQR 25–50, IQR 50–75)
- 4 line series (AVG 2, MIN, MAX, AVG) for markers and error bar attachment
- 1 error bar on the MAX series

## Structure

### Column Y-axis (stacked, in order)
1. `Sales Quantity PERCENTILE 25` — invisible spacer (color = white)
2. `Sales Quantity IQR 25-50` — light shade of main color
3. `Sales Quantity IQR 50-75` — dark shade of same color

### Line Y-axis (in order)
1. `AVG 2` — duplicate of AVG; used for outer ring marker
2. `Sales Quantity MIN` — dash marker, 7px
3. `Sales Quantity MAX` — dash marker, 7px (error bar attaches here)
4. `Sales Quantity AVG` — filled circle, 6px, white border

### Marker Formatting
- AVG 2 (outer ring): filled circle 7px, border = 1px purple, match line color off
- MIN/MAX: dash, 7px, rotation 0, purple, no border
- AVG (inner dot): filled circle 6px, white border 1px

### Error Bar (on MAX series)
- Enable = On
- Upper bound = MAX
- Lower bound = MIN
- Relationship = Absolute
- Bar = On, width 1, border 0, custom color
- Markers = On, shape = dash, size 5px

### Visual Cleanup
- Turn off all line series lines (markers only)
- Turn off gridlines, title, axis titles, legend
- Column Layout: space between categories 75%, space between series 3px

## Key Mechanism

The stacked columns build the box from bottom up: the invisible PERCENTILE 25 spacer pushes the IQR 25-50 series up from the baseline to the correct starting position. The error bar's `Relationship = Absolute` setting ensures bounds are interpreted as absolute values rather than relative to the series.

## Related

- [[Error-Bar-Dumbbell-Chart]]
- [[Box-Plot-Anatomy]]
- [[Outlier-Detection-Box-Plot]]
- [[Distribution-Shapes-Normal-Right-Skewed-Left-Skewed]]
