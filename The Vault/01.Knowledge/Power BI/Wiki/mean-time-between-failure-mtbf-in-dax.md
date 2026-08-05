---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "operations", "mtbf", "reliability", "uptime"]
note_type: pattern

---

# Mean Time Between Failure (MTBF) in DAX

Measuring the average time between equipment or system failures.

## Formula

```
MTBF = ( Total Operating Time ) / ( Number of Failures )
```

## DAX Pattern

```dax
Total Operating Hours :=
SUM( 'Equipment'[OperatingHours] )

Failure Count :=
COUNTROWS( 'Failures' )

MTBF (Hours) :=
DIVIDE( [Total Operating Hours], [Failure Count] )
```

## Notes

- Higher MTBF = more reliable equipment
- Combine with MTTR (Mean Time to Repair) for complete reliability picture
- Segment by equipment type or location for root cause analysis

## Related

- [[effect]]
- [[duration-calculations-in-dax]]
