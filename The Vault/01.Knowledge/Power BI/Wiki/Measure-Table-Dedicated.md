---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-bi, measure, data-modeling, organization, best-practice]
---

# Measure Table: Dedicated

Create a dedicated single-column table to hold all measures in one organized location.

## Definition

Rather than scattering measures across fact and dimension tables, create a single dummy table (one column, one row, data type Integer) as a container for all measures. This gives you one place to find and manage every measure, and enables display folders for further grouping.

## Key Points

- Create via Modeling → New Table: `Measures = DATATABLE("Col", INTEGER, {{1}})`
- Set the column to Integer (not hidden by default) — the single row value is irrelevant
- Move all measures into the table in Model View
- Does **not** improve model performance — purely organizational
- Display folders (inside the measure table) can further group by category: Revenue, Occupancy, etc.
- Some developers prefer keeping measures inside their related fact table — both approaches are valid
- A clean model is easier to maintain, especially as measure count grows

## Example

**Create the table:**
```
Measures = DATATABLE("Col", INTEGER, {{1}})
```
Set column type to Integer.

**Move measures:**
In Model View → select measure → Properties → Table → choose Measures.

**Organize with display folders:**
Properties → Display Folder → `Revenue`, `Occupancy`, `KPIs`, etc.

## Related

- [[Bulk-Edit-Measure-Properties-Model-View]] — bulk editing inside the measure table
- [[Organizing-Measures-Display-Folders]] — existing note on display folders
- [[Measure-Tables-in-Power-BI]] — existing note on measure tables
