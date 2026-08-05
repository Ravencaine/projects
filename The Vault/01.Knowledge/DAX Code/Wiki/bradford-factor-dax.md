---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, hr, absenteeism, bradford-factor]
---

# Bradford Factor in DAX

The Bradford Factor weights employee absenteeism by frequency of absences. Frequent short absences are more disruptive (and penalized more heavily) than fewer long absences.

## Purpose

Bradford Factor = S² × D, where:
- S = total days absent in the period
- D = number of distinct absence incidents

An employee absent 3 times for 2 days each (S=6, D=3) scores 54. An employee absent once for 6 days (S=6, D=1) scores 6. The frequent absentee scores 9× worse despite identical total absence days.

## Formula

```dax
Bradford Factor =
    VAR __Start = MIN( 'Dates'[Date] )
    VAR __End = MAX( 'Dates'[Date] )
    VAR __EmployeeContext = DISTINCT( 'Employees'[Employee] )
    VAR __Absences =
        ADDCOLUMNS(
            ADDCOLUMNS(
                FILTER(
                    ALL( 'Absences' ),
                    [Employee] IN __EmployeeContext
                    && [Start Date] <= __End
                    && [End Date] >= __Start
                ),
                "__Min", MAX( __Start, [Start Date] ),
                "__Max", MIN( __End, [End Date] )
            ),
            "__WorkDays", NETWORKDAYS( [__Min], [__Max] )
        )
    VAR __AbsentDays = SUMX( __Absences, [__WorkDays] )
    VAR __Instances = COUNTROWS( __Absences )
    VAR __Result = __Instances ^ 2 * __AbsentDays
    RETURN
        __Result
```

## Key Insight

The squared instances (S²) mean frequency is exponentially penalized. Organizations typically set threshold scores for managerial review:
- < 50: normal range
- 50–500: concern
- > 500: serious concern requiring action

## Notes

- **NETWORKDAYS**: automatically excludes weekends and optionally holidays
- **Two-layer ADDCOLUMNS**: first layer clamps dates to period boundaries, second layer calculates workdays
- **Alexis Olson optimization**: using DISTINCT instead of SELECTEDCOLUMNS for employee context
- Combine with [[absenteeism-rate-dax]] for a complete absenteeism picture

## Related

- [[absenteeism-rate-dax]] — raw absenteeism percentage
- [[employee-turnover-rate-etr-dax]] — turnover
- [[human-capital-value-added-hcva-dax]] — employee value
