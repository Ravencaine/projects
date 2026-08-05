---
created: 2026-08-02
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data
note_type: pattern
tags: [power-bi, bookmarks, navigation, visual-type, slicer, user-empowerment]
---

# Bookmark Navigator for Visual Type Switching

A set of bookmarks — one per chart type — stacked in the same canvas position, switched by a bookmark navigator button group.

## Setup

1. Build one visual per type (bar, column, line, table, matrix) in the **same position**
2. Bind all to the same Metric + Dimension field parameters
3. Create one **bookmark** per visual type
4. In each bookmark, **uncheck "Data"** → ensures slicer selections persist when switching
5. Add a **bookmark navigator** button group to the page

## Critical Setting

| Setting | Value | Reason |
|---------|-------|--------|
| **Data** in bookmark options | **Unchecked** | Preserves Metric + Dimension slicer state across visual switches |

With Data unchecked, switching bookmarks only changes *which visual is visible* — not the underlying parameter selections.

## Copy-Paste Template

Isabelle provides a "View Selection" object group in the PBIX that includes:
- SVG/icon images for each chart type
- A bookmark holder visual
- Pre-styled button layout

Paste into any report, then connect to your own bookmarks.

## Icon Options

Default Power BI visual screenshots work natively. Replace with custom SVG icons to match the report's design system.

## Related

- [[visual-explorer-pattern-field-parameters-bookmark-switching]] — parent pattern
