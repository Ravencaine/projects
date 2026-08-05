---
title: "Organizational Chart in Power BI Using a Decomposition Tree"
source: "https://databear.com/organizational-chart-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-06-01
created: 2026-08-04
description: "Create an organizational chart in Power BI with the decomposition tree. A simple way to show hierarchies—no custom visuals required."
Processed: "Unprocessed"
---
If you’re building Power BI reports for HR or working with hierarchical data, then mastering the **organizational chart in Power BI** is a must. This visual helps users clearly understand reporting structures, making it ideal for organizational planning, management, and HR analytics.

In this guide, you’ll learn how to build a professional, interactive org chart using **Power BI’s native decomposition tree visual** —no third-party visuals or custom scripts required.

##### Why Use a Decomposition Tree for Organizational Charts?

While Power BI lacks a dedicated org chart visual, the **decomposition tree** can be cleverly adapted to display employee hierarchies. By preparing your data and using built-in DAX functions, you can represent any organizational structure from top-level executives to entry-level staff.

##### Step 1: Prepare Your Hierarchical Data

You’ll need an employee table with:

- **Employee ID**
- **Manager ID**
- **Employee Name**

This setup allows you to define relationships using the `PATH()` function.![](99.System/Attachments/Screenshot-2025-06-01-130601.png)

##### Example Table:

| Employee ID | Name | Manager ID |
| --- | --- | --- |
| 1 | John Smith | null |
| 2 | Mike Thompson | 1 |
| 3 | Emily Carter | 2 |

##### Step 2: Create a Hierarchy with DAX

Use the `PATH()` function to trace each employee’s reporting line:

```
Path = PATH(Employee[EmployeeID], Employee[ManagerID])
```

Then, use `PATHITEM()` and `LOOKUPVALUE()` to extract names at each level:

```
Level2 = LOOKUPVALUE(Employee[Name], Employee[EmployeeID], PATHITEM(Employee[Path], 2, INTEGER))
```

Repeat for as many levels as needed.![](99.System/Attachments/Screenshot-2025-06-01-131303.png)

##### Step 3: Visualize in a Matrix (Optional Step)

Before using the decomposition tree, it’s helpful to test your hierarchy in a **matrix visual**:

- Add Level 1, Level 2, etc. to **rows**
- Expand levels to see how the data unfolds
- Use filters to hide blanks at lower levels ![](99.System/Attachments/Screenshot-2025-06-01-131519.png)

##### Step 4: Build the Decomposition Tree

1. Insert the **Decomposition Tree** visual.
2. Drag `Level 1` into the **Analyze** field.
3. Use the **\+ icons** to expand down to `Level 2`, `Level 3`, and so on.
4. Hide the metric values using font color formatting if they’re not meaningful.![](99.System/Attachments/Screenshot-2025-06-01-131910.png)

##### Step 5: Enhance the Visual

##### Custom Styling:

- Use **Conditional Formatting** to distinguish full-time, part-time, or contract employees.
- Format the **bars** to remove confusing value-based widths (use Count Distinct).

##### Tree Connectors:

- Customize connector lines for better readability.

##### Interactive Filters:

- Overlay the top of the visual with a slicer (e.g., by department) for cleaner navigation.![](99.System/Attachments/Screenshot-2025-06-01-132712.png)

##### Step 6: Add a Custom Tooltip

Create a **tooltip report page** with:

- Employee photo
- Key competencies
- Email and phone

Then assign it under:  
**Visual > Format > Tooltip > Report Page**

This enhances interactivity and context.

![](99.System/Attachments/Screenshot-2025-06-01-132536.png)

##### Use PowerPoint to Design Your Button Overlays

Need to hide unwanted UI elements? Use **blank images or shapes from PowerPoint** as overlay tools. Save as PNG/SVG and drop them directly into your report for a clean finish.

##### Final Result

You’ll have a fully interactive, easy-to-read **Power BI organizational chart** that:

- Clearly shows reporting lines
- Supports drill-down navigation
- Integrates tooltips for context
- Looks professional with minimal effort

**Ready to master Power BI and create stunning reports from start to finish?**  
Explore [Data Bear’s Power BI Training Program](https://databear.com/power-bi-training/) —ideal for professionals who want to build smart, scalable business dashboards.