---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: pattern
tags: [power-bi, disconnected-table, slicers, data-modeling, power-query]
related:
  - "[[Slicer-Highlight-vs-Filter]]"
  - "[[Slicer-Highlight-Measure-IN-VALUES-Snippet]]"
---

# Disconnected Table (Slicer Pattern)

A table that exists in the data model but has **no active relationships** to any other table. Used to build slicers that interact with measures via DAX (rather than through filter propagation) or to decouple slicer behaviour from standard data model filtering.

## Purpose

In a standard Power BI model, any slicer built on a dimension table filters the fact table through the relationship. A disconnected table breaks that relationship intentionally — its slicer selections do not filter the data model directly. Instead, DAX measures read the slicer state using functions like `SELECTEDVALUE` or `IN VALUES()` and apply custom logic (highlighting, dynamic titles, conditional calculations).

## Components

1. **Disconnected table:** single-column table populated with distinct values from a dimension
2. **No relationships:** zero relationships to any other table in the model
3. **Slicer:** built on the disconnected table column
4. **DAX measure(s):** read the disconnected table slicer state and apply logic
5. **Conditional formatting or visual treatment:** driven by the measure output

## Structure

### Power Query (M Code)

```m
// Creates a single-column table of distinct values from a dimension column
// No relationships are created — the table is stand-alone
let
    Source = SourceTable,
    ProductsOnly = Table.SelectColumns(Source, {"Product"}),
    DistinctProducts = Table.Distinct(ProductsOnly)
in
    DistinctProducts
```

### Common Usage Patterns

**Pattern 1 — Highlight vs Filter:**
Use with `SELECTEDVALUE` + `IN VALUES()` measure to highlight selected rows instead of filtering.

**Pattern 2 — Dynamic Titles:**
```dax
Dynamic Title =
"Showing: "
& CONCATENATEX(
    VALUES('DisconnectedTable'[Column]),
    'DisconnectedTable'[Column],
    ", "
)
```

**Pattern 3 — Dynamic Calculation Context:**
```dax
Selected Calc =
IF(
    HASONEVALUE('DisconnectedTable'[Column]),
    SWITCH(
        VALUES('DisconnectedTable'[Column]),
        "A", [Measure A],
        "B", [Measure B],
        [Default Measure]
    )
)
```

## When to Use

- Slicer behaviour that must not filter data (highlight, annotate, compare)
- Dynamic titles based on multi-select slicer state
- Scenario analysis (what-if slicers that switch between calculations)
- Avoiding bi-directional relationship pitfalls

## Variations

- **Single-value disconnected table:** One column, used for on/off toggles or single selections
- **Multi-column disconnected table:** Multiple columns for cross-filtering via DAX
- **Calculated table (DAX):** Use `DATATABLE` or `FILTER(ALL(...))` to create disconnected tables without Power Query

See also [[Conditional-Formatting-in-Power-BI]] and [[filter]] for the supporting technologies.

## Related

- [[Slicer-Highlight-vs-Filter]] — primary use case: highlight instead of filter
- [[Slicer-Highlight-Measure-IN-VALUES-Snippet]] — DAX measure using `IN VALUES()` with a disconnected table
