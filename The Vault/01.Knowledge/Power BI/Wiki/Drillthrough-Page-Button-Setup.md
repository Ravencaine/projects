---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Drillthrough Button in Power BI.md"
note_type: workflow
tags: [power-bi, drillthrough, button, navigation, page-design]
---

# Drillthrough Page + Button Setup

Create a drillthrough page and a custom drillthrough button in Power BI so users can navigate from a summary visual to a detail page by selecting a value.

## Prerequisites

- Power BI Desktop
- A report with at least one existing page containing a visual

## Steps

### 1. Create a new page

Add a new report page using the `+` (New Page) icon in Power BI Desktop.

### 2. Name and hide the page

1. Rename the page using the `DT` prefix followed by the dimension name, e.g., `DT Country` or `DT Product`
2. Right-click the page tab → **Hide page**

Hiding the page prevents users from navigating to it directly — they can only reach it via the drillthrough action.

### 3. Design the detail page

Add the visuals you want to appear when the user drills through. These are the detail views that explain the selected value.

### 4. Define the drillthrough dimensions

In the drillthrough page's **Filters** pane, under **Drillthrough filters**, add the fields that should act as the drillthrough trigger.

> Adding the first field to the drillthrough filters pane **automatically creates a back button** on the page. No manual button needed for back navigation.

### 5. Verify the drillthrough works

Return to the source page. Right-click on a data point in a visual and confirm the drillthrough page appears in the context menu.

### 6. Create the drillthrough button

1. On the source page, go to **Insert** → **Button** → select a button type
2. In the button properties, set **Action** → **Type** to `Drillthrough`
3. Set **Destination** to the hidden drillthrough page (e.g., `DT Country`)
4. Enable the action and optionally style the button

The button replaces the need to right-click and is easier for end users to discover.

### 7. Test end-to-end

1. Select a value in the source visual
2. Click the drillthrough button
3. Confirm the detail page opens with the selected context pre-filtered
4. Click the back button to return to the source page

## Variations

**Button-based vs right-click only:** If the report audience is not power users, always add the button. If building for analyst audiences who are comfortable with right-click, the button is optional.

**Multi-field drillthrough:** Add multiple fields to the drillthrough filters pane to allow drilling through on more than one dimension. Each field creates a separate drillthrough path.

**Drillthrough with field parameters:** Use field parameters to let users select which dimension drives the drillthrough, enabling a single drillthrough page to serve multiple scenarios.

## Common Errors

- **Page not hidden** → Users see the drillthrough page in the page list and may navigate directly, bypassing the filter context
- **Destination not set on button** → Button renders but does nothing; set the destination in the button's Action properties
- **No back button** → The back button auto-creates when you add a field to the drillthrough filters pane — not when you add it manually. If missing, check the drillthrough filters.

## Related

- [[Drillthrough-Page-DT-Prefix]] — naming convention for drillthrough pages
- [[Bookmark-Navigator-for-Visual-Type-Switching]] — bookmark-based page navigation patterns
- [[Button-Slicer]] — button-driven interactions
- [[Selection-Bookmarks-Panel-Organization]] — bookmark management
