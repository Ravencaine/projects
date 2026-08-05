---
created: 2026-08-02
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, function, date, edate]
---

# Date Last Month

Shifts the maximum date back by one month using `EDATE`.

```dax
Date Last Month = EDATE([Maximum Date], -1)
```

## EDATE

```
EDATE(<start_date>, <months>)
```

Returns the date `months` before (negative) or after (positive) the start date. This is the standard DAX function for period-offset arithmetic.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
