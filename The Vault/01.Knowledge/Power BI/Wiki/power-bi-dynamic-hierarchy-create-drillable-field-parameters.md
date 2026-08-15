---
created: 2026-08-11
source: Power BI Dynamic Hierarchy: Create Drillable Field Parameters
note_type: pattern
tags: [power-bi, field-parameters, dynamic-hierarchy, drill-down]
---

# Dynamic Hierarchy via Field Parameter with Grouping Column

Switching between hierarchies (e.g., Date and Location) on a single chart via Field Parameters while preserving full drill-down and drill-up behaviour.

## Purpose

Field Parameters let users switch which field drives a visual axis, but each field has its own hierarchy. By default, Power BI loses drill functionality when you swap between hierarchies. This pattern restores it.

## When to Use

- Report space is limited and multiple charts can be consolidated
- Users need interactive drill-down analysis
- Executive dashboards where clean design matters
- Enterprise reporting where visual clutter reduces adoption

## Pattern

### Step 1: Build the Field Parameter

1. Go to **Modeling > New Parameter > Fields**
2. Add hierarchy fields in the correct order:
   - Year → Quarter → Month (Date hierarchy)
   - Region → Location (Location hierarchy)
3. Name it **Dynamic Hierarchy**
4. Enable the slicer option
5. Click Create

### Step 2: Add the Grouping Column

The Field Parameter creates a calculated table behind the scenes. Access it in Table View.

1. Switch to **Table View**
2. Locate the Dynamic Hierarchy parameter table
3. It has three columns: Name, Field, Order
4. Add a 4th column: **Grouping**

| Name | Field | Order | Grouping |
|------|-------|-------|----------|
| Year | Date[Year] | 0 | Dates |
| Quarter | Date[Quarter] | 1 | Dates |
| Month | Date[Month] | 2 | Dates |
| Region | Location[Region] | 3 | Location |
| Location | Location[Location] | 4 | Location |

### Step 3: Update the Slicer

Return to Report View. In the slicer:

- Replace the default parameter column with the **Grouping** column
- Turn on **Single Select**
- Optionally switch to Tile style and remove the header

Drill behaviour is now preserved within each hierarchy group.

## Key Concept

Power BI treats each field independently in Field Parameters. The Grouping column tells the engine which fields belong to the same logical hierarchy, so drill paths stay intact when switching between groups.

## Related

- [[dynamic-hierarchy-field-parameter-drill]] — the grouping column concept in isolation
