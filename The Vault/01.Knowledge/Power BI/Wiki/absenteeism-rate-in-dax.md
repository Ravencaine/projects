---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "hr", "absenteeism", "kpi"]
note_type: pattern

---

# Absenteeism Rate in DAX

Measuring unplanned employee absences as a proportion of total available hours.

## Formula

```
Absenteeism Rate = ( Unplanned Absence Hours / Total Available Hours ) * 100
```

## DAX Pattern

```dax
Total Available Hours :=
SUMX( 'Employees', 'Employees'[Headcount] * 'Calendars'[WorkHours] )

Absenteeism Rate :=
DIVIDE(
    SUM( 'Absences'[AbsenceHours] ),
    [Total Available Hours]
) * 100
```

## Notes

- Filter out planned absences (vacation, holidays) from the numerator
- Use a separate absence type dimension table to distinguish categories
- Segment by department or manager for targeted interventions

## Related

- [[turnover-rate]]
- [[bradford-factor-in-dax]]
- [[value_add]]
