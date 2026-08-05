---
created: 2026-08-02
source: Revolutionize Your Bar Charts: Axis Titles Atop Bars in Power BI
note_type: pattern
tags: [powerbi, pattern, bar-chart, axis, custom-label, visual-formatting, compact]
---

# Bar Chart: Axis Titles Atop Bars (Disable Axes + Empty Measure + Custom Labels)

Replaces standard Y/X axes with custom inline labels on the bars themselves for a compact, label-forward aesthetic.

**Steps:**

1. **DAX measure for the metric:** `Vacant positions = SUM('Postes vacants'[Valeur])`
2. **Disable both Y-axis and X-axis** in the visual formatting pane — clears space for labels
3. **Zero-constant measure** `Empty = 0` — placed on the X-axis to create bar-width spacing
4. **Custom label measure** concatenates category name with value:
   ```dax
   Data label =
   VAR _Region = SELECTEDVALUE('Postes vacants'[Région administrative])
   RETURN _Region & ": " & [Vacant positions]
   ```
5. Place the custom label measure on the `Empty` series → toggle on **Custom label** → enter the measure in the Field box
6. **Tune visual settings:** Inner Padding (bar spacing), Minimum Category Width (bar width)

**Result:** region names appear directly on top of each bar alongside the value — no traditional axis text needed.

> Inspired by Bas (How To Power BI), adapted by Bittar for the KI Data Science audience.
