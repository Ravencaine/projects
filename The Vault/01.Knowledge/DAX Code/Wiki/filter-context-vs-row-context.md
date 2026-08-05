---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: atomic
tags: [dax, atomic, filter-context, row-context]
---

# Filter Context vs Row Context

The two evaluation contexts in DAX that determine how formulas are calculated — and the distinction that separates people who write DAX comfortably from those who fight it.

## Definition

**Filter context** is the set of filters currently applied when a measure is evaluated: slicer selections, visual-level filters, page filters, and any CALCULATE filter arguments. It determines which rows contribute to aggregation functions.

**Row context** is the active row during iteration: it occurs inside calculated columns and iterator functions like SUMX. It does not filter rows by itself — it just points to "the current row."

## Key Points

- Filter context comes from visuals, slicers, filters, and CALCULATE — it determines what data is visible
- Row context occurs inside calculated columns and iterators (SUMX, AVERAGEX, etc.) — it makes "this row" available
- Row context does **not** automatically create filter context — a measure reference inside an iterator behaves differently
- CALCULATE converts row context to filter context (context transition)

## Filter Context Example

```dax
Total Sales = SUM(RetailSalesTransactions[NetAmount])
-- If visual is filtered to Store = "STORE001",
-- only that store's sales are summed
```

## Row Context Example

```dax
SUMX(RetailSalesTransactions, [Quantity] * [UnitPrice])
-- Walks through each row, multiplies Quantity × UnitPrice,
-- then sums the results
```

## Why This Matters

A calculated column referencing another table's aggregated value behaves strangely unless CALCULATE bridges the gap. Without CALCULATE, the row context is active but no filter exists on the related table, so aggregation functions return the grand total rather than the related value.

```dax
-- Without CALCULATE: returns grand total for every row
Column = SUM(RelatedTable[Amount])

-- With CALCULATE: context transition filters to current row
Column = CALCULATE(SUM(RelatedTable[Amount]))
```

## Related

- [[calculate]] — the function that performs context transition
- [[measures-vs-calculated-columns]] — practical consequences of context type choice
