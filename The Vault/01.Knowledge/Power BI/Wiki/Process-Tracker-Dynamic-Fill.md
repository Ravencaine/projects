---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [shapes, fill-color, border-color, icons, progress-tracker]
related: [HTML-Content-Visual, SWITCH, Process-Tracker-Complete]
---

# Shape-Based Process Tracker (Dynamic Fill Color)

Uses Power BI shape objects (ovals, rectangles, lines) placed on the canvas, with DAX measures assigned to the shape's Fill Color and Border Color properties to create a fully dynamic, multi-step process tracker.

## Data Model

Two tables, **no relationships** in the model:

**JobReqs** table:

| Job Requisition | Current Stage |
|-----------------|--------------|
| JR-001 | Applications Screening |
| JR-002 | Job Posting |

**Stages** table (sort order):

| Stage | Order |
|-------|-------|
| Job Posting | 1 |
| Applications Screening | 2 |
| Phone Interview | 3 |
| On-site Interview | 4 |
| Offer | 5 |

## DAX Measures

**Stage order for selected job:**
```dax
Selected Stage Order =
VAR _SelectedStage = SELECTEDVALUE(JobReqs[Current Stage])
RETURN
    CALCULATE(
        MAX(Stages[Order]),
        FILTER(Stages, Stages[Stage] = _SelectedStage)
    )
```

**Color constants:**
```dax
_const Color Blue   = "#4059ad"   // completed
_const Color Orange = "#fe5f55"   // in progress
_const Color Grey   = "#B5C2CA"   // not started
_const Color Green  = "#018b77"   // accent
_const Color Trans  = "#FFFFFF00" // transparent
```

**Fill color for each step:**
```dax
Step 1 Fill Color =
    SWITCH(TRUE(),
        [Selected Stage Order] > 1, [_const Color Blue],
        [Selected Stage Order] = 1, [_const Color Orange],
        [_const Color Grey]
    )
```

**Border color for connector lines:**
```dax
Step 1 Line Color =
    IF(
        [Selected Stage Order] > 1,
        [_const Color Blue],
        [_const Color Grey]
    )
```

## Setup Steps

1. Insert ovals from the **Insert → Shapes** menu for each process step.
2. Insert lines between steps as connectors.
3. Add text boxes below each oval for step names.
4. Add icon images (PNG, from Flaticon) on top of each oval.
5. Add rounded-corner rectangles above each step for "In Progress" labels.
6. For each shape, assign the corresponding measure to its **Fill Color** or **Border Color** in the formatting pane.
7. Add a slicer for `Job Requisition` from the `JobReqs` table.

## Notes

- No DAX relationship needed — the `CALCULATE + FILTER` pattern looks up the stage order from the Stages table without a relationship.
- Each shape gets its own named measure (`Step 1 Fill Color`, `Step 2 Fill Color`, etc.).
- `IF` and `SWITCH` drive all color logic — the measures are read-only by the shapes.
- For icons, Bittar uses the **HTML Content** custom visual with Font Awesome CDN — see [[HTML-Content-Visual]].
- The transparent color (`#FFFFFF00`) hides the "In Progress" label border for completed steps.

## Related

- [[HTML-Content-Visual]] — Font Awesome icons via HTML Content visual
- [[SWITCH]] — core conditional logic for all color assignments
- [[Process-Tracker-Complete]] — full end-to-end workflow
