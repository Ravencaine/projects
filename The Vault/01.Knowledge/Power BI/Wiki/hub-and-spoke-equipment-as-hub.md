---
created: 2026-07-31
updated: 2026-08-02
source: From Messy Power BI Relationships to a Clean Fleet Analytics Model.md
source_url: https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
note_type: pattern
tags: [power-bi, data-modeling, fleet-analytics, hub-and-spoke, star-schema, relationship]
---

# Hub-and-Spoke: Equipment as the Central Hub

Use the most-connected entity as the hub — all facts and dimensions connect through or to it, never to each other.

## Purpose

In fleet analytics, equipment is the entity that links nearly every operational signal: revenue, fuel, maintenance, operators, payroll, and projects. Making Equipment the hub creates a clean star schema where every fact connects to `dimEquipment` directly, and other dimensions connect only through their relevant fact tables.

## The Problem

Starting with a naive model, dimensions connect to each other:

```
dimOperator
   ├── dimEmployee
   ├── dimEquipment
   └── dimRegion
fctPayroll
fctEquipmentTransactions
```

`dimOperator` contains operator attributes, equipment assignments, AND region information — creating multiple relationship paths. Power BI now has multiple ways to propagate filters, leading to ambiguous relationships, circular dependency errors, and incorrect totals.

## The Solution

Restructure so dimensions describe entities and relationships belong in fact tables:

```
dimEquipment
dimEmployee
dimRegion
dimDate
```

All operational facts connect through `dimEquipment`:

```
dimEquipment
              │   │   │
fctEquipmentTransactions ──*
              │
          fctFuel ──────────*
              │
       fctMaintenance ──────*────── dimDate
              │
    fctOperatorAssignment ──*
              │
         dimEmployee
              │
         fctPayroll ────────*
```

## Why Equipment

- Every operational transaction is tied to a machine
- Revenue, fuel, maintenance, utilization — all are equipment-centric
- Other entities (employees, projects, regions) attach through facts, not directly to each other

## Key Rule

> Dimensions describe entities. Relationships belong in fact tables. Avoid dimension-to-dimension relationships.

## When to Use

- Fleet, mining, construction, logistics analytics
- Any dataset where one physical asset type is central to all operations
- Multi-entity datasets where naive modeling creates multiple relationship paths

## Related

- [[assignment-table-as-fact-pattern]] — bridge-as-fact: operator assignments as a fact table
- [[operational-triangle-model]] — the three core entities in equipment-heavy operations
- [[many-to-many-bridge-table-pattern]] — bridge table pattern (survey domain, same principle)
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — foundational star schema
