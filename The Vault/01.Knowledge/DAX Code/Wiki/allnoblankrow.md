---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter]
---

# ALLNOBLANKROW

From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a column but the blank row, and disregards any context filters that might exist.

## Syntax

```dax
ALLNOBLANKROW( {<table> | <column>[, <column>[, <column>[,…]]]} )
```

## Remarks

The ALLNOBLANKROW function only filters the blank row that a parent table, in a relationship, will show when there are one or more rows in the child table that have non-matching values to the parent column. See the