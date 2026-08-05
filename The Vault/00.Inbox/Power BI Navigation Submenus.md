---
title: "Power BI Navigation Submenus"
source: "https://databear.com/power-bi-custom-navigation-submenus/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-07-13
created: 2026-08-04
description: "Create custom Power BI navigation submenus with PowerPoint, buttons, and bookmarks. Improve UX/UI with this advanced step-by-step tutorial."
Processed: "Unprocessed"
---
Creating polished, intuitive **Power BI navigation submenus** is one of the most effective ways to enhance user experience in your reports. Whether you’re aiming for a clean layout, dark theme consistency, or interactive elements that mimic modern apps, this guide walks you through every step from visual design to functional bookmarking.

By mastering submenu navigation, you’ll deliver reports that look better, work smarter, and keep your users engaged.

##### Why Use Power BI Navigation Submenus?

Custom navigation submenus help bring structure and flow to Power BI dashboards. Benefits include:

- Clean, uncluttered report pages
- Enhanced visual hierarchy and UX
- Seamless transitions between pages
- Tailored styling for brand consistency
- Full control over bookmark-driven interactions

When designed well, navigation submenus can make Power BI feel like a polished, professional web application.

##### What You’ll Need

To follow this tutorial, you’ll need:

- Power BI Desktop
- Microsoft PowerPoint
- A color picker tool (optional, for theme alignment)

##### Step-by-Step Guide: Creating Navigation Submenus in Power BI

##### 1\. Design the Submenu Layout in PowerPoint

Open PowerPoint and insert a **speech bubble shape**. Resize it to approximately `2.7 in x 2.25 in` and fill it with a dark theme color like `#333333`. This creates the base for your submenu popup.

Add a soft shadow to give the element depth and improve visual polish. ![Design the Submenu Layout in PowerPoint](99.System/Attachments/Design_the_Submenu_Layout_in_PowerPoint.png)

##### 2\. Create Circular Buttons for Navigation Items

Insert **five circle shapes**, one for each submenu item. Remove their outlines and apply a soft edge to modernize their look. Align them vertically using PowerPoint’s **Align > Distribute Vertically** feature.

Use each metric’s theme color (like Sales, Units, Profit) to fill the circles. If needed, use a color picker to extract these hex codes from your report visuals.

##### 3\. Add Icons and Divider Lines

Center white icons within each circle to visually represent the submenu actions (e.g., a dollar sign for Gross Sales). Below each icon, insert a transparent white divider line (75% transparency, 0.25in thickness) to separate items and enhance readability.

Group all elements and export the finished submenu as a **PNG**.![Add Icons and Divider Lines](99.System/Attachments/Add_Icons_and_Divider_Lines.png)

##### Bringing Your Design into Power BI

Back in Power BI Desktop:

1. Insert the PNG using **Insert > Image**
2. Position it beneath your page header or title area
3. Use the **Selection Pane** to manage its layer position for consistency ![Bringing Your Design into Power BI](99.System/Attachments/Bringing_Your_Design_into_Power_BI.png)

##### Building Interactive Buttons Over Your Submenu

Now you’ll overlay invisible buttons to make each submenu item interactive.

##### Default State Setup

- Insert blank buttons over each circle
- Remove borders and icons
- Set text font to **Segoe UI**, color white, aligned left
- Adjust the width to fit each item ![Building Interactive Buttons Over Your Submenu Power BI Navigation Submenus](99.System/Attachments/Building_Interactive_Buttons_Over_Your_Submenu_Power_BI_Navigation_Submenus.png)

##### Hover State Styling

- Change font to **Segoe UI Semibold**
- Add a colored background that matches each metric theme
- Set transparency to **75%** for a subtle hover effect ![Hover State Styling Power BI Navigation Submenus ](99.System/Attachments/Hover_State_Styling_Power_BI_Navigation_Submenus_.png)

##### Creating Bookmarks for Interactivity

Use Power BI’s **Bookmarks** pane to drive your submenu’s behavior.

##### Key Bookmarks to Create:

- One to **open** the submenu
- One to **close** it

Make sure to **uncheck “Data”** and **check “Selected visuals”** for each bookmark. This prevents data visuals from resetting when bookmarks are toggled.

##### Assigning Actions to Buttons

Configure each button to navigate to a specific view or page via its assigned bookmark. Use clear naming conventions like:

- `units_view`
- `sales_view`
- `period_submenu_open`

This makes future edits easier and keeps your file organized.

##### Reusing the Submenu on Multiple Pages

To apply your Power BI navigation submenu on other report pages:

1. Copy the grouped PNG and buttons
2. Paste them onto the desired page
3. Create new open/close bookmarks specific to that page
4. Update each button’s actions accordingly

Consistent naming and organization are key here.

##### Layer Management Best Practices

Effective use of Power BI’s **Selection Pane** helps manage layers and interactivity. Tips:

- Clearly name all visuals, shapes, and buttons
- Group elements by function (e.g., `Submenu_Group`, `Icons_Group`)
- Toggle visibility to debug bookmark actions quickly

Organized layers make it far easier to maintain and scale your reports over time.

##### Test Everything Before Publishing

Before sharing your report, thoroughly test:

- Bookmark toggle behaviors (open/close submenu)
- Navigation button links and hover states
- Visual alignment across all report pages

##### Learn Advanced UX/UI for Power BI

Want to go even further with your Power BI skills? Check out this hands-on training:

**[Power BI Training Data Bear](https://databear.com/power-bi-training/)**

This course dives deeper into [report design](https://databear.com/power-bi-july-update/ "Power BI July Update"), interactivity, and real-world UX techniques to help your dashboards stand out and perform.

##### Final Thoughts

Building custom **Power BI navigation submenus** is a powerful way to level up your report design. With just PowerPoint, bookmarks, and a few best practices, you can transform basic dashboards into highly interactive, user-friendly tools.

Keep practicing these techniques, and you’ll quickly build a reputation for producing enterprise-grade Power BI experiences.