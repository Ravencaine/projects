---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Your Power BI Reports with Slicer Panels.md"
note_type: workflow
tags: [power-bi, slicer-panel, bookmark, button, grouping, z-order, ui-ux]
---

# Slicer Panel Workflow

Collapsible panel of slicers that can be shown/hidden via a bookmark-linked button — keeps reports clean while preserving filter functionality.

## Steps

### 1. Create and Style Slicers
- Add slicers to canvas (Date, Category, etc.)
- Style consistently: font size, color, background
- Use Format Painter to copy styling between slicers

### 2. Add Background Shape
- Insert → Shapes → Rectangle
- Position behind the slicers
- Apply theme colors or manual formatting
- Use Selection pane (View tab) to set Z-order: rectangle must appear *above* the canvas but *below* the slicer

### 3. Add Toggle Button
- Insert → Buttons → Blank → choose icon (arrow, hamburger menu, etc.)
- Position within the panel area
- Resize to fit

### 4. Group Elements
- Select: slicers + rectangle + button
- Right-click → Group
- Name the group "Slicer Panel"
- Group moves as one unit

### 5. Create Bookmarks
- Bookmarks pane (View tab) → Add
- **Bookmark 1:** with panel visible → name "Show Slicer Panel" → uncheck **Data** (preserve selections)
- **Bookmark 2:** with panel hidden → name "Hide Slicer Panel" → uncheck **Data**
- Both bookmarks capture visibility state only

### 6. Link Button to Bookmarks
- Select the toggle button → Format → Action
- Type: **Bookmark**
- Bookmark: choose the hide/show target
- (Optional) Add tooltip for UX

### 7. Link Image to Opposite Bookmark
- Hamburger/menu icon image → Action → Bookmark → opposite state
- Now icon and button toggle in opposite directions

## Key Rules
- **Uncheck Data on bookmarks:** otherwise toggling resets all slicer selections
- **Hold Ctrl + click** to test button actions in Power BI Desktop
- Selection pane controls Z-order; rectangle must be visually behind slicers
- Grouping locks the spatial relationship between elements

## Related
- [[Source-Enhance-Your-Power-BI-Reports-with-Slicer-Panels]] — source note
- [[bookmarks-in-power-bi]] — bookmark reference
- [[drillthrough-page-button]] — button setup
