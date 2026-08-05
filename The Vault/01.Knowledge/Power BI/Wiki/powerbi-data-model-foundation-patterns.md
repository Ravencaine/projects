---
created: 2026-08-01
updated: 2026-08-02
source: "We Replaced 47 Excel Files With One Power BI Model. Here's What Actually Happened.md"
note_type: atomic
tags: [power-bi, data-model, star-schema, ETL, incremental-refresh, data-dictionary]
---

# Power BI Data Model Foundation Patterns

## Star Schema Design

### Fact Tables
- **FactSales:** Every sales transaction (grain = one row per sale)
- **FactInventory:** Daily inventory snapshots
- **FactFinancials:** Monthly financial entries

### Dimension Tables
- **DimDate:** Every day 2020–2030 (continuous calendar)
- **DimProduct:** All products
- **DimCustomer:** All customers
- **DimEmployee:** All employees
- **DimRegion:** All regions/territories
- **DimAccount:** Chart of accounts (for finance)

Rule: One central Date dimension. Relate all fact tables to it (InvoiceDate, ShipDate, DueDate → DimDate).

## ETL Process (Extract, Transform, Load)

### Extract
- ERP sales transactions: every hour
- Warehouse inventory levels: every 4 hours
- Financial data: nightly

### Transform
- **Standardize names:** "Widget A" vs "WidgetA" vs "WIDGET-A" → one canonical form
- **Validate dates:** catch future dates, nulls, invalid formats
- **Calculate derived fields:** profit margin, days in inventory, etc.
- **Flag anomalies:** sales over $100K, negative inventory, zero-quantity orders

### Load
- Append to fact tables (incremental load)
- Update dimension tables (Slowly Changing Dimensions — SCD Type 2 for historical changes)
- Log every load with timestamp and row count

## Incremental Refresh Strategy

Critical for large datasets (14M rows in this case):

| Data Age | Refresh Strategy |
|----------|-----------------|
| > 2 years (historical) | Load once, never refresh |
| Last 2 years | Refresh nightly |
| Current month | Refresh every hour |

**Result:** Load time 3 hours → 12 minutes.

## Validation Layer Before Load

SQL checks before data enters the warehouse:

```sql
-- Check 1: Row count shouldn't drop more than 10%
IF @TodayCount < (@YesterdayCount * 0.9)
    RAISERROR('Row count dropped 10%+. Check source.', 16, 1)

-- Check 2: No future dates
IF EXISTS (SELECT 1 FROM TodaysLoad WHERE OrderDate > GETDATE())
    RAISERROR('Future dates found in OrderDate.', 16, 1)

-- Check 3: Sales total within expected range (3x flag)
IF @TodayTotal > (@HistoricalAvg * 3)
    RAISERROR('Total sales 3x higher than historical avg.', 10, 1)
```

6 data quality issues caught in first month using these checks.

## Data Dictionary (Document Everything)

### Table documentation
- Business purpose
- Refresh frequency
- Data source
- Key fields
- **Grain** (what does one row represent?)
- Example queries

### Field documentation
- Business definition
- Data type
- Source system + field
- Calculation logic (if derived)
- Business rules

**Why it matters:** New analyst (Jordan) given data dictionary → built correct customer retention analysis in 2 hours, no help needed.

## Commission Calculation in DAX (Real-World Example)

```c
Commission =
VAR BaseTier =
    SWITCH(
        TRUE(),
        [YTD Sales] < 500000,  0.08,
        [YTD Sales] < 1000000, 0.10,
        [YTD Sales] >= 1000000, 0.12,
        0.08
    )
VAR Accelerator =
    IF([YTD Sales] > 1000000, 0.02, 0)
VAR SpecialDealBonus =
    CALCULATE(
        SUM(Deals[BonusAmount]),
        Deals[SpecialCommission] = TRUE
    )
VAR TotalRate = BaseTier + Accelerator
VAR Commission = ([Monthly Sales] * TotalRate) + SpecialDealBonus
RETURN Commission
```

Plus a manual adjustments table (documented with reason + approver).

Match rate vs. Excel: 98.7%. The 1.3% discrepancies were Excel errors (rounding + missed deals).

## Performance Optimization

When a report took 45 seconds to load:

- Removed unnecessary columns from data model
- Created aggregated tables for summary views
- Implemented incremental refresh
- Added query folding (push filters to source)

**Result:** 45 seconds → 3.2 seconds.
