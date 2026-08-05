---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table-manipulation]
---

# Table Manipulation Functions Overview

DAX provides a rich set of table manipulation functions that create, combine, filter, and transform tables.

## Table Creation

| Function | Purpose |
|----------|---------|
| `DATATABLE` | Inline data table declaration |
| `GENERATESERIES` | Generate a sequence of numbers or dates |
| `ROW` | Single-row table with named columns |
| `DISTINCT` | Distinct values from a column |
| `VALUES` | Distinct values including blank row |
| `TOPN` | Top N rows by a sort expression |
| `FILTER` | Table filtered by a Boolean condition |

## Table Combination

| Function | Purpose |
|----------|---------|
| `UNION` | Stack tables (rows appended; duplicate rows kept) |
| `INTERSECT` | Rows appearing in both tables |
| `EXCEPT` | Rows in table1 not in table2 |
| `CROSSJOIN` | Cartesian product of tables |
| `GENERATE` | Cartesian product with row context from table1 |
| `GENERATEALL` | Like GENERATE but includes all table1 rows |
| `NATURALINNERJOIN` | Inner join on common column names |
| `NATURALLEFTOUTERJOIN` | Left outer join on common column names |

## Table Transformation

| Function | Purpose |
|----------|---------|
| `ADDCOLUMNS` | Add computed columns to a table |
| `SELECTCOLUMNS` | Pick/rename columns from a table |
| `SUMMARIZECOLUMNS` | Group by + aggregate (DAX query workhorse) |
| `SUMMARIZE` | Group by with rollup groups (legacy) |
| `TREATAS` | Apply a column as a filter without a physical relationship |
| `GROUPBY` | Like SUMMARIZECOLUMNS but supports nested aggregations |

## Key Notes

- Table functions return **tables**, not scalar values — they must be used inside measures or as arguments to other functions
- `SUMMARIZECOLUMNS` is the preferred grouping function for calculated tables and DAX queries
- `ADDCOLUMNS(SUMMARIZECOLUMNS(...))` is the standard pattern for named grouped aggregations
- `TREATAS` applies a virtual relationship — useful when two columns share the same values but aren't physically joined
- `DATATABLE` accepts only literal constants — no references to columns or measures

## Related

- [[calculate]] — using table results in measures
- [[summarizecolumns]] — function
- [[addcolumns]] — function
