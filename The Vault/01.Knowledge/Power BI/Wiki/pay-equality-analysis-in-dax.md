---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, hr, pay-equity, gender-pay-gap, compensation]
note_type: pattern

---

# Pay Equality Analysis in DAX

Comparing compensation across demographic groups to identify pay gaps.

## Pattern

```dax
Avg Salary by Group :=
AVERAGEX(
    SUMMARIZECOLUMNS(
        'Employees'[Department],
        'Employees'[Gender],
        'Employees'[Grade],
        "AvgSalary", AVERAGE( 'Employees'[Salary] )
    ),
    [AvgSalary]
)

Pay Gap :=
VAR __MaleAvg = CALCULATE( [Avg Salary], 'Employees'[Gender] = "Male" )
VAR __FemaleAvg = CALCULATE( [Avg Salary], 'Employees'[Gender] = "Female" )
RETURN
DIVIDE( __MaleAvg - __FemaleAvg, __MaleAvg )
```

## Notes

- Always control for role, grade, tenure when comparing pay
- Pay gap analysis should be reviewed by HR for compliance

## Related

- [[value_add]]
- [[turnover-rate]]
