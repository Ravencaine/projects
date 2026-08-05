---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [field-parameters, dynamic-axis, dynamic-measure, what-if]
related: [SWITCH, SELECTEDVALUE, More-Power-to-Your-Users-Field-Parameters]
---

# Field Parameters (Dynamic Axis Switching)

Uses Power BI Field Parameters to let users select which metric or dimension appears on an axis, without needing multiple visuals or complex measure switching.

## Setup

1. Go to **Modeling → New parameter → Fields**.
2. Select the fields to make switchable (e.g., `Revenue`, `Units Sold`, `Average Price`).
3. Power BI creates:
   - A `Field Parameter` table with a `[Fields]` column.
   - An `[Fields]` measure that returns the selected field.

## Using the Parameter

Drag the `[Fields]` column to the X-axis (or Y-axis) of a visual.

Power BI automatically switches the axis data based on the user's slicer selection from the Field Parameter table.

## Dynamic Title with SELECTEDVALUE

```dax
Chart Title =
    "Performance by " & SELECTEDVALUE('Field Parameter'[Fields], "Revenue")
```

## Dynamic Measure Selection

For more control, use `SELECTEDVALUE` inside a `SWITCH` to pick which measure to display:

```dax
Selected KPI =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Field Parameter'[Fields]) = "Revenue", [Revenue],
        SELECTEDVALUE('Field Parameter'[Fields]) = "Units Sold", [Units Sold],
        SELECTEDVALUE('Field Parameter'[Fields]) = "Average Price", [Average Price]
    )
```

## Notes

- Field Parameters were introduced in the June 2022 Power BI update — no older version support needed.
- The `[Fields]` measure Power BI generates uses `TREATAS` internally to handle the dynamic axis assignment.
- Bittar's Market Watch dashboard uses Field Parameters to let users switch between different stock metrics on the same axis.
- Field Parameters work with: bar charts, line charts, area charts, scatter charts, and column charts.
- To combine Field Parameters with the new slicer (November 2023 update), use a Field Parameter table alongside a separate Period slicer table.

## Related

- [[SWITCH]] — select the correct measure based on parameter value
- [[SELECTEDVALUE]] — read the user's selection
- [[Field-Parameters]] — full workflow note
