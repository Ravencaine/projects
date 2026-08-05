---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [context-switching, visual-filter, IF-measure, stacked-visuals]
related: [Dual-Bubble-Chart-Overlay, Dynamic-Line-Area-Chart-Color]
---

# Context-Sensitive Visual Toggling

Uses an `IF` measure as a visual-level filter to show or hide entire visual layers, switching between different chart types depending on the user's data selection.

## Pattern

**Step 1 — Create a toggle measure:**
```dax
Show Bar Chart =
    IF(
        [Total Categories] <= 5,
        1,
        BLANK()
    )
```

**Step 2 — Create the alternate view:**
```dax
Show Summary Cards =
    IF(
        [Total Categories] > 5,
        1,
        BLANK()
    )
```

**Step 3 — Assign to each visual's filter pane:**

- Visual A (Bar Chart): filter = `Show Bar Chart` equals `1`
- Visual B (Summary Cards): filter = `Show Summary Cards` equals `1`

**Step 4 — Overlay visuals in the same position.**

## Bubble Chart Example (Selective Labels)

In Bittar's bubble chart article, two identical bubble charts are overlaid — one shows all labels, the other shows only top-N labels:

```dax
Values To Show =
VAR _No1 = CALCULATE([No.1 Ranking], ALL(...))
VAR _No2 = CALCULATE([No.2 Ranking], ALL(...))
VAR _No3 = CALCULATE([No.3 Ranking], ALL(...))
RETURN
    SWITCH(
        TRUE(),
        SELECTEDVALUE(...) = _No1, 1,
        SELECTEDVALUE(...) = _No2, 1,
        SELECTEDVALUE(...) = _No3, 1,
        0
    )
```

- Chart A filter: `Values To Show` = 0 (shows all non-top-N labels)
- Chart B filter: `Values To Show` = 1 (shows only top-3 labels)
- Chart B has data labels enabled; Chart A does not.

## Notes

- `BLANK()` in the filter means "hide this visual" — blank does not pass the filter.
- This is the same mechanism as the [[Dual-Bubble-Chart-Overlay]] and [[Dynamic-Line-Area-Chart-Color]] patterns — just varying which dimension controls the toggle.
- Works with any visual type — cards, KPIs, tables, charts.
- For a cleaner implementation, group the overlaid visuals and control their visibility from a single bookmark.
- Bittar's bubble chart technique uses `Values To Show` as a 0/1 measure to separate the label and no-label layers — this is a special case where the two charts use the same data but different label settings.

## Related

- [[Dual-Bubble-Chart-Overlay]] — specific application for bubble chart labels
- [[Dynamic-Line-Area-Chart-Color]] — overlay for conditional color
- [[if]] — measure that returns 1 or BLANK()
