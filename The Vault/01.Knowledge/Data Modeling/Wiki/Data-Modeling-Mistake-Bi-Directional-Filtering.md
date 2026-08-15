---
created: 2026-08-13
source: 5 Mistakes in Power BI Data Modeling (And How to Fix Them)
note_type: pattern
tags: [power-bi, data-modeling, bi-directional, cross-filter, filter-direction, beginner]
---

# Data Modeling Mistake: Overusing Bi-Directional Filtering

<!-- Bi-directional filtering seems convenient but creates ambiguity, performance problems, and unexpected row duplication. Single-direction is almost always correct. -->

## The Mistake

Enabling **Both** directions on a relationship (Dimension ↔ Fact) propagates filters both ways through the model.

```
❌ Cross filter direction = Both
   Customer → Sales ← Product
   (Customer filters Sales AND Product filters Customer)
```

This causes:
- Ambiguity when multiple paths exist
- Row duplication (same row counted through multiple paths)
- Performance degradation as filter context propagates everywhere
- Counterintuitive results in slicers and visuals

## Why It Feels Right

Bi-directional is tempting when:
- A slicer on one table does not seem to affect another table
- The user expects "filter everything everywhere"
- Bridge tables are not yet set up for M:M scenarios

The underlying issue is usually a **missing relationship**, not the wrong filter direction.

## The Fix Pattern

### Rule 1 — Default to Single Direction

```
✓ Cross filter direction = Single (Dimension → Fact)
   DimCustomer ──→ FactSales
   (Customer filters Sales — never the reverse)
```

### Rule 2 — Only Use Bi-Directional with a Bridge Table

For genuine many-to-many (e.g., Students ↔ Classes through an Enrollment bridge):

```
DimStudent
    └──→ BridgeEnrollment ←──
                            DimClass
```

Enable bi-directional only on the bridge relationship.

### Rule 3 — Diagnose Before Changing Direction

```
1. Check Model view: is there actually a relationship between the two tables?
2. Verify cardinality: is it truly many-to-many?
3. Check for multiple paths: removing ambiguity first is better than going bidirectional
```

## Bi-Directional via DAX Instead of Model

If you need cross-table filtering in a specific measure, use CROSSFILTER in DAX instead of changing the model-wide setting:

```dax
Revenue by Student =
CALCULATE(
    SUM(Sales[Amount]),
    CROSSFILTER(Students[StudentID], Sales[StudentID], Both)
)
```

This keeps the default model direction clean while enabling cross-filtering only where needed.

## Related

- [[CROSSFILTER-Oneway-Directional-Options]] — Power BI: all filter direction options
- [[relationship-types-one-to-many-many-to-many]] — Data Modeling: when M:M actually applies
- [[data-model-5-common-problems-fixes]] — Power BI: Problem 5 (bidirectional causing duplication)
- [[Data-Modeling-Mistake-Broken-Relationships]] — this KB: missing relationships as the real cause
