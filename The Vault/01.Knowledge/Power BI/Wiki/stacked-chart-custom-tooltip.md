---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: pattern
tags: [power-bi, pattern, tooltip, matrix-visual, tooltip-page, disconnected-table, measure]
---

# Stacked Chart Custom Tooltip Page

A dedicated tooltip page that replaces the chart's native tooltip with a custom Matrix showing real category names, percentages, and absolute values — with the highlighted category listed first and the rest in original order.

## Why the Native Tooltip Doesn't Work

The native tooltip shows "Position 1", "Position 2"… — not the real category names — because the chart series are position-based, not category-based. A custom tooltip page is required.

## The Tooltip Position Table

```dax
Tooltip Position =
DATATABLE ( "Pos", INTEGER,
    { {1}, {2}, {3} /* …, {N} */ }
)
```

This tiny disconnected table replaces `Dim[Category]` as the Matrix's row source. Because its rows are pre-ordered (1, 2, 3…), the Matrix rows come out **highlighted-first, no helper sort column needed**.

## Tooltip Measures

### Ord Category — Which Category Occupies This Row's Position

```dax
Ord Category =
VAR Pos = SELECTEDVALUE ( 'Tooltip Position'[Pos] )
VAR Sel = SELECTEDVALUE ( Selector[Category] )
VAR SelRank = SWITCH ( Sel,
    "Value A", 1, "Value B", 2, "Value C", 3 /* …, N, "Value N" */ )
VAR Offset = Pos - 1
VAR TargetRank = IF ( Pos = 1, SelRank,
    IF ( Offset < SelRank, Offset, Offset + 1 ) )
RETURN
    IF ( NOT ISBLANK ( Sel ),
        SWITCH ( TargetRank,
            1, "Value A", 2, "Value B", 3, "Value C" /* …, N, "Value N" */
        )
    )
```

### Ord Value — Percentage for This Row's Category

```dax
Ord Value =
VAR TargetCategory = [Ord Category]
RETURN
    IF ( NOT ISBLANK ( TargetCategory ),
        CALCULATE ( [Your % Measure], Dim[Category] = TargetCategory )
    )
```

### Ord Absolute Value — Raw Value for This Row's Category

```dax
Ord Absolute Value =
VAR TargetCategory = [Ord Category]
RETURN
    IF ( NOT ISBLANK ( TargetCategory ),
        CALCULATE ( [Your Measure], Dim[Category] = TargetCategory )
    )
```

### Ord Font Color — Bold the Highlighted Row

```dax
Ord Font Color =
IF ( SELECTEDVALUE ( 'Tooltip Position'[Pos] ) = 1, "#004E89" )
```

Returns blank for other rows so they keep normal font color.

## Tooltip Page Setup

1. Add a new report page → **Format pane → Page type: Tooltip**
2. Drop a **Matrix** visual (not Table — see gotcha below)
   - **Rows**: `Tooltip Position[Pos]`
   - **Values**: `Ord Category`, `Ord Value`, `Ord Absolute Value`
3. Apply `Ord Font Color` as conditional font color on the Category field
4. On the main chart → **Format visual → Tooltips → Type: Report page** → select the tooltip page

## Gotcha: Use Matrix, Not Table

A plain Table visual cannot dynamically re-sort its rows by a measure unless that measure is a visible column. A Matrix visual respects the row order of the grouping column directly — which is why `Tooltip Position[Pos]` (pre-sorted 1, 2, 3…) is used as the row source.

## Expected Behavior

With no slicer selection, the tooltip shows empty (all Ord measures depend on `SELECTEDVALUE(Selector[Category])` which is blank). Select a category on the main page — slicer selections apply report-wide and the tooltip populates.

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[color-by-position-visual-formatting]] — `pattern`
