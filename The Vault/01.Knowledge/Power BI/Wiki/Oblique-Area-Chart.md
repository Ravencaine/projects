---
created: 2026-07-29
updated: 2026-08-04
source: "How I Built a Modern Oblique Area Chart in Power BI Using Only Native Visuals.md"
note_type: workflow
tags: [area-chart, line-chart, oblique, error-bands, error-band-as-mask, background-image, figma, native-visuals, custom-tooltip, vital-stats, ki-data-science]
related: [Error-Band-as-White-Out-Mask, Time-Period-Slicers, figma-to-power-bi-canvas-background, Bar-to-Area-Conversion, Dynamic-Line-Area-Chart-Color, Source-Oblique-Area-Chart]
---

# Oblique Area Chart (Line Chart + Background PNG + Error Bands)

Recreates the modern, slanted/oblique area chart look seen in healthcare and modern consumer apps — using **only native Power BI visuals**: a **line chart**, a **transparent oblique PNG background**, and **error bands repurposed as a white-out mask**.

> **Correction 2026-08-04:** This note previously described the technique as a bar-to-area conversion with `MAXX(...)*1.05` buffer math. Per the verified source article ([[Source-Oblique-Area-Chart]]), the technique is actually a **line chart** (not bar conversion), uses `CALCULATE(MAXX(...)) + 0.05 * _MaxVital` style var-based buffer math, and the "magic" step is [[Error-Band-as-White-Out-Mask|error bands used as a white-out mask]] (not statistical error bars).

## Data Model

A single wide-but-tall table with a discriminator column — the article's pattern is generalisable to any metric that has min/max/avg per date.

```text
Vital Stats
├── Date           (date)
├── Measure Type   (text: "Average" | "Max" | "Min")
└── Value          (number)
```

The three core measures each filter by `Measure Type` and sum `Value`:

```dax
Average Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Average")
    )

Max Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Max")
    )

Min Vital =
    CALCULATE(
        SUM('Vital Stats'[Value]),
        FILTER('Vital Stats', 'Vital Stats'[Measure Type] = "Min")
    )
```

The detail tables (any columnar tables of vitals) feed the aggregate `Vital Stats` table — only `Vital Stats` is plotted.

## Prerequisites

- A Power BI line chart (not an area chart — see "Why a line chart, not an area chart" below).
- An "Average / Max / Min" measure trio as above, plus the two helper measures below.
- A Figma (or PowerPoint / Affinity / Canva) export of an oblique background PNG sized to match the chart's plot area.
- A single-select slicer on `Vital` (the metric to view).

## Steps

### 1. Build the line chart

Add `Date` to the X-axis and all three measures (`Average Vital`, `Max Vital`, `Min Vital`) to the Y-axis of a **line chart**. Add a single-select slicer on the vital name. At this stage you have a typical three-line chart.

### 2. Add an oblique background PNG

1. Design the oblique background in Figma (e.g., a white rectangle with a diagonal cut on the bottom edge, with whatever decorative shape/color sits behind it).
2. Export as **PNG** with transparency preserved.
3. In Power BI, add the PNG as a background image behind the chart area.
4. Resize the image and chart so the image covers the entire **plot area**, sitting *behind* the chart.
5. Turn off the chart's own background (Visualizations → Format → Plot area / Wall / Floor → transparency = 100% or disabled fills). The chart must not paint over the oblique PNG.

> For a SVG (whole-canvas background) workflow see [[figma-to-power-bi-canvas-background]]. The article here uses a PNG sized to the plot area, which gives finer control over which part of the design is "behind the chart."

### 3. Constrain the Y-axis with `Max Graph Area` / `Min Graph Area`

These two measures inflate the natural min/max by 5% so the chart gets head/foot room. **Use these as the chart's Y-axis min and max** — not the natural Max Vital / Min Vital — so the chart edges don't slam against the top of the plot area:

