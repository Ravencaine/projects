---


title: "Power Query Group By (Multiple Columns)"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern]
note_type: reference
description: "Power Query Group By — aggregating with one or two fields, with optional aggregation of a third field. From Dunlop Nobel Prize example."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Group By

Groups rows by one or more columns and computes an aggregation (count, sum, average, etc.) for each group.

## Single-Column Group By

```
Home → Group By → select column → select aggregation
```

## Two-Column Group By

Power Query can group by two fields simultaneously, creating a cross-tabulation.

From the Nobel Prize example:

```
Group By: category + year
Aggregation: Count rows
```

Result: a row for each unique (category, year) combination.

## Three-Column Group By with Aggregation

```
Group By: [category, year]
Aggregations: [surname] → Count Rows
```

This creates a row per (category, year) with the count and an additional column showing the laureate's surname.

## Applied Steps

All Group By configurations are stored in the **Query Settings → Applied Steps** pane and can be re-edited by clicking the gear icon next to "Grouped Rows."

## Source Reference

Chapter 8, Nobel Prize JSON example, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
