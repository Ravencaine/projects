---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, reliability, mtbf, mttr, maintenance, operations]
---

# MTBF and MTTR in DAX

Mean Time Between Failures and Mean Time to Repair — operational reliability metrics.

## MTBF (Mean Time Between Failures)

```
MTBF = Total Operating Time / Number of Failures
```

```dax
MTBF =
    VAR __TotalOperatingTime = SUM( 'Equipment'[OperatingHours] )
    VAR __Failures = COUNTROWS( FILTER( 'Events', 'Events'[Type] = "Failure" ) )
    RETURN DIVIDE( __TotalOperatingTime, __Failures, BLANK() )
```

Higher MTBF = more reliable system.

## MTTR (Mean Time to Repair)

```
MTTR = Total Repair Time / Number of Repairs
```

```dax
MTTR =
    VAR __TotalRepairTime = SUM( 'Events'[RepairDuration] )
    VAR __Repairs = COUNTROWS( FILTER( 'Events', 'Events'[Type] = "Repair" ) )
    RETURN DIVIDE( __TotalRepairTime, __Repairs, BLANK() )
```

Lower MTTR = faster recovery from failures.

## Combined: System Availability

```dax
Availability =
    VAR __MTBF = [MTBF]
    VAR __MTTR = [MTTR]
    RETURN DIVIDE( __MTBF, __MTBF + __MTTR, 0 )
```

Expressed as a percentage: 99% availability means the system is down less than 3.65 days per year.

## Related

- [[overall-equipment-effectiveness-oee-dax]] — OEE incorporates availability
- [[on-time-in-full-otif-dax]] — operations metrics
- [[quality-rate-defect-dax]] — quality component of OEE
