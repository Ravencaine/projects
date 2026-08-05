---


title: "Power Query Choose Columns and Remove Columns"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern]
note_type: reference
description: "Choose Columns and Remove Columns in Power Query — keep only needed columns before loading. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Choose Columns / Remove Columns

## Choose Columns

Keeps **only** the selected columns. All others are removed.

```
Home → Choose Columns → check the columns to retain
```

Useful when importing a wide table but only a few columns are needed for analysis.

## Remove Columns

Removes **only** the selected columns. All others are retained.

```
Home → Remove Columns
```

Or: select columns → right-click → **Remove Columns**

## Comparison

| Operation | Result |
|-----------|--------|
| Choose Columns | Keep checked columns; discard rest |
| Remove Columns | Discard checked columns; keep rest |

## Keyboard Shortcut

Select a column header → **Ctrl+click** another header to multi-select → right-click → choose operation.

## Typical Workflow

```
From Web / From Database
  → Query Editor opens with all columns
  → Choose Columns (keep only needed)
  → Close & Load
```

This reduces memory usage and improves PowerPivot/Power Map performance.

## Source Reference

Chapter 8, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
