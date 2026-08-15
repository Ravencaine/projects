---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
source_url: "https://www.sqlbi.com/articles/dynamic-formatting-by-hierarchy-level-with-isinscope-and-isatlevel/"
author: "[[Marco Russo & Alberto Ferrari]]"
site: https://www.sqlbi.com
published: 2026-07-14
source_type: article
kb_routing: DAX Code
tags: [isinscope, isatlevel, dynamic-formatting, conditional-formatting, visual-calculation, switch, collapse, removefilters, allselected, dax]
---

# Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL

Marco Russo & Alberto Ferrari · SQLBI · 2026-07-14

Apply different formatting rules at each level of a hierarchy. Year level: background shade reflects share of grand total. Quarter level: status color (green above avg, pink below). Month level: gold flag for months exceeding 15% of year. Each level has its own logic — the measure needs to detect the current level before applying its rule.

Two DAX functions address this: **ISINSCOPE** (semantic model measure) and **ISATLEVEL** (visual calculation at report layer). Both detect the level correctly — the choice is about *where* the logic lives.

## Key concepts

**ISINSCOPE** in a measure: inspects group-by columns of the query. Reusable across reports. Requires semantic model authoring rights.

**ISATLEVEL** in a visual calculation: inspects the visual layout (VISUAL SHAPE of the query). Requires no change to semantic model. Operates on the smaller set of rows used to populate the visual — usually faster.

Both use the same SWITCH TRUE dispatch pattern — test most-specific level first (month → quarter → year).

## ISINSCOPE measure example (Level Color)

```dax
Level Color =
SWITCH(
    TRUE,
    -- Month level: highlight months exceeding 15% of their year
    ISINSCOPE('Date'[Year Month]) || ISINSCOPE('Date'[Year Month Short]),
        VAR MonthValue = [Sales Amount]
        VAR YearTotal = CALCULATE([Sales Amount], REMOVEFILTERS('Date'), VALUES('Date'[Year]))
        VAR Share = DIVIDE(MonthValue, YearTotal)
        RETURN IF(Share > 0.15, "Gold", BLANK()),
    -- Quarter level: green if at or above average, pink if below
    ISINSCOPE('Date'[Year Quarter]),
        VAR QuarterValue = [Sales Amount]
        VAR AverageQuarter = CALCULATE(
            AVERAGEX(VALUES('Date'[Year Quarter]), [Sales Amount]),
            REMOVEFILTERS('Date')
        )
        RETURN IF(QuarterValue >= AverageQuarter, "LightGreen", "LightPink"),
    -- Year level: shade by share of grand total
    ISINSCOPE('Date'[Year]),
        VAR YearValue = [Sales Amount]
        VAR GrandTotal = CALCULATE([Sales Amount], REMOVEFILTERS('Date'))
        VAR Share = DIVIDE(YearValue, GrandTotal)
        RETURN SWITCH(TRUE,
            Share > 0.40, "SteelBlue",
            Share > 0.25, "CornflowerBlue",
            Share > 0.15, "SkyBlue",
            "LightBlue"
        )
)
```

## ISATLEVEL visual calculation example

```dax
Visual Level Color =
SWITCH(
    TRUE,
    -- Month level
    ISATLEVEL([Year-Quarter-Month Month]),
        VAR MonthValue = [Sales Amount]
        VAR YearTotal = COLLAPSE([Sales Amount], [Year-Quarter-Month Quarter])
        VAR Share = DIVIDE(MonthValue, YearTotal)
        RETURN IF(Share > 0.15, "Gold", BLANK()),
    -- Quarter level
    ISATLEVEL([Year-Quarter-Month Quarter]),
        VAR QuarterValue = [Sales Amount]
        VAR AverageQuarter = CALCULATE(AVERAGEX(ROWS, [Sales Amount]))
        RETURN IF(QuarterValue >= AverageQuarter, "LightGreen", "LightPink"),
    -- Year level
    ISATLEVEL([Year-Quarter-Month Year]),
        VAR YearValue = [Sales Amount]
        VAR GrandTotal = COLLAPSEALL([Sales Amount], ROWS)
        VAR Share = DIVIDE(YearValue, GrandTotal)
        RETURN SWITCH(TRUE,
            Share > 0.40, "SteelBlue",
            Share > 0.25, "CornflowerBlue",
            Share > 0.15, "SkyBlue",
            "LightBlue"
        )
)
```

## Synoptic Panel use case

Non-calendar hierarchy (venue seating: Seat → Sector → Category). Same SWITCH dispatch pattern detects the seat/sector/category level. Measure uses ISINSCOPE; visual calculation uses ISATLEVEL.

```dax
% Occupation =
VAR AverageTicketEvent = DIVIDE([# Tickets], [# Events])
RETURN SWITCH(
    TRUE,
    ISINSCOPE(Seats[Seat]), (AverageTicketEvent > 0) * 1,
    ISINSCOPE(Seats[Sector]) || ISINSCOPE(Seats[Category]), DIVIDE(AverageTicketEvent, [Tot seats]),
    BLANK()
)
```

## Choosing between ISINSCOPE and ISATLEVEL

**Use ISINSCOPE in a measure when:**
- You own the semantic model
- The logic needs to be reusable across multiple reports
- The format logic needs data not represented in the visual

**Use ISATLEVEL in a visual calculation when:**
- You cannot or do not want to modify the semantic model (shared dataset)
- The logic is purely presentation-related
- You want better performance (operates on visual rowset, not full model)

## Per-level arithmetic: REMOVEFILTERS vs ALLSELECTED

- **REMOVEFILTERS:** compares against full model totals (ignores visual slicers). Use when comparing against absolute totals.
- **ALLSELECTED:** compares against visible totals in the visual. Use when comparing against the displayed date range only.

## Related

- [[Distinguishing HASONEVALUE from ISINSCOPE]] (SQLBI companion article)
- [[Using ALLEXCEPT versus ALL and VALUES]] (SQLBI — REMOVEFILTERS/VALUES pattern)
