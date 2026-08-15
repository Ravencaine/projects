---
title: "Deep dive into conditional formatting for lines and legends"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-conditional-formatting-for-lines-and-legends/ba-p/5331078?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-08-04
created: 2026-08-08
description: "Power BI now supports conditional formatting for lines and legends across many visuals. You can apply gradients, rules, or field-driven colors to"
Processed: "Unprocessed"
---
Power BI now supports conditional formatting for lines and legends across many visuals. You can apply gradients, rules, or field-driven colors to keep reports consistent, draw attention to important values, and reduce manual maintenance as data changes.

For charts with legends, you can define colors once in a measure or column and reuse them throughout a report. For line charts, you can format entire lines, individual segments, shading, markers, and series labels. This makes it easier to highlight the latest period, show increases and decreases, or emphasize specific data points dynamically.

## What is conditional formatting?

Conditional formatting dynamically controls a visual property such as color, text, or a value. Depending on the setting, you can use:

- **Rules** based on numeric ranges, percentiles, or specific values and text.
- **Gradients** with minimum and maximum colors and an optional midpoint.
- **Field values** from a measure or column that returns a color or value. This option provides the most flexibility, reuse, and maintainability.

Visual calculations can also supply field values, allowing you to define DAX logic directly in a visual instead of creating a reusable model measure.

## Where is it available?

The new capabilities close many of the remaining conditional-formatting gaps:

- **Line, area, stacked area, and 100% stacked area charts:** Format whole lines and shading, multiple legend series, individual line segments, and markers. Segment colors can use hard or gradient transitions and appear to the left, center, or right of a marker.
- **Bar, column, combo, ribbon, pie, donut, and funnel charts:** When a legend is present, format each legend category with gradients, rules, or field values.

These additions build on existing options for titles, backgrounds, borders, axis ranges, tables and matrices, scatter markers, maps, cards, slicers, buttons, alt text, and category colors in charts without legends.

## Common scenarios

### Highlight the latest year in a line chart

For a year-over-year line chart, use a gradient to emphasize the latest year while fading earlier years into gray. This keeps seasonal context visible without competing with the current result.

1. Open **Lines > Color** in the formatting pane and select the **Fx** button.
2. Set **Format style** to **Gradient**.
3. Base the formatting on a measure that returns the latest year.
4. Use light gray for the lowest value, darker gray for the midpoint, and blue for the highest value.
5. Select **OK**.

![DataZoe_1-1785432988503.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357327i424E26C0DE8C5974/image-size/large?v=v2&px=999 "DataZoe_1-1785432988503.png")

*Figure: Conditional formatting to highlight the latest year.*

The latest year remains highlighted as new data arrives or the selected date range changes. The same colors can also control markers and series labels. Use the eraser to clear the formatting or the Fx button to edit it.

### Show increases and decreases with line segments

Segment formatting can highlight spikes and dips based on the value plotted in the chart.

1. Open **Lines > Color**, select **Fx**, and choose **Gradient**.
2. Base the formatting on the line value.
3. Use dark red for the minimum, gray at zero, and dark blue for the maximum.
4. Select **OK**.

![DataZoe_2-1785433008416.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357328i4F59F7F32B3C6777/image-size/large?v=v2&px=999 "DataZoe_2-1785433008416.png")

*Figure: Conditional formatting to highlight line segments.*

After applying the formatting, adjust the segment type to left, center, or right. You can also enable gradient blending and turn on **Shade area** so the fill matches the line. Because the logic is attached to the visual, new spikes and dips are formatted automatically.

### Highlight minimum and maximum markers

Markers now have their own conditional-formatting control, removing the need for older workarounds. Create a DAX measure that returns the theme’s positive color for the maximum value, the negative color for the minimum, and a transparent color for all other points.

1. Open **Markers > Color** and select **Fx**.
2. Set **Format style** to **Field value**.
3. Select the marker-color measure and choose **OK**.

![DataZoe_3-1785433024039.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357329i5F448A63BDE8F8D2/image-size/large?v=v2&px=999 "DataZoe_3-1785433024039.png")

*Figure: Conditional formatting to highlight the minimum and maximum markers using theme sentiment colors.*

Only the minimum and maximum markers appear, and their colors follow the report theme. Reusing the measure across visuals keeps the logic centralized and easy to update.

### Keep legends consistent across visuals

Consistent category colors make a report easier to understand. If a model column contains color values, use it to conditionally format every chart that shares the category.

1. Open the visual’s color setting and select **Fx**.
2. Choose **Field value** and select the color field.
3. Select **OK** and repeat for the other visuals.

![DataZoe_4-1785433033200.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357330iEF2E76A2E5DEC360/image-size/large?v=v2&px=999 "DataZoe_4-1785433033200.png")

*Figure: The card can act as the legend for all visuals on the page now the legends are all synced.*

All visuals now use the same color source. You can even remove repeated legends and use one visual, such as a card, as a central legend. New categories inherit their defined colors without requiring report updates.

### Apply gradients across a legend

Value-based gradients were previously available only when categories appeared on an axis. They now work when a legend is present. With a legend, the regular category legend remains visible while the plotted colors reflect the underlying value. This makes it easier to compare overall trends with results by category, and the gradient continues to work as new periods appear.

![DataZoe_5-1785433045131.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357331i400837863BCC02F3/image-size/large?v=v2&px=999 "DataZoe_5-1785433045131.png")

*Figure: Gradient styling based on value is now available for charts with legends.*

### Use colors with field parameters

Field parameters let report viewers switch measures or axes across multiple visuals. Add a color column to the parameter table so each measure has a consistent color.

![DataZoe_6-1785433056628.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357333i03C414384E890C9A/image-size/large?v=v2&px=999 "DataZoe_6-1785433056628.png")

*Figure: A field parameter of measures can have the color specified instead of using the same color for all measures.*

1. Open the visual’s color setting and select **Fx**.
2. Choose **Field value** and select the parameter’s color column.
3. Select **OK**.

![DataZoe_7-1785433056632.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1357332iC6D7E5C336D30A3E/image-size/large?v=v2&px=999 "DataZoe_7-1785433056632.png")

*Figure: Now the color changes with the measure selection.*

When the selected measure changes, its assigned color follows across every formatted visual, making the current analysis easier to recognize.

## Next steps

Conditional formatting for lines and legends helps reports stay polished, consistent, and responsive to changing data. Define the logic once, reuse it across visuals, and let the report update automatically as new categories, periods, and values appear.

- **Learn more:** Explore the [Conditional formatting in Power BI visuals](https://learn.microsoft.com/power-bi/visuals/power-bi-visualization-conditional-formatting) documentation.
- **Try it:** Look for the **Fx** button in supported formatting settings.