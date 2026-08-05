---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "operations", "tickets", "support", "queue"]
note_type: pattern

---

# Open Tickets in DAX

Counting unresolved support or task tickets as of a given date.

## Pattern

```dax
Open Tickets :=
VAR __AsOfDate = MAX( 'Dates'[Date] )
RETURN
COUNTROWS(
    FILTER(
        'Tickets',
        'Tickets'[OpenedDate] <= __AsOfDate
        && OR(
            ISBLANK( 'Tickets'[ClosedDate] ),
            'Tickets'[ClosedDate] > __AsOfDate
        )
    )
)
```

## Notes

- `OpenedDate <= AsOfDate AND (ClosedDate is blank OR ClosedDate > AsOfDate)`
- Use a date table for consistent "as of" reporting

## Related

- [[order-fulfillment-in-dax]]
- [[duration-calculations-in-dax]]
