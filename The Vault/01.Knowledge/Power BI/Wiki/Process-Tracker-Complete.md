---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [process-tracker, shapes, icons, dynamic-fill, border-color, progress]
related: [Process-Tracker-Dynamic-Fill, HTML-Content-Visual, SWITCH]
---

# Process Tracker — Complete Workflow

End-to-end implementation of a multi-step process tracker in Power BI using shapes, DAX measures, and the HTML Content visual.

## Step 1 — Data Model

Create two tables in Excel and load to Power BI (no relationships):

**JobReqs:**

| Job Requisition | Current Stage |
|----------------|--------------|
| JR-001 | Applications Screening |
| JR-002 | Job Posting |

**Stages:**

| Stage | Order |
|-------|-------|
| Job Posting | 1 |
| Applications Screening | 2 |
| Phone Interview | 3 |
| On-site Interview | 4 |
| Offer | 5 |

## Step 2 — Shapes

From **Insert → Shapes**, place:
- **Ovals** for each step (Job Posting, Applications Screening, etc.)
- **Lines** between each oval as connectors
- **Text boxes** below each oval with step names
- **Rectangles** (rounded corners) above each oval for "In Progress" labels
- **Images** (from Flaticon) on top of each oval

## Step 3 — DAX Measures

**Stage lookup:**
```dax
Selected Stage Order =
VAR _SelectedStage = SELECTEDVALUE(JobReqs[Current Stage])
RETURN
    CALCULATE(
        MAX(Stages[Order]),
        FILTER(Stages, Stages[Stage] = _SelectedStage)
    )
```

**Colors:**
```dax
_const Color Blue   = "#4059ad"
_const Color Orange = "#fe5f55"
_const Color Grey   = "#B5C2CA"
_const Color Green  = "#018b77"
_const Color Trans  = "#FFFFFF00"
```

**Per-step fill color (repeat for each step):**
```dax
Step 1 Fill =
    SWITCH(TRUE(),
        [Selected Stage Order] > 1, [_const Color Blue],
        [Selected Stage Order] = 1, [_const Color Orange],
        [_const Color Grey]
    )
```

**Per-step border color:**
```dax
Step 1 Border =
    IF(
        [Selected Stage Order] > 1,
        [_const Color Blue],
        [_const Color Grey]
    )
```

**Progress label:**
```dax
Step 1 Progress Label =
    IF([Selected Stage Order] = 1, "In Progress")
```

**Progress label border:**
```dax
Step 1 Progress Border =
    IF([Selected Stage Order] = 1, [_const Color Green], [_const Color Trans])
```

**Icons (HTML Content):**
```dax
Step 1 Icon =
    SWITCH(TRUE(),
        [Selected Stage Order] > 1, [_const Icon Green Check],
        [Selected Stage Order] = 1, [_const Icon In Progress]
    )
```

## Step 4 — Assign Measures

For each shape: select the shape → **Fill → fx → Field value** → select the corresponding measure.

Repeat for border color, progress label, and progress border.

## Step 5 — Add Slicer

Add a Slicer visual with `Job Requisition` from the `JobReqs` table.

## Notes

- No data model relationship is needed — the `CALCULATE + FILTER` pattern looks up stage order without a relationship.
- Each step requires its own named measure — Power BI does not support parameterized shapes.
- Test each step's color by selecting different job requisitions from the slicer.
- The HTML Content visual must be added separately for the icons — shapes handle fill/border; HTML Content handles icons.

## Related

- [[Process-Tracker-Dynamic-Fill]] — pattern note with DAX details
- [[HTML-Content-Visual]] — Font Awesome icons
- [[SWITCH]] — conditional logic for all color and icon assignments
