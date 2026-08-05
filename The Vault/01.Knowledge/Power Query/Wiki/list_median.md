---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["list", "m-function"]
---


# List.Median

Returns the median item of the list list. This function returns null if the list contains no non- null values. If there is an even number of items, the function chooses the smaller of the two median items unless the list is comprised entirely of datetimes, durations, numbers or times, in which case it returns the average of the two items. Example Find the median of the list {5, 3, 1, 7, 9}. Usage Power Query M powerquery-mList.Median({5, 3, 1, 7, 9}) Output 5 Related content Comparison criteria Last updated on 03/24/2026 --- PAGE 735 ---

## Signature

```m
List.Median(list as list, optional comparisonCriteria as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| list | list | |
| optional comparisonCriteria | any | |

## Returns

any

