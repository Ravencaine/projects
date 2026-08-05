---


title: "YEAR"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, date]
note_type: function
description: "YEAR — extracts the four-digit year from a date value. Used in DAX date manipulation and time intelligence. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# YEAR

Extracts the four-digit year from a date value.

## Syntax

```
YEAR( <date> )
```

## Example

```dax
FiscalYear :=
IF(
    MONTH( Sales[OrderDate] ) >= 7,
    YEAR( Sales[OrderDate] ) + 1,
    YEAR( Sales[OrderDate] )
)
```

## Related Functions

- `MONTH` — extracts the month number
- `DAY` — extracts the day of month
- `WEEKDAY` — returns day of week number
- `FORMAT( date, "YYYY" )` — string alternative

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
