---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# Period-to-Date: DATESYTD, DATESMTD, DATESQTD, DATESWTD

Return a table of dates from the start of the period to the current context date. Used as CALCULATE filters.

## Signatures

```dax
DATESYTD(<dates>[, <year_end_date>])
DATESMTD(<dates>)
DATESQTD(<dates>)
DATESWTD(<calendar>)
```

## Parameters

| Function | Parameter | Notes |
|----------|-----------|-------|
| `DATESYTD` | `year_end_date` | (Optional) Fiscal year-end month/day, e.g. "06/30" |
| `DATESWTD` | `calendar` | Only works with calendar-based date tables |

## Examples

```dax
-- Year-to-date sales
Sales YTD = CALCULATE([Sales], DATESYTD('Date'[Date]))

-- Month-to-date sales
Sales MTD = CALCULATE([Sales], DATESMTD('Date'[Date]))

-- Quarter-to-date sales
Sales QTD = CALCULATE([Sales], DATESQTD('Date'[Date]))

-- YTD with fiscal year ending June 30
Sales FYTD = CALCULATE([Sales], DATESYTD('Date'[Date], "06/30"))
```

## Notes

- All return a **table of dates**: must be used as a filter inside CALCULATE
- `DATESYTD` is the most common; `year_end_date` is essential for fiscal year reporting
- `DATESWTD` requires a calendar table (ISO week dates) — does not work with standard date columns
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[openingbalanceyear]], [[closingbalanceyear]]

## Related

- [[datesytd]]
- [[openingbalanceyear]]
- [[closingbalanceyear]]
