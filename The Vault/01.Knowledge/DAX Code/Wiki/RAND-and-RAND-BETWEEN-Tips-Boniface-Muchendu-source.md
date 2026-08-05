---
created: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
source_url: https://databear.com/rand-and-rand-between-functions/
note_type: source
tags: [dax, rand, random, mock-data, tiebreaker, databear]
---

# RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)

Two practical DAX functions for generating random numbers in Power BI — RAND() for decimals between 0–1, and RAND.BETWEEN() for integers within a range — with use cases for mock data and rank tiebreaking.

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2024-03-10
> **URL:** https://databear.com/rand-and-rand-between-functions/
> **Routed to:** DAX Code

## Summary

Boniface Muchendu (DataBear) covers two DAX functions for random number generation: `RAND()` produces a random decimal between 0 and 1; `RAND.BETWEEN(min, max)` produces a random integer within a specified range. Two practical applications: generating mock test data (e.g., random end dates within a window), and breaking ties in rankings by adding a random tiebreaker column.

## Key Claims

- `RAND()` generates a new random decimal (0–1) on every refresh — no parameters
- `RAND.BETWEEN(min, max)` generates a random integer between the two bounds inclusive
- Both are **volatile functions** — output changes on every data refresh and user interaction
- Performance impact increases with dataset size — use judiciously
- `RAND.BETWEEN()` can be used to generate random offsets from a base date (e.g., end date = start date + `RAND.BETWEEN(5, 10)` days)
- Adding `RAND()` as a tiebreaker column in a ranking table ensures unique ordering for equal-ranked items

## Notable Details

- Both functions are DAX, not Power Fx — the Microsoft Learn link points to Power Fx docs but the behaviour is the same
- `RAND()` is parameterless; `RAND.BETWEEN()` takes two integer parameters
- Neither function accepts a seed — results are different on every refresh
- Volatility means they affect model caching and can slow refresh, especially in calculated columns on large tables

## Extracted Notes

Links to notes derived from this source:

- [[RAND-function]] — `function` — `RAND()` generates a random decimal between 0 and 1
- [[RANDBETWEEN-function]] — `function` — `RAND.BETWEEN()` generates a random integer within a range
- [[Tie-Breaking-RAND-Pattern]] — `pattern` — using `RAND()` to break ties in ranking
- [[RAND-Volatile-Gotcha]] — `gotcha` — both functions are volatile; performance and refresh implications
- [[Mock-Data-Generation-RAND]] — `atomic` — using `RAND.BETWEEN()` for test data generation

## Metadata

| Field | Value |
|-------|-------|
| Source file | RAND() and RAND.BETWEEN() Tips (Boniface Muchendu).md |
| Archived at | — |
| Ingestion date | 2026-08-05 |
| Word count | ~300 |
