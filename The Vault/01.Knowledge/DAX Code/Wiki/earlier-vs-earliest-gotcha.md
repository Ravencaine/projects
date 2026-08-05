---
created: 2026-07-27
updated: 2026-08-02
source: "Understanding EARLIER in DAX: The Time Machine You Didn't Know You Had"
note_type: gotcha
tags: [dax, earlier, error, row-context, nested-context]
---

# EARLIER/EARLIEST Refers to Earlier Row Context That Doesn't Exist

**Error message:** "EARLIER/EARLIEST refers to an earlier row context which doesn't exist"

## Expected Behaviour

EARLIER should return the value of the specified column from the outer row context.

## Actual Behaviour

DAX throws an error: the expression containing EARLIER is evaluated outside any iterator, so no outer row context exists.

## Why It Happens

EARLIER and EARLIEST only function inside an iterator (SUMX, AVERAGEX, FILTER, ADDCOLUMNS, etc.). If EARLIER appears in a measure that is not called from within an iterator, there is no "earlier" row context to access.

**Common scenarios:**

1. EARLIER used directly in a measure without an enclosing iterator
2. EARLIER used inside CALCULATE at the top level of a measure (not nested inside an iterator)
3. EARLIER used with a level > 1 where only 1 level of nesting exists

**Example of the error:**

```dax
-- This throws the error — no iterator wrapping EARLIER
Bad Measure =
VAR OuterValue = EARLIER(Table[Date])  -- ERROR: no outer row context
RETURN
    CALCULATE(SUM(Table[Amount]), Table[Date] <= OuterValue)
```

## How to Handle It

**Fix 1: Wrap in an iterator**

```dax
Good Measure =
SUMX (
    Table,
    VAR OuterDate = EARLIER(Table[Date])  -- OK: inside SUMX
    RETURN
        CALCULATE(SUM(Table[Amount]), Table[Date] <= OuterDate)
)
```

**Fix 2: Use current row value directly instead of EARLIER**

```dax
-- When only the current row's value is needed (no nesting):
Good Measure =
SUMX (
    Table,
    VAR CurrentDate = Table[Date]  -- Current row value, no EARLIER needed
    RETURN
        CALCULATE(SUM(Table[Amount]), Table[Date] <= CurrentDate)
)
```

**Fix 3: Use measure branching instead of EARLIER**

```dax
-- For many running-total scenarios, CALCULATE-based patterns are cleaner:
Running Total =
CALCULATE (
    [Total Sales],
    ALL(Table),
    Table[Date] <= MAX(Table[Date])
)
```

## Related

- [[earlier-function]]
- [[earlier-in-dax-source]]
- [[filter-context-vs-row-context]] — context layering is key to understanding why EARLIER/EARLIEST behave differently