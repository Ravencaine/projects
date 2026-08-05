---
created: 2026-08-02
updated: 2026-08-02
source: Creating a Date Table in Power BI.md
note_type: function
tags: [power-query, m, function, date-series]
---

# List.Dates — M Date Series Generator

Generates a list of consecutive date values from a start date for a given count. The foundational M function for building a Date Table in Power Query.

## Signature

```
List.Dates(start as date, count as number, step as duration) as list
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start` | Date | The first date in the returned list |
| `count` | Number | Number of dates to generate |
| `step` | Duration | Increment between dates — `#duration(1, 0, 0, 0)` for daily |

## Returns

A list of `count` date values starting at `start`, incremented by `step`.

## Examples

```m
-- Generate 365 daily dates starting 1 Jan 2024:
List.Dates(#date(2024, 1, 1), 365, #duration(1, 0, 0, 0))

-- Dynamic version (driven by fact table):
let
    StartDate = Date.From(List.Min(Source[OrderDate])),
    EndDate   = Date.From(List.Max(Source[OrderDate])),
    Days      = Duration.Days(EndDate - StartDate) + 1,
    Dates     = List.Dates(StartDate, Days, #duration(1, 0, 0, 0))
in
    Dates
```

## Notes

- `List.Dates` returns a list, not a table — wrap it in `Table.FromList()` to convert to a table.
- Always wrap `List.Min()` and `List.Max()` results in `Date.From()` to strip any datetime component.
- The `step` duration must be `#duration(1, 0, 0, 0)` for daily dates; use `#duration(7, 0, 0, 0)` for weekly.

## Related

- [[list-min-m]] — `function`
- [[list-max-m]] — `function`
- [[power-query-date-table-build]] — `pattern`
- [[table_fromlist]] — `function`
