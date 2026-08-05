---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, date-time]
---

# DATE, DATEVALUE, DAY, MONTH, YEAR, QUARTER

Construct or extract parts from a date value.

## DATE

```dax
DATE(<year>, <month>, <day>)
```

Returns a date value constructed from the given year, month, and day integers.

| Term | Definition |
|------|------------|
| `year` | 1–9999 |
| `month` | 1–12 |
| `day` | 1–31 |

## DATEVALUE

```dax
DATEVALUE(<date_text>)
```

Converts a text string to a date value. Useful for importing date text from external sources.

```dax
DATEVALUE("2024-03-15")
DATEVALUE('Sales'[DateString])
```

## DAY / MONTH / YEAR / QUARTER

```dax
DAY(<date>)      -- 1 to 31
MONTH(<date>)    -- 1 to 12
YEAR(<date>)     -- 1900 to 9999
QUARTER(<date>)  -- 1, 2, 3, or 4
```

## Examples

```dax
-- Create a date from components
StartDate = DATE(2020, 1, 1)

-- Extract parts
YearNum = YEAR('Date'[Date])
MonthNum = MONTH('Date'[Date])

-- Use in IF or SWITCH for custom groupings
Fiscal Quarter =
SWITCH(TRUE(),
    MONTH('Date'[Date]) <= 3, "Q1",
    MONTH('Date'[Date]) <= 6, "Q2",
    MONTH('Date'[Date]) <= 9, "Q3",
    "Q4"
)
```

## Notes

- DATE accepts out-of-range values and rolls them forward (e.g., month 13 → January of next year)
- DATEVALUE is locale-sensitive — "03/04/2024" could be March 4 or April 3 depending on system locale
- YEAR, MONTH, DAY, QUARTER work on any date expression (column, function result, etc.)
- Use FORMAT for custom date part extraction: `FORMAT(date, "yyyy")` for year as text

## Related

- [[calendar-and-calendarauto]]
- [[today]]
- [[format]] — custom date formatting
