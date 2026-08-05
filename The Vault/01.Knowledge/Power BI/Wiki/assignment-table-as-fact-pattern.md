---
created: 2026-07-31
updated: 2026-08-02
source: From Messy Power BI Relationships to a Clean Fleet Analytics Model.md
source_url: https://medium.com/microsoft-power-bi/from-messy-power-bi-relationships-to-a-clean-fleet-analytics-model-d9ae82bb323c
note_type: pattern
tags: [power-bi, data-modeling, bridge-table, many-to-many, fleet-analytics, fact-table]
---

# Assignment Table as Fact Pattern

Treat operational assignment/relationship tables as fact tables, not dimensions — eliminating ambiguous many-to-many paths.

## Purpose

Operator ↔ Equipment assignments are relationships, not attributes. Modeling them as a dimension creates a many-to-many path through other dimensions, causing filter ambiguity. Modeling them as a fact table (`fctOperatorAssignment`) resolves this cleanly: one-to-many from each dimension, no ambiguity.

## The Problem

If operator assignments live in `dimOperator` alongside attributes:

```c
dimOperator
   ├── operator attributes
   ├── equipment assignments  -- PROBLEM: M2M
   └── region information
```

The resulting model has multiple paths between dimensions → ambiguous filter propagation → wrong totals.

## The Solution

Pull assignments out of the dimension entirely:

```c
fctOperatorAssignment
   EmployeeCode
   EquipmentID
```

`fctOperatorAssignment` is a fact table — one row per operator-equipment assignment, expected to have duplicates (one operator, many machines).

```
dimEmployee
     │
fctOperatorAssignment
     │
dimEquipment
```

Now each dimension relationship is one-to-many. No ambiguity.

## Why This Works

- An assignment is a relationship event, not an entity description
- Dimensions describe static attributes; assignments describe operational connections
- One-to-many from each dimension is unambiguous; many-to-many through a dimension is not
- M2M in the fact (multiple assignments) is correct and expected; M2M through a dimension is the anti-pattern

## Contrast with Bridge Tables

| Aspect | Classic Bridge Table | Assignment-as-Fact |
|--------|---------------------|--------------------|
| Purpose | Resolve M2M for counting | Represent operational relationships |
| Content | Respondent ↔ Answer keys | Operator ↔ Equipment |
| Joins | Bridge → Dim (one-to-many each side) | Each Dim → Fact (one-to-many) |
| Row count | Can explode with large M2M sets | Grows with assignment events |
| Use case | Survey analytics | Fleet, project, resource management |

The structural pattern is identical; the domain and naming differ.

## Related

- [[hub-and-spoke-equipment-as-hub]] — why Equipment becomes the hub in fleet models
- [[many-to-many-bridge-table-pattern]] — bridge table for survey data (same principle, different domain)
- [[operational-triangle-model]] — the three-entity triangle this pattern sits within
