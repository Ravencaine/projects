---
created: 2026-08-11
source: Power BI Dynamic Hierarchy: Create Drillable Field Parameters
note_type: workflow
tags: [power-bi, field-parameters, dynamic-hierarchy]
---

# Dynamic Hierarchy — Step-by-Step

Workflow to build a single chart that switches between two hierarchical dimensions while preserving drill-down and drill-up.

## Prerequisites

- Power BI Desktop
- A data model with at least two hierarchies (e.g., Date: Year/Quarter/Month and Location: Region/Location)
- Separate tables or columns for each hierarchy

## Steps

**Step 1 — Recreate hierarchies in the Field Parameter**
- Go to Modeling > New Parameter > Fields
- Add Date fields in order: Year, Quarter, Month
- Add Location fields in order: Region, Location
- Name it "Dynamic Hierarchy"
- Enable slicer, click Create

**Step 2 — Add Grouping column in Table View**
- Switch to Table View
- Find the Dynamic Hierarchy calculated table
- Add a 4th column named "Grouping"
- Populate: Year/Quarter/Month = "Dates", Region/Location = "Location"

**Step 3 — Update the slicer**
- Return to Report View
- Replace the default parameter field in the slicer with the Grouping column
- Enable Single Select
- Optionally remove the header and use Tile style

**Step 4 — Validate**
- Select "Dates" in the slicer: drill Year → Quarter → Month works
- Select "Location": drill Region → Location works

## Common Mistakes

- Adding fields to the Field Parameter in the wrong order — drill levels will be wrong
- Using the parameter column instead of the Grouping column in the slicer — drill won't work
- Missing single-select enforcement — multi-select breaks hierarchy logic
