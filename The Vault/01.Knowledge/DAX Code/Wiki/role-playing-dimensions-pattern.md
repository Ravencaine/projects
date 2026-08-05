---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
note_type: atomic
tags: [dax, data-modeling, role-playing-dimensions, date-table, beginner]
---

# Role-Playing Dimensions: Single Date Table vs Duplicated

When a fact table has multiple date columns (e.g., InvoiceDate, ShipDate, DueDate), two modeling approaches compete: a single shared Date dimension, or multiple duplicated Date tables.

## Approach 1: Duplicated Date Tables (Anti-Pattern)

Create a separate Date table for each role:

```
Date_Invoice (InvoiceDate → Date_Invoice[Date])
Date_Ship    (ShipDate    → Date_Ship[Date])
```

**Problem:** Each Date table creates its own filter context. A slicer on Date_Invoice does not filter Date_Ship — they are independent. Comparing Invoice Date and Ship Date on the same visual becomes impossible.

## Approach 2: Single Date Table + USERELATIONSHIP (Preferred)

Use one Date dimension for all date roles:

```
Date (shared)
  Sales[InvoiceDate] → Date[Date]   ← Active
  Sales[ShipDate]   → Date[Date]   ← Inactive (activated via USERELATIONSHIP)
  Sales[DueDate]    → Date[Date]   ← Inactive
```

**Benefit:** One shared Date dimension means one set of slicers, one filter context, unified timeline. USERELATIONSHIP activates whichever inactive relationship is needed per measure.

## When Duplication Is Justified

Duplicating Date tables can be appropriate when:
- Each role needs **completely different attributes** (e.g., InvoiceDate needs fiscal calendar columns that ShipDate doesn't)
- The roles are **never used together** in the same report
- The performance benefit of a narrower table outweighs the complexity cost

In most analytics scenarios — especially when users need to compare perspectives — a single shared Date table with USERELATIONSHIP is the cleaner solution.

## Why Single Date Table Keeps Filters Unified

In Power BI, a slicer connected to Date automatically filters everything related to Date. With a single table:

```dax
-- Both measures respond to the same Date slicer
Sales by Invoice Date = SUM ( Sales[SalesAmount] )
Sales by Ship Date =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
)
```

Switching the Date slicer updates both metrics simultaneously because they both point to the same Date dimension.

## Best Practice Rule

> **Keep one Date table. Use USERELATIONSHIP for alternate time perspectives. Duplicate only when each role needs its own attribute structure that can't coexist in one table.**

## Related

- [[uselationship-function]] — mechanics of USERELATIONSHIP
- [[dynamic-date-switching-with-switch]] — SWITCH pattern for slicer-driven switching between date perspectives
- [[role-playing-date-calculated-columns]] — related: role-playing dates via DAX calculated columns instead of relationships
