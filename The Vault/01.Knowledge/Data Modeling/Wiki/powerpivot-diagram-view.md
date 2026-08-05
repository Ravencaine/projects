---


title: "PowerPivot Diagram View"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, powerpivot, data-modeling, pattern]
note_type: pattern
description: "PowerPivot Diagram View — visual representation of table relationships, relationship arrows, diagram vs. Manage Relationships screen."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# PowerPivot Diagram View

A visual canvas in PowerPivot showing all tables in the Data Model and the relationships between them.

## Access

```
PowerPivot → Manage → Diagram View (tab)
```

## What It Shows

- All tables listed as boxes
- **Arrows** between tables indicate relationships
- Foreign key → Primary key direction shown by arrow

## Relationship Direction

| Arrow Direction | Meaning |
|----------------|---------|
| Many → One | Foreign key points to primary key |
| Arrow shows filter direction | How context propagates |

## Caveat: Arrow Imprecision

> The arrows in Diagram View are **imprecise**: they show general direction but don't precisely track which field names link to which. Scroll through field names without changing arrow position.

## More Precise View: Manage Relationships

```
PowerPivot → Manage → Design → Manage Relationships
```
Or: **Data → Relationships**

This shows exact field names for each relationship.

## Use Cases

- Quickly confirm all expected tables are loaded
- Spot missing relationships
- Plan which relationships need USERELATIONSHIP overrides

## Source Reference

Chapter 4, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
