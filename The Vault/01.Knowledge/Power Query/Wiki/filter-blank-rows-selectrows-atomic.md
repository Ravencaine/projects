---
created: 2026-08-09
updated: 2026-08-09
source: "Easily Remove Blank Rows in a Table using Power Query(.pbix included).md"
note_type: atomic
tags: [power-query, table-selectrows, blank-rows, filter, m-code, atomic]
---

# Filter Blank Rows with Table.SelectRows Atomic

**Type:** Atomic · **KB:** Power Query · **Source:** [[source-remove-blank-rows-power-query]]

`Table.SelectRows` with a conditional `each` expression filters out rows where a specified column is null or empty. This is the core M formula for blank-row removal.

## Formula

```
Table.SelectRows(Source, each ([ColumnName] <> "" and [ColumnName] <> null))
```

- `<> ""` — excludes empty strings
- `<> null` — excludes null values
- Both conditions are required: empty strings and nulls are distinct in M

## Example

```
Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null))
```

Removes rows where Column2 is blank.

## Context

In the Advanced Editor, this replaces or is added after the Source step:

```m
let
    Source = Csv.Document(File.Contents("..."), [Delimiter=",", ...]),
    FilterJunkRows = Table.SelectRows(Source, each ([Column2] <> "" and [Column2] <> null)),
    PromotedHeaders = Table.PromoteHeaders(FilterJunkRows, [PromoteAllScalars=true])
in
    PromotedHeaders
```

## Level

Beginner
