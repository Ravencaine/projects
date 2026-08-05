---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX - The Power of Variables (VAR).md"
note_type: atomic
tags: [dax, var, anti-patterns, limits, gotcha, beginner]
---

# VAR: Anti-Patterns and Limits

VAR is powerful, but it has specific limits. Using it in the wrong situations causes errors or subtle bugs.

## Anti-Pattern 1: Inline Literals

Don't use VAR to store a single literal value — just inline it:

```dax
-- Unnecessary: VAR for a literal
VAR Multiplier = 100
RETURN
[Revenue] * Multiplier

-- Better: inline
RETURN
[Revenue] * 100
```

VAR earns its keep with **expressions**, not constants.

## Anti-Pattern 2: Expecting Dynamic Filter Context Inside VAR

Variables capture their defining expression at evaluation time. If the expression depends on the current filter context, that context is fixed at the point of definition — not at RETURN.

**Wrong assumption:**
```dax
VAR TotalRows = COUNTROWS ( Sales )
RETURN
DIVIDE ( [Total Revenue], TotalRows )   -- TotalRows is fixed per context
```

This is usually fine — but if the intent is to recalculate `TotalRows` in a different context, VAR will hold the stale value.

**Fix:** move the expression into the RETURN if it needs to re-evaluate in different contexts, or accept that VAR captures one context.

## Anti-Pattern 3: Using VAR for Row Context Iteration

In **calculated columns**, VAR variables behave differently from measures. Row context is not automatically available inside a VAR the way it is in an implicit iteration:

```dax
-- In a calculated column — potential issue
VAR DailyTotal = SUM ( Sales[Revenue] )   -- SUM ignores row context in a column
RETURN
DailyTotal / [RowCount]                  -- context may be wrong
```

For row-level calculations in calculated columns, use explicit iterators (`SUMX`, `MAXX`, etc.) rather than relying on VAR to carry row context.

## Anti-Pattern 4: Shadowing Measures with the Same Name

A VAR with the same name as a measure does **not** shadow the measure:

```dax
VAR Revenue = [Total Revenue]   -- creates a new variable named Revenue
RETURN
Revenue + [Total Revenue]       -- both the variable AND the measure are accessible
```

This is sometimes intentional but can cause confusion. Use distinct naming: `vRevenue` or `CalcRevenue` for variables.

## Anti-Pattern 5: Deeply Nested VAR (Hard to Read)

Excessive VAR nesting in RETURN makes debugging harder:

```dax
-- Too many intermediate variables for a simple result
VAR A = [X]
VAR B = [Y]
VAR C = A + B
VAR D = [Z]
VAR E = C * D
RETURN
E
```

Use VAR for genuinely complex intermediate steps — not as a replacement for clear expression structure.

## Limit: Scope Is Measure-Local Only

A VAR defined in one measure cannot be referenced in another measure. There is no cross-measure variable sharing.

**Solution for cross-measure reuse:** use measure branching (small base measures) instead.

## Limit: Cannot Be Used Outside a Measure

VAR is valid only inside a `RETURN` block within a measure or calculated column definition. It cannot be used in:
- Query-level DAX (DAX Studio EVALUATE without a measure wrapper)
- Power Query M code
- Calculation groups at the expression level (though it works within individual expressions)

## Related

- [[var-syntax-and-pattern]] — correct VAR / RETURN usage
- [[var-performance-benefit]] — when VAR helps performance
- [[var-calculate-filter-composition]] — VAR + CALCULATE patterns
