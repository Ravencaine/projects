---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [dax, pattern, year-over-year, calculate, time-intelligence]
---

# DAX Year-over-Year: CALCULATE + LEFT + Calculated Field Composition

A three-step pattern for building year-over-year growth calculations in DAX using CALCULATE to filter by year and calculated field chaining.

## Purpose

Year-over-year (YoY) analysis compares a metric for the current period against the same period in the prior year. In DAX, this is achieved by (1) building a base measure, (2) using CALCULATE to create period-specific copies of that measure, and (3) composing them in a growth formula.

## Components

- Base measure: `SUM()` of a fact table column
- Period filter: `LEFT()` to extract year from a text-based DateKey
- Filter modifier: `CALCULATE()`
- Calculated field reference: `[MeasureName]` in square brackets

## Structure

```dax
-- Step 1: Base measure — total sales
StoreSales := CALCULATE(
    SUM(dbo_FactSales[TotalSales]),
    dbo_DimChannel[ChannelName] = "Store"
)

-- Step 2: Period-specific measures using CALCULATE + LEFT
StoreSales2009 := CALCULATE(
    [StoreSales],
    LEFT(dbo_DimDate[Datekey], 4) = "2009"
)

StoreSales2008 := CALCULATE(
    [StoreSales],
    LEFT(dbo_DimDate[Datekey], 4) = "2008"
)

-- Step 3: Growth calculation — reference other calculated fields
SalesChange := ([StoreSales2009] - [StoreSales2008]) / [StoreSales2008]
```

## Example

The Contoso PowerPivot example in Ch7:
1. `StoreSales` sums TotalSales where ChannelName = "Store"
2. `StoreSales2009` adds a filter: LEFT(Datekey, 4) = "2009"
3. `StoreSales2008` adds a filter: LEFT(Datekey, 4) = "2008"
4. `SalesChange` computes the percentage change — the result was a -12% decline in 2009 store sales

## Variations

- **Date table with proper date type:** If DateKey is a real DATE column, use `YEAR([DateKey]) = 2009` instead of LEFT
- **Multiple periods:** Add `Q1Sales`, `Q2Sales` measures using `MONTH()` or `QUARTER()` in the filter
- **Chained on top of CALCULATE:** YoY can be built entirely within one CALCULATE using `DATESYTD()` or `SAMEPERIODLASTYEAR()` — more idiomatic modern DAX

## Notes

- The `:=` syntax (label:) defines the calculated field identifier
- Calculated fields can reference other calculated fields defined earlier in the calculation area
- Format `SalesChange` as Percentage after creating it

## Related

- [[dax-calculate-function]] — the core filter-context function
- [[dax-left-function]] — text extraction for year filtering
- [[dax-operators]] — arithmetic operators for the growth formula
- [[dax-kpi-create-key-performance-indicator]] — adding a KPI layer on top of YoY metrics
