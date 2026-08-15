---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, project, burndown, earned-value]
note_type: pattern

---

# Burndown Chart in DAX

Visualizing work remaining against an idealized schedule for project tracking.

## Purpose

A burndown chart shows cumulative work remaining on a project over time. It compares actual progress against the expected linear burn rate.

## Data Model

Requires a Project table with: ID, Phase, Task, Work, Start Date, Finish Date, % Complete, Planned Value, Earned Value.

## DAX Pattern

```dax
Total Work :=
SUM( 'Project'[Work] )

Cumulative Completed :=
VAR __CurrentDate = MAX( 'Dates'[Date] )
RETURN
SUMX(
    FILTER(
        ALL( 'Project' ),
        'Project'[Finish] <= __CurrentDate
    ),
    'Project'[Work] * 'Project'[% Complete]
)

Remaining Work :=
[Total Work] - [Cumulative Completed]

Ideal Burndown :=
VAR __Today = TODAY()
VAR __TotalDays = DATEDIFF( MIN( 'Project'[Start] ), MAX( 'Project'[Finish] ), DAY )
VAR __DaysElapsed = DATEDIFF( MIN( 'Project'[Start] ), __Today, DAY )
RETURN
[Totl Work] * ( 1 - DIVIDE( __DaysElapsed, __TotalDays ) )
```

## Notes

- Actual line: plot Remaining Work over time
- Ideal line: linear decline from Total Work to 0
- Deviation from ideal signals schedule risk

## Related

- [[earned-value-management-evm-dax]]
- [[schedule-variance-and-spi-in-dax]]
- [[cost-performance-index-cpi-in-dax]]
