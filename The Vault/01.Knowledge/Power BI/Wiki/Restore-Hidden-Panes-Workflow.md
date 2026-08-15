---
created: 2026-08-09
updated: 2026-08-09
source: "Fix Hidden Panes in Power BI (Quick Guide).md"
note_type: workflow
tags: [power-bi, power-query, ui, panes, layout, workflow]
---

# Restore Hidden Panes in Power BI

Step-by-step process for restoring accidentally hidden UI panes in Power Query Editor and Power BI Desktop.

## Power Query Editor

### Restore the Queries Pane (Chevron)

1. Look for the **chevron (arrow)** on the left edge of the window
2. Click it to expand
3. The query list reappears instantly

### Restore the Applied Steps Pane

1. Go to the **View** tab
2. Under **Layout**, click **Query Settings**
3. The Applied Steps pane reappears on the right

### Turn the Formula Bar Back On

1. Go to the **View** tab
2. Check the **Formula Bar** option
3. M expressions reappear above the data preview

### Enable Parameters

1. Go to the **View** tab
2. Enable **Parameters**
3. Parameter options become available in the ribbon and conditional logic dialogs

## Power BI Desktop

### Use the Pane Manager

1. Go to the **View** tab
2. Select **Pane Manager**
3. Toggle visibility of any pane:
   - Filters
   - Data
   - Build (Visualizations)
   - Format
   - Bookmarks
   - Selection
   - Performance Analyzer
   - Sync Slicers

### Manage Excess Panes

- **Chevron:** minimize a pane
- **Ellipses (⋯):** close a pane
- **Resize handles:** adjust pane width manually

## Rule of Thumb

> Always check the **View tab first** whenever a pane disappears — in Power Query Editor, Power BI Desktop, or Microsoft Fabric.

## Related

- [[filter-best-practices]] — filters pane workflows
- [[Slicer-Panel-Workflow]] — pane management in report design
