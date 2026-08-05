---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, dashboard, workflow, development]
---

# Power BI Dashboard Development Workflow

A structured end-to-end process for building an executive retail sales dashboard — from source data to published report.

## Purpose

Provides a repeatable, quality-controlled workflow for dashboard development that ensures nothing is skipped and the final output is credible and maintainable.

## Steps

### 1. Requirements gathering

Identify the business questions the dashboard must answer. For a retail executive dashboard:
- What KPIs are most critical? (Total Sales, Profit, Orders, AOV)
- Who is the audience? (C-suite, regional managers, category owners)
- What time period should be shown? (current year, last 12 months, YoY)
- What filters do users need? (Region, Category, Segment, Date)

### 2. Data acquisition and review

- Obtain the source dataset or database connection
- Review columns, data types, row counts, and sample values
- Identify quality issues (duplicates, nulls, inconsistent naming) — document them

### 3. Data preparation (Power Query)

Follow the [[retail-power-query-data-preparation]] pattern:
- Clean and standardize
- Create calculated date columns
- Build the Calendar table
- Set data types
- Create dimension tables

### 4. Data modeling

- Create a star schema: one fact table (Sales), dimension tables (DimDate, DimGeography, DimProduct, DimCustomer)
- Set relationships with single-directional filters from dimensions to fact
- Mark the Calendar table as a Date Table
- Avoid bidirectional cross-filtering unless required by the model

### 5. DAX measure development

Create core measures first:
- `Total Sales`, `Total Profit`, `Total Orders`, `Average Order Value`
- `Profit Margin`, `YoY Change`, `Sales vs Target`
- Additional measures as required by the design

### 6. Visual design

Assemble the report page in order:
1. Slicers along the top or left side
2. KPI cards row below slicers
3. Sales trend chart occupying the upper centre
4. Category comparison chart lower left
5. Geographic analysis lower right
6. Supporting visuals (top products, customer segments, shipping) in remaining space

### 7. Validation

- Cross-check totals in the dashboard against source data
- Verify filters cascade correctly through all visuals
- Confirm date hierarchy drill-down works
- Test on different screen sizes (phone/tablet layout)

### 8. Publish and share

- Publish to a Power BI Workspace
- Configure scheduled refresh (gateway if on-premises data)
- Set up row-level security if different users should see different regions
- Share via app or direct access

## Related

- [[executive-kpi-card-row]] — `pattern`
- [[sales-trend-line-chart]] — `pattern`
- [[interactive-slicer-configuration]] — `pattern`
- [[calendar-table-time-intelligence]] — `pattern`
- [[retail-power-query-data-preparation]] — `pattern`
