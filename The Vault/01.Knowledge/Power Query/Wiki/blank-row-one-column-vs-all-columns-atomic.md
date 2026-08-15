---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Remove Blank Rows in a Table using Power Query(.pbix included).md"
note_type: atomic
tags: [power-query, blank-rows, filter, column-scope, gotcha, atomic]
---

# Blank Row Filter — One Column vs All Columns Gotcha

**Type:** Atomic · **KB:** Power Query · **Source:** [[source-remove-blank-rows-power-query]]

Filtering blank rows by checking a single reference column may leave rows that are blank in other columns. A row where Column2 has a value but Column3 is empty will pass the filter — and may still distort aggregations.

## The scope issue

`Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null))` only checks Column2. If Column3, Column4, or other columns in that row are blank, the row is kept.

## When this matters

- Multi-column datasets where blanks appear in different columns per row
- Aggregations that depend on all columns being populated
- Merges that fail due to nulls in non-reference columns

## More robust pattern

Check all columns, or identify the specific columns that must be populated:

```m
// Filter rows where ANY of these columns are blank
Table.SelectRows(Source, each (
    [Column2] <> "" and [Column2] <> null
    and [Column3] <> "" and [Column3] <> null
))
```

Or remove rows where **all** columns are blank:

```m
Table.SelectRows(Source, each not List.IsEmpty(List.RemoveNulls(Record.ToList(_))))
```

## Rule of thumb

Before filtering, determine: which columns must have values? Check only those. Checking one column is a pragmatic shortcut for simple datasets but can leave dirty data in complex ones.
