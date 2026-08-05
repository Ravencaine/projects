---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, manufacturing, oee]
---

# Overall Equipment Effectiveness (OEE)

## Purpose

OEE is the standard manufacturing KPI for measuring how efficiently equipment
is utilized versus its maximum theoretical potential. It combines three
independent loss factors into a single score:

```
OEE = Availability × Performance × Quality
```

| Factor | What it measures | Good benchmark |
|--------|-----------------|---------------|
| **Availability** | Was the machine available to run? | > 90% |
| **Performance** | Did it run at full speed? | > 95% |
| **Quality** | Were the output parts good? | > 99% |
| **OEE** | Overall efficiency | > 85% (world-class) |

## Component Formulas

### Availability

Percentage of planned operating time the machine was actually running
(excludes downtime for repairs, maintenance, changeovers, etc.).

```dax
Availability =
    VAR __Start = DATE( 2022, 1, 1 )
    VAR __End   = DATE( 2025, 12, 31 )
    VAR __OperatingHours = DATEDIFF( __Start, __End, HOUR )
    VAR __Machines       = COUNTROWS( 'Machines' )
    VAR __Table =
        ADDCOLUMNS(
            'MTBF',
            "__Hours", DATEDIFF( [RepairStarted], [RepairCompleted], HOUR )
        )
    VAR __TotalDowntime        = SUMX( __Table, [__Hours] )
    VAR __TotalOperatingHours = __OperatingHours * __Machines
    VAR __Result = DIVIDE( __TotalOperatingHours - __TotalDowntime, __TotalOperatingHours )
    RETURN __Result
```

### Performance

Ratio of actual units produced to the theoretical maximum at full capacity.

```dax
Performance =
    DIVIDE(
        SUMX( 'Production', [Actual] ),
        SUMX( 'Production', [Capacity] ),
        0
    )
```

### Quality

Ratio of good (non-defective) units produced to total units produced.

```dax
Quality =
    DIVIDE(
        SUMX( 'Production', [Good] ),
        SUMX( 'Production', [Actual] ),
        0
    )
```

### Combined OEE

```dax
OEE = [Availability] * [Performance] * [Quality]
```

## Data Model

| Table | Columns | Role |
|-------|---------|------|
| `Machines` | `MachineName` | Disconnected or related dimension — distinct list of machines |
| `MTBF` | `MachineName`, `RepairStarted`, `RepairCompleted`, `MaintenanceType` | Downtime log — each row is an unavailable period |
| `Production` | `MachineName`, `Date`, `Capacity`, `Actual`, `Good` | Daily production stats |

**Availability logic:** `TotalOperatingHours` assumes 24/7 continuous operation
across all machines. `__TotalDowntime` sums all repair hours from the MTBF
log. Availability = (Operating − Downtime) / Operating.

## What Each Loss Factor Reveals

- **Availability loss**: why the machine was stopped: planned maintenance,
  unplanned breakdowns, changeovers, material shortages
- **Performance loss**: why throughput was below capacity: slow cycles,
  small stoppages, idling
- **Quality loss**: why parts were rejected: defects, rework, scrap

## Notes

- The OEE calculation assumes **24/7 operation**: adjust `__OperatingHours`
  using `NETWORKDAYS` or actual scheduled hours if your operation is not
  continuous.
- **Simplifying assumptions:** Each machine runs for the full period (2022–2025)
  without scheduled shutdowns. Extend the `__Table` filter in Availability to
  exclude preventative maintenance rows if you want to track *unplanned*
  downtime separately.
- OEE of **100%** means the machine ran at full speed, with zero defects, for
  the entire planned time — an aspirational target.
- **OEE × Availability × Performance × Quality**: all three are expressed as
  ratios (0–1). Multiply them to get the combined score.

## Related

- [[on-time-in-full-otif-dax]] — supply chain fulfillment KPIs
- [[earned-value-management-evm-dax]] — project performance indices
