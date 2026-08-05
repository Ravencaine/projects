---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, conditional, label, chart]
---

# Turnover Variance_Positive

Returns the turnover rate variance only when it is negative (i.e., turnover improved). Used as a dummy measure for conditional label background formatting.

## Signature

```dax
Turnover Variance_Positive =
    IF(
        [Turnover Rate Variance] < 0,
        [Turnover Rate Variance]
    )
```

## Parameters

None.

## Returns

The variance value if negative; BLANK otherwise.

## Notes

The naming reflects the visual intent — "Positive" in the label background sense means a favorable outcome (turnover went down), not a positive number. See `Dummy Measures for Label Background` for the full technique. Both this and `Turnover Variance_Negative` are added to the chart's Values field; `IF` ensures only one fires per data point.

## Related

- [[dummy-measures-for-label-background]]
- [[Turnover-Rate-Variance]]
