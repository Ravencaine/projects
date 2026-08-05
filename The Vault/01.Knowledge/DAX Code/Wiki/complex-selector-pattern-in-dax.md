---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "selector", "disconnected", "multi-column"]
note_type: pattern

---

# Complex Selector Pattern in DAX

Using disconnected tables with multi-column logic to implement complex selection criteria.

## Purpose

Standard slicers filter on single columns. Complex selectors use disconnected tables with DAX to implement multi-column, range-based, or conditional selection.

## Multi-Column Selector

```dax
Selected Sales :=
VAR __Selector = VALUES( 'Criteria'[CriteriaID] )
RETURN
SUMX(
    FILTER(
        'Products',
        CONTAINSSTRING( CONCATENATEX( __Selector, [CriteriaID], "," ), [ProductID] )
    ),
    [Sales]
)
```

## Notes

- Combine with disconnected tables for ranges (e.g., "Price $50-100")
- TREATAS() enables virtual joins between selectors and fact tables

## Related

- [[disconnected-tables-in-dax]]
- [[cross-fact-treatas-virtual-relationships]]
