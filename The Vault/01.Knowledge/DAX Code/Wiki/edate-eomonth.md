---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# EDATE and EOMONTH

Shift dates by months, or return the last day of a month.

## EDATE

```dax
EDATE(<start_date>, <months>)
```

Returns the date N months before or after `start_date`. Positive `months` moves forward, negative moves backward.

## EOMONTH

```dax
EOMONTH(<start_date>, <months>)
```

Returns the last day of the month N months before or after `start_date`.

## Examples

```dax
-- 3 months from today
Future = EDATE(TODAY(), 3)

-- Last day of this month
Month End = EOMONTH(TODAY(), 0)

-- Last day of month 3 months ago
Prior Month End = EOMONTH(TODAY(), -1)

-- Maturity date: 6 months from issue date
Due Date = EDATE('Invoice'[IssueDate], 6)
```

## Notes

- EDATE: useful for calculating dates that should land on the same day of month (maturity, due date, subscription renewal)
- EOMONTH: returns the last calendar day of the target month
- Both accept negative months to go backward in time
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[date]], [[today]]

## Related

- [[date]]
- [[today]]
