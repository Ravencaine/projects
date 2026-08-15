---
created: 2026-08-05
updated: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
note_type: function
tags: [dax, function, random, randbetween, integer, volatile]
---

# RAND.BETWEEN()

Generates a random integer between two specified values (inclusive). Recalculates on every data refresh and user interaction.

## Signature

```dax
RAND.BETWEEN(<min>, <max>)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `min` | Integer | The lower bound (inclusive) |
| `max` | Integer | The upper bound (inclusive) |

## Returns

`Integer` — a random integer in the range `[min, max]`.

## Remarks

- Both arguments must be integers
- `RAND.BETWEEN()` is a **volatile function:** it returns a new value on every evaluation
- No seed parameter — the sequence cannot be reproduced
- Often used to add a random integer offset to a date or numeric column

## Example

```dax
// Random end date: start date + 5 to 10 days
RandomEndDate = 'Tasks'[StartDate] + RAND.BETWEEN(5, 10)

// Random score between 1 and 100
RandomScore = RAND.BETWEEN(1, 100)
```

## Related

- [[RAND-function]]
- [[RAND-Volatile-Gotcha]]
- [[Mock-Data-Generation-RAND]]
