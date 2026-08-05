---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: atomic
tags: [dax, fundamentals, context]
---

# DAX Context

DAX formulas evaluate within a **context**: the set of conditions that determines which rows are visible and what values are used in calculations.

## Definition

Context is the set of data that is active for evaluation. Without context, a DAX formula cannot determine its result.

## Key Points

### Row Context

Row context iterates over rows. It exists in:
- **Calculated columns**: each row is evaluated with its own context
- **Iterator functions** (SUMX, MAXX, etc.) — explicitly loop over rows

Row context automatically includes the current row's values. `RELATED()` can follow relationships to fetch related rows.

### Filter Context

Filter context is the set of active filters from:
- Report filters, slicers, and cross-drillthrough
- CALCULATE filter arguments
- Relationship traversal

Filter context is applied **before** aggregation — it determines which rows are included.

### Query Context

Query context is the full set of filters implicitly applied when a query runs — each cell in a PivotTable or report point generates its own query context.

### Context Propagation

Row context does **not** automatically propagate across relationships. Use `RELATED()` for calculated columns or `CALCULATE()` with relationship functions to apply cross-table filters.

### Context Interaction

- Row context + Filter context coexist — a measure in a calculated column evaluates with both
- Nested iterators create nested row contexts
- CALCULATE can **modify** filter context: adding, removing, or replacing filters

## Context Rules

- Measures: no row context by default — only filter context
- Calculated columns: row context always present
- CALCULATE(CALCULATE(...)) nesting: inner CALCULATE runs first, then outer
- `REMOVEFILTERS()` clears all filters; `ALL()` removes filters and ignores existing context

## Related

- [[dax-overview]] — atomic
- [[dax-data-types]] — atomic
- [[calculate]] — function
- [[calculate-table]] — function
- [[filter]] — function
- [[all]] — function
- [[related]] — function
- [[earlier]] — function
