---
created: 2026-07-27
updated: 2026-08-02
source: "Understanding EARLIER in DAX: The Time Machine You Didn't Know You Had"
note_type: function
tags: [dax, earlier, earliest, row-context, nested-context, running-totals]
---

# EARLIER Function

Accesses the value of a column from the OUTER row context within a nested iterator or CALCULATE context. Essential for running totals and calculations requiring the "previous" row context.

## Signature

```dax
EARLIER ( <Column> [, <Level> ] )
EARLIEST ( <Column> )
```

- `EARLIER(Column)` defaults to level 1 (immediate outer context)
- `EARLIER(Column, N)` accesses N levels of nesting up
- `EARLIEST(Column)` always accesses the outermost (top-level) context

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<Column>` | column | Column whose outer-row value to retrieve |
| `<Level>` | integer | Number of nesting levels to go back (default: 1) |

## Returns

The scalar value of Column from the specified outer row context.

## Examples

**Running total within a category:**

```dax
Running Total =
SUMX (
    Table,
    VAR CurrentDate = EARLIER(Table[Date])
    RETURN
        CALCULATE (
            SUM(Table[Amount]),
            Table[Date] <= CurrentDate,
            Table[Category] = EARLIER(Table[Category])
        )
)
```

**Cumulative sales per product (with display order):**

```dax
Cumulative Sales =
SUMX (
    Products,
    VAR CurrentProduct  = Products[ProductKey]
    VAR CurrentOrder    = EARLIER(Products[DisplayOrder])
    RETURN
        CALCULATE (
            [Total Sales],
            Products[ProductKey] = CurrentProduct,
            Products[DisplayOrder] <= CurrentOrder
        )
)
```

**Two levels of nesting with EARLIER(Column, 2):**

```dax
-- If inside FILTER inside another iterator, EARLIER goes level 1,
-- EARLIER(Column, 2) goes to the outermost iterator's context
```

## Notes

- EARLIER only works inside an iterator (SUMX, FILTER, ADDCOLUMNS, etc.) — outside an iterator, there is no outer row context, and EARLIER throws an error
- VAR can replace EARLIER in many cases where you only need the current row's value
- When EARLIER causes context transition (inside CALCULATE), it converts row context to filter context

## Related

- [[earlier-vs-earliest-gotcha]] — common error and resolution
- [[filter-context-vs-row-context]] — foundational row context concept
- 
- [[sumx]] — EARLIER is often needed inside SUMX row contexts for cumulative/running calculations
