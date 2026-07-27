---
created: 2026-07-27
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 2"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-2-7b00a1662317"
note_type: atomic
tags: [dax, atomic, context-transition, calculate]
---

# Context Transition with CALCULATE

The mechanism by which CALCULATE converts an active row context into an equivalent filter context — the key behaviour that makes CALCULATE powerful inside iterators and calculated columns.

## Definition

**Context transition** occurs when CALCULATE runs inside a row context (inside a calculated column or inside an iterator like SUMX). Each active row context is converted into a filter on the corresponding table — effectively one row acting as a one-row filter. This allows measures referenced inside iterators to behave correctly in the row's context.

## Key Points

- CALCULATE evaluates its expression argument **as a measure** — applying filter context, not row context
- When CALCULATE runs inside an iterator, row context → filter context conversion happens automatically
- Context transition can be expensive on large tables: each row triggers its own mini filter operation
- This is why a measure reference inside SUMX behaves differently from a plain column reference

## Example

```dax
-- Inside AVERAGEX, each store creates a row context
-- CALCULATE converts that row context to filter context
-- so [Sales] evaluates for each store individually
MEASURE AvgSalesPerStore =
AVERAGEX(
    VALUES(Stores[StoreID]),   -- Creates row context per store
    CALCULATE([Sales])         -- Context transition: row → filter
)
-- Result: average of each store's total sales
```

Without CALCULATE: `[Sales]` would be evaluated in the outer filter context, ignoring the AVERAGEX row iteration — giving the grand total for every row.

## Related

- [[calculate]] — the function that performs context transition
- [[filter-context-vs-row-context]] — the two contexts involved
- [[averagex]] — iterator that commonly benefits from context transition
