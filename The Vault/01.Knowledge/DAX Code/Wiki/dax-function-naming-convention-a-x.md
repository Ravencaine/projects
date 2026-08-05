---
created: 2026-08-01
updated: 2026-08-02
source: "Unraveling DAX Functions The Mystery Behind AVERAGE, AVERAGEA, and AVERAGEX.md"
note_type: atomic
tags: [dax, naming-convention, iterator, beginner]
---

# DAX Function Naming Convention — "A" and "X" Suffixes

## The Core Rule

DAX uses two suffixes to signal behavior:

| Suffix | Meaning | Example |
|--------|---------|---------|
| **A** | Includes **All** value types | AVERAGEA, COUNTA, SUMA |
| **X** | e**X**pression iterator | AVERAGEX, SUMX, MAXX, MINX |

## "A" Suffix — All Value Types Included

Functions ending in **A** process columns but include non-numeric values that the base function would skip.

| Base | "A" variant | Difference |
|------|-------------|-----------|
| `AVERAGE` | `AVERAGEA` | Includes TRUE=1, FALSE=0, numeric-text as numbers |
| `COUNT` | `COUNTA` | Counts all non-empty cells (text + numbers), not just numbers |
| `SUM` | `SUMA` | Includes TRUE=1, FALSE=0, numeric-text (rarely used) |

### The "A" Rule

> "A" = **includes All types**: Booleans, text, and numeric-text are all counted/averaged/summed.

**Caution:** SUMA is rarely needed — use it only when column has deliberate mixed types.

## "X" Suffix — Iterator with Expression

Functions ending in **X** iterate over a table and evaluate an expression for each row before aggregating.

| Base | "X" variant | Expression example |
|------|-------------|-------------------|
| `SUM` | `SUMX` | `SUMX(Sales, Sales[Qty] * Sales[Price])` |
| `AVERAGE` | `AVERAGEX` | `AVERAGEX(Sales, Sales[Qty] * Sales[Price])` |
| `MAX` | `MAXX` | `MAXX(Sales, Sales[Qty] * Sales[Price])` |
| `MIN` | `MINX` | `MINX(Sales, Sales[Qty] * Sales[Price])` |
| `COUNT` | `COUNTX` | `COUNTX(Sales, Sales[Qty] * Sales[Price])` |
| `COUNTA` | `COUNTX` | Same function — X handles both |
| `COUNTROWS` | `COUNTX` | `COUNTX(Sales, 1)` (counts rows) |

### The "X" Rule

> "X" = iterates over table rows, evaluates the e**X**pression per row, then aggregates the result.

## Combined — "AX" Suffix

There is no "AX" in DAX, but combining both rules:

| Function | Meaning |
|----------|---------|
| `SUMX` | Iterate table + apply expression + sum results |
| `MAXX` | Iterate table + apply expression + find max |
| `MINX` | Iterate table + apply expression + find min |
| `AVERAGEX` | Iterate table + apply expression + average results |
| `COUNTX` | Iterate table + apply expression + count non-blank results |

## Memory Aid

```
A = All (values count)
X = eXpression (per-row evaluation)
```

Think: **"AX"** is for when you need **A**ll the flexibility of **X**pression evaluation.
