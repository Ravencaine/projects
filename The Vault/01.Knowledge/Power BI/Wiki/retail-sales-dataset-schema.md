---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: reference
tags: [power-bi, reference, schema, retail, dataset]
---

# Retail Sales Dataset Schema

Canonical column inventory for a retail sales fact table and its dimension tables, derived from the Executive Retail Sales Dashboard source.

## Fact Table: Sales

| Column | Type | Description |
|--------|------|-------------|
| Order ID | Text | Unique order identifier |
| Order Date | Date | Date the order was placed |
| Customer Name | Text | Name of the customer |
| Customer Segment | Text | Consumer / Corporate / Home Office |
| Product Name | Text | Full product name/SKU description |
| Product Category | Text | Top-level category (Technology, Furniture, Office Supplies) |
| Sub-Category | Text | Second-level category under Product Category |
| Sales | Decimal | Total sales amount for the line item |
| Quantity | Integer | Number of units ordered |
| Profit | Decimal | Profit for the line item (Sales - COGS - Discount) |
| Discount | Decimal | Discount applied to the line item |
| Region | Text | Geographic region |
| State | Text | State within the region |
| City | Text | City within the state |
| Shipping Mode | Text | Standard / Second Class / First Class / Same Day |

## Dimension Tables

### DimCustomer

| Column | Type |
|--------|------|
| Customer Name | Text (PK) |
| Customer Segment | Text |
| City | Text |
| State | Text |
| Region | Text |

### DimProduct

| Column | Type |
|--------|------|
| Product Name | Text (PK) |
| Product Category | Text |
| Sub-Category | Text |

### DimDate (Calendar)

| Column | Type |
|--------|------|
| Date | Date (PK) |
| Year | Integer |
| Quarter | Text (Q1–Q4) |
| Month | Text |
| Month Number | Integer |
| Week of Year | Integer |
| Day of Week | Text |

### DimGeography

| Column | Type |
|--------|------|
| City | Text (PK) |
| State | Text |
| Region | Text |
| Country | Text |

## Notes

- Order ID + Line Item Number may be needed as a composite key for fact rows if one order has multiple line items.
- Discount and Profit are derived columns — verify their calculation logic with the data source owner before using them in the model.
- Shipping Mode can be a separate dimension or a column on the fact table.

## Related

- [[retail-power-query-data-preparation]] — `pattern`
- [[power-bi-dashboard-development-workflow]] — `pattern`
