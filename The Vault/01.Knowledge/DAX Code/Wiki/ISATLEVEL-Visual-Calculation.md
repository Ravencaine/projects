---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: pattern
tags: [dax, isatlevel, visual-calculation, collapse, collapseall, conditional-formatting, report-layer, pattern]
---

# ISATLEVEL Visual Calculation Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Use ISATLEVEL in a visual calculation to drive per-level conditional formatting. Logic lives at the report layer — no semantic model changes needed. Report developers without model authoring rights can implement this.

## When to use

- Consuming a shared dataset you cannot modify
- Logic is purely presentation-related and confined to one visual
- Performance matters — operates on the visual rowset, not the full model
- You want formatting changes without going through a deployment cycle

## Structure

```dax
Visual Level Color =
SWITCH(
    TRUE,
    -- Leaf level: share of parent using COLLAPSE
    ISATLEVEL([Hierarchy Leaf]),
        VAR LeafValue = [BaseMeasure]
        VAR ParentTotal = COLLAPSE([BaseMeasure], [Hierarchy Parent])
        RETURN IF(DIVIDE(LeafValue, ParentTotal) > 0.15, "Gold", BLANK()),

    -- Mid level: comparison to average (visual-aware)
    ISATLEVEL([Hierarchy Mid]),
        VAR MidValue = [BaseMeasure]
        VAR Average = CALCULATE(AVERAGEX(ROWS, [BaseMeasure]))
        RETURN IF(MidValue >= Average, "LightGreen", "LightPink"),

    -- Root level: share of grand total using COLLAPSEALL
    ISATLEVEL([Hierarchy Root]),
        VAR RootValue = [BaseMeasure]
        VAR GrandTotal = COLLAPSEALL([BaseMeasure], ROWS)
        VAR Share = DIVIDE(RootValue, GrandTotal)
        RETURN SWITCH(TRUE,
            Share > 0.40, "SteelBlue",
            Share > 0.25, "CornflowerBlue",
            Share > 0.15, "SkyBlue",
            "LightBlue"
        )
)
```

## COLLAPSE vs COLLAPSEALL — hierarchy navigation

| Function | What it does |
|----------|-------------|
| `COLLAPSE(measure, [Hierarchy Parent])` | Collapse one level up from current cell to the specified parent level |
| `COLLAPSEALL(measure, ROWS)` | Collapse all the way to the grand total (top of visual) |

These are the visual-calculation equivalents of `CALCULATE(..., REMOVEFILTERS(...))` in a measure.

## Visual reference syntax

ISATLEVEL takes a **visual reference**, not a model column path. Use the name as it appears in the visual (e.g., `[Year-Quarter-Month Month]`, not `'Date'[Month]`).

## Hidden measures required

For the visual calculation to access measure values as columns, include those measures as **hidden measures** in the visual.

## Synoptic Panel variant

```dax
Occupation Visual Calc =
VAR AverageTicketEvent = DIVIDE([# Tickets], [# Events])
RETURN SWITCH(
    TRUE,
    ISATLEVEL([Seat]),
        (AverageTicketEvent > 0) * 1,
    ISATLEVEL([Sector]) || ISATLEVEL([Category]),
        DIVIDE(AverageTicketEvent, [Tot seats]),
    BLANK()
)
```

## Performance advantage

Visual calculations operate on the smaller set of rows used to populate the visual. A measure could require additional internal queries to the full model, resulting in slower reports.

## Related

- [[SWITCH-Level-Dispatch-Pattern]] — general dispatch framework
- [[COLLAPSE-COLLAPSEALL-Hierarchy-Navigation]] — visual hierarchy navigation
- [[ISINSCOPE-vs-ISATLEVEL-Architectural-Location]] — architectural decision
