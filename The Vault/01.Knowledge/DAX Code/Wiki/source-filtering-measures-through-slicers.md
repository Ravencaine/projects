---
created: 2026-08-09
updated: 2026-08-09
source: "Filtering measures through slicers.md"
source_url: "https://www.sqlbi.com/articles/filtering-measures-through-slicers/"
author: "[[Marco Russo & Alberto Ferrari]]"
site: https://www.sqlbi.com
published: 2026-05-04
source_type: article
kb_routing: DAX Code
tags: [dax, calculation-groups, selectedmeasure, filter, slicer, keeplfilters, filter, granularity]
---

# Filtering Measures Through Slicers

Marco Russo & Alberto Ferrari · SQLBI · sqlbi.com · 2026-05-04

## Core concept

A slicer cannot filter a measure directly. You must define the **granularity:** the column/entity to which the measure is applied. "Filter Sales Amount > 100k" is nonsensical. "Filter products with sales > 100k" makes sense.

## Two patterns

**Fixed granularity:** single table (Product) hardcoded in function; calculation items for each threshold.

**Dynamic granularity:** disconnected `TableToFilter` table (Product/Customer/Store) passed to SWITCH; users choose granularity via second slicer.

## Functions

`Local.FilterProductsBasedOnMeasure(resultExpression, filterMeasure, filterLimit)` — KEEPFILTERS + FILTER on Product table.

`Local.FilterTableBasedOnMeasure(resultExpression, filterMeasure, filterLimit)` — SWITCH on TableToFilter selection; dynamic granularity.

## Key functions used

- `SELECTEDMEASURE()` — returns the currently evaluated measure
- `KEEPFILTERS()` — prevents filter overwrites
- `FILTER()` — applies row filter on specified table
- `CALCULATE()` — evaluates expression under modified filter context
- `SELECTEDVALUE()` — reads disconnected table selection
- `SWITCH()` — branches on granularity selection
