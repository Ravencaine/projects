---
created: 2026-08-13
source: 5 Mistakes in Power BI Data Modeling (And How to Fix Them)
note_type: pattern
tags: [power-bi, data-modeling, date-table, time-intelligence, beginner, dimension-table]
---

# Data Modeling Mistake: No Dedicated Date Table

<!-- Using raw date columns instead of a dedicated Date dimension limits time intelligence functions and breaks fiscal period analysis. Every Power BI model needs a proper date table. -->

## The Mistake

Relying on the raw date column from the fact table (e.g., `Sales[OrderDate]`) instead of a separate Date dimension.

```
❌ Raw date column: Sales[OrderDate] = "2026-05-14"
   → Just a date value, no hierarchy, no fiscal periods
   → No YTD, MTD, PY comparison possible via time intelligence
   → Visual axis shows individual dates instead of months/quarters
```

## What a Date Table Provides

A proper date dimension enables:

| Feature | Without Date Table | With Date Table |
|---------|-------------------|-----------------|
| YTD / MTD / QTD | Manual workaround | `TOTALYTD()`, `TOTALMTD()` |
| Same Period Last Year | Complex manual logic | `SAMEPERIODLASTYEAR()` |
| Fiscal Year reporting | Hard-coded month numbers | `FiscalYear`, `FiscalQuarter` columns |
| Month/Quarter hierarchy | Individual dates in axis | `Year → Quarter → Month → Day` |
| Working days / holidays | Not possible | `IsWorkingDay`, `HolidayName` |

## The Fix Pattern

### Step 1 — Create a Dedicated Date Table

```dax
DateTable =
CALENDAR(
    DATE(2020, 1, 1),
    DATE(2030, 12, 31)
)
```

Or via Power Query (M code) for more control — see [[dax-date-table-build]].

### Step 2 — Mark It as a Date Table

```
Model View → Select DateTable[Date] → Table Properties → Mark as date table
```

### Step 3 — Build the Attribute Columns

```dax
DateTable[Year]        = YEAR(DateTable[Date])
DateTable[Quarter]     = "Q" & FORMAT(DateTable[Date], "Q")
DateTable[Month]       = FORMAT(DateTable[Date], "MMMM")
DateTable[Month Number]= MONTH(DateTable[Date])
DateTable[Day of Week] = FORMAT(DateTable[Date], "DDDD")
DateTable[Fiscal Year] = IF(MONTH(DateTable[Date]) >= 7,
                           YEAR(DateTable[Date]) + 1,
                           YEAR(DateTable[Date]))
```

### Step 4 — Connect to Fact Table

```
DimDate[DateKey] ──→ FactSales[OrderDate]
```

## The Hierarchy Pattern

```
Date[Year]
    └── Date[Quarter]
        └── Date[Month]
            └── Date[Date]
```

Set this hierarchy in the field list so visuals automatically roll up correctly.

## Role-Playing Dates

If the fact has multiple date columns (OrderDate, ShipDate, DueDate), see [[role-playing-date-calculated-columns]] for handling multiple inactive relationships.

## Related

- [[dax-date-table-build]] — DAX Code: CALENDAR / CALENDARAUTO patterns
- [[date-table-as-backbone]] — Data Modeling: date table as the model spine
- [[date-table-post-creation-checklist]] — Data Modeling: validation after creation
- [[role-playing-date-calculated-columns]] — Data Modeling: multiple date roles on one fact
- [[creating-date-table-power-bi-source]] — Power BI: source reference
