---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: atomic
tags: [dax, fundamentals]
---

# DAX Overview

Data Analysis Expressions (DAX) is a formula expression language for Power BI, Analysis Services, and Power Pivot in Excel data models.

## Definition

DAX formulas include functions, operators, and values to perform advanced calculations and queries on related tables and columns in tabular data models.

## Key Points

- DAX formulas are used in **measures**, **calculated columns**, **calculated tables**, and **row-level security**
- DAX always references a **complete column or table**: never individual cells or ranges
- DAX can return either a **scalar value** or a **table**
- Unlike Excel, DAX has **no named ranges** and requires fully qualified references
- DAX is based on SQL Server Analysis Services — behaviour may differ from Excel in edge cases
- DAX is constantly improved: new functions released monthly with Power BI service updates

## Context

DAX evaluates in one of two contexts:
- **Row context**: current row (in calculated columns or iterators like SUMX)
- **Filter context**: the set of rows visible due to report filters, slicers, and relationships
- **Query context**: the subset implicitly retrieved for a formula based on the full filter context

Understanding context is critical to writing correct and performant DAX.

## Formulas

DAX formulas must begin with `=` and can nest up to **64 levels** of functions in calculated columns. Measures use the name-first syntax: `Total Sales := SUM(Sales[Amount])`.

## Related

- [[dax-data-types]] — atomic
- [[dax-context]] — atomic
- [[measures-vs-calculated-columns]] — atomic
- [[calculate]] — function
