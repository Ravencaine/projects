---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: pattern
tags: [error-bars, dumbbell-chart, range-chart, power-bi]
---

# Error Bar Dumbbell Chart

Build a horizontal range/dumbbell chart (showing spread between two values per category) using only error bars on a clustered bar chart — no custom visual.

## Purpose

Show the range or spread between two values per category — ideal for before/after comparisons, price ranges, or any scenario where the gap between two values tells the story. All three segments (lower whisker, IQR, upper whisker) are rendered as error bars.

## Components

- **3 invisible anchor series** (returning 0) that carry the error bars
- **3 error bars**: lower whisker, upper whisker, IQR connecting bar
- **Optional filter**: filter to only active/available records

## Structure

### Anchor Measures (all return 0)
```dax
starting point = 0
starting point1 = 0
starting point3 = 0
```

### Stat Measures (filtering for available records)
```dax
Min Value Property Available =
CALCULATE( MIN( 'Table'[Price] ), 'Table'[Status] = "Available" )

P25 Property Available =
CALCULATE( PERCENTILE.INC( 'Table'[Price], 0.25 ), 'Table'[Status] = "Available" )

P75 Property Available =
CALCULATE( PERCENTILE.INC( 'Table'[Price], 0.75 ), 'Table'[Status] = "Available" )

Max Value Property Available =
CALCULATE( MAX( 'Table'[Price] ), 'Table'[Status] = "Available" )
```

### Visual Setup
1. Clustered bar chart: Y-axis = City Name, X-axis = starting point, starting point1, startingpoint3
2. Declutter: turn off title, all axis titles, legend
3. Layout: Space between categories = 50%, Space between series = 100%, Overlap = on
4. Three error bars:
   - **starting point (lower whisker)**: Upper = P25, Lower = Min, bar color = light shade, width 1
   - **starting point1 (upper whisker)**: Upper = Max, Lower = P75, bar color = light shade, border 1px
   - **startingpoint3 (IQR)**: Upper = P75, Lower = P25, bar color = dark shade, width 2

## Key Mechanism

Three invisible series + three carefully configured error bars replace what would normally be a custom visual. The Overlap setting stacks the three series so the error bars align on the same row. Border on the upper whisker creates the gap between whisker and IQR.

## Related

- [[Error-Bar-Data-Flags]]
- [[Error-Bar-Rounded-Bars]]
- [[Error-Bar-Boxplot]]
- [[Box-Plot-Anatomy]]
