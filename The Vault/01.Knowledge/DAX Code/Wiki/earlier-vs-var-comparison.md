---
created: 2026-08-01
updated: 2026-08-02
source: "Understanding EARLIER in DAX The Time Machine You Didn't Know You Had.md"
note_type: atomic
tags: [dax, earlier, var, readability, measured-columns, beginner]
---

# EARLIER vs VAR Comparison

## The Problem with EARLIER

- Works only in calculated columns (not measures)
- Hard to read with nested calls
- Breaks easily when logic moves to measures
- Two identical column references (`EARLIER(Sales[Customer]) && Sales[Customer]`) are confusing

## EARLIER Pattern (Legacy)

```c
Running Total =
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(
        Sales,
        Sales[Customer] = EARLIER(Sales[Customer]) &&
        Sales[Month]    <= EARLIER(Sales[Month])
    )
)
```

## VAR Pattern (Modern — Preferred)

```c
Running Total =
VAR Cust = Sales[Customer]
VAR Mo   = Sales[Month]
RETURN
    CALCULATE(
        SUM(Sales[Sales]),
        FILTER(Sales, Sales[Customer] = Cust && Sales[Month] <= Mo)
    )
```

**Benefits of VAR over EARLIER:**
| Benefit | Detail |
|---------|--------|
| Readability | Named variables self-document intent |
| Works in measures | VAR works anywhere (calculated column or measure) |
| Reusability | Same variable used multiple times = computed once |
| Performance | DAX engine can optimize VAR evaluation |
| Debugging | Easier to inspect intermediate values |

## Rule of Thumb

> EARLIER = Old Time Machine (still valid, limited)
> VAR = Modern Jetpack (preferred for new work)

Use VAR for clarity, flexibility, and speed. Reserve EARLIER for legacy calculated column patterns.
