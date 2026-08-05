---
created: 2026-07-27
updated: 2026-08-02
source: "Time Intelligence in DAX: The Secret Behind YTD, QTD, and SamePeriodLastYear"
note_type: comparison
tags: [dax, time-intelligence, sameperiodlastyear, parallelperiod, prevmonth, prevquarter]
---

# SAMEPERIODLASTYEAR vs PARALLELPERIOD vs PREVIOUSMONTH

Three DAX approaches for period-over-period comparisons — each handles gaps and non-contiguous date ranges differently.

## SAMEPERIODLASTYEAR

Shifts the current date context back exactly one year.

```dax
Sales LY =
CALCULATE (
    [Total Sales],
    SAMEPERIODLASTYEAR ( Date[Date] )
)
```

**Behavior:** Returns the same number of days as the current context, shifted back 1 year. Requires a continuous date series — if current context has gaps, SAMEPERIODLASTYEAR may return fewer/more dates than expected.

**Use when:** Date table is continuous (no missing dates), and you want the same day count shifted back.

## PARALLELPERIOD

Shifts by complete month/quarter/year boundaries, ignoring gaps.

```dax
Sales LY Parallel =
CALCULATE (
    [Total Sales],
    PARALLELPERIOD ( Date[Date], 1, YEAR )
)
```

**Behavior:** Returns a full month/quarter/year of data, even if the current context is within a partial period. Shifts by N periods at the specified granularity.

**Use when:** You need full-period comparisons regardless of current selection, or when date table has gaps.

## PREVIOUSMONTH / PREVIOUSQUARTER / PREVIOUSYEAR

Returns all dates in the immediately prior period.

```dax
Sales Prev Month =
CALCULATE (
    [Total Sales],
    PREVIOUSMONTH ( Date[Date] )
)
```

**Behavior:** Returns all dates in the month before the max date in current context. Automatically handles partial periods.

**Use when:** You always want the full prior period, not the same-day-count shifted back.

## Decision Framework

| Scenario | Best function |
|---------|--------------|
| Same day-count shifted back 1 year (contiguous dates) | SAMEPERIODLASTYEAR |
| Full month shifted back regardless of selection | PREVIOUSMONTH |
| Full quarter shifted back regardless of selection | PREVIOUSQUARTER |
| Need exact N period shift at specific granularity | PARALLELPERIOD |
| Date table has gaps | PREVIOUSMONTH/PREVIOUSQUARTER or PARALLELPERIOD |

## Related

- [[time-intelligence-ytd-pattern]]
- 
- [[calculate]] — both functions are typically wrapped inside CALCULATE to apply the shifted date filter
