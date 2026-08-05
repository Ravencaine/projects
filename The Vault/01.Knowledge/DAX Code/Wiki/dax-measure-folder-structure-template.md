---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: reference
tags: [dax, measure-library, folder-structure, organization, business-domain, template]
---

# DAX Measure Folder Structure Template

The canonical folder structure for organizing a shared DAX measure library by business function and calculation type.

## Purpose

Organizes measures visually so analysts can find them by browsing. Complements naming conventions (searchability) with spatial organization (browsability).

## The Standard Template

```
📁 _Base Measures
   📁 Sales
      - _Sales Amount
      - _Sales Quantity
      - _Sales Cost
   📁 Customer
      - _Customer Count
      - _Active Customers
      - _New Customers
   📁 Product
      - _Product Count
      - _Product Categories
   📁 Date
      - _Current Date
      - _Fiscal Year Start
📁 Time Intelligence
   📁 Sales
      - Sales LY
      - Sales YTD
      - Sales MTD
      - Sales QTD
   📁 Customer
      - Customers LY
      - Customer Growth YoY
📁 Comparisons & Variance
   📁 Sales
      - Sales vs LY
      - Sales vs LY %
      - Sales vs Target
      - Sales vs Target %
📁 KPIs & Metrics
   📁 Customer
      - Customer Lifetime Value
      - Customer Acquisition Cost
      - Customer Retention Rate
   📁 Sales
      - Revenue per Customer
      - Average Order Value
      - Conversion Rate
📁 Utilities
   - Selected Period Text
   - Has Data
   - Row Count
📁 Formatting
   - Format Percentage
   - Format Currency
   - Format Variance
📁 _Exploration
   📁 [AnalystName]_[Project]
      - #Test Metric
      - #Cohort Analysis v1
```

## Why Each Folder Exists

| Folder | Purpose |
|--------|---------|
| `_Base Measures` | Building-block measures prefixed with `_`. Internal use only — not exposed directly to business users |
| `Time Intelligence` | All period-over-period measures (LY, YTD, MTD, QTD, YoY%). Scattered = chaos |
| `Comparisons & Variance` | Variance, %, difference measures |
| `KPIs & Metrics` | Business-level composite metrics — the "answer" measures |
| `Utilities` | Helper measures that support other measures but aren't business metrics |
| `Formatting` | Display formatting measures |
| `_Exploration` | Temporary space for experimentation. Not shared until promoted |

## Folder Naming Rules

1. **Base measures ALWAYS start with underscore**: signals "building block, not final metric"
2. **Maximum 3 levels of folders**: if you need more, refactor the categories
3. **Folders use business language, not technical terms**: `Sales` not `Fact_Sales`
4. **Utilities and Formatting get their own folders**: they're infrastructure, not business metrics
5. **Time Intelligence gets a dedicated folder**: it's a calculation type, not a business function

## Starting Point (Minimum Viable)

Start with 3–5 business domain folders. Expand when a category reaches 10+ measures:

```
📁 _Base Measures
   📁 [Domain 1]
   📁 [Domain 2]
   📁 Date
📁 Time Intelligence
📁 KPIs & Metrics
📁 Utilities
📁 _Exploration
```

## The Progressive Folder Structure

Start minimal. Add folders as the model grows:

| Model Size | Folder Depth |
|------------|-------------|
| 20–50 measures | 2 levels (Category → Measure) |
| 50–150 measures | 3 levels (Category → Domain → Measure) |
| 150+ measures | Consider splitting into multiple model partitions |

## Why Folders Match Business Language

Business users should understand the organization without a data dictionary. `Sales`, `Customer`, `Product` are self-explanatory. `Fact_Sales`, `Dim_Customer` require training.

## Related

- [[implement-dax-measure-library-architecture]] — implementation workflow
- [[dax-measure-naming-convention-framework]] — naming conventions
- [[measure-governance-process]] — governance
