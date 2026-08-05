---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [qa-visual, best-practices, synonyms, relationships, data-model]
---

# Q&A Best Practices — Preparing Your Data Model

The single biggest factor in Q&A accuracy is the data model. Human-readable names, good relationships, and explicit synonyms make Q&A reliable.

## Purpose

Q&A is only as good as the data model it sits on. A poorly structured model will produce unreliable answers.

## Components

### 1. Human-Readable Column Names

Rename columns to match how users think:

| Technical name | Human-readable name |
|---------------|-------------------|
| `SUM_FactSales_SalesAmount` | Total Sales |
| `D_Product_ProdSubCat_Lkup` | Product Subcategory |
| `FK_Customer_Dim` | Customer |

### 2. Define Relationships

- Q&A follows model relationships to navigate between tables
- Ensure relationships are correctly set (1-to-many, cross-filter direction)
- Name relationships descriptively if using bidirectional cross-filtering

### 3. Add Synonyms

Open Q&A Setup → Synonyms tab:
- Add all business terms for each column (e.g., "revenue", "sales", "turnover" → TotalSalesAmount)
- Add exclusions for ambiguous terms ("Sales" can mean units or revenue — exclude where inappropriate)

### 4. Set Up Question Suggestions

Pre-populate the visual with 3–5 suggested questions users are most likely to ask. These appear when the user clicks the question box.

### 5. Configure Field Types

Mark columns as: Date, Numeric, Text, Geographic — this helps Q&A interpret the question correctly.

## Related

- [[qa-field-synonyms]]
- [[qa-underline-states]]
- [[semantic-matching-qa-visual]]
