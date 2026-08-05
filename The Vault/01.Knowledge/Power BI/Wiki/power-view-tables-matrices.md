---


title: "Power View Tables and Matrices"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-view, pattern]
note_type: pattern
description: "Power View tables and matrices — summarized data, aggregation, filter pane settings, multiple years in a matrix. From Dunlop Chapter 6."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power View: Tables and Matrices

## Table

Drag fields to the design surface. Power View automatically **summarizes** numeric fields (SUM) and lists unique text fields.

- Hover over a value to see the full detail
- Use the **Filters pane** to limit what appears in the table
- Add a **Tile** layer on top for section headers

## Matrix

A two-dimensional cross-tabulation similar to an Excel PivotTable:

```
Columns: Year (e.g., 2011, 2012)
Rows:    Product category
Values:  SalesAmount (SUM)
```

Multiple years can be displayed as separate columns by selecting multiple year fields.

## Filtering in Power View

**Filters pane** applies to the entire report:

- Filter by top N items
- Filter by field value
- Multiple filters can coexist

## Source Reference

Chapter 6, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
