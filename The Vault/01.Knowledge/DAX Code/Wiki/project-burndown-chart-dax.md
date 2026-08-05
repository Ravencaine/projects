---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, project-management, burndown, scrum, agile]
---

# Project Burndown Chart in DAX

Burndown charts visualize cumulative work remaining vs an idealized linear burndown. Essential for Agile/Scrum project tracking.

## Purpose

Burndown = Total Project Hours − Cumulative Work Completed. The ideal line is linear (same hours per day). The actual line shows real progress. Gap between lines = schedule variance.

## Formula

### Idealized Burndown

```dax
Idealized Burndown =
    VAR __Date = MAX( 'Dates'[Date] )
    VAR __StartDate = MINX( 'Project', 'Project'[Start] )
    VAR __FinishDate = MAXX( 'Project', 'Project'[Finish] )
    VAR __TotalProjectHours = SUMX( ALL( 'Project' ), 'Project'[Work] )
    VAR __IdealHoursPerDay =
        DIVIDE(
            __TotalProjectHours,
            ( __FinishDate - __StartDate ) + 1,
            0
        )
    VAR __IdealConsumedHours = __IdealHoursPerDay * ( ( __Date - __StartDate ) + 1 )
    VAR __Result =
        IF(
            __Date > __FinishDate,
            BLANK(),
            __TotalProjectHours - __IdealConsumedHours
        )
    RETURN __Result
```

### Actual Burndown

```dax
Burndown =
    VAR __ReportingDate = DATE( 2025, 4, 1 )
    VAR __Date = MAX( 'Dates'[Date] )
    VAR __CumulativeHours =
        SUMX(
            FILTER(
                ALL( 'Dates' ),
                'Dates'[Date] <= __Date
                && 'Dates'[Date] <= __ReportingDate
            ),
            [Hours Worked]    -- measure from Hours table
        )
    RETURN __CumulativeHours
```

## Key Metrics

| Measure | Formula |
|---------|---------|
| Total Hours | SUMX(ALL('Project'), 'Project'[Work]) |
| Ideal / Day | Total / (FinishDate − StartDate + 1) |
| Ideal Consumed | Ideal/Day × Days Elapsed |
| Ideal Remaining | Total − Ideal Consumed |
| Actual Remaining | Total − Actual Completed |

## Notes

- **Dates table is disconnected**: all filtering comes through Project/Hours relationship
- **Idealized line does not exclude weekends**: use NETWORKDAYS in the denominator to adjust
- **Reporting date**: hardcoded reporting date captures actual burndown up to that point; beyond that = blank
- **EV**: compare actual burndown to Earned Value ([[earned-value-management-evm-dax]]) for cost + schedule combined view

## Deckler Variant — Hours Table + Cumulative SUMX

Deckler's implementation connects a separate `Hours` table (via Project ID relationship) for actual hours worked, keeping the `Dates` table fully disconnected:

```dax
Idealized Burndown =
    VAR __Date = MAX( 'Dates'[Date] )
    VAR __StartDate = MINX( 'Project', 'Project'[Start] )
    VAR __FinishDate = MAXX( 'Project', 'Project'[Finish] )
    VAR __TotalProjectHours = SUMX( ALL( 'Project' ), 'Project'[Work] )
    VAR __IdealHoursPerDay =
        DIVIDE(
            __TotalProjectHours,
            ( __FinishDate - __StartDate ) + 1,
            0
        )
    VAR __IdealConsumedHours = __IdealHoursPerDay * ( ( __Date - __StartDate ) + 1 )
    VAR __Result =
        IF(
            __Date > __FinishDate,
            BLANK(),
            __TotalProjectHours - __IdealConsumedHours
        )
    RETURN __Result

Burndown =
    VAR __ReportingDate = DATE( 2025, 4, 1 )
    VAR __Date = MAX( 'Dates'[Date] )
    VAR __StartDate = MINX( 'Project', 'Project'[Start] )
    VAR __FinishDate = MAXX( 'Project', 'Project'[Finish] )
    VAR __TotalProjectHours = SUMX( ALL( 'Project' ), 'Project'[Work] )
    VAR __TotalConsumedHours =
        SUMX(
            FILTER(
                ALL( 'Hours' ),
                'Hours'[Date] <= __Date
            ),
            'Hours'[Hours]
        )
    VAR __Result =
        IF(
            __Date > __ReportingDate,
            BLANK(),
            __TotalProjectHours - __TotalConsumedHours
        )
    RETURN __Result
```

**Key differences from the standard approach:**
- `Hours` table carries `ID` → `Date` relationship; `SUMX + FILTER(ALL('Hours'), ...)` accumulates hours worked up to each date
- `__ReportingDate` hard-cutoff: days after the reporting date return `BLANK()` — shows work remaining as of a snapshot date
- To exclude weekends from the ideal line, replace `( __FinishDate - __StartDate ) + 1` with `NETWORKDAYS( __StartDate, __FinishDate )` in `__IdealHoursPerDay`

**Visual:** Line chart — X-axis: Dates[Date]; Y-axis: Idealized Burndown + Burndown.

**Deckler tip:** Initially more work was done than expected (actual below ideal); mid-to-late March stalled (actual above ideal). The divergence signals where to investigate.

## Related

- [[earned-value-management-evm-dax]] — EV, PV, AC, SPI, CPI
- project-burndown-chart-dax — this pattern
