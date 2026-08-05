---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: function
tags: [power-query, m, function, aggregation]
---

# List.Max — M Maximum Aggregator

Returns the maximum value from a column or list. Used in Power Query Date Table builds to dynamically detect the latest date in the fact table.

## Signature

```
List.Max(list as list, optional default as any, optional comparisonCriteria as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `list` | List | The list or column to evaluate |
| `default` | Any | Optional — value to return if the list is empty |
| `comparisonCriteria` | Any | Optional — comparison logic |

## Returns

The maximum value in the list.

## Examples

```m
-- Maximum date from a column:
List.Max(Source[OrderDate])

-- With type conversion (strip time component):
Date.From(List.Max(Source[OrderDate]))

-- Extend to end of year (best practice):
Date.EndOfYear(List.Max(Source[OrderDate]))
```

## Notes

- Like `List.Min`, always wrap with `Date.From()` to strip any datetime component.
- For production Date Tables, wrap `List.Max` in `Date.EndOfYear()` to ensure the table covers full calendar years — no partial months at year boundaries.
- Best practice: extend `EndDate` to December 31 of the year after the latest data date, so forecast and budget visuals always have valid date rows.

## Related

- [[list-min-m]] — `function`
- [[list-dates-m]] — `function`
- [[power-query-date-table-build]] — `pattern`
