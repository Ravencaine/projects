---
created: 2026-08-05
updated: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
note_type: gotcha
tags: [dax, gotcha, volatile, rand, performance, random]
---

# RAND() and RAND.BETWEEN() Are Volatile

`RAND()` and `RAND.BETWEEN()` are volatile functions. Their output changes on every data refresh and on every user interaction — which has two significant consequences: **unpredictable results** and **performance degradation**.

## Definition

A volatile DAX function is re-evaluated on every request for its value. Unlike stable functions (which compute once per filter context and cache the result), volatile functions do not cache — they recalculate each time they are referenced.

## Key Points

- **Output changes every refresh:** `RAND()` produces a different decimal, `RAND.BETWEEN()` a different integer, each time the dataset refreshes or a user interacts with the report
- **No seed parameter:** Unlike many random functions in other languages, DAX `RAND()` has no seed argument — the sequence cannot be reproduced
- **Model caching is disrupted:** Because the value changes on every call, the query engine cannot cache the result, forcing full recomputation
- **Performance impact:** On large tables, volatile calculated columns cause significant slowdowns — the column is recalculated for every row on every refresh
- **Sort order is unstable:** Using `RAND()` for tiebreaking means the order of tied rows shifts on every refresh — not reproducible
- **DAX Studio / Best Practice Analyzer warning:** Both functions are flagged as performance anti-patterns in large datasets

## Recommendations

| Situation | Recommendation |
|-----------|---------------|
| Static mock data | Use `RAND()` once to generate values, then convert to static values via copy-paste as values |
| Tiebreaker in a visual sort | Acceptable — ordering is cosmetic, not data |
| Dynamic ranking in a measure | Avoid — ranking will shift on every interaction |
| Large calculated column | Avoid — creates a new random value per row per refresh |

## Related

- [[RAND-function]]
- [[RANDBETWEEN-function]]
- [[Tie-Breaking-RAND-Pattern]]
- [[dax-performance-patterns]]
