---

created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: ["dax", "pattern", "hr", "absenteeism", "networkdays", "absence", "employee"]

---

# Absenteeism Rate in DAX

Absenteeism measures unexpected employee unavailability (sick days, no-shows) as distinct from planned PTO, holidays, and leave. It is expressed as: unexpected absence hours ÷ total scheduled hours.

## Purpose

Track unplanned absences at the individual and department level, accounting for employees who join or leave mid-period, and absences that span date boundaries.

## Full Implementation

Requires: a `Dates` table, an `Employees` table, and an `Absences` table with a one-to-many relationship from `Employees`.

```dax
Absenteeism =
VAR __Start = MIN( 'Dates'[Date] )
VAR __End = MAX( 'Dates'[Date] )
VAR __EmployeeContext = SELECTCOLUMNS( 'Employees', "__Employee", [Employee] )
VAR __Employees =
    ADDCOLUMNS(
        ADDCOLUMNS(
            FILTER(
                ALL( 'Employees'),
                [Employee] IN __EmployeeContext &&
                [Hire Date] <= __End &&
                [Term Date] >= __Start
            ),
            "__Min", IF( [Hire Date] > __Start, [Hire Date], __Start ),
            "__Max", IF( [Term Date] < __End, [Term Date], __End )
        ),
        "__WorkDays", NETWORKDAYS( [__Min], [__Max] )
    )
VAR __TotalDays = SUMX( __Employees, [__WorkDays] )
VAR __Absences =
    ADDCOLUMNS(
        ADDCOLUMNS(
            FILTER(
                ALL( 'Absences'),
                [Employee] IN __EmployeeContext &&
                (
                    ( [Start Date] >= __Start && [End Date] <= __End ) |
                    ( [Start Date] <= __Start && [End Date] >= __Start && [End Date] <= __End ) |
                    ( [Start Date] >= __Start && [Start Date] <= __End && [End Date] > __End ) |
                    ( [Start Date] <= __Start && [End Date] >= __End )
                )
            ),
            "__Min", IF( [Start Date] < __Start, __Start, [Start Date] ),
            "__Max", IF( [End Date] > __End, __End, [End Date] )
        ),
        "__WorkDays", NETWORKDAYS( [__Min], [__Max] )
    )
VAR __AbsentDays = SUMX( __Absences, [__WorkDays] )
VAR __Result = DIVIDE( __AbsentDays, __TotalDays, 0 ) + 0
RETURN __Result
```

Format as percentage with 2 decimal places.

## How It Works

The measure handles **four absence scenarios** depending on where the absence date range falls relative to the reporting period:

| Scenario | Start | End |
|----------|-------|-----|
| Fully inside period | ≥ Start | ≤ End |
| Spans period start | ≤ Start | ≥ Start and ≤ End |
| Spans period end | ≥ Start and ≤ End | > End |
| Spans entire period | ≤ Start | ≥ End |

The calculation:
1. Gets the period start and end from the Dates context.
2. Builds `__Employees` — only employees active during the period, clamped to their hire/term dates.
3. Uses `NETWORKDAYS(__Min, __Max)` to count workdays (excludes weekends by default).
4. Builds `__Absences` filtering for the four cross-boundary scenarios.
5. Sums absence workdays and divides by total scheduled workdays.

## Notes

- `NETWORKDAYS` excludes weekends (Saturday/Sunday) by default. Pass a holiday date table as the 4th parameter to exclude additional dates.
- For 7-day operations, replace `NETWORKDAYS` with: `([__Max] - [__Min]) * 1` or a `COUNTROWS(EXCEPT(GENERATESERIES(...), {DATE(...)}))` pattern.
- The `+ 0` at the end ensures a numeric zero is returned for employees with no absences (instead of BLANK), so the Matrix visual shows all rows.

## Related

- [[employee-turnover-rate-etr-dax]]
- [[networkdays]]
- [[bradford-factor-dax]]
