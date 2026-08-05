---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# WEEKDAY, WEEKNUM, YEARFRAC

Extract day-of-week, week number, or fractional year between two dates.

## WEEKDAY

```dax
WEEKDAY(<date>[, <return_type>])
```

Returns a number 1–7 identifying the day of the week.

| return_type | Week starts | 1 | 7 |
|---|---|---|---|
| 1 (default) | Sunday | Sunday | Saturday |
| 2 | Monday | Monday | Sunday |
| 3 | Monday | Monday | Sunday (0–6) |

## WEEKNUM

```dax
WEEKNUM(<date>[, <return_type>])
```

Returns the ISO week number of the year.

| return_type | System | Description |
|---|---|---|
| 1 (default) | System 1 | Week 1 = week containing Jan 1 |
| 21 | System 2 (ISO) | Week 1 = week containing first Thursday |

## YEARFRAC

```dax
YEARFRAC(<start_date>, <end_date>[, <basis>])
```

Returns the fraction of the year between two dates (useful for accrual calculations).

| basis | Day count basis |
|---|---|
| 0 (default) | US (NASD) 30/360 |
| 1 | Actual/actual |
| 2 | Actual/360 |
| 3 | Actual/365 |
| 4 | European 30/360 |

## Examples

```dax
-- Day of week (1=Sunday by default)
DayNum = WEEKDAY('Date'[Date])

-- Is it a weekend?
Is Weekend = WEEKDAY('Date'[Date], 2) >= 6

-- ISO week number
ISO Week = WEEKNUM('Date'[Date], 21)

-- Fraction of year for interest accrual
Accrued Interest = [Principal] * [Rate] * YEARFRAC([StartDate], [EndDate], 1)
```

## Notes

- WEEKDAY with return_type=2 is most common for Monday-start weeks
- WEEKNUM with 21 is the ISO 8601 standard — week 1 contains the first Thursday
- YEARFRAC basis=1 (actual/actual) is most accurate for financial calculations
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[date]]
- [[datediff]]
