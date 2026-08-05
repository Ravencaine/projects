---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: gotcha
tags: [dax, gotcha, blank, measures]
---

# Avoid Converting BLANKs to Values

It is tempting to convert BLANK results to zero (or another default value) in measure formulas, but this degrades performance and user experience.

## Expected Behaviour

When a measure cannot return a meaningful value in the current context, it should return BLANK so report visuals filter out that row grouping automatically.

## Actual Behaviour

Returning 0 instead of BLANK causes:
- All row groupings with no data to appear in the report (with a value of 0)
- Slower report rendering because every row must be rendered
- Incorrect subtotals and grand totals (zeros are counted in aggregations)

## Why It Happens

DAX BLANK values are automatically excluded from report visuals by default. Converting BLANK to 0 eliminates this behaviour. The `DIVIDE` function's third argument (alternate result) is a common source of this pattern.

## How to Handle It

```dax
-- WRONG: converts BLANK to 0
Profit Margin := DIVIDE([Profit], [Sales], 0)

-- CORRECT: returns BLANK when Sales is 0 or BLANK
Profit Margin := DIVIDE([Profit], [Sales])
```

Only use an alternate result in `DIVIDE` when you genuinely want to display a specific value. For most measure scenarios, let BLANK propagate — visuals will handle it correctly.

## Related Gotchas

- [[divide-function-vs-divide-operator]] — related to BLANK handling
- [[use-selectedvalue-instead-of-values]] — pattern note
