---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Percentile

Returns one or more sample percentiles of the list list. If the value percentiles is a number between 0.0 and 1.0, it will be treated as a percentile and the result will be a single value corresponding to that probability. If the value percentiles is a list of numbers with values between 0.0 and 1.0, the result will be a list of percentiles corresponding to the input probability. The PercentileMode option in options can be used by advanced users to pick a more-specific interpolation method but is not recommended for most uses. Predefined symbols PercentileMode.ExcelInc and PercentileMode.ExcelExc match the interpolation methods used by the Excel functions PERCENTILE.INC and PERCENTILE.EXC. The default behavior matches PercentileMode.ExcelInc. The symbols PercentileMode.SqlCont and PercentileMode.SqlDisc match the SQL Server behavior for PERCENTILE_CONT and PERCENTILE_DISC, respectively.

## Signature

```m
List.Percentile(
list as list,
percentiles as any,
optional options as nullable record
) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| percentiles | any | |
| optional options | nullable record | |

## Returns

any

### Example 1

Find the first quartile of the list {5, 3, 1, 7, 9}.

```m
List.Percentile({5, 3, 1, 7, 9}, 0.25)
```

// Output
```
3
```

### Example 2

Find the quartiles of the list {5, 3, 1, 7, 9} using an interpolation method matching Excel's PERCENTILE.EXC.

```m
List.Percentile({5, 3, 1, 7, 9}, {0.25, 0.5, 0.75},
[PercentileMode=PercentileMode.ExcelExc])
```

// Output
```
{2, 5, 8}
```

