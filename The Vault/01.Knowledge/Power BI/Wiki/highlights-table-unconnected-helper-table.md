---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: pattern
tags: [powerbi, pattern, disconnected-table, button-slicer]
---

# Highlights Table (Unconnected Helper Table)

A small table created in Power Query with sequential integer values (1, 2, 3...) that is left **unconnected** to the data model and used solely to drive button slicer navigation.

## Purpose

The Highlights table maps button clicks to numeric "Order" values that SWITCH statements read via `SELECTEDVALUE()`. Because it has no relationships, it never filters data directly — it only signals which highlight is active.

## Components

1. **Power Query table** — single column `Order` with values 1, 2, 3, 4 (one per highlight)
2. **Button slicer** — bound to `Highlights[Order]`, formatted as a vertical list of buttons
3. **Callout value label** — bound to a SWITCH-based DAX measure that returns the appropriate text
4. **Supporting DAX measures** — one measure per highlight, each returning a formatted text string

## Structure

```
Power Query → Highlights table (unconnected)
     ↓
Button Slicer on Highlights[Order]
     ↓
Callout value label → Highlight Headers SWITCH measure
```

## Example

```m
// Power Query: create a single-column table
let
    Source = Table.FromList({1, 2, 3, 4}, Splitter.SplitByNothing()),
    RenamedColumns = Table.RenameColumns(Source, {{"Column1", "Order"}})
in
    RenamedColumns
```

```dax
// DAX: map Order to display text
Highlight Headers =
    SWITCH(
        SELECTEDVALUE(Highlights[Order]),
        1, [High OT Flag Highlight],
        2, [Biggest Rise Highlight],
        3, [Top Unit Highlight],
        4, [Lowest Fill Rate Highlight]
    )
```

## Variations

- Use text values instead of integers for more descriptive button labels — but numeric Order is simpler for SWITCH logic
- Add a second `Label` column to the table to store pre-written button text instead of generating it via DAX
- Extend to 5+ highlights by adding more rows and SWITCH cases

## Related

- [[Button-Slicer]]
- [[Dynamic-Chart-SWITCH-on-Button-Slicer]]
- [[Dynamic-KPI-Card-Layout]]
- [[complex-selector-pattern-in-dax]]
