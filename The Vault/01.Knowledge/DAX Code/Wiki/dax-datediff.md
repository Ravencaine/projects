---


title: "DATEDIFF"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, date]
note_type: function
description: "DATEDIFF — returns the number of boundaries crossed between two dates. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# DATEDIFF

Returns the number of interval boundaries crossed between two dates.

## Syntax

```
DATEDIFF( <start_date>, <end_date>, <interval> )
```

## Intervals

| Interval | Description |
|----------|-------------|
| SECOND | Seconds |
| MINUTE | Minutes |
| HOUR | Hours |
| DAY | Days |
| WEEK | Weeks |
| MONTH | Months |
| QUARTER | Quarters |
| YEAR | Years |

## Example

```dax
Days Overdue :=
DATEDIFF( Sales[DueDate], Sales[DeliveryDate], DAY )
```

## DATEDIF vs DATEDIFF

| Function | Excel/Power Query | DAX |
|----------|------------------|-----|
| `DATEDIF` | Undocumented Excel function | Not in DAX |
| `DATEDIFF` | Not in Excel | Native DAX function |

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
