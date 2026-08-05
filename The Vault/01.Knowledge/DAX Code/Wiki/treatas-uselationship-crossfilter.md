---
created: 2026-08-01
updated: 2026-08-02
source: "TREATAS in DAX - Connecting Unrelated Tables Like Magic.md"
note_type: atomic
tags: [dax, treatas, USERELATIONSHIP, CROSSFILTER, virtual-relationships, CALCULATE, intermediate]
---

# TREATAS vs USERELATIONSHIP vs CROSSFILTER

Three functions for situations where the standard relationship model doesn't fit. Each solves a different problem.

## Decision Rule of Thumb

| Situation | Function |
|-----------|----------|
| Relationship exists but is inactive | `USERELATIONSHIP` |
| Same tables, wrong filter direction | `CROSSFILTER` |
| No relationship exists at all | `TREATAS` |

## USERELATIONSHIP

Activates an **existing but inactive** relationship inside CALCULATE.

```c
Total Revenue by Ship Date =
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Sales[ShipDate], 'Date'[Date])
)
```

Requires: a physical relationship in the model (even if marked inactive).
Does NOT: create a new relationship.

## CROSSFILTER

Changes the **direction** of an existing relationship inside CALCULATE — useful when you need cross-filtering in the opposite direction.

```c
-- Both directions (bi-directional)
CALCULATE(
    [Total Sales],
    CROSSFILTER(Sales[CustomerID], Customer[CustomerID], BOTH)
)

-- None (disable filtering)
CALCULATE(
    [Total Sales],
    CROSSFILTER(Sales[CustomerID], Customer[CustomerID], NONE)
)
```

Requires: a physical relationship to exist.
Does NOT: create a new relationship or change the model.

## TREATAS

Creates a **virtual relationship** where no physical relationship exists.

```c
Total Campaign Sales =
CALCULATE(
    [Total Sales],
    TREATAS(
        VALUES(Campaign[PromoCode]),
        Sales[PromoCode]
    )
)
```

Requires: nothing — no physical relationship needed.
Does: applies filter from one table onto another for the duration of the measure.

## Comparison Table

| Aspect | USERELATIONSHIP | CROSSFILTER | TREATAS |
|--------|----------------|-------------|---------|
| Needs physical relationship | Yes | Yes | No |
| Creates new relationship | No | No | Yes (virtual) |
| Handles duplicate keys | Via model | Via model | Yes |
| Handles data type mismatch | Via model | Via model | Via CONVERT |
| Performance | Good | Good | Moderate |
| Use when | Inactive relationship | Wrong direction | No relationship exists |

## Combining Them

All three can coexist in the same CALCULATE:

```c
Revenue by Ship Date Campaign =
CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Sales[ShipDate], 'Date'[Date]),
    TREATAS(
        VALUES(Campaign[PromoCode]),
        Sales[PromoCode]
    ),
    CROSSFILTER(Sales[CustomerID], Customer[CustomerID], BOTH)
)
```

## Related

- [[treatas-virtual-relationships]] — TREATAS core pattern
- [[treatas-performance-pitfalls]] — performance when using TREATAS with these
