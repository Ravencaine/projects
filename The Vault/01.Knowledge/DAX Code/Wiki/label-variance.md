---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, measure, label, variance]
---

# Label Variance

A formatted variance string with directional arrow prefix and percentage value.

## Signature

```dax
Label Variance =
VAR _Var = [Turnover Rate Variance]
RETURN
    IF(
        _Var > 0,
        "↑ " & FORMAT(_Var, "0.00%"),
        "↓ " & FORMAT(ABS(_Var), "0.00%")
    )
```

## Parameters

None.

## Returns

A string like `"↑ 2.34%"` or `"↓ 1.05%"`. Returns blank if `_Var = 0`.

## Notes

`FORMAT(ABS(_Var), "0.00%")` converts the raw decimal to a percentage string. Using `ABS()` inside FORMAT ensures no double minus sign (FORMAT handles the sign via the arrow prefix). The `VAR _Var` pattern prevents double evaluation of the measure.

## Related

- [[Variance-Arrow-Label]]
- [[Label-Font-Color-SWITCH]]
