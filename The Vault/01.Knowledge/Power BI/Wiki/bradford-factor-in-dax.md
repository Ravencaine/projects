---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "hr", "bradford-factor", "attendance"]
note_type: pattern

---

# Bradford Factor in DAX

The Bradford Factor identifies employees with frequent short-term absences — a pattern more disruptive than fewer longer absences.

## Formula

```
Bradford Factor = ( S * S ) * D
```
Where:
- S = Number of separate absence spells (incidents) in a period
- D = Total number of days absent

## DAX Pattern

```dax
Bradford Factor :=
VAR __Spells = COUNTROWS( 'Absences' )
VAR __Days = SUM( 'Absences'[Days] )
RETURN
POWER( __Spells, 2 ) * __Days
```

## Interpretation

- Score > 500: review warranted
- Score > 1000: formal action recommended
- High score + low days = frequent short absences (very disruptive)

## Notes

- Use the No CALCULATE pattern to build the filtered absence table
- Period should be rolling 52 weeks
- Exclude approved leave types

## Related

- [[absenteeism-rate-in-dax]]
- [[turnover-rate]]
- [[value_add]]
