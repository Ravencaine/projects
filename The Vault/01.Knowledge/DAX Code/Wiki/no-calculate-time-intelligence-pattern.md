---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, time-intelligence, no-calculate]
note_type: pattern

---

# No CALCULATE Time Intelligence Pattern

Performing period-over-period calculations without CALCULATE or DAX time intelligence functions.

## Purpose

DAX time intelligence functions (DATESYTD, SAMEPERIODLASTYEAR, PARALLELPERIOD, etc.) are notoriously problematic — they require a contiguous date table and have subtle edge cases. The No CALCULATE approach replaces them with explicit date offsets.

## Core Principle

Rather than relying on function-specific logic, use `DATEADD()` with explicit offsets to shift the date context:

```dax
-- Current period sales
Sales := SUM( 'Sales'[Amount] )

-- Previous period using offset
Sales Previous Period :=
VAR __CurrentDate = MAX( 'Dates'[Date] )
VAR __PrevDate = DATEADD( ALL( 'Dates'[Date] ), -1, MONTH )
VAR __Sales = SUM( 'Sales'[Amount] )
VAR __PrevSales =
    CALCULATE(
        SUM( 'Sales'[Amount] ),
        'Dates'[Date] = __PrevDate
    )
RETURN
__PrevSales
```

## No CALCULATE Version

```dax
Sales Previous Period No CALC :=
VAR __Table =
    FILTER(
        ALL( 'Dates'[Date] ),
        'Dates'[Date] < MAX( 'Dates'[Date] )
    )
RETURN
SUMX(
    __Table,
    [Sales Amount]
)
```

## Why Avoid DAX Time Intelligence Functions

- They fail silently when the date table is not contiguous
- They behave differently in DirectQuery vs Import mode
- Their filter context requirements are opaque
- Explicit offsets are more predictable and debuggable

## Related

- [[no-calculate-dax-pattern]]
- [[offset-based-date-calculations]]
- [[date-table-creation-in-dax]]
- [[rolling-periods-in-dax]]
