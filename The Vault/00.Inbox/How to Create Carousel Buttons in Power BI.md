---
title: "How to Create Carousel Buttons in Power BI"
source: "https://databear.com/power-bi-carousel-buttons/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-05-04
created: 2026-08-04
description: "Learn how to create native carousel buttons in Power BI using field parameters and button slicers—no custom visuals required."
Processed: "Unprocessed"
---
**Power BI carousel buttons** allow users to cycle through visuals, measures, or text within a single report space—making your dashboards more interactive and space-efficient. While Power BI doesn’t include a native carousel visual, this guide shows how to simulate the same functionality using button slicers and field parameters. We’ll walk through several practical use cases, including switching between KPIs, toggling dimensions, and displaying text content, all with built-in Power BI features.

[Learn Power BI from industry experts at DataBear](https://databear.com/power-bi-training/)

---

##### What Are Carousel Buttons in Power BI?

Carousel buttons in Power BI simulate a user-friendly way to **cycle through content**, such as:

- Measures (e.g., Sales, Quantity, Average Sales)
- Dimensions (e.g., Category, Year, Product)
- Text content or descriptions

They are built using **button slicers** and **field parameters** introduced in recent updates, making it possible to build advanced interactive visuals without any custom visuals.

---

##### Step-by-Step: Create a Measure Carousel

##### 1\. Set Up Your Measures

Create the measures you want to cycle through. For example:

- `Sales` = Quantity × Price
- `Quantity` = SUM(Quantity)
- `Average Sales` = AVERAGEX(…) ![Creating a field parameter in Power BI to enable carousel buttons for switching between Sales, Quantity, and Average Sales measures](99.System/Attachments/Creating_a_field_parameter_in_Power_BI_to_enable_carousel_buttons_for_switching_between_Sales,_Quant.png)

##### 2\. Create a Field Parameter

- Go to **Modeling > New Field Parameter**
- Select all three measures
- Ensure “Add slicer to page” is checked
- Name it appropriately (e.g., `Measure Parameter`) ![Bar chart in Power BI using carousel buttons to toggle between different measures for total sales by product category.](99.System/Attachments/Bar_chart_in_Power_BI_using_carousel_buttons_to_toggle_between_different_measures_for_total_sales_by.png)

##### 3\. Update Your Visual

- Add a bar chart
- Replace the Y-axis value with the new parameter field
- The chart now updates based on slicer selection

##### 4\. Convert Slicer to Button Carousel

- Change the slicer type to **Button**
- Format the buttons to look like a carousel:
	- Background: Transparent
		- Selection: Single select + “For selection” on
		- Shape: Rounded rectangle
		- Layout: Single row
		- Callout values: Off
- Resize and place the carousel beneath or beside your visual ![Creating a text parameter in Power BI to enable carousel buttons that cycle through multiple text-based visuals](99.System/Attachments/Creating_a_text_parameter_in_Power_BI_to_enable_carousel_buttons_that_cycle_through_multiple_text-ba.png)

---

##### Make the Title Dynamic

You can bind the chart title to reflect the selected measure:

- Click on the visual title > select **Value** under *Title text*
- Choose the same **field parameter** used for the carousel

This ensures the title dynamically updates when a different option is selected.

---

##### Carousel Buttons for Text Displays

You can also cycle through different text blocks using a similar approach:

- Create multiple DAX measures with sample or dynamic text
- Add them to a new **field parameter**
- Use a **card visual** to display the text
- Use a **button slicer** to act as the carousel ![Text carousel in Power BI showing placeholder text with carousel buttons for cycling through different content options.](99.System/Attachments/Text_carousel_in_Power_BI_showing_placeholder_text_with_carousel_buttons_for_cycling_through_differe.png)

---

##### Alternate Styles: Compact, Rectangular, or Vertical

To match your report layout, you can modify the carousel format:

- **Rectangular Buttons**: Change border radius to 0
- **Vertical Carousel**: Change layout to a single column
- **Compact Pills**: Use custom padding to make buttons smaller and text readable ![](99.System/Attachments/Screenshot-2025-05-02-145705.png)

---

##### Combine Measure and Category Carousels

You can use **two independent field parameters**:

- One for measures (Sales, Quantity, Avg Sales)
- Another for categories (Year, Product, Category Name)

Each carousel can be placed in a different position (e.g., horizontal below chart and vertical on the left). Titles and visuals will respond dynamically.

---

##### When to Use Carousel Buttons

##### Pros:

- Clean interface when space is limited
- Seamless navigation between multiple views
- Useful for mobile-optimized dashboards

###### Cons:

- May lack clarity without visible labels
- Not ideal for users who need to see all options at once

For more accessible designs, consider using **standard buttons with visible labels** rather than minimalist carousel styles.

---

##### Style and Branding

You can match the carousel button styles to your company’s color palette:

- Customize button fill, borders, and transparency
- Use Format Painter to apply styles across multiple slicers
- Set states (default, hover, selected) to control interactive feedback

---

##### Final Thoughts

Carousel buttons offer a sleek, interactive way to navigate between multiple insights in a single Power BI page. By combining field parameters and the new button slicer, you can simulate a carousel experience that’s flexible, dynamic, and completely native to Power BI—no custom visuals needed.

Explore more Power BI capabilities through structured learning:  
[Power BI Training by DataBear](https://databear.com/power-bi-training/)