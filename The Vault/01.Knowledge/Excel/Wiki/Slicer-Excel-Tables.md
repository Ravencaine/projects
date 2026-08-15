---
created: 2026-08-08
updated: 2026-08-08
source: "6 Excel features I use in every spreadsheet I create"
source_url: https://www.howtogeek.com/microsoft-excel-features-i-use-in-every-spreadsheet/
author:
  - name: Tony Phillips
    source: How-To Geek
note_type: atomic
tags: [excel, slicer, filter, table, dashboard, interactive]
related:
  - "[[Excel-Table-Ctrl-T]]"
  - "[[conditional-formatting]]"
---

# Slicers in Excel Tables

Slicers provide a visual, button-based interface for filtering Excel Tables and PivotTables — replacing the small dropdown arrows in column headers with large, clearly labelled, always-visible filter buttons.

## When to Use Slicers vs Column Filter Arrows

| Situation | Use slicers | Use filter arrows |
|-----------|------------|-----------------|
| Repeatedly switching between categories | ✓ faster, reusable | requires opening menu each time |
| Sharing with non-technical users | ✓ obvious active state | less obvious filter is active |
| Dashboard or tracker with multiple filter fields | ✓ visual, prominent | clutter in header row |
| Quick one-off filter | | ✓ faster for a single use |
| Hiding filter UI from end users | | ✓ slicers are always visible |

Tony Phillips (HowToGeek, 2026-07-10): *"The problem is that filter menus are hidden behind small drop-down buttons. If I'm repeatedly switching between categories... opening a menu, finding the right option, and clearing the filter again becomes surprisingly tedious."*

## Insert a Slicer

```
Insert → Slicer
  OR
PivotTable Analyze → Insert Slicer
```

Select the checkboxes for each column you want to create a slicer for. Each column becomes a separate slicer object on the worksheet.

## Slicer Settings

| Setting | Location | Effect |
|---------|----------|--------|
| Multi-select | Click buttons while holding Ctrl | Select multiple values simultaneously |
| Clear filter | Click funnel icon top-right | Reset to show all |
| Header caption | Slicer Settings → Caption | Rename the slicer title |
| Columns | Slicer Settings → Columns | Display buttons in N columns instead of 1 |
| Style | Slicer Settings → Style | Choose from preset visual styles |

## Slicers vs PivotTable Slicers

Slicers are commonly associated with PivotTables but work equally well on standard Excel Tables:

| | Slicer on Excel Table | Slicer on PivotTable |
|---|---|---|
| Source | Excel Table | PivotTable |
| Filters | Table columns | PivotTable fields |
| Button values | Unique values in column | Row/column labels from PivotTable |
| Multiple slicers | ✓ | ✓ |
| Works on dashboard | ✓ | ✓ |

## Slicer + Conditional Formatting Combo

When slicers filter visible rows, conditional formatting rules (applied to the underlying table) continue to work — the slicer narrows the visible range and CF reacts to what's shown:

1. Create Excel Table → Apply conditional formatting rules
2. Insert Slicer for the relevant column(s)
3. User filters via slicer buttons → CF highlights update automatically within the visible subset

## Related

- [[Excel-Table-Ctrl-T]] — slicers are most powerful when built on top of an Excel Table
- [[conditional-formatting]] — CF provides visual intelligence on top of slicer filtering
