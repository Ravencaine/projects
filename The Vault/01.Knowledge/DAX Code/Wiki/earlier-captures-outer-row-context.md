---
created: 2026-08-01
updated: 2026-08-02
source: "Gaps and Islands Solving Consecutive Active Days in Power BI.md"
note_type: atomic
tags: [dax, dax-context, earlier, row-context, iterator, nested-iteration]
---

# EARLIER Captures Row Context Across Iterator Boundaries

EARLIER resolves to the current row's value from the **outer** iterator when used inside a **nested** iterator, enabling cross-row comparisons within the same table.

## The Problem It Solves

When you nest one iterator inside another (e.g., RANKX inside ADDCOLUMNS), the inner iterator's row context shadows the outer one. `LessonStreaks[user_id]` inside the inner FILTER refers to the inner iteration's current row — not the outer row you actually need.

EARLIER breaks out of the shadow and reads the outer row's value.

## Syntax

```dax
EARLIER(<column>[, <number>])
```

- `<column>` — the column to read from the outer row context
- `<number>` — (optional) how many levels of context to escape; defaults to 1

## Worked Example from Gaps and Islands

```dax
"Ranking",
RANKX(
    FILTER(
        SUMMARIZE(LessonStreaks, LessonStreaks[user_id], LessonStreaks[date]),
        LessonStreaks[user_id] = EARLIER(LessonStreaks[user_id])  -- outer row's user
    ),
    LessonStreaks[date],
    ,
    ASC
)
```

Without EARLIER, the FILTER would compare every inner row's user_id to itself — always TRUE. EARLIER makes the comparison reference the **outer ADDCOLUMNS row's user**, so the FILTER correctly builds a per-user ranked table.

## EARLIER vs EARLIEST

| | EARLIER | EARLIEST |
|--|---------|----------|
| Levels escaped | 1 (or N) | All — goes to the original filter context |
| Use case | Single-level nesting | Deeply nested iterators |

## Common Gotcha

EARLIER is only needed when you have **nesting**. If you only have one iterator, use the column reference directly — EARLIER would be redundant and confusing.

## Related

- [[gaps-and-islands-theory]] — uses EARLIER in the rank subtraction trick
- [[dax-gaps-and-islands-pattern]] — the full pattern using EARLIER in nested iterators
- [[streak-detection-in-dax]] — existing vault pattern; EARLIER also used there
- [[row-context-vs-filter-context]] — foundational context concept; EARLIER operates within row context
