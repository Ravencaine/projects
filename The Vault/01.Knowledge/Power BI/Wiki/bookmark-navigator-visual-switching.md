---
created: 2026-08-02
source: Build a Visual Explorer in Power BI — Let Users Choose What and How They See Data.md
note_type: pattern
tags: [powerbi, bookmarks, navigation, visual-switching, ui-patterns]
---

# Bookmark Navigator for Visual Switching

A set of overlapping visuals (bar, column, line, table, matrix) positioned at the same canvas location, each paired with a bookmark, switched by a bookmark navigator button group.

## Purpose

Allows users to switch between chart types without losing their current field parameter selections. The visual type change is triggered by a bookmark, which preserves filter context while toggling visibility of the underlying visual.

## Components

- Multiple visuals placed at identical coordinates (overlapping)
- One bookmark per visual, with **Data unchecked** (prevents slicer reset on switch)
- A button group (or image-based selector) linked to each bookmark via the bookmark navigator
- Visual icons (bar, column, line, table, matrix) as button labels

## Structure

### Bookmarks

For each visual type (bar, column, line, table, matrix):

1. Create the visual and position it exactly where you want it.
2. Create a bookmark targeting that visual.
3. In the bookmark options, **uncheck Data** — this is critical: it prevents the field parameter slicers from resetting when switching visuals.
4. Optionally uncheck Background to see the visual clearly while editing.

### Bookmark Navigator

The bookmark navigator button group is added to the canvas from the Insert tab → Buttons → Bookmark Navigator. Each button is linked to a bookmark. When a user clicks a button, the corresponding bookmark activates, hiding all visuals except the targeted one.

### Copying the UI Group

The "View Selection" group (bookmark navigator + visual icons) can be copied from the included PBIX file and pasted into any report, then connected to new bookmarks.

## Key Rules

- All visuals must be stacked at the same position. Even 1px offset will cause a visible jump.
- The **Data checkbox in bookmark options must be unchecked** — this is the mechanism that preserves slicer state across visual switches.
- Visual icons used for buttons should match the report's UI style.

## Related

- [[visual-explorer-pattern]]
