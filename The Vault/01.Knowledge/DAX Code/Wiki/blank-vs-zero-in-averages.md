---
created: 2026-07-27
updated: 2026-08-02
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: gotcha
tags: [dax, gotcha, blank, average, aggregation]
---

# BLANK() vs 0 in Averages

BLANK() and 0 are not equivalent in DAX aggregations — BLANK propagates correctly through averages and percentages, while 0 is treated as a measured value.

## Expected Behaviour

If a store has zero sales, its average sales should exclude that store from the denominator — treating it as missing data rather than a zero measurement.

## Actual Behaviour

```
Store A: 100
Store B: 0      -- zero value (store was open, made no sales)
Store C: BLANK() -- no data (store was not operating)

AVERAGE(A, B, C) = (100 + 0) / 2 = 50  -- C excluded from denominator
AVERAGE(A, B, C) = (100 + 0 + BLANK) / ? = BLANK -- BLANK propagates
```

## Why It Happens

- DAX aggregation functions (SUM, AVERAGE, COUNT, etc.) **ignore BLANK rows** in both numerator and denominator
- A literal `0` is a **measured value**: it participates in the count and sum
- The `IF(ISBLANK(...), 0, ...)` pattern converts a missing value to an explicit zero — which is sometimes intentional and sometimes a mistake

## How to Handle It

**For inventory aging buckets and similar summing patterns:** use `IF(ISBLANK(...), 0, ...)` because you need buckets to sum to 100% — BLANK would break the total.

**For averages where missing means "not applicable":** return BLANK and let the aggregation function handle it correctly — this keeps averages accurate.

```dax
-- Good: bucket sum (blank would break total)
RETURN IF(ISBLANK(_weeksold), 0, _weeksold)

-- Good: average sales (blank excluded from denominator)
RETURN IF(ISBLANK([Sales]), BLANK(), [Sales])
```

## Related Gotchas

- [[divide-function-vs-divide-operator]] — related BLANK() handling in division
- [[conditional-variance-display-percent-hide]] — the BLANK guard pattern
