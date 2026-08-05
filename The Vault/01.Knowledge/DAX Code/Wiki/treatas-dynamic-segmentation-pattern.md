---
created: 2026-07-27
updated: 2026-08-02
source: "TREATAS in DAX: Connecting Unrelated Tables Like Magic"
note_type: pattern
tags: [dax, treatas, dynamic-segmentation, what-if-analysis, virtual-relationship]
---

# TREATAS Dynamic Segmentation Pattern

Uses TREATAS to apply a parameter table's selected values as a filter to a fact table column, enabling what-if segmentation analysis without modifying the data model.

## Purpose

Filter a fact table by an arbitrary set of values (from a parameter/what-if table) that has no relationship to the fact table. Common use cases: price range segments, customer lifetime value tiers, product category filters.

## Components

- TREATAS — applies parameter values as filter to fact table
- VALUES() — extracts currently selected values from parameter table
- CALCULATE() — applies the virtual filter

## Structure

```dax
Sales for Segment =
CALCULATE (
    [Total Sales],
    TREATAS (
        VALUES(PriceSegments[ProductKey]),
        Sales[ProductKey]
    )
)
```

## Example

Scenario: A retailer has a "PriceSegment" table with product keys for budget/mid/premium tiers — populated by a what-if parameter. No relationship to Sales.

```dax
Budget Segment Sales =
CALCULATE (
    [Total Sales],
    TREATAS (
        VALUES(PriceSegments[ProductKey]),
        Sales[ProductKey]
    )
)
```

Users change the PriceSegment selection via slicer — TREATAS applies the new filter — Sales recalculates for that segment.

## Related

- [[treatas-function]]
- [[treatas-vs-userelationship-comparison]]
