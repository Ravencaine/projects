---
created: 2026-08-06
updated: 2026-08-06
source: Bookmarks in Power BI for Enhanced Report Interactivity.md
source_url: https://databear.com/bookmarks-in-power-bi/
note_type: reference
tags: [power-bi, bookmarks, buttons, navigation, selection-pane, user-interactivity]
---

# Bookmarks in Power BI — Complete Guide

A bookmark captures the exact state of a report page: visual positions, filter/slicer state, visibility, spotlight, and selection. They enable view-switching, guided tours, and interactive toggles without manual reconfiguration.

## Quick Reference

### What a Bookmark Captures

| State Component | Description |
|----------------|-------------|
| **Visual positions** | Size, position, and arrangement of every visual on the page |
| **Filters & slicers** | Current filter/slicer selections (controlled by **Data** toggle) |
| **Visibility** | Per-visual show/hide state from the Selection Pane (controlled by **All visuals** toggle) |
| **Spotlight** | Which visual is in spotlight mode (controlled by **Display** toggle) |
| **Selection** | Which visual is selected (controlled by **Display** toggle) |

### Creating a Bookmark

1. Arrange the report to the desired state
2. **View → Bookmarks** pane and **Selection** pane
3. **Bookmarks pane → Add:** captures the current state
4. Rename the bookmark to a descriptive label

### Bookmark Options (per bookmark)

| Option | Default | Effect when checked |
|--------|---------|-------------------|
| **All visuals** | ✓ | Captures/restores visibility of all visuals |
| **Data** | ✓ | Captures/restores current filter and slicer state |
| **Display** | — | Captures/restores spotlight and selection state |

### Showing / Hiding Visuals (via Selection Pane)

The Selection Pane lists all objects on the page. Toggle visibility with the eye icon:

- Open eye → visual is visible in the bookmark
- Closed eye → visual is hidden in the bookmark

Use this to create focused views that suppress secondary visuals.

### Buttons with Bookmarks

1. **Insert → Button** (Blank or icon)
2. Format the button: text label, color, alignment
3. **Format pane → Action → On → Bookmark**
4. Select the target bookmark

A button bookmark navigates the user to the bookmarked state on click.

### Bookmark Navigator

**Insert → Buttons → Bookmark Navigator** automatically creates a button group covering all bookmarks on the page. Useful when 3+ bookmarks need to be accessible.

### Grouping Bookmarks

Select multiple bookmarks in the pane → right-click → **Group**. Groups appear as collapsible sections. The Bookmark Navigator handles groups natively.

## Notes

- A bookmark captures the state **at creation time:** create it after setting up all filters, slicers, and visual arrangements
- **Uncheck Data** when switching bookmarks on the same data context — otherwise slicer state resets on every bookmark switch
- **Uncheck All visuals** + use the Selection Pane to hide/show specific visuals across bookmark states
- The Selection Pane must remain open when creating bookmarks to ensure visibility states are captured correctly
- Bookmarks work across pages when triggered by buttons — useful for navigation menus

## Related

- [[bookmark-navigator-for-visual-type-switching]] — specific use case: switching chart types via bookmark navigator
- [[large-data-table-ux-power-bi]] — uses bookmarks for Overview/Detailed View toggle pattern
