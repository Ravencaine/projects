---
created: 2026-07-31
updated: 2026-08-02
source: From Messy Power BI Relationships to a Clean Fleet Analytics Model.md
source_url: https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
note_type: pattern
tags: [power-bi, data-modeling, fleet-analytics, operational-model, star-schema]
---

# Operational Triangle Model

In equipment-heavy industries, operational data revolves around three core entities: Operator, Equipment, and Project. Adding time gives the operational grain.

## Purpose

The Operational Triangle is a conceptual framework for structuring any equipment-centric operational dataset. It identifies the three entities that drive business activity, then attaches all operational facts to them via a shared date dimension.

## The Triangle

```
dimOperator
                 │
                 │
dimProject ── fctOperations ── dimEquipment
                 │
                 │
               dimDate
```

The shared `fctOperations` fact table sits at the center, with three dimensions radiating outward.

## The Grain

Adding time gives the operational grain:

```
Operator + Equipment + Project + Date
```

Every operational fact in the model is either:
- A direct observation at this grain, or
- An aggregate of observations at this grain

## What It Enables

| Question | How the Triangle Answers It |
|----------|----------------------------|
| Which machines are most profitable? | Equipment → Revenue / Cost facts |
| Which operators generate the most revenue? | Operator → Revenue facts |
| Which projects consume the most equipment? | Project → Equipment Hours facts |
| Utilization over time? | Equipment + Date in fact |
| Cross-project operator productivity? | Operator + Project + Date |

## Fleet-Specific Extension

In fleet analytics specifically, Equipment becomes the hub (see [[hub-and-spoke-equipment-as-hub]]), and the triangle becomes a hub-and-spoke with Equipment at the center:

```
dimEquipment
           │
           │
dimOperator ── fctOperatorAssignment ── dimEquipment
           │
      dimProject
           │
       dimDate
```

## Relationship to Other Patterns

- [[hub-and-spoke-equipment-as-hub]] — the Physical Triangle concretises this concept for fleet operations
- [[assignment-table-as-fact-pattern]] — the Operator ↔ Equipment leg of the triangle modeled as a fact
- [[consolidated-activity-fact-pattern]] — what happens when multiple facts at the same grain merge into one

## Related

- [[hub-and-spoke-equipment-as-hub]] — fleet-specific hub pattern
- [[assignment-table-as-fact-pattern]] — operator-equipment assignments as facts
- [[consolidated-activity-fact-pattern]] — consolidating same-grain facts into one
