---
created: 2026-07-27
updated: 2026-08-02
source: "Is Your Power BI Slow? 10 Ways to Optimize Your Data Model"
note_type: pattern
tags: [power-bi, performance, optimization, data-model, aggregations]
---

# Power BI Performance Optimization Pattern

A structured approach to diagnosing and fixing slow Power BI reports, organized by impact level.

## Quick Wins (High Impact, Low Effort)

### 1. Remove Unused Columns and Tables

- Open Performance Analyzer in Power BI Desktop
- Run each visual and note slow queries
- Remove any columns/tables not contributing to slow queries from the model

### 2. Set Data Types Correctly

- Text instead of Date = string comparison instead of date arithmetic
- Whole number columns stored as Decimal = unnecessary conversion
- Verify all columns: right-click column > **Change Type**

### 3. Reduce Cardinality on Large Dimensions

- High-cardinality columns (unique IDs, free-text) should be hidden or removed
- DimDate: use integer date keys instead of full date strings where possible
- DimCustomer: avoid using email or address columns as filters

## Medium Effort

### 4. Configure Aggregations

- For large fact tables (10M+ rows): create an aggregation table at a higher granularity
- Power BI can automatically use the aggregation instead of the full table
- Configure: right-click table > **Aggregations** > set granularity

### 5. Use USERELATIONSHIP for Role-Playing Dimensions

- Do NOT duplicate Date tables for Invoice Date, Ship Date, Due Date
- Create one Date table with inactive relationships; use USERELATIONSHIP in DAX

### 6. Disable Bidirectional Cross-Filtering Globally

- Bidirectional cross-filtering causes each filter to propagate in both directions
- Enable it only on specific relationships where required (and measure the impact)

## High Effort

### 7. Materialize Calculations in the Source

- Calculated columns in Power BI are evaluated at refresh time — not at query time
- If a column is used in aggregations or joins, compute it in SQL/Power Query instead

### 8. Create Summary Tables

- For common aggregations (monthly sales by product): create a pre-aggregated table
- Reduces the query workload for frequently-used calculations

### 9. Reduce Active Relationships

- Only one active relationship per table pair
- Multiple inactive relationships are fine but require USERELATIONSHIP in DAX

### 10. Optimize Power BI Service Refresh

- Schedule dataset refresh during off-peak hours
- Use Incremental Refresh for large datasets (new in Power BI)

## Performance Checklist

- [ ] All measures <500ms (verify with Performance Analyzer)
- [ ] No bidirectional cross-filtering globally
- [ ] Aggregations configured for tables >1M rows
- [ ] Data types verified for all columns
- [ ] Unused tables/columns removed

## Related

- [[dax-performance-5000-measures-source]] — DAX-level performance patterns
- [[power-bi-dashboard-checklist]]
