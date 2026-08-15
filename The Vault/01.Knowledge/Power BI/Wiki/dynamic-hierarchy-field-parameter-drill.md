---
created: 2026-08-11
source: Power BI Dynamic Hierarchy: Create Drillable Field Parameters
note_type: pattern
tags: [power-bi, field-parameters, grouping-column, drill-down]
---

# Grouping Column Preserves Drill in Field Parameter Hierarchies

Adding a Grouping column to a Field Parameter's calculated table tells Power BI which fields belong to the same hierarchy, restoring drill behaviour when switching axes.

## Purpose

Field Parameters treat every field as independent. Without grouping, Power BI does not know which fields form a logical drill path. The Grouping column bridges this gap by tagging fields with a shared group name.

## How It Works

1. Field Parameter creates a calculated table with Name, Field, Order columns
2. Add a 4th Grouping column with values like "Dates" and "Location"
3. Use the Grouping column (not the parameter column) in the slicer
4. Power BI now understands which fields share a hierarchy

## Example

| Grouping | Field | Drill behaviour |
|----------|-------|---------------|
| Dates | Date[Year] | Year → Quarter → Month |
| Dates | Date[Quarter] | Quarter → Month |
| Dates | Date[Month] | Leaf node |
| Location | Location[Region] | Region → Location |
| Location | Location[Location] | Leaf node |

## Context

Part of [[power-bi-dynamic-hierarchy-create-drillable-field-parameters]]. The grouping column is the critical step that separates a working dynamic hierarchy from a broken one.
