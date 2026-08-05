---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [bubble-chart, dual-overlay, selective-labels, top-n, axis-sync]
related: [Context-Sensitive-Visual-Toggle, RANKX, SWITCH]
---

# Dual Bubble Chart Overlay (Selective Labels)

Overlays two identical bubble charts to show data labels on only a selected subset of bubbles (e.g., top 3 by a metric) while keeping all bubbles visible.

## The Problem

Power BI's native bubble chart does not support conditional data labels — enabling labels shows them on all bubbles, which is unreadable for charts with many categories.

## The Solution

1. Create **two identical bubble charts** using the same data.
2. Add a `Values To Show` measure to each chart's filter pane:
   - Chart A: filter = `Values To Show` = 0 (no labels)
   - Chart B: filter = `Values To Show` = 1 (labels shown)
3. Enable **data labels** only on Chart B.
4. Overlay Chart B on top of Chart A.
5. Synchronize axes using fixed min/max measures.

## DAX Measures

**Top-N ranking (remove slicer filter for absolute ranking):**
```dax
No.1 Ranking =
    CALCULATE(
        RANKX(
            ALL('NAICS Industry'[Industry]),
            [Vacancy Rate],
            ,
            DESC,
            DENSE
        ),
        REMOVEFILTERS()
    )
```

**Values To Show (filter control):**
```dax
Values To Show =
VAR _No1 = CALCULATE([No.1 Ranking], ALL('NAICS Industry'[Industry]))
VAR _No2 = CALCULATE([No.2 Ranking], ALL('NAICS Industry'[Industry]))
VAR _No3 = CALCULATE([No.3 Ranking], ALL('NAICS Industry'[Industry]))
RETURN
    SWITCH(
        TRUE(),
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No1, 1,
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No2, 1,
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No3, 1,
        0
    )
```

**Axis synchronization:**
```dax
Max X Axis =
    MAXX(
        ALL('NAICS Industry'[Industry]),
        [Vacancy Rate]
    ) + 0.02

Max Y Axis =
    MAXX(
        ALL('NAICS Industry'[Industry]),
        [Payroll Employees]
    ) + 500000
```

## Notes

- `REMOVEFILTERS()` inside `CALCULATE` makes the ranking absolute — top 3 always highlighted regardless of slicer selection.
- Set `DENSE` rank in `RANKX` to avoid gaps in the ranking sequence.
- Axis synchronization is critical — use `MAXX(ALL(...), [Metric])` to find the absolute max and add a small buffer (+0.02 for rates, +500000 for large numbers).
- Remove axis titles and gridlines from Chart B (the overlay) for a clean look — only Chart A's axes should show.
- Bittar also adds a manual legend explaining the bubble size since Power BI's native bubble chart doesn't auto-generate a size legend.

## Related

- [[RANKX]] — identify top-N items
- [[SWITCH]] — generate 0/1 flag for filter
- [[Context-Sensitive-Visual-Toggle]] — the IF/BLANK pattern driving the overlay
