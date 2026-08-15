---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: pattern
tags: [dax, switch, isinscope, isatlevel, level-detection, specificity, conditional-formatting, pattern]
---

# SWITCH Specificity-Ordering Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

When dispatching on hierarchy level using ISINSCOPE or ISATLEVEL, test from **most specific to least specific:** otherwise parent levels match at every leaf cell and the wrong branch fires.

## The problem

ISINSCOPE/ISATLEVEL return TRUE for all ancestor levels. At the month level, `ISINSCOPE('Date'[Year Month]) = TRUE`, `ISINSCOPE('Date'[Year Quarter]) = TRUE`, and `ISINSCOPE('Date'[Year]) = TRUE` — all simultaneously.

## The solution

Order SWITCH branches from most-specific (leaf) to least-specific (root):

```dax
SWITCH(
    TRUE,
    -- Test 1: most specific (leaf level)
    ISINSCOPE('Date'[Year Month]) || ISINSCOPE('Date'[Year Month Short]),
        <leaf branch>,
    -- Test 2: mid level
    ISINSCOPE('Date'[Year Quarter]),
        <mid branch>,
    -- Test 3: least specific (root level)
    ISINSCOPE('Date'[Year]),
        <root branch>
)
```

The first branch that matches "wins" — so most specific must be first.

## Why this matters for non-calendar hierarchies too

The same principle applies to any multi-level hierarchy (e.g., Seat → Sector → Category). At the Seat level, both ISINSCOPE(Seat) and ISINSCOPE(Sector) and ISINSCOPE(Category) are all TRUE.

## Double-columns for leaf level

The month-level branch checks two columns because the visual has two versions of the month:

```dax
ISINSCOPE('Date'[Year Month]) || ISINSCOPE('Date'[Year Month Short])
```

This handles both the full month name and the 3-letter abbreviation used in the visual.

## Related

- [[SWITCH-Level-Dispatch-Pattern]] — general dispatch framework
- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — real-world implementation
- [[SWITCH-Condition-Order-Matters-Gotcha]] — the gotcha when this is violated
