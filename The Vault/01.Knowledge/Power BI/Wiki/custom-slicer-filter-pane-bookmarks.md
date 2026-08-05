---
created: 2026-08-02
source: Streamline Data Exploration with a Custom Slicer/Filter Pane in Power BI
note_type: pattern
tags: [powerbi, pattern, slicer, filter, bookmark, action, panel, ui, ux]
---

# Custom Slicer/Filter Pane: Shapes + Bookmarks + Actions

A collapsible filter panel built from shapes and bookmarks that hides on the canvas until the user clicks a trigger button, saving page real estate.

**6-step build:**

1. **Filter button** — place an icon image on the canvas; assign a "Go to page" or "Bookmark" action to it
2. **Panel skeleton** — on a dedicated section/page: background rectangle (styled), close button image (Flaticon or similar), transparent full-dashboard shape (to catch outside clicks)
3. **Slicers** — add all required slicers inside the panel; ensure they are ordered in front of the transparent background shape
4. **Bookmarks** — two bookmarks per page: "Filter Open" (panel visible, `Data=Off`, `All Visuals=Off`) and "Filter Close" (panel hidden); assign "Filter Open" to the icon action, "Filter Close" to the transparent background action
5. **Applied filter indicator** — DAX measure showing current slicer selections; display at top of dashboard so users know what is filtered when panel is closed
6. **Cross-page sync** — copy panel shapes to each page; new bookmarks per page; copy slicers separately (not inside the shape group) to enable the synchronization option

**Key design rules:**
- Synchronize slicers across pages so filter state persists
- Make applied filters visible even when panel is closed (Step 5 measure)
- Close action on transparent background prevents navigation errors (user accidentally re-clicking the icon)

> See `display-applied-filters-DAX.md` for the measure that renders active slicer selections as text.
