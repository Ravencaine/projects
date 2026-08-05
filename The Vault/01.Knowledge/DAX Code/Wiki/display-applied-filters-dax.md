---
created: 2026-08-02
updated: 2026-08-03
source: Streamline Data Exploration with a Custom Slicer/Filter Pane in Power BI
note_type: pattern
tags: [dax, pattern, isfiltered, concatenatex, allselected, filter, slicer, display]
---

# Display Applied Filters via DAX: ISFILTERED + CONCATENATEX + ALLSELECTED

Renders the currently active slicer selections as readable text for display at the top of a report, even when the filter panel is closed.

```dax
Selected Slicers =
VAR country_selected =
    IF(
        ISFILTERED(Geography[Country]),
        " >" & [TR Country] & ": " & CONCATENATEX(ALLSELECTED(Geography[Country]), Geography[Country], ",")
    )
VAR city_selected =
    IF(
        ISFILTERED(Geography[City]),
        " >" & [TR City] & ": " & CONCATENATEX(ALLSELECTED(Geography[City]), Geography[City], ",")
    )
VAR management_level_selected =
    IF(
        ISFILTERED('Management Level'[Management Level]),
        " >" & [TR Management Level] & ": " &
            CONCATENATEX(ALLSELECTED('Management Level'[Management Level]), 'Management Level'[Management Level], ",")
    )
RETURN "Filter: " & country_selected & city_selected & management_level_selected
```

**Pattern per slicer column:**

```dax
VAR _selected =
    IF(
        ISFILTERED(<column>),
        " >" & [TR <column>] & ": " &
            CONCATENATEX(ALLSELECTED(<column>), <column>[column], ",")
    )
```

**Functions used:**

- `ISFILTERED(<column>)` — TRUE if the slicer is active; guards each section so inactive slicers contribute nothing
- `ALLSELECTED(<column>)` — returns the filtered set of values (not the full table)
- `CONCATENATEX(..., <column>[column], ",")` — joins the selected values with a comma delimiter

**Design:** Place this measure in a text box at the top of the report page so users can always see what is filtered — even when the custom filter panel is closed.
