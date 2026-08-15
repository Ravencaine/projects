---
created: 2026-08-13
source: 5 Mistakes in Power BI Data Modeling (And How to Fix Them)
note_type: pattern
tags: [power-bi, data-modeling, relationships, one-to-many, filter-direction, beginner]
---

# Data Modeling Mistake: Broken Relationships

<!-- Missing or incorrect relationships break filter flow and produce wrong totals — a common beginner mistake with an obvious fix pattern. -->

## The Mistake

Two failure modes:

1. **Missing relationship** — tables not connected, so slicers have no effect
2. **Incorrect relationship** — wrong direction, wrong cardinality, or duplicate path

## Symptom Pattern

- Time intelligence calculations return blank or zero
- Slicers do not filter the expected visuals
- Totals are wrong (often 10x too high)
- Visual shows "(Blank)" category rows with values

## The Fix Pattern

### Step 1 — Diagnose in Model View

```
Look for:
- Red exclamation marks → broken relationship
- */* cardinality → many-to-many (often wrong)
- Multiple paths between two tables → ambiguity
```

### Step 2 — Fix Cardinality

```
Rule: Dimension → Fact = One-to-Many
Example: Customer[CustomerID] ──→ Orders[CustomerID]
         (one customer, many orders)
```

### Step 3 — Set Filter Direction

```
Correct: Single direction (Dimension → Fact)
Wrong:   Bidirectional (both tables filter each other)

Only use bidirectional with a dedicated bridge table for genuine M:M.
```

### Step 4 — Verify with a Simple Test

```dax
-- Test measure: does it return the correct grand total?
Total Sales = SUM(Sales[Amount])
-- Put in a table with DimProduct[Category] — should show one row per category
```

## Common Specific Cases

### Missing date relationship
Sales not connected to Date → time intelligence (YTD, MTD, SAMEPERIODLASTYEAR) fails silently.

```
Fix: Create relationship between Sales[OrderDate] and DimDate[Date]
     Use USERELATIONSHIP if you also need ShipDate or DueDate.
```

### Wrong direction
Relationship exists but points Fact → Dimension instead of Dimension → Fact.

```
Fix: Click relationship line → Properties → Cross filter direction → Single (Dimension to Fact)
```

### Duplicate relationship path
Two separate paths from Customer to Sales (e.g., both CustomerID and CustomerRegion) create ambiguity.

```
Fix: Remove one path. Keep only the necessary join.
```

## Related

- [[data-model-5-common-problems-fixes]] — Power BI: 5-problem diagnostic (Problem 1 & 2 match this)
- [[relationship-types-one-to-many-many-to-many]] — Data Modeling: cardinality options
- [[CROSSFILTER-Oneway-Directional-Options]] — Power BI: filter direction in DAX
- [[role-playing-date-calculated-columns]] — handling multiple date columns on one fact
