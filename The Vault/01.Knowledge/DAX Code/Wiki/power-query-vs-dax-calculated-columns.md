---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Working with Fields and Measures.md"
note_type: atomic
tags: [dax, power-query, calculated-column, m-language, beginner, performance]
---

# Power Query vs DAX Calculated Columns

Columns can be created in two places in Power BI: Power Query (M language) and the data model (DAX). The choice matters for performance, flexibility, and model size.

## The Priority Rule

> **Do as much as possible in Power Query. Use DAX calculated columns only when you must.**

Power Query transformations happen before data is compressed and loaded into the model. DAX calculated columns are evaluated after compression and stored as additional data. M transformations cost less storage; DAX columns cost more.

## Use Power Query When

- Simple text manipulation (trim, proper case, find/replace)
- Extracting date components (year, month, quarter from a date)
- Splitting or merging columns
- Replacing values or removing errors
- The calculation doesn't need data from related tables

```m
// Power Query M — runs before compression
= Table.AddColumn(#"PreviousStep", "Year",
    each Date.Year([OrderDate]))
```

Power Query handles this at lower storage cost than the equivalent DAX column.

## Use DAX Calculated Columns When

- You need to use `RELATED()` to pull data from another table
- The calculation requires context from the model layer (relationships, row context transitions)
- The formula needs DAX-specific functions that don't exist in M (e.g., `CONCATENATEX`, `FORMAT` with complex patterns)
- The column will be used as a dimension for cross-table filtering

```dax
// DAX — required because it uses RELATED()
ProductFullCategory =
RELATED(ProductCategory[CategoryName]) & " - " &
RELATED(ProductSubcategory[SubcategoryName])
```

`RELATED()` requires the model layer — it can't be replicated in Power Query.

## Decision Checklist

| Question | Answer | Use |
|----------|--------|-----|
| Is it a simple transformation (trim, case, date part)? | Yes | Power Query |
| Does it need data from another table? | Yes | DAX |
| Is it a category or classification? | Yes | DAX (if needs RELATED) or Power Query |
| Is it for performance (avoiding complex M)? | — | Depends — test both |
| Is it a numeric aggregation? | Yes | Measure (not column) |

## Practical Default

Start with Power Query. If the transformation can't be done there (needs `RELATED()`, needs row context with DAX-specific functions, or Power Query is making the M script too complex), use a DAX calculated column.

## Related

- [[calculated-column-performance-impact]] — storage cost of DAX vs M
- [[calculated-column-row-context]] — DAX column context behaviour
- [[calculated-column-vs-measure-decision-tree]] — columns vs measures
