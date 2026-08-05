---
created: 2026-07-27
updated: 2026-08-02
source: "TREATAS in DAX: Connecting Unrelated Tables Like Magic"
note_type: comparison
tags: [dax, treatas, userelationship, crossfilter, virtual-relationships]
---

# TREATAS vs USERELATIONSHIP vs CROSSFILTER

Three DAX mechanisms for controlling cross-table filter flow without adding physical relationships.

## Overview

| Function | What it does | Requires existing relationship? | Use when |
|---------|-------------|-------------------------------|---------|
| USERELATIONSHIP | Activates an existing inactive relationship | Yes (inactive) | Same column, different active path needed |
| TREATAS | Applies arbitrary value set as filter | No | No relationship exists; filter by calculated set |
| CROSSFILTER | Modifies relationship direction or disables cross-filtering | Yes | Bidirectional filtering needed; one-direction-only limitation |

## TREATAS

Applies a set of column values as a filter to any target column.

```dax
CALCULATE (
    [Total Sales],
    TREATAS ( TOPN(10, VALUES(Products[Product]), [Total Sales]), Products[Product] )
)
```

**Best for:** Filtering by a calculated set (Top N, arbitrary selection, parameter-driven filter) where no relationship exists.

## USERELATIONSHIP

Activates an existing inactive relationship between two tables.

```dax
CALCULATE (
    [Total Sales],
    USERELATIONSHIP ( Sales[ShipDate], Date[Date] )
)
```

**Best for:** Same column used in multiple roles (Invoice Date + Ship Date via same Date table); inactive relationship already exists.

## CROSSFILTER

Changes the filter direction of an existing relationship for the current calculation.

```dax
CALCULATE (
    [Total Sales],
    CROSSFILTER ( Sales[ProductKey], Products[ProductKey], BOTH )
)
```

Options: `ONEWAY` (forces single direction), `BOTH` (enables bidirectional), `NONE` (disables cross-filtering).

**Best for:** Forcing bidirectional filtering on a one-to-many relationship without using bidirectional cross-filtering in the model.

## Decision Framework

1. Does a relationship exist but is inactive? → USERELATIONSHIP
2. Do you need to filter by a calculated set with no relationship at all? → TREATAS
3. Do you need to change filter direction without adding bidirectional cross-filter globally? → CROSSFILTER
4. Do you need both tables to filter each other dynamically? → Model-level bidirectional relationships or CROSSFILTER

## Multi-Date Scenario (Mark Chen, 2025)

The most common TREATAS win in real data models: a fact table has multiple date columns (OrderDate, ShipDate, DueDate, PaymentDate) but only one active relationship to the Date table can exist.

- USERELATIONSHIP requires the inactive relationship to be pre-defined in the model — with many date columns this creates a sprawl of inactive relationships.
- TREATAS needs **no relationships at all** for the non-primary date columns — each measure defines its own virtual relationship at evaluation time.

Example: one Date slicer driving all four KPIs simultaneously:
```dax
Shipped Qty =
CALCULATE(
    SUM(Transactions[Quantity]),
    TREATAS(VALUES('Date'[Date]), Transactions[ShipDate])
)
```
All measures share the same Date dimension; only the TREATAS mapping changes per measure.

See [[treatas-multi-date-metrics]] for the full pattern.

## Related

- [[treatas-function]]
- [[userelationship-function]]
- [[role-playing-dimensions-pattern]]
- [[calculate]] — both TREATAS and USERELATIONSHIP are used within CALCULATE to modify context