```dax
Max Graph Area =
VAR _MaxVital =
    CALCULATE(
        MAXX(ALL('Vital Stats'[Date]), [Max Vital])
    )
RETURN
    _MaxVital + 0.05 * _MaxVital

Min Graph Area =
VAR _MinVital =
    CALCULATE(
        MINX(ALL('Vital Stats'[Date]), [Min Vital])
    )
RETURN
    _MinVital - 0.05 * _MinVital
```

Assign both to the chart's Y-axis Minimum / Maximum via **Field value** (Visualizations → Format → Y-axis → Min / Max → Field value).

### 4. Mask the chart edges with error bands (white-out trick)

In the **Analytics** pane of the visualization, create error bars:

- **Max Vital series** — Upper bound = `Max Graph Area`, Lower bound = `Max Vital`
- **Min Vital series** — Upper bound = `Min Vital`, Lower bound = `Min Graph Area`
- Enable only the **Error Band** option (not the line/bar caps). Set style to **Fill**. Set fill color to **white**. Transparency = **0%**.

Then set the **line color** of both `Max Graph Area` and `Min Graph Area` series to **white** so the helper series disappear.

The effect: anything above `Max Vital` and anything below `Min Vital` is painted solid white by the error band, hiding the chart's natural rectangular bounding box. The oblique background PNG "shows through" through the white, giving the illusion of a modern slanted-area look.

> See [[Error-Band-as-White-Out-Mask]] for the standalone technique (it's generalisable to many decorative chart tricks, not just this oblique look).

### 5. Final formatting touches

- `Average Vital` line: darker blue, **4 px** width.
- `Max Vital` / `Min Vital` series: **6 px** markers.
- Remove axis titles; update label font for cleanliness.
- Assign a **custom tooltip page** to the chart so `Max Graph Area` / `Min Graph Area` (invisible helper measures) don't pollute the default tooltip.

### 6. (Optional) Wire a dynamic X-axis to a period slicer

Use a period lookup table (`"1W"`, `"1M"`, `"6M"`, `"1Y"`) and a `Minimum Date` measure to drive the chart's X-axis minimum via Field value — see [[Time-Period-Slicers]].

## Why a Line Chart, Not an Area Chart

The article explicitly states the look is built with a **line chart**, not an area chart, and not via [[Bar-to-Area-Conversion]]. The fill effect comes entirely from the background PNG + white-out error bands. The line chart's translucent strokes deliberately sit on top of the oblique background, so any added area fills would interfere with the design.

## Why `CALCULATE(MAXX(ALL(...)))` with a Variable

`MAXX(ALL(...), [Max Vital])` alone can be influenced by whatever filter context happens to live on the page (e.g., the vital slicer). Wrapping it in `CALCULATE(...)` and assigning to a `_MaxVital` variable isolates the calculation: the variable stores the *unconstrained global* max vital regardless of the slicer, then the buffer arithmetic (`+ 0.05 * _MaxVital`) runs on that single unfiltered value. This produces a stable chart envelope regardless of which vital is selected.

## Notes

- The background PNG is purely decorative — there is no statistical meaning, no shaded confidence interval, no actual uncertainty being communicated. Use with clear labelling so the audience doesn't read statistical intent into it.
- Test the PNG background at multiple zoom levels and on Power BI Service (rendering can shift).
- Bittar's PBIX is available for download from the article (see source note for the Google Drive link).
- Do **not** also apply [[Dynamic-Line-Area-Chart-Color]] overlay — the single line chart is the whole picture; overlays would muddy the design.

## Related

- [[Error-Band-as-White-Out-Mask]] — the specific white-out error band trick (distinct from statistical error bars)
- [[Time-Period-Slicers]] — dynamic X-axis minimum driven by a period slicer
- [[figma-to-power-bi-canvas-background]] — Figma SVG → whole canvas background (sibling workflow)
- [[Bar-to-Area-Conversion]] — a different colour-area technique; **does not** produce the oblique look
- [[Dynamic-Line-Area-Chart-Color]] — overlay approach for per-segment colour; **not used** in this chart
- [[Source-Oblique-Area-Chart]] — verified source article
