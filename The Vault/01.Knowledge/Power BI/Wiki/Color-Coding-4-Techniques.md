---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [conditional-formatting, color-coding, color-by-measure, color-by-rules]
related: [SWITCH, Dynamic-Bar-Chart-Color, Color-Area-Charts-With-Markers]
---

# Color-Coding 4-Technique Reference

A comprehensive reference of four conditional formatting techniques in Power BI, ranging from simple to advanced.

## Technique 1 — Color by Rules (Static Thresholds)

Apply static threshold rules directly in the formatting pane.

- Use when thresholds are fixed (e.g., ≥ 80% = green, < 50% = red).
- Set in: **Visualizations → Format → Cell elements → Conditional formatting → Background color → Rules**.

## Technique 2 — Color by Field Value (SWITCH + DAX)

Assign a DAX measure returning hex color strings to a field value formatting property.

```dax
Category Color =
    SWITCH(
        SELECTEDVALUE(Category[Category]),
        "Revenue",     "#76E3B4",
        "Cost",        "#EE6064",
        "Budget",      "#F5A623",
        "#B5C2CA"
    )
```

- Assign the measure to **Data colors → Field value**.
- Works on: bar charts, column charts, table matrices.
- In Bittar's process tracker, this drives the fill color of shape objects.

## Technique 3 — Color by Measure (Dynamic Thresholds)

Use a measure to calculate dynamic thresholds, then assign it as a field value color.

```dax
Dynamic Color =
    SWITCH(
        TRUE(),
        [Metric] >= [Max Threshold], "#76E3B4",
        [Metric] >= [Min Threshold], "#F5A623",
        "#EE6064"
    )
```

- Thresholds themselves are DAX measures — they recalculate with the data.
- Assign to: **Data colors → Apply to → Field value** → select the color measure.

## Technique 4 — Overlay Charts (Line/Area Color)

Native per-series formatting does not support conditional coloring. Use two overlaid charts.

See: [[Dynamic-Line-Area-Chart-Color]]

## Summary Table

| Technique | Visual Type | Dynamic Thresholds | Per-Point Color |
|-----------|------------|-------------------|----------------|
| Rules (pane) | Table, Matrix, KPI | ❌ (static) | N/A |
| Field Value (DAX) | Bar, Column, Table | ✅ | N/A |
| Color by Measure | Bar, Column, KPI | ✅ | N/A |
| Overlay Charts | Line, Area | ✅ | ✅ |

## Notes

- Technique 2 and 3 are the most powerful — the measure runs in the filter context of the visual, so colors respond to slicers and cross-filtering.
- For shapes and text boxes, assign the color measure to the **Fill → fx → Field value** option.
- Power BI caches color assignments — force a refresh by toggling a slicer or pressing F5.
- Bittar's articles use Technique 3 (dynamic thresholds via SWITCH) in virtually every visualization.

## Related

- [[SWITCH]] — core DAX function for all conditional coloring
- [[Dynamic-Line-Area-Chart-Color]] — Technique 4 overlay
- [[Color-Area-Charts-With-Markers]] — combining color with markers and target lines
