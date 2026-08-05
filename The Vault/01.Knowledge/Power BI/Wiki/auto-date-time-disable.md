---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, date, performance, intermediate, best-practice]
---

# Auto Date/Time: Disable It, Build One DimDate

Power BI silently creates a hidden date table for every date column in your model. Turn this off and build one shared date dimension.

## The Problem with Auto Date/Time

On a model with 12 date columns, Power BI creates 12 invisible date tables — each adding overhead to refresh and memory. Hidden, undocumented, and unnecessary.

## How to Disable It

**File → Options → Data Load** → uncheck **Auto Date/Time**

Do this in every production model. Microsoft recommends it.

## The Replacement: One Shared DimDate

```dax
DimDate =
ADDCOLUMNS (
    CALENDAR ( DATE ( 2022, 1, 1 ), DATE ( 2026, 12, 31 ) ),
    "Year",        YEAR ( [Date] ),
    "Month",       FORMAT ( [Date], "MMM" ),
    "MonthNumber", MONTH ( [Date] ),
    "Quarter",     "Q" & QUARTER ( [Date] ),
    "YearMonth",   FORMAT ( [Date], "YYYY-MM" )
)
```

Mark as Date Table: Table Tools → Mark as Date Table → select the Date column.

## DateTime Columns: Split Instead of Keep

Full DateTime accurate to the millisecond = thousands of unique values per day. Wrecks compression.

**Split into:**
- `Date` column → date only (lower cardinality, compresses well)
- `Time` column → time only (only if genuinely needed for analysis)

If the original DateTime is needed for precise timestamps, keep it. If you only report by day, keep only the date.

## Related

- [[vertipaq-column-cardinality]] — DateTime split as a cardinality reduction case
- [[role-playing-date-calculated-columns]] — handling multiple date columns (OrderDate, ShipDate)
- [[ecommerce-model-step-by-step]] — DimDate built as part of the e-commerce model
