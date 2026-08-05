---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "time-intelligence", "reverse-ytd", "remaining-period"]
note_type: pattern

---

# Reverse Year-To-Date in DAX

Calculating the remaining days in the current period — opposite of YTD.

## Purpose

Reverse YTD shows how much is left to achieve in the current period.

```dax
Reverse YTD Sales :=
VAR __TotalYear = SUMX( ALL( 'Dates' ), [Sales Amount] )
VAR __YTD = [Sales YTD]
RETURN
__TotalYear - __YTD
```

## Notes

- Useful for sales quota and target tracking
- Can be combined with a date table to show by-month breakdown

## Related

- [[no-calculate-time-intelligence-pattern]]
- [[rolling-periods-in-dax]]
