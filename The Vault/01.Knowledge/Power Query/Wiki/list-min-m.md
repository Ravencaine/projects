---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: function
tags: [power-query, m, function, aggregation]
---

# List.Min — M Minimum Aggregator

Returns the minimum value from a column or list. Used in Power Query Date Table builds to dynamically detect the earliest date in the fact table.

## Signature

```
List.Min(list as list, optional default as any, optional comparisonCriteria as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `list` | List | The list or column to evaluate |
| `default` | Any | Optional — value to return if the list is empty |
| `comparisonCriteria` | Any | Optional — comparison logic |

## Returns

The minimum value in the list.

## Examples

```m
-- Minimum date from a column:
List.Min(Source[OrderDate])

-- With type conversion (strip time component):
Date.From(List.Min(Source[OrderDate]))

-- Minimum numeric value:
List.Min(Source[Sales])
```

## Notes

- When applied to a date column, `List.Min` may return a datetime. Always wrap with `Date.From()` before passing to `List.Dates`.
- For empty columns, `List.Min` returns null unless a `default` value is provided.
- Used as the dynamic `StartDate` driver in Power Query Date Table builds.

## Related

- [[list-max-m]] — `function`
- [[list-dates-m]] — `function`
- [[power-query-date-table-build]] — `pattern`
