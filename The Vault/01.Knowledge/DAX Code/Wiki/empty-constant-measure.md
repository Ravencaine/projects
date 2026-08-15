---
created: 2026-08-02
updated: 2026-08-02
source: Revolutionize Your Bar Charts: Axis Titles Atop Bars in Power BI
note_type: snippet
tags: [dax, snippet, constant, zero, x-axis, bar-chart, visual]
---

# Empty = 0 — Zero-Constant Measure for X-Axis Spacing

A measure returning a literal `0` placed on a chart axis to control bar sizing and spacing when the axis is disabled.

```dax
Empty = 0
```

**Purpose:** With Y-axis and X-axis turned off in a bar chart, placing this measure on the X-axis gives the visual engine a reference for bar width and spacing. It produces no visible data — only structural layout control.

> Used in the "Axis Titles Atop Bars" pattern where it holds the custom label measure via the Custom label field.
