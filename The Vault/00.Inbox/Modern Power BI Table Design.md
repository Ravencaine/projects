---
title: "Modern Power BI Table Design"
source: "https://databear.com/modern-power-bi-table/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-04
created: 2026-08-04
description: "Learn how to create a clean, modern Power BI table with icons, formatting, and filters to boost user experience and report interactivity."
Processed: "Unprocessed"
---
Creating a **modern Power BI table** is not just about looks it’s about function. By combining smart formatting, conditional logic, and thoughtful layout, you can craft a **modern Power BI table** that feels intuitive and delivers insights more effectively than a default visual. This transformation is especially valuable when sharing reports with stakeholders who expect both clarity and style.

##### Objective

- Eliminate visual clutter like horizontal scroll bars
- Create precise alignment with a clean background
- Integrate dynamic icons and image URLs
- Apply conditional formatting for immediate insight
- Build interactive filters and views with bookmarks

##### Step 1: Design Your Background in PowerPoint

Start by designing your layout in PowerPoint. This provides better control over margins and visual structure than Power BI’s native design tools.

Key elements to include in your PowerPoint background:

- A white box to hold your table content
- A light gray header bar where column headers will sit
- Optional areas for cards or filters

Export this slide as an image and set it as the background of your Power BI page. Use the *Fit* option for the image scaling to ensure precise alignment.![Design Your Background in PowerPoint](99.System/Attachments/Design_Your_Background_in_PowerPoint.png)

---

## Step 2: Insert and Align the Table in Power BI

After uploading the background, insert your table visual:

- Resize and position it so the column headers align exactly with the gray bar in your background.
- Zoom in (e.g., 400%) for pixel-perfect placement.
- Use the arrow keys to nudge the table into place.
- Eliminate horizontal scroll bars by adjusting column widths and using abbreviated field versions like `DateShort` or `CountryShort`.

Manually adjust the table’s left and right edges to ensure the scroll bar, if it appears, aligns outside the background. Use a shape to visually check for consistent left and right margins.

## Step 3: Refine Field Names and Abbreviations

Clarity matters. Rename columns to match the language your users are familiar with:

- `DateShort` becomes `Order Date`
- `Gross Sales` becomes `Total Sales`
- `Units Sold` becomes `Items`
- Abbreviations like `RSM` (Regional Sales Manager) should only be used if your audience understands them.

Apply consistent casing (e.g., title case) and consider bolding headers for better visual hierarchy.![Refine Field Names and Abbreviations](99.System/Attachments/Refine_Field_Names_and_Abbreviations.png)

## Step 4: Insert Image URLs for a More Visual Table

Adding image icons can give your report a modern, polished look.

Examples include:

- Product icons next to item names
- Country flags next to customer names
- Profile images for sales reps (RSMs)

Steps to implement:

1. Add columns with hosted image URLs to your data model.
2. Set the data category of those fields to *Image URL*.
3. Drag them into your table before the corresponding field.
4. Remove the column title by replacing it with a space.

To add image URLs:

- Export your dimension table to Excel.
- Add a new column with hosted URLs (e.g., from imgbb or a company-approved host).
- Import the file back into Power BI and create a one-to-one relationship on the key field.![](99.System/Attachments/Screenshot-2025-06-22-130738.png)

## Step 5: Style and Format the Table

Visual adjustments significantly improve readability:

- **Table Style**: Minimal
- **Gridlines**: Horizontal only, hex color `#E7E7E7`
- **Borders**: Off
- **Image Size**: 22 pixels
- **Row Padding**: 10–11 for breathing room

Typography:

- **Font**: Segoe UI
- **Size**: 10pt
- **Color**: `#333333`
- **Header Background**: `#F5F5F5` (to match your PowerPoint gray bar) ![](99.System/Attachments/Screenshot-2025-06-22-131350.png)

## Step 6: Apply Conditional Formatting

To highlight key performance indicators:

- Use icon sets for fields like `Net Profit Margin`:
	- Green up arrow for positive
		- Red down arrow for negative
- Use data bars to emphasize positive values:
	- Set the negative bar color to white to effectively hide them
		- Set minimum value to 0 to suppress bars for negative figures

These small touches make it easier for users to quickly scan and interpret trends.![](99.System/Attachments/Screenshot-2025-06-22-131740.png)

## Step 7: Add Summary Cards

Use the *Card (New)* visual to display high-level metrics at the top of your report. This helps users focus on the most important figures.

Include:

- Total Orders
- Gross Sales
- Returns
- Month-over-month comparison

Design notes:

- Use consistent icon size (25px) and 20px spacing
- Reduce font size for long labels (e.g., 9pt) to avoid truncation

## Step 8: Build Interactive Navigation Tabs

Allow users to switch between customer, reseller, and combined views by using bookmarks and buttons.

1. Group each view (e.g., `Group Order Table Customer`) using the selection pane.
2. Create separate button sets for each view so they can be styled independently.
3. Set up bookmarks to toggle each group:
	- Keep *Data* unchecked to preserve filter selections across views.
4. Highlight the active tab using button formatting.

## Step 9: Create a Custom Filter Panel

Instead of using the default Power BI filter pane, build your own slicer panel:

- Group all slicers into one selection group (e.g., `Group Slicer`)
- Add toggle buttons for opening and closing
- Use bookmarks to:
	- Show or hide the slicer group
		- Clear all slicer selections without changing the view
- Avoid using both the custom panel and built-in filters to reduce confusion

This gives you full design control over how filters appear and behave.

## Step 10: Finalize Bookmarks and Default States

Create and label bookmarks strategically:

- **Default View**: Resets all filters (Data = checked)
- **Customer/Reseller/All Views**: Maintain user filters (Data = unchecked)
- **Slicer Bookmarks**: Apply only to slicer group using *Selected visuals*

Use the *Selection Pane* to validate that the correct groups appear or hide when interacting with each bookmark.

## Conclusion

By following these steps, you’ve created a high-quality, interactive table in Power BI that aligns with modern UX design standards. With carefully controlled spacing, dynamic icons, clean visuals, and intuitive navigation, your report becomes not just informative—but enjoyable to use.

If you’re interested in leveling up your Power BI UX and UI design skills, check out Data Bear’s [Power BI Training Courses](https://databear.com/power-bi-training/). Their hands-on approach is ideal for mastering both fundamentals and advanced visual design.