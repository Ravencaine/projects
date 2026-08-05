---
created: 2026-08-05
updated: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
note_type: pattern
tags: [dax, pattern, rank, tiebreaker, random, rand]
---

# Tie-Breaking with RAND()

Use `RAND()` as a tiebreaker column to enforce unique ordering when two or more rows share the same rank — critical for deterministic Top N displays and leaderboards.

## Purpose

`RANKX()` produces duplicate rank values when multiple rows share the same measure value. Adding a `RAND()` column as a secondary sort key makes each row's order unique, eliminating ties in any ranking or sorted table visual.

## Structure

```dax
// Calculated column — adds a new random decimal per row
RandomTiebreaker = RAND()

// Measure — RANKX with tiebreaker sort
RankWithTiebreaker =
RANKX(
    ALL('Table'),
    [Measure] * 1000000 + [RandomTiebreaker],
    ,
    DESC,
    DENSE
)
```

Or in a table visual: add both `[Measure]` and `[RandomTiebreaker]` to the visual, sort by `Measure` (descending), then by `RandomTiebreaker` (descending).

## Why Multiply Measure by 1,000,000

Multiplying the measure value by a large constant before adding the tiebreaker ensures the tiebreaker only affects rows that are truly tied — the fractional tiebreaker cannot outweigh different measure values.

## Notes

- The tiebreaker recalculates on every refresh — rank ordering will shift between refreshes
- This is only appropriate for display/UI ordering, not for persistent ordering in source data
- `RAND()` has no seed — ordering is not reproducible across runs

## Related

- [[RAND-function]]
- [[RAND-Volatile-Gotcha]]
