---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-query, pattern, etl, data-preparation, retail]
---

# Retail Power Query Data Preparation

A structured ETL pipeline in Power Query that cleans and transforms raw retail transaction data before it reaches the data model — covering deduplication, type correction, calculated columns, and dimension normalization.

## Purpose

Ensures the data feeding the Power BI model is accurate, consistent, and optimized. Poor quality data at this stage produces misleading dashboards regardless of how well the DAX or visuals are built.

## Steps

1. **Connect** to the source (Excel, CSV, SQL database, etc.)
2. **Remove duplicates:** use Remove Rows → Remove Duplicates on Order ID + Line Item
3. **Handle missing values:** replace nulls in critical columns (Customer Name, Order Date, Sales, Profit) or filter out incomplete rows
4. **Standardize text:** TRIM and UPPER/LOWER on Product Name, Category, Region, State to eliminate casing inconsistencies
5. **Correct regional data:** map inconsistent state/region names (e.g., "Calif." → "California") using a mapping table or Replace Values
6. **Format dates:** ensure Order Date is a proper Date type, not text
7. **Create calculated columns**:
   - `Year = Date.Year([Order Date])`
   - `Month = Date.Month([Order Date])`
   - `Quarter = "Q" & Number.ToText(Date.QuarterOfYear([Order Date]))`
   - `Week = Date.WeekOfYear([Order Date])`
8. **Establish relationships:** in the data model view, link fact table to dimension tables (DimDate, DimGeography, DimProduct, DimCustomer)
9. **Set data types:** mark Sales and Profit as Decimal Number, Order Date as Date, Quantity as Whole Number
10. **Disable load** for intermediate/navigation step queries

## M Code Example

```m
// Year column
Table.AddColumn(Source, "Year", each Date.Year([Order Date]), Int64.Type)

// Quarter column
Table.AddColumn(AddedYear, "Quarter", each "Q" & Number.ToText(Date.QuarterOfYear([Order Date])), type text)

// Remove duplicates on Order ID
Table.Distinct(Source, {"Order ID"})
```

## Variations

- **Large datasets**: use SQL to pre-aggregate in the source database before loading — reduces refresh time
- **Multiple sources**: use a Union query or Append to combine data from different regions or systems before transformation

## Related

- [[calendar-table-time-intelligence]] — `pattern`
- [[power-query-etl-workflow]] — `pattern`
