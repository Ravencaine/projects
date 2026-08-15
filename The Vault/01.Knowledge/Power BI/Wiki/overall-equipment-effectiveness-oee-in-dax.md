---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, operations, oee, manufacturing, uptime]
note_type: pattern

---

# Overall Equipment Effectiveness (OEE) in DAX

Measuring manufacturing equipment productivity using the OEE framework.

## OEE Formula

```
OEE = Availability x Performance x Quality
```

Where:
- Availability = Operating Time / Planned Production Time
- Performance = (Ideal Cycle Time x Total Output) / Operating Time
- Quality = Good Output / Total Output

## DAX Pattern

```dax
Availability :=
DIVIDE( [OperatingTime], [PlannedTime] )

Performance :=
DIVIDE( [IdealCycleTime] * [TotalUnits], [OperatingTime] )

Quality :=
DIVIDE( [GoodUnits], [TotalUnits] )

OEE :=
[Availability] * [Performance] * [Quality]
```

## OEE Benchmarks

| OEE | Classification |
|-----|---------------|
| 100% | Perfect production |
| 85%+ | World-class |
| 60-85% | Typical manufacturer |
| < 60% | Improvement needed |

## Related

- [[mtbf-mttr-reliability-dax]]
- [[on-time-in-full-otif-dax]]
