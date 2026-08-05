---
created: 2026-07-31
updated: 2026-08-02
source: From Messy Power BI Relationships to a Clean Fleet Analytics Model.md
source_url: https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
note_type: pattern
tags: [power-bi, data-modeling, fact-table, consolidated-fact, star-schema, grain]
---

# Consolidated Activity Fact Pattern

When multiple fact tables share the same grain, merge them into a single unified Activity Fact table for simpler measures and faster development.

## Purpose

Fleet analytics typically generates separate fact tables for different operational signals:
- Revenue transactions
- Fuel consumption
- Maintenance events
- Payroll hours

If all of these share the same grain (e.g., `Equipment + Date`), they can be consolidated into one table. This simplifies DAX measures dramatically — profit is a single column subtraction, not a sum across multiple tables.

## Structure

A consolidated Activity Fact at `Equipment + Date` grain:

```
fctActivity
   EquipmentKey (FK)
   DateKey (FK)
   Revenue
   FuelCost
   MaintenanceCost
   PayrollHours
```

## Why Consolidate

**Before (separate facts):**
```dax
Machine Profit =
    SUM ( fctRevenue[Revenue] )
  - SUM ( fctFuel[Cost] )
  - SUM ( fctMaintenance[Cost] )
  - SUMX ( fctPayroll, [HourlyRate] * [Hours] )
```

**After (consolidated):**
```dax
Machine Profit =
    SUM ( fctActivity[Revenue] )
  - SUM ( fctActivity[FuelCost] )
  - SUM ( fctActivity[MaintenanceCost] )
  - SUM ( fctActivity[PayrollHours] ) * [HourlyRate]
```

Fewer table references → simpler measures → fewer relationship paths for the engine to traverse.

## Grain Consistency Rule

> Consolidate only when grain is identical. Mixing grains (e.g., Payroll at `Employee + Date`, Revenue at `Equipment + Date`) in the same table produces incorrect aggregations.

If grains differ, keep facts separate.

## When NOT to Consolidate

- Facts have different grains (e.g., payroll at employee level, revenue at equipment level)
- Update frequencies differ significantly (payroll weekly, transactions daily)
- Teams own different facts — consolidation adds coordination cost
- The same fact is sourced from multiple upstream systems — separate staging keeps lineage clear

## Relationship to Other Patterns

The Consolidated Activity Fact is the final evolution of the Operational Triangle when all triangle legs share the same grain:

```
dimEquipment
              │
fctActivity ── dimDate
              │
        dimOperator
              │
         dimProject
```

## Related

- [[operational-triangle-model]] — the three-entity framework this consolidates within
- [[hub-and-spoke-equipment-as-hub]] — hub pattern this sits on top of
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — foundational star schema principles
- [[power-bi-correct-granularity-and-scd]] — grain consistency and its performance implications
