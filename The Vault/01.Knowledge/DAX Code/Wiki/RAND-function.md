---
created: 2026-08-05
updated: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
note_type: function
tags: [dax, function, random, rand, volatile]
---

# RAND()

Generates a random decimal number greater than or equal to 0 and less than 1. Recalculates on every data refresh and user interaction.

## Signature

```dax
RAND()
```

No parameters.

## Returns

`Double` — a random decimal value in the range `[0, 1)`.

## Remarks

- `RAND()` is a **volatile function** — it returns a new value on every evaluation
- It has no seed parameter — the sequence cannot be reproduced
- Volatility means it is re-evaluated on every interaction (slicer change, filter, refresh), which affects performance
- See [[RAND-Volatile-Gotcha]] for implications

## Common Uses

- Tiebreaking in rankings: add `RAND()` as a sort column to order equal-ranked items uniquely
- Random sampling: select a fraction of rows by filtering on `RAND() < threshold`
- Mock data generation in calculated columns

## Example

```dax
// Random tiebreaker column
RandomTiebreaker = RAND()

// Random 10% sample
IsInSample = IF(RAND() < 0.1, TRUE(), FALSE())
```

## Related

- [[RANDBETWEEN-function]]
- [[RAND-Volatile-Gotcha]]
- [[Tie-Breaking-RAND-Pattern]]
- [[Mock-Data-Generation-RAND]]
