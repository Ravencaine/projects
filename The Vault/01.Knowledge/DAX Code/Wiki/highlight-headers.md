---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, overtime, highlight]
---

# Highlight Headers

A SWITCH measure that returns the formatted text for the currently selected highlight button.

## Signature

```dax
Highlight Headers =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Flag Highlight],
        2, [Biggest Rise Highlight],
        3, [Top Unit Highlight],
        4, [Lowest Fill Rate Highlight]
    )
```

## Parameters

None — reads `SELECTEDVALUE(Highlights[Order])` directly.

## Returns

A string — the text of the active highlight.

## Notes

`SELECTEDVALUE` returns the single selected value from the button slicer. When nothing is selected, `SELECTEDVALUE` returns BLANK — SWITCH falls through without a matching case and also returns BLANK. The underlying highlight measures return formatted strings with emoji prefixes and metric detail (e.g. `"👥 5 employees >10h OT this week"`).

## Related

- [[button-slicer]]
- [[highlights-table-unconnected-helper-table]]
- [[High-OT-Flag-Highlight]]
- [[Biggest-Rise-Highlight]]
- [[Top-Unit-Highlight]]
- [[Lowest-Fill-Rate-Highlight]]
