---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, quality, defects, manufacturing, oee]
---

# Quality Rate in DAX

Manufacturing quality metric: good units produced as a percentage of total units started.

## Formula

```
Quality Rate = (Total Units - Defective Units) / Total Units × 100
```

Or equivalently:

```
Quality Rate = Good Units / Total Units × 100
```

## DAX Pattern

```dax
Quality Rate =
    DIVIDE(
        SUM( 'Production'[GoodUnits] ),
        SUM( 'Production'[TotalUnits] ),
        0
    )
```

## Defect Rate (Complement)

```dax
Defect Rate =
    DIVIDE(
        SUM( 'Production'[DefectiveUnits] ),
        SUM( 'Production'[TotalUnits] ),
        0
    )
```

## First Pass Yield

```dax
First Pass Yield =
    DIVIDE(
        SUM( 'Production'[UnitsPassingFirstInspection] ),
        SUM( 'Production'[TotalUnits] ),
        0
    )
```

First Pass Yield is typically lower than final Quality Rate because rework can rescue some initially-defective units.

## Related

- [[overall-equipment-effectiveness-oee-dax]] — OEE = Availability × Performance × Quality
- [[mtbf-mttr-reliability-dax]] — reliability metrics
- [[order-fulfillment-dax]] — order-level quality
