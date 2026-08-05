---
created: 2026-08-01
updated: 2026-08-02
source: "Understanding EARLIER in DAX The Time Machine You Didn't Know You Had.md"
note_type: atomic
tags: [dax, earlier, earliest, nested-row-contexts, intermediate]
---

# EARLIER and EARLIEST with Nested Row Contexts

## Context Ladder Rules

Each iterator adds a new level to the row context stack:

```
Level 1 (outermost) = CALCULATE / calculated column row
Level 2              = First iterator (FILTER, SUMX, ADDCOLUMNS...)
Level 3              = Second nested iterator
... and so on
```

## EARLIER() — One Level Up

`EARLIER()` captures the row context immediately outside the current one.

```c
EARLIER(Sales[Customer])
// → value from the outer row context (one level up)
```

## EARLIEST() — The Top Level

`EARLIEST()` skips all intermediate levels and goes straight to the outermost context (the calculated column row, or the visual filter context in a measure).

```c
EARLIEST(Sales[Customer])
// → value from the top-most (outermost) context
```

## Example: Three Nested Levels

If you have a calculated column with two nested iterators:

```c
Result =
ADDCOLUMNS(
    FILTER(
        ADDCOLUMNS(
            Sales,
            "Col1", EARLIEST(Sales[Region])   // Level 1 (outermost)
        ),
        [Col1] = EARLIER([Col1])              // Level 2
    ),
    "Col2", EARLIER(Sales[Product])          // Level 3 (inner)
)
```

## When to Use EARLIER vs EARLIEST

| Scenario | Use |
|----------|-----|
| Need the row from the immediately enclosing context | `EARLIER()` |
| Need the top-level row regardless of nesting depth | `EARLIEST()` |
| Refactoring EARLIER chains to VAR | Capture intermediate values in VARs instead |

## Refactoring Nested EARLIER Chains

Deeply nested EARLIER chains are a code smell — refactor with VAR:

```c
// Before: nested EARLIER
VAR Outer = EARLIER(Sales[Customer])
VAR Inner = EARLIER(EARLIER(Sales[Product]))
// Refactor to: flat VAR captures
VAR Cust  = Sales[Customer]
VAR Prod  = Sales[Product]
```

This eliminates the mental overhead of tracking context levels.
