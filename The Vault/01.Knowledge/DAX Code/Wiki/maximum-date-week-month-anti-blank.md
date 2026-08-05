---
created: 2026-08-02
source: Power BI Time Hacks: Mastering Dynamic Date Views
note_type: atomic
tags: [dax, atomic, max, calculate, filter, date, calendar]
---

# Maximum Date/Week/Month: MAX + CALCULATE + FILTER Anti-Blank

Returns the maximum date/week/month visible in the current context, filtering out blank rows from the fact table.

```dax
Maximum Date =
    MAX('Asset Data'[Date])

Maximum Week =
    CALCULATE(
        MAX('Calendar'[Weekly]),
        FILTER(
            'Asset Data',
            'Asset Data'[Date] <> BLANK()
        )
    )

Maximum Month =
    CALCULATE(
        MAX('Calendar'[Monthly]),
        FILTER(
            'Asset Data',
            'Asset Data'[Date] <> BLANK()
        )
    )
```

**Design:** `MAX('Asset Data'[Date])` gives the single max date directly. For `Weekly` and `Monthly`, wrapping in `CALCULATE(MAX(...), FILTER(..., <>BLANK()))` ensures blanks in the fact table don't suppress valid calendar weeks/months from being selected.
