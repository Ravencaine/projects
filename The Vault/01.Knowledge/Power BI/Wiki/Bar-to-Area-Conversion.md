---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [area-chart, bar-chart, conversion, markers, color]
related: [Dynamic-Line-Area-Chart-Color, Color-Coding-4-Techniques]
---

# Bar-to-Area Conversion Hack

Build a bar chart with conditional formatting, then convert it to an area chart — Power BI preserves the per-series color assignment, enabling colored area charts that are otherwise impossible to build natively.

## Why This Works

Power BI natively supports conditional formatting on bar charts (clustered bar, stacked bar) via field values or measures. However, area charts and line charts do not support per-point conditional color formatting.

By building a bar chart first and assigning dynamic colors via DAX + field value formatting, then switching the visual type to **Area chart**, Power BI retains the color assignments.

## Step-by-Step

1. **Build a Clustered Bar Chart** using the metric as both the value and the color-by field.
2. **Create a color measure:**
   ```dax
   Bar Color =
       SWITCH(
           TRUE(),
           [Metric] >= [Target], "#76E3B4",
           [Metric] >= [Warning], "#F5A623",
           "#EE6064"
       )
   ```
3. **Assign the color measure** to the color-by field in the formatting pane (Field Value property).
4. **Switch the visual type** from Bar to Stacked Area or Clustered Area.
5. **Enable Data Labels** to display the metric values on each area segment.
6. **Enable Markers** for additional visual clarity at data points.

## Notes

- Bittar's "How I Built a Modern Oblique Area Chart" article ([[Source-Oblique-Area-Chart]]) does **not** use this technique — it uses a **line chart** plus a background PNG plus [[Error-Band-as-White-Out-Mask|error bands as a white-out mask]]. The oblique look is built from graphics composition, not per-series colouring. See [[Oblique-Area-Chart]] for the corrected workflow. (Note: a previous version of this note incorrectly linked the article to this technique.)
- After switching to area, the **Color** formatting option in the visual pane is disabled — the colors come entirely from the field value measure, not the visual formatting.
- If colors don't transfer, the color measure may not be formatted as a hex string — ensure the measure returns `"#RRGGBB"` exactly.
- Works for Stacked Area, Clustered Area, and Line charts.
- Add error bars from the Analytics pane for further visual richness.

## Related

- [[Dynamic-Line-Area-Chart-Color]] — overlay technique (alternative approach)
- [[Color-Coding-4-Techniques]] — reference for the four color techniques
- [[Oblique-Area-Chart]] — complete workflow using this hack
