---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# TODAY, NOW, UTCTODAY, UTCNOW

Return the current date and/or time.

## TODAY

```dax
TODAY()
```

Returns the current date (no time component). Recalculates on every refresh.

## NOW

```dax
NOW()
```

Returns the current date and time. Recalculates on every refresh.

## UTCTODAY and UTCNOW

```dax
UTCTODAY()
UTCNOW()
```

Return the current date/time in UTC (Coordinated Universal Time), regardless of the model's local timezone.

## Examples

```dax
-- Current date
Today = TODAY()

-- Current date and time
Now = NOW()

-- Is the date in the past?
Is Past = 'Date'[Date] < TODAY()

-- Days since today
Days Since Today = DATEDIFF('Date'[Date], TODAY(), DAY)
```

## Notes

- **TODAY** and **NOW** are volatile — they recalculate on every query/refresh. Avoid using them in calculated columns unless you want them to update with each query
- **UTCTODAY** and **UTCNOW** return UTC time regardless of the model's regional settings
- For measures, TODAY/NOW is generally fine; for calculated columns it can cause unexpected behaviour
- Use `DATE(YEAR(TODAY()), MONTH(TODAY()), DAY(TODAY()))` if you need TODAY without volatile time
- TODAY() = DATEVALUE(NOW()) in practice (both return the same date)
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[date]] — date construction
- [[datediff]] — date arithmetic
