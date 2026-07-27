---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# DATEADD, DATESBETWEEN, DATESINPERIOD

Shift dates or build custom date ranges for CALCULATE filters.

## DATEADD

```dax
DATEADD(<dates>, <number_of_intervals>, <interval>)
```

Returns a table of dates shifted forward or backward by N intervals.

| `interval` | Values |
|------------|--------|
| DAY, MONTH, QUARTER, YEAR | Standard intervals |
| WEEK | Calendar only |

**Special behaviour:** When the last 2 days of a month are selected and shifted by MONTH, DAX uses "extension" semantics — it extends to the end of the shifted month (e.g., Feb 27–28 + 1 month → Mar 27–31).

## DATESBETWEEN

```dax
DATESBETWEEN(<dates>, <start_date>, <end_date>)
```

Returns a table of dates between two fixed dates. Best for custom ranges.

## DATESINPERIOD

```dax
DATESINPERIOD(<dates>, <start_date>, <number_of_intervals>, <interval>)
```

Returns a table of N consecutive intervals starting from `start_date`.

| `interval` | Notes |
|------------|-------|
| DAY, WEEK, MONTH, QUARTER, YEAR | Standard |
| WEEK | Calendar only |

## Examples

```dax
-- Same period last year
Sales Last Year = CALCULATE([Sales], DATEADD('Date'[Date], -1, YEAR))

-- Previous month
Sales Prev Month = CALCULATE([Sales], DATEADD('Date'[Date], -1, MONTH))

-- Last 30 days from today
Last 30d = CALCULATE([Sales], DATESINPERIOD('Date'[Date], TODAY(), -30, DAY))

-- Custom range
Q1 Range = CALCULATE([Sales], DATESBETWEEN('Date'[Date], DATE(2024,1,1), DATE(2024,3,31)))
```

## Notes

- All return a **table** — used as a CALCULATE filter argument
- Prefer DATESINPERIOD over DATESBETWEEN for standard intervals
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[sameperiodlastyear]], [[datesmtd-datesqtd-datesytd]]

## Related

- [[datesmtd-datesqtd-datesytd]]
- [[sameperiodlastyear]]
