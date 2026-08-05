---
created: 2026-08-02
source: Revolutionize Your Bar Charts: Axis Titles Atop Bars in Power BI
note_type: snippet
tags: [dax, snippet, selectedvalue, concat, custom-label, bar-chart]
---

# Data Label = SELECTEDVALUE(Category) & ": " & [Metric] — Inline Concatenation

Combines the current category name with its metric value into a single string for use as a bar chart custom label.

```dax
Data label =
VAR _Region = SELECTEDVALUE('Postes vacants'[Région administrative])
RETURN _Region & ": " & [Vacant positions]
```

**Pattern:** `SELECTEDVALUE(<column>)` extracts the single active category in the current filter context; concatenating it with the metric creates a self-contained label (e.g., `"Capitale-Nationale: 42"`). Place this measure on an `Empty = 0` series and enable **Custom label** to render it on the bar.

> Used in the "Axis Titles Atop Bars" pattern for a label-forward bar chart with no traditional axes.
