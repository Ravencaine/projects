---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, switch, dynamic-title, title]
---

# Graph Title

A SWITCH measure that returns a static title string for the dynamic chart based on the selected highlight.

## Signature

```dax
Graph Title =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, "Employees with >10h of OT This Week",
        2, "Variation of OT Hours per FTE Since Last Week",
        3, "OT Hours This Week",
        4, "Shift Fill Rate by Department"
    )
```

## Parameters

None — reads `SELECTEDVALUE(Highlights[Order])` directly.

## Returns

A string — the title for the active chart.

## Notes

Bound to the chart's **Title** property. Unlike the subtitle, the title is always a static string — no DAX computation, just one of four pre-written strings selected by SWITCH. The subtitle (via `Graph Subtitle`) adds the dynamic detail computed from the actual data.

## Related

- [[Graph-Subtitle]]
- [[Column-Value]]
- [[Column-Color]]
