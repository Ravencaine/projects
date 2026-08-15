---
created: 2026-08-14
source: 4 ways to use error bars in Power BI - small feature, big impact.md
note_type: pattern
tags: [error-bars, rounded-bars, power-bi]
---

# Error Bar Rounded Bars

Add rounded end caps to a horizontal bar chart using error bars with filled-circle markers — eliminating the need for a custom visual.

## Purpose

Achieve pill-shaped / rounded bar chart aesthetics using only native Power BI formatting. No custom visual required.

## Components

- Clustered bar chart
- Error bar on the Sales Actual series
- Two invisible anchor measures returning 0 (optional, can use existing series)

## Structure

### Visual Setup
1. Insert clustered bar chart: Y-axis = Category, X-axis = Sales Actual
2. Go to Format → Error bars → select Sales Actual series:
   - Enable = On
   - Type = By Percentage
   - Upper bound = 0%
   - Lower bound = 100%
3. Under Bar:
   - Bar = On
   - Color = match main bar color
   - Width = 1
   - Border size = 0px
4. Under Markers:
   - Markers = On
   - Shape = filled circle
   - Size = 10px
   - Color = match bar color
5. Adjust Space between Categories until the circles align with bar ends
6. Set X-axis min/max with a buffer measure to ensure the left cap is not clipped

## Key Mechanism

Setting the error bar bounds to `Upper = 0%` and `Lower = 100%` creates a bar that spans the full width of the main bar — then the filled circle markers at each end create the illusion of rounded caps. The error bar type `By Percentage` is relative to the series value itself.

## Variations

- Reduce circle size for subtler rounding (6–8px)
- Use a slightly different color for the markers to create a two-tone effect
- Combine with bar transparency for glassy effect

## Related

- [[Error-Bar-Data-Flags]]
- [[Error-Bar-Dumbbell-Chart]]
- [[Error-Bar-Boxplot]]
