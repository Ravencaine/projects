---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, data-modeling, performance, star-schema, vertipaq, beginner, intermediate]
---

# Star Schema: The Biggest Performance Win

Switching from a flat wide table to a proper star schema was the single biggest fix — roughly halved the load time on its own.

## The Flat Table Problem

A single wide table with all columns (40+ columns, 12M rows) forces VertiPaq to scan low-compression columns it wasn't designed for. Every row contains repeated descriptive text (customer names, product categories, region names) that doesn't compress well.

**The result:** 8.9-second DAX queries.

## The Star Schema Solution

Split into one skinny fact table and compact dimension tables:

```
                    ┌─────────────┐
                    │  DimDate    │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
    ┌─────────┴───┐  ┌────┴────┐  ┌────┴────┐
    │ DimCustomer │  │DimProduct│  │DimRegion│
    └─────────────┘  └─────────┘  └─────────┘
                     ┌───────────┐
                     │ FactSales │  (keys + measures only)
                     └───────────┘
```

**FactSales:** OrderID, CustomerID, ProductID, DateID, Quantity, LineTotal
**DimCustomer:** CustomerID, Name, City, Segment (150 rows)
**DimProduct:** ProductID, Name, Category, Brand (500 rows)
**DimDate:** Date, Year, Month, Quarter, YearMonth

## Why VertiPaq Loves This Shape

VertiPaq compresses each column independently. A small, low-cardinality column (Region with 5 values) compresses to near-zero. A repeated customer name compresses well because it's stored once in a lookup table. The fact table's numeric columns compress efficiently.

The engine scans a skinny table with integer keys instead of a wide table with repeated text.

## Results

- Matrix DAX query: 8.9s → ~4s (before any other fixes)
- Model structure: flat 42-column table → proper star schema
- Time to implement: one afternoon in Power Query

## Relationship Direction

Keep all relationships **single-direction** pointing from dimension to fact. Bidirectional filters cause ambiguity and row duplication in larger models.

## Related

- [[vertipaq-column-cardinality]] — why column-level compression is so important
- [[performance-analyzer-workflow]] — measure before and after
- [[dax-measure-optimization-patterns]] — lighter DAX on top of a clean model
