---
title: "Power BI Static Tables in 3 Easy Steps"
source: "https://databear.com/power-bi-static-tables-in-3-easy-steps/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-01-21
created: 2026-08-04
description: "Static tables, immune to the refreshing tides, offer a stable foundation for analysis and enhance clarity like seasoned navigators. This blog equips you with the tools to craft these reliable companions."
Processed: "Unprocessed"
---
Ready to infuse your Power BI reports with unwavering data anchors? Static tables, immune to the refreshing tides, offer a stable foundation for analysis and enhance clarity like seasoned navigators. This blog equips you with the tools to craft these reliable companions, empowering you to:

- Navigate the Simplicity of Enter Data: Perfect for small, readily available tables, copy your data from Excel or another source and paste it directly into Power BI Desktop. Define data types in Power Query Editor for seamless integration.
- Master the Flexibility of ROW and UNION: For larger, more intricate tables, unleash the dynamic duo of ROW and UNION. Define each column header and value with the ROW function, then stack your meticulously crafted rows like lego blocks using UNION to build your complete table.
- Embrace the Elegance of DATATABLE: Craving syntactic finesse? DATATABLE awaits. Define your column names and data types once, then nestle your rows within curly brackets – a symphony of data at your fingertips. This method shines for tables with numerous rows, minimizing redundancy and maximizing clarity.

Let’s embark on this practical journey!

1. #### Enter Data The Quick and Easy Route to Static tables
- Step 1: Prepare your data in Excel or another source. Ensure it’s a small, readily available table.
- Step 2: Open Power BI Desktop.
- Step 3: Click “Home” > “Enter Data.”
- Step 4: Paste your data directly into the window.

![Enter Data The Quick and Easy Route to Static tables](99.System/Attachments/Enter_Data_The_Quick_and_Easy_Route_to_Static_tables.png)

- Step 5: Define the data types for each column in the Power Query Editor. Click the column header, then choose the appropriate type (e.g., whole number, text).
- Step 6: Load the table by clicking “Close & Apply” or press Ctrl+Enter.

![Apply and close](99.System/Attachments/Apply_and_close.png)

2. #### ROW and UNION: Building Blocks of Complexity
- **Step 1:** Open Power BI Desktop and navigate to the Modeling tab.
- **Step 2:** Click “New Table” and choose “Blank Table.”
- **Step 3:** In the formula bar, type row (, then define your first column header and its value within parentheses (e.g., row (“Category”, “Condiments”),). Repeat for each column.
- **Step 4:** Press Enter after the final value to create the first row.
- **Step 5:** For additional rows, simply type, followed by another row ( function with its column headers and values.
- **Step 6:** To combine rows, type union ( before the first row ( function of your second row. Repeat for subsequent rows.
- **Step 7:** Press Enter to see your complete table materialize!
3. #### DATATABLE: A Symphony of Conciseness
- **Step 1:** Open Power BI Desktop and navigate to the Modeling tab.
- **Step 2:** Click “New Table” and choose “Blank Table.”
- **Step 3:** In the formula bar, type datatable (, then define your column names and data types within parentheses (e.g., datatable (Category: category, Product: text, Total Sales: integer).
- **Step 4:** Within curly brackets, list your rows, each containing values in the defined order (e.g., {{“Condiments”, “Ketchup”, 20}, {“Dairy”, “Milk”, 15}}).
- **Step 5:** Press Enter to witness your elegant static table come to life!

##### Bonus Tip: Unleash the Power of Dynamic Expressions

Integrate dynamic expressions within ROW functions to link table values to existing measures in your report. This allows your static table to subtly adapt, reflecting changes in your data without compromising its inherent stability.

Remember: Choose the method that best suits your table size, complexity, and desired level of dynamism. With practice and exploration, you’ll become a master architect of static tables, empowering your reports with unwavering data foundations.

So, embark on your Power BI static table journey today! Craft them with passion, and watch your reports blossom into havens of stability and insight.

This blog equips you with the practical skills to build static tables in Power BI, empowering you to transform your reports into reliable and insightful masterpieces.

Remember to check out the Data Bear training **[page](https://databear.com/power-bi-training/)** for some awesome courses.

The Microsoft **[page](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-new-card?tabs=On-the-ribbon)** show in more detail how to manage the formatting.