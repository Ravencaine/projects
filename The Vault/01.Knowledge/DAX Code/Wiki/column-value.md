---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, switch, dynamic, chart]
---

# Column Value

A SWITCH measure that returns the active chart metric based on the selected button highlight.

## Signature

```dax
Column Value =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Employees (Last 7 Days)],
        2, [OT Hours per FTE Variance %],
        3, [OT Hours This Week],
        4, [Filled Rate % This Week]
    )
```

## Parameters

None — reads `SELECTEDVALUE(Highlights[Order])` directly.

## Returns

A scalar metric — whichever measure corresponds to the selected highlight.

## Notes

Bound to the **Values** field of a clustered column chart. When the button slicer selection changes, the chart immediately switches to displaying the corresponding metric. Each highlight maps to a semantically different metric type: a count (highlight 1), a percentage variance (highlight 2), an absolute total (highlight 3), and a fill rate (highlight 4).

## Related

- [[Column-Color]]
- [[Graph-Title]]
- [[Graph-Subtitle]]
- [[highlights-table-unconnected-helper-table]]
