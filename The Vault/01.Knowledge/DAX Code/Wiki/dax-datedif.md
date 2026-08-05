---


title: "DATEDIF"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, date]
note_type: function
description: "DATEDIF — calculates the difference between two dates in years, months, or days. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# DATEDIF

Calculates the difference between two dates in a specified unit (year, month, or day).

## Syntax

```
DATEDIF( <start_date>, <end_date>, <unit> )
```

## Units

| Unit | Returns |
|------|---------|
| `"Y"` | Difference in complete years |
| `"M"` | Difference in complete months |
| `"D"` | Difference in days |
| `"MD"` | Difference ignoring years and months |
| `"YM"` | Difference ignoring years |
| `"YD"` | Difference ignoring years |

## Example

```dax
Age Years := DATEDIF( Employee[BirthDate], TODAY(), "Y" )
```

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
