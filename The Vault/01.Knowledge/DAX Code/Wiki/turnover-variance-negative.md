---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, conditional, label, chart]
---

# Turnover Variance_Negative

Returns the turnover rate variance only when it is zero or positive (i.e., turnover worsened or unchanged). Used as a dummy measure for conditional label background formatting.

## Signature

```dax
Turnover Variance_Negative =
    IF(
        [Turnover Rate Variance] >= 0,
        [Turnover Rate Variance]
    )
```

## Parameters

None.

## Returns

The variance value if zero or positive; BLANK otherwise.

## Notes

The naming reflects the visual intent — "Negative" in the label background sense means an unfavorable outcome (turnover went up), not a negative number. See `Dummy Measures for Label Background` for the full technique. The `>= 0` condition captures both worsening and flat scenarios with the same styling.

## Related

- [[dummy-measures-for-label-background]]
- [[Turnover-Rate-Variance]]
