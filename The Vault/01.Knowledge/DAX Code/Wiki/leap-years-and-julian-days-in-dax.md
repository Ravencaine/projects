---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, date, leap-year, julian-day, calendar]
note_type: pattern

---

# Leap Years and Julian Days in DAX

Handling leap year logic and converting dates to Julian Day Numbers.

## Leap Year Check

```dax
Is Leap Year :=
VAR __Year = YEAR( [Date] )
RETURN
OR(
    AND( MOD( __Year, 4 ) = 0, MOD( __Year, 100 ) <> 0 ),
    MOD( __Year, 400 ) = 0
)
```

## Julian Day Number

```dax
Julian Day :=
VAR __Y = YEAR( [Date] )
VAR __M = MONTH( [Date] )
VAR __D = DAY( [Date] )
RETURN
__D - 32075
    + 1461 * ( __Y + 4800 + ( __M - 14 ) / 12 ) / 4
    + 367 * ( __M - 2 - 12 * ( ( __M - 14 ) / 12 ) ) / 12
    - 3 * ( ( __Y + 4900 + ( __M - 14 ) / 12 ) / 100 ) / 4
```

## Notes

- Julian Day Number is the number of days since Jan 1, 4713 BC
- Useful for astronomical calculations and date arithmetic

## Related

- [[date-table-creation-in-dax]]
- [[time-tables-in-dax]]
