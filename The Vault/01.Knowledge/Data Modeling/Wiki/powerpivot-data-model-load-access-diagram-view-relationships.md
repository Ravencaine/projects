---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [powerpivot, data-model, relationship, diagram-view, power-query]
---

# PowerPivot Data Model: Load from Access, Diagram View, Relationships

A step-by-step pattern for loading multiple related tables into PowerPivot, inspecting the auto-detected relationship graph, and creating Pivot Tables from two or more related tables.

## Purpose

PowerPivot lets you load data from external databases (Access, SQL Server, Azure) and automatically imports any relationships defined in the source. The Diagram View then shows the star schema visually, and Pivot Tables can span multiple tables via the relationship chain.

## Components

- PowerPivot for Excel add-in (included in Excel 2013 Standard and above)
- External database with pre-existing relationships (Access, SQL, etc.)
- PowerPivot Table Import Wizard

## Structure

```
1. Get External Data → From Database → From Access
2. Browse → select .accdb/.mdb file → Test Connection → Next
3. Choose "Select from a list of tables and views" → select all tables
4. Finish → relationships auto-imported
5. Open PowerPivot Diagram View → inspect relationships
6. Pivot Table → drag fields from multiple related tables
```

## Steps

1. **Open PowerPivot:** PowerPivot tab → Manage
2. **Import from Access:**
   - Get External Data → From Database → From Access
   - Browse → select the Access .accdb file → Test Connection → Next
   - Choose "Select from a list of tables and views"
   - Click the top-left checkbox to select all tables → Finish
   - Wait for import (Northwind with 9 employees, 48 orders → 432 rows if no join specified)
3. **Inspect in Diagram View:**
   - PowerPivot ribbon → Diagram View
   - Tables appear as nodes; relationship arrows show foreign-key links
   - Note: arrows are directional — the direction matters for filtering context
4. **Check Relationships (tabular view):**
   - Minimize PowerPivot window → Data tab → Relationships
   - Shows the actual field names in each relationship (more precise than Diagram View arrows)
5. **Create Pivot Table from Multiple Tables:**
   - PowerPivot tab → Manage → return to Data View if in Diagram View
   - Click Pivot Table → New Worksheet
   - In the PivotTable Fields pane: click the right-arrow next to each table to expand
   - Drag dimension fields (e.g., `ProductName`) from dimension tables to Rows
   - Drag measure fields (e.g., `OnHand`) from fact tables to Values
   - PowerPivot automatically traverses the relationship chain

## Notes

- PowerPivot tables are read-only after import — reimport to update data
- If a relationship is missing, click Manage Relationships on the Design tab
- The Contoso sample (Tinyurl.com/PowerPivotSamples) is the canonical source for exercises
- Diagram View arrows are approximate — always verify relationship field names via the tabular Relationships view

## Related

- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — the conceptual model that the diagram visualizes
- [[dax-calculate-function]] — filtering over imported relationships
- [[sql-equijoin-vs-cartesian-product]] — the SQL JOIN concept underlying PowerPivot relationships
