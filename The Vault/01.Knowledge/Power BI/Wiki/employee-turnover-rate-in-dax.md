---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "hr", "employee-turnover", "kpi"]
note_type: pattern

---

# Employee Turnover Rate (ETR) in DAX

Measuring the rate at which employees leave an organization.

## Purpose

ETR is one of the most important HR KPIs. A high ETR indicates loss of knowledge, productivity loss, and replacement costs.

## Formula

```
ETR = ( Employees Leaving / Average Employees ) * 100
```

ETR is calculated for specific periods — annually, quarterly, or monthly.

## DAX Pattern

```dax
Dates =                            -- Date table
ADDCOLUMNS(
    CALENDAR( DATE(2020,1,1), DATE(2025,12,31) ),
    "Quarter", QUARTER( [Date] ),
    "Month", FORMAT( [Date], "mmmm" ),
    "MonthSort", MONTH( [Date] ),
    "Year", YEAR( [Date] )
)

ETR :=
DIVIDE(
    COUNTROWS( 'Terminations' ),
    AVERAGE( 'EmployeeCounts'[Count] )
) * 100
```

## Notes

- Denominator uses average headcount, not ending headcount
- Segment by department, location, or tenure for deeper insight
- Combine with time offsets for period-over-period comparison

## Related

- [[absenteeism-rate-in-dax]]
- [[bradford-factor-in-dax]]
- [[headcount-metrics-in-dax]]
