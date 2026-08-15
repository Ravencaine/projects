---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: pattern
tags: [power-bi, field-parameters, kpi, hierarchy, slicers]
related:
  - "[[Field-Parameters-Show-Values]]"
---

# Field Parameters KPI Hierarchy

Group Field Parameters measures into named hierarchies (e.g., Sales, Earnings) by adding extra columns to the generated Field Parameters table.

## Purpose

Field Parameters let users select which measure to display in a visual, but all measures appear as a flat list. This pattern creates folder-like grouping by adding a Tag/Group column to the Field Parameters table, enabling collapsible or labelled groupings in the slicer.

## Components

1. **Field Parameters table:** created via Modeling tab → New Parameter → Fields
2. **KPI column:** the generated column holding measure names (standard Field Parameter behaviour)
3. **Tag column:** user-added column that groups measures into categories
4. **Order column:** existing column that controls sort order
5. **Slicer:** configured with Tag at the top level, KPI as the child

## Structure

### Step 1 — Create Field Parameters

```
Modeling tab → New Parameter → Fields
Name: KPI
Measures: Total Sales, Pseudo Sales Commissions, More Commission
→ Add slicer to page → Create
```

### Step 2 — Edit the Field Parameters Table

Open the Field Parameters table in Data view. By default it has three columns:

| KPI | KPI Fields | KPI Order |
|-----|-----------|-----------|

Add a fourth column, `KPI Tag`:

| KPI | KPI Fields | KPI Order | KPI Tag |
|-----|-----------|-----------|---------|

Fill in tag values:

| KPI | KPI Fields | KPI Order | KPI Tag |
|-----|-----------|-----------|---------|
| Total Sales | [Total Sales] | 1 | Sales |
| Pseudo Sales Commissions | [Pseudo Sales Commissions] | 2 | Sales |
| More Commission | [More Commission] | 3 | Earnings |

### Step 3 — Configure Slicer Hierarchy

1. In the slicer, drag `KPI Tag` above `KPI Fields`
2. The slicer now displays:

```
▼ Earnings
    More Commission
    Pseudo Sales Commissions
▼ Sales
    Total Sales
```

## Example

- **Sales group:** Total Sales
- **Earnings group:** Pseudo Sales Commissions, More Commission
- Users see organized folders in the slicer; selecting a measure updates the visual

## Variations

- **Multi-level hierarchy:** Add more than one tag column for sub-grouping
- **Icons:** Use emoji in tag values for visual differentiation in the slicer
- **Dynamic grouping:** Derive tag values from a measure or calculation for dynamic categorization

## Related

- [[Field-Parameters-Show-Values]] — sibling pattern using the same Field Parameters table
