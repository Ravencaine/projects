---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, date-table, calendar, fiscal, power-bi, data-modeling]
---

# AutoDateTable — Calendar Table Generator

Builds a complete Date table with standard and fiscal columns in one call. Drop-in across PBIX files for consistent date intelligence.

## Signature

```c
UDF AutoDateTable =
    ( startDate : DATETIME,
      endDate   : DATETIME,
      fiscalStartMonth : INT64   // 1..12
    ) => ...
```

## Columns Generated

| Column | Description |
|--------|-------------|
| `Date` | Calendar dates (via `CALENDAR`) |
| `DateKey` | `YYYYMMDD` integer key |
| `Year` | Calendar year |
| `MonthNo` | Month number 1–12 |
| `Month` | Short month name (MMM) |
| `Quarter` | Q1–Q4 |
| `StartOfMonth` | First day of month |
| `EndOfMonth` | Last day of month |
| `WeekNoMon` | Week number (Monday-based) |
| `YearMonth` | `YYYY-MM` string |
| `FiscalYear` | Fiscal year (shifted by `fiscalStartMonth`) |
| `FiscalMonthNo` | Fiscal month 1–12 |
| `FiscalQuarter` | Fiscal Q1–Q4 |
| `IsToday` | Boolean flag for today |
| `IsCurrentMonth` | Boolean flag for current month |

## Usage

```c
Date =
AutoDateTable(
    DATE(YEAR(MIN(Sales[Date]))-1, 1, 1),
    EOMONTH(MAX(Sales[Date]), 0),
    1   // fiscal year starts January
)
```

After creation: **Table tools → Mark as date table → Date[Date]**.

## Fiscal Logic

Fiscal year rolls forward when `MONTH(date) >= fiscalStartMonth`:

```
FiscalYear = YEAR(date) + IF(MONTH(date) >= fiscalStartMonth, 1, 0)
FiscalMonthNo = MOD(MONTH(date) - fiscalStartMonth + 12, 12) + 1
```

## Config

`// 🔧 CONFIG` — change `fiscalStartMonth` (e.g., `7` for July FY) and date range logic.

## Related

- [[date-table-creation-in-dax]]
