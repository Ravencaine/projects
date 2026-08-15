---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 3
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
note_type: pattern
tags: [dax, production, goal, variance, date, context]
---

# Dynamic Goal Selection via SELECTEDVALUE

Detect what time granularity the user is viewing (day, month, year, or custom range) and automatically select the appropriate target. Nested `SELECTEDVALUE` checks cascade from most specific to least specific.

## The Problem

Production targets exist at multiple granularities: daily, monthly, annual. A measure must detect the current view and choose the right target — without hardcoding.

## SELECTEDVALUE Behaviour

| Condition | Return Value |
|-----------|-------------|
| Exactly one value in filter context | That value |
| Multiple values (e.g., full month selected) | `BLANK()` |
| No values selected | `BLANK()` |

## Pattern: Nested SELECTEDVALUE Cascade

```dax
MEASURE [HL_PT_Goal] =
IF(
    SELECTEDVALUE(dateTable[Date]),        -- 1. Single day selected?
        [HL_PT_Daily],                      --    Use daily target
    IF(
        SELECTEDVALUE(dateTable[Month]),   -- 2. Single month selected?
            [HL_PT_Monthly],               --    Use monthly target
        [HL_PT_Annual]                     -- 3. Otherwise, use annual target
    )
)
```

Evaluation order: day check → month check → fallback to annual.

## Custom Range Handling

When the user selects a date range (not a single value), `SELECTEDVALUE` returns BLANK. A separate measure sums daily targets across the range:

```dax
MEASURE [HL_PT_Goal_range] =
CALCULATE(
    SUM('ProductionTargets'[DailyTarget_HL_Static])
    -- Sums daily targets across the selected date range
)

MEASURE [HL_PT_%_range] =
IF(
    [HL_PT_Goal_range] = 0,
    BLANK(),
    DIVIDE([HL_Units_D365_#], [HL_PT_Goal_range]) - 1
)
```

## Variance Measure

```dax
MEASURE [HL_PT_%] =
IF(
    SELECTEDVALUE(dateTable[Date]),
        DIVIDE([HL_Units_D365_#], [HL_PT_Daily]) - 1,
    DIVIDE([HL_Units_D365_#], [HL_PT_Annual]) - 1
)
```

## StarTOFMONTH for Monthly Target Anchoring

Monthly targets stored at the first-of-month row. Use `STARTOFMONTH` to anchor to that row regardless of which day the user has selected:

```dax
MEASURE [HL_PT_Monthly] =
CALCULATE(
    SUM('ProductionTargets'[MonthlyTarget_HL_Static]),
    STARTOFMONTH(dateTable[Date])
)
```

## Related

- [[STARTOFMONTH-Date-Anchoring]] — anchors to first of month for row-level target lookups
- [[Conditional-Variance-Display-Hide-Minus-100]] — variance pattern with ISBLANK guard
- [[DIVIDE-Safe-Division]] — safe division pattern (zero → BLANK)
