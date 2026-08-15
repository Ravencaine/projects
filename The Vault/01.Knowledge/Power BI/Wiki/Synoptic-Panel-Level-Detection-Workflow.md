---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: workflow
tags: [power-bi, isinscope, isatlevel, synoptic-panel, custom-visual, non-calendar-hierarchy, level-detection, workflow]
---

# Synoptic Panel Level Detection Workflow

**Type:** Workflow · **KB:** Power BI · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Use ISINSCOPE or ISATLEVEL to drive per-level formatting in non-calendar hierarchies, demonstrated with the OKVIZ Synoptic Panel custom visual. Same SWITCH dispatch principle as calendar hierarchies — the hierarchy is simply different.

## The Synoptic Panel context

Synoptic Panel maps measure values to regions on an image (e.g., seats in a venue). The hierarchy is **Seat → Sector → Category**, not a calendar hierarchy. The business logic:

| Level | Rule | Implementation |
|-------|------|---------------|
| Category | Gradient by occupation % | `DIVIDE(avgTickets, totalSeats)` |
| Sector | Gradient by occupation % | `DIVIDE(avgTickets, totalSeats)` |
| Seat | Binary: occupied or empty | `(avgTickets > 0) * 1` |

## Measure-based approach (ISINSCOPE)

```dax
% Occupation =
VAR AverageTicketEvent = DIVIDE([# Tickets], [# Events])
RETURN SWITCH(
    TRUE,
    ISINSCOPE(Seats[Seat]),
        (AverageTicketEvent > 0) * 1,
    ISINSCOPE(Seats[Sector]) || ISINSCOPE(Seats[Category]),
        DIVIDE(AverageTicketEvent, [Tot seats]),
    BLANK()
)
```

Key: Sector and Category share the same calculation — listed together in one branch.

## Visual calculation approach (ISATLEVEL)

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

Same structure — visual reference syntax instead of model column paths.

## Setup steps

1. Create hidden measures in the model: `[# Tickets]`, `[# Events]`, `[Tot seats]`
2. In the Synoptic Panel visual, include these as hidden measures
3. Assign the color measure to the Custom Color property
4. The visual detects level and applies the correct branch automatically

## Principle transfer

Any multi-level hierarchy — geographic (Country/Region/City), organizational (Division/Department/Team), product (Category/Subcategory/Product) — uses the same SWITCH dispatch pattern.

## Related

- [[SWITCH-Level-Dispatch-Pattern]] — the generic dispatch framework
- [[Choose-ISINSCOPE-vs-ISATLEVEL-Workflow]] — choosing between implementations
