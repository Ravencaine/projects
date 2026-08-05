---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, variance, turnover]
---

# Turnover Rate Variance

Absolute difference between the current rolling 12-month turnover rate and the prior period's rate.

## Signature

```dax
Turnover Rate Variance = [Turnover Rate] - [Turnover Rate Last Month]
```

## Parameters

None — references two other measures.

## Returns

A decimal. Negative = turnover improved (fewer leavers relative to headcount). Positive = turnover worsened.

## Notes

For turnover specifically, the sign is inverted from typical variance: a negative variance is good (fewer people left), a positive variance is bad. This must be reflected in conditional formatting and highlight text. `[[Label-Font-Color-SWITCH]]` inverts the color assignment accordingly.

## Related

- [[Turnover-Rate]]
- [[Turnover-Rate-Last-Month]]
- [[dummy-measures-for-label-background]]
