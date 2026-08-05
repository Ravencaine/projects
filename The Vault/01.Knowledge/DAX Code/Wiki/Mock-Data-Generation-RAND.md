---
created: 2026-08-05
source: RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)
note_type: atomic
tags: [dax, mock-data, testing, randbetween, rand, random]
---

# Mock Data Generation with RAND()

Use `RAND.BETWEEN()` to generate realistic random test data for data models and visual prototyping — without real data.

## Definition

Creating synthetic rows or column values (random end dates, scores, durations) using `RAND.BETWEEN()` to populate a data model during development and testing.

## Key Points

- **Use case:** Testing reports before real data is available, or building demos and templates
- **`RAND.BETWEEN()` for integer ranges:** Generates random integers within a realistic min-max window
- **Date offsets:** Add a random integer offset to a base date column to create plausible related dates
- **One-time conversion recommended:** Run the calculated column once, then copy-paste as values to make it static — avoids volatile behaviour in production
- **Realistic ranges matter:** Choose min/max values that match the real-world domain — e.g., task duration in business days

## Example

```dax
// Random end date: 5 to 10 calendar days after start date
RandomEndDate = 'Tasks'[StartDate] + RAND.BETWEEN(5, 10)

// Random rating from 1 to 5
RandomRating = RAND.BETWEEN(1, 5)

// Random amount between $10 and $500
RandomAmount = RAND.BETWEEN(10, 500)
```

## Notes

- After generating values, convert the calculated column to static values (Power Query → Remove Duplicates → load as values) to eliminate the volatile recalculation
- For large test datasets, generate the data in Excel or Power Query rather than as DAX calculated columns

## Related

- [[RANDBETWEEN-function]]
- [[RAND-function]]
- [[RAND-Volatile-Gotcha]]
