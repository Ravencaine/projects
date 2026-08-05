---
created: 2026-08-01
updated: 2026-08-02
source: "Understanding EARLIER in DAX The Time Machine You Didn't Know You Had.md"
note_type: atomic
tags: [dax, earlier, row-context, calculated-columns, filter, CALCULATE, beginner]
---

# EARLIER Row Context Mechanism

## The Core Rule

EARLIER only works with **two nested row contexts**:
- Outer loop → the calculated column row
- Inner loop → an iterator (FILTER, SUMX, ADDCOLUMNS, etc.)
- EARLIER → "look up" to the outer loop's current row value

Without two nested contexts, EARLIER throws: *"EARLIER/EARLIEST refers to an earlier row context which doesn't exist."*

## Why the Error Happens

```c
// BROKEN — no outer loop context for EARLIER to reference
Running Total =
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(Sales, Sales[Month] <= EARLIER(Sales[Month]))
)
```

Error: no outer row context to travel back to.

## The Fix — Use EARLIER Inside a Calculated Column

```c
// WORKS — outer = calculated column row, inner = FILTER iterator
Running Total =
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(
        Sales,
        Sales[Customer] = EARLIER(Sales[Customer]) &&
        Sales[Month]     <= EARLIER(Sales[Month])
    )
)
```

Each row of the calculated column = outer context. FILTER iterates over Sales = inner context. EARLIER() steps back one level.

## Visual: Context Ladder

```
Row Context 1 (outer = calculated column row)
  │
  └── EARLIER() climbs back up here
        │
        └── Row Context 2 (inner = FILTER/SUMX iterator)
```

## Context Transition Is in Disguise

EARLIER is context transition under the hood:
- Each iterator creates a new row context
- EARLIER lets you refer to the one "above" on the ladder
- Think: "Go one step up and fetch that value."

## Multiple Nested Levels

| Function | Direction |
|----------|-----------|
| `EARLIER()` | One level up the context ladder |
| `EARLIEST()` | Top-most (outermost) level |

Three nested loops → `EARLIER(EARLIER(...))` chains one level each time.
