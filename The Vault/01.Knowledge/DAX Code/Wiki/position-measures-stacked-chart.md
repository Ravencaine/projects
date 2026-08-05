---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
note_type: function
tags: [dax, function, position-measure, rank-arithmetic, switch, calculate, stacked-chart]
---

# Position Measures (Position 1–N)

A set of measures — one per stacking slot — that dynamically assign the selected category to Position 1 (the baseline) and distribute all remaining categories across Positions 2 through N in their original relative order.

## Position 1 — Always the Selected Category

```dax
Position 1 =
VAR Sel = SELECTEDVALUE ( Selector[Category] )
RETURN
    IF ( NOT ISBLANK ( Sel ),
        CALCULATE ( [Your Measure], Dim[Category] = Sel )
    )
```

## Position k — Remaining Categories (General Formula)

```dax
Position 2 =
-- for "Position k", replace every k below with (k - 1)
VAR Sel = SELECTEDVALUE ( Selector[Category] )
VAR SelRank =
    SWITCH ( Sel,
        "Value A", 1, "Value B", 2, "Value C", 3 /* …, "Value N", N */
    )
VAR TargetRank = IF ( 1 < SelRank, 1, 1 + 1 )
VAR TargetCategory =
    SWITCH ( TargetRank,
        1, "Value A", 2, "Value B", 3, "Value C" /* …, N, "Value N" */
    )
RETURN
    IF ( NOT ISBLANK ( Sel ),
        CALCULATE ( [Your Measure], Dim[Category] = TargetCategory )
    )
```

For Position 3, change `1` → `2` throughout the `TargetRank` calculation:
```dax
VAR TargetRank = IF ( 2 < SelRank, 2, 2 + 1 )
```

## How the Rank Arithmetic Works

Every category has a fixed rank (1, 2, 3…, N). When a category is selected, its rank is removed from the list. The remaining ranks are compacted:

> **k, if k comes before the selected rank; k + 1, otherwise**

Single line: `TargetRank = IF ( k < SelRank, k, k + 1 )`

This means non-selected categories always maintain their original relative order, regardless of which category is selected.

## Alternative for N=3 (Simple SWITCH)

For exactly 3 categories, skip the rank formula and write direct SWITCH branches:

```dax
Position 2 =
VAR Sel = SELECTEDVALUE ( Selector[Category] )
RETURN
    SWITCH ( TRUE (),
        Sel = "Value A", CALCULATE ( [Your Measure], Dim[Category] = "Value B" ),
        Sel = "Value B", CALCULATE ( [Your Measure], Dim[Category] = "Value A" ),
        CALCULATE ( [Your Measure], Dim[Category] = "Value A" )
    )
```

Simpler to read for small, fixed N. Use the general formula for 5+ categories.

## Related

- [[stacked-chart-baseline-highlight-pattern]] — `pattern`
- [[stacked-chart-baseline-order-matters]] — `atomic`
- [[color-by-position-visual-formatting]] — `pattern`
