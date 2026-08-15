---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: pattern
tags: [power-bi, field-parameters, dynamic-visuals, user-experience]
---

# Field Parameters: Dynamic User-Controlled Visuals

Use field parameters to let end users dynamically switch which dimensions or measures appear in a single visual — without building multiple separate visuals.

## Purpose

Traditionally, if users wanted to switch a visual between Revenue by Property, Revenue by Region, and Revenue by Booking Channel, you would build three separate visuals and place them on the same canvas. Field parameters replace this by letting the user pick from a slicer — one visual adapts to show the chosen field. The same approach works for measures: users can switch between Total Revenue, Occupancy Rate, and Bookings in the same visual.

## Components

- **Field Parameter**: a special calculated table created via Modeling → New Field Parameter
- **Parameter Slicer**: automatically added when the parameter is created — drives which field/measures are active
- **Dynamic visual**: the chart itself uses the parameter's field values instead of hard-coded columns
- Two types:
  1. **Dimension switching**: Property Name, Region, Booking Channel, etc.
  2. **Measure switching**: Total Revenue, Occupancy Rate, Bookings, ADR, etc.

## Structure

**Field parameter (calculated table):**
```
What to show = {(Property Name), (Region), (Booking Channel)}
```

**DAX measure using field parameter:**
```dax
Dynamic Measure =
SWITCH(
    TRUE(),
    ISINSCOPE('What to show'[Property Name]), [Total Revenue],
    ISINSCOPE('What to show'[Region]), [Total Revenue by Region],
    ISINSCOPE('What to show'[Booking Channel]), [Total Revenue by Channel],
    [Total Revenue]
)
```

## Example

**Create:**
1. Go to Modeling → New Field Parameter
2. Add: Property Name, Booking Channel, Region
3. Click Create → parameter table + slicer added
4. Drop parameter onto visual axis instead of a static column
5. User selects from slicer → visual updates

**Measure switching (tip #2 variant — adding measures):**
1. Create second field parameter: Bookings, Occupancy Rate, Total Revenue, ADR
2. Drop onto Values field well — replaces static measure
3. User controls both category (dimension parameter) AND calculation (measure parameter)

## Variations

- **Two-parameter combo**: one parameter for category axis, one for measure — gives users full control over both X-axis and Y-axis content
- Can be combined with [[bookmark-navigator-for-visual-type-switching]] for visual type switching on top of field switching
- Measure parameters require SWITCH/ISINSCOPE to route which measure to display

## Related

- [[Field-Parameters.md]] — general field parameters reference
- [[Field-Parameters-KPI-Hierarchy]] — using field parameters for KPI hierarchy drilling
- [[field-parameters-for-metric-dimension-selection]] — metric/dimension matrix pattern
- [[SWITCH-TRUE-vs-Nested-IF]] — SWITCH TRUE pattern used in dynamic measure routing
- [[bulk-edit-measure-properties-model-view]] — bulk editing after moving measures
