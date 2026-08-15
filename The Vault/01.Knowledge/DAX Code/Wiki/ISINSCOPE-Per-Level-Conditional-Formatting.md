---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: pattern
tags: [dax, isinscope, conditional-formatting, measure, semantic-model, level-detection, dynamic-formatting, pattern]
---

# ISINSCOPE Per-Level Conditional Formatting Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Use ISINSCOPE in a semantic model measure to drive per-level conditional formatting. Logic lives in the model — reusable across all reports consuming this dataset.

## When to use

- You own the semantic model and can add measures
- Level-detection logic needs to be reusable across multiple reports
- The format logic needs access to data not represented in the visual
- You want the formatting to persist regardless of which visual displays the measure

## Structure

```dax
Level Color =
SWITCH(
    TRUE,
    ISINSCOPE('Date'[MonthColumn]) || ISINSCOPE('Date'[MonthColumnShort]),
        -- Leaf: exception detection (e.g., > 15% of year)
        VAR LeafValue = [BaseMeasure]
        VAR ParentTotal = CALCULATE(
            [BaseMeasure],
            REMOVEFILTERS('Date'),
            VALUES('Date'[ParentColumn])
        )
        RETURN IF(DIVIDE(LeafValue, ParentTotal) > 0.15, "Gold", BLANK()),

    ISINSCOPE('Date'[QuarterColumn]),
        -- Mid: comparison to average
        VAR MidValue = [BaseMeasure]
        VAR Average = CALCULATE(
            AVERAGEX(VALUES('Date'[QuarterColumn]), [BaseMeasure]),
            REMOVEFILTERS('Date')
        )
        RETURN IF(MidValue >= Average, "LightGreen", "LightPink"),

    ISINSCOPE('Date'[YearColumn]),
        -- Root: share of grand total
        VAR RootValue = [BaseMeasure]
        VAR GrandTotal = CALCULATE([BaseMeasure], REMOVEFILTERS('Date'))
        VAR Share = DIVIDE(RootValue, GrandTotal)
        RETURN SWITCH(TRUE,
            Share > 0.40, "SteelBlue",
            Share > 0.25, "CornflowerBlue",
            Share > 0.15, "SkyBlue",
            "LightBlue"
        )
)
```

## Key patterns inside each branch

**Leaf level:** share of parent: `CALCULATE(measure, REMOVEFILTERS('Date'), VALUES('Date'[ParentColumn]))`

**Mid level:** comparison to average: `AVERAGEX(VALUES('Date'[MidColumn]), measure)` inside CALCULATE + REMOVEFILTERS

**Root level:** share of grand total: `CALCULATE(measure, REMOVEFILTERS('Date'))`

## REMOVEFILTERS vs ALLSELECTED

- **REMOVEFILTERS:** ignores slicers, compares against full model. Use when absolute comparison is correct.
- **ALLSELECTED:** respects visual slicers, compares against displayed range. Use when comparison should be local to what the visual shows.

## Synoptic Panel variant

Non-calendar hierarchies (e.g., Seats[Seat] → Seats[Sector] → Seats[Category]) use the same pattern:

```dax
% Occupation =
VAR AverageTicketEvent = DIVIDE([# Tickets], [# Events])
RETURN SWITCH(
    TRUE,
    ISINSCOPE(Seats[Seat]),
        (AverageTicketEvent > 0) * 1,           -- binary: sold or not
    ISINSCOPE(Seats[Sector]) || ISINSCOPE(Seats[Category]),
        DIVIDE(AverageTicketEvent, [Tot seats]), -- gradient
    BLANK()
)
```

## Related

- [[SWITCH-Level-Dispatch-Pattern]] — general dispatch framework
- [[ISINSCOPE-vs-ISATLEVEL-Architectural-Location]] — architectural decision
- [[REMOVEFILTERS-vs-ALLSELECTED-for-Per-Level-Rules]] — which CALCULATE modifier to use
