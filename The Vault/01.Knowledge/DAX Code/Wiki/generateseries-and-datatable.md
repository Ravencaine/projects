---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table-manipulation]
---

# GENERATESERIES and DATATABLE

Inline table creation functions for constants.

## GENERATESERIES

Generates a single-column table of sequential values.

### Signature

```dax
GENERATESERIES(<start_value>, <end_value>[, <increment_value>])
```

### Examples

```dax
-- Numbers 1 to 10
GENERATESERIES(1, 10)

-- Even numbers 2 to 20
GENERATESERIES(2, 20, 2)

-- Dates from today to 30 days out
GENERATESERIES(TODAY(), TODAY() + 30, 1)
```


## DATATABLE

Declares a table of literal values inline.

### Signature

```dax
DATATABLE(
    ColumnName1, DataType1, { { Value1 }, { Value2 }, … },
    ColumnName2, DataType2, { { Val1, Val2 }, { Val3, Val4 }, … }
)
```

### Supported Data Types

`BOOLEAN`, `CURRENCY`, `DATETIME`, `DOUBLE`, `INTEGER`, `STRING`

### Examples

```dax
-- Simple constant table
DATATABLE(
    "Fruit", STRING, { {"Apple"}, {"Banana"}, {"Cherry"} }
)

-- Multi-column table
DATATABLE(
    "Name", STRING, "Age", INTEGER, { {"John", 25}, {"Jane", 30} }
)
```

## Notes

- DATATABLE only accepts **literal constants**: no columns, measures, or expressions
- DATATABLE values may use: constants, `BLANK()`, `DATE()`, `TIME()`, and unary minus for negatives
- GENERATESERIES can use scalar expressions for start/end (including TODAY(), NOW())
- Use DATATABLE for small lookup tables and GENERATESERIES for numeric/date sequences

## Related

- [[table-manipulation-functions-overview]]
- [[union-intersect-except]]
