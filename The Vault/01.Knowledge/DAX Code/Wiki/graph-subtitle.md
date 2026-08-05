---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, switch, dynamic, subtitle]
---

# Graph Subtitle

A SWITCH measure that returns a formatted detail string for the dynamic chart subtitle, mirroring the text logic of the corresponding highlight measures.

## Signature

```dax
Graph Subtitle =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Flag Highlight Subtitle],
        2, [Biggest Rise Highlight Subtitle],
        3, [Top Unit Highlight Subtitle],
        4, [Lowest Fill Rate Highlight Subtitle]
    )
```

## Parameters

None — reads `SELECTEDVALUE(Highlights[Order])` directly.

## Returns

A string — the subtitle text for the active chart.

## Notes

Each subtitle measure (`High OT Flag Highlight Subtitle`, etc.) mirrors the logic of the corresponding main highlight measure but includes additional detail appropriate for a chart subtitle. These are stored under the `Graph/Subtitles` folder in the PBIX measure tree.

## Related

- [[Graph-Title]]
- [[Column-Value]]
- [[high-ot-flag-highlight]]
