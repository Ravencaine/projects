---
title: "Conditional Formatting in Power BI"
source: "https://databear.com/conditional-formatting-in-power-bi/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2024-06-04
created: 2026-08-04
description: "In this blog post, I’ll cover the basics and provide practical examples of conditional formatting in Power BI."
Processed: "Unprocessed"
---
Let’s dive into the world of **conditional formatting in Power BI**. Whether you’re a seasoned Power BI user or just getting started, understanding how to apply conditional formatting can significantly enhance your visualizations. In this blog post, I’ll cover the basics and provide practical examples.

**Conditional formatting** allows you to dynamically change the appearance of elements in your Power BI visuals based on specific conditions. You can emphasize certain data points, highlight outliers, or create custom formatting rules—all without writing complex DAX expressions. Another reason why conditional formatting in Power BI is powerful is its ability to dynamically adapt to changes in data. As your dataset evolves, the formatting rules remain in place, ensuring that your visualizations always reflect the most relevant insights. Moreover, by using custom expressions and rules, you can create sophisticated formatting logic that goes beyond simple color changes, allowing for more nuanced and context-aware designs.

### Applying Conditional Formatting in Power BI

**1\. Select Your Visual**: Start by choosing the table or matrix visualization you want to format.

![TableMatrix](99.System/Attachments/TableMatrix.png)

**2\. Choose the Field**: On the data pane, choose the data you want in your table. I used sales by day.

![TableSalesByDay](99.System/Attachments/TableSalesByDay.png)

**3\. Decide on the criteria of your conditional formatting:** In my example I want to add condition formatting to the sales on days that it was higher than 6000.

**4\. Pick Your Formatting Type**:

1. - **Background Color**: Change the background color of cells.
		- **Font Color**: Modify the font color of text within cells.
		- **Data Bars**: Represent values as horizontal bars within cells.

**5\. Applying conditional formatting in Power BI:** Click on your table and navigate to the formatting pane, you will see the option so Cell elements, this is where you choose the field that will have the conditional formatting applied and also what type you want to choose.

![Cell_Elements](99.System/Attachments/Cell_Elements.png)

Once you’ve switched the slider to ON, it will by default apply the basic for of the conditional formatting for the type. To configure your rules you need to go to the fx (formula) button

![FXButton](99.System/Attachments/FXButton.png)

Then you get this screen.

![Background Colour](99.System/Attachments/Background_Colour.png)

In my example I want to apply a rule. This is how I am configuring my example.

![Rules in Conditional Formatting](99.System/Attachments/Rules_in_Conditional_Formatting.png)

You can apply this to any of the conditional formatting types. See the example of the different type below.

#### Background Colour

![Background Colour eg](99.System/Attachments/Background_Colour_eg.png)

#### Font Colour

![Font Colour](99.System/Attachments/Font_Colour.png)

#### Icon added

![Icon](99.System/Attachments/Icon.png)

**Practical Examples**

1. **Sales Performance**:
	- Apply a green background to cells with sales above the average.
		- Use red font for sales below the average.
		- Add data bars to visualize sales distribution.
2. **KPI Tracking**:
	- Highlight KPIs that meet or exceed targets using custom colors.
		- Show KPI icons (e.g., thumbs up or down) based on performance.
3. **Conditional Web Links**:
	- Turn URLs into clickable links within your table or matrix.
		- For instance, link product names to their respective web pages.

Remember that conditional formatting enhances readability and draws attention to critical insights. Experiment with different options to find what works best for your specific use case.

In summary, conditional formatting in Power BI empowers you to create visually appealing and informative reports. Whether you’re analyzing sales data, tracking KPIs, or building interactive dashboards, mastering this feature will take your Power BI skills to the next level!

More information on how to format your report can be found [here](https://learn.microsoft.com/en-us/power-bi/visuals/service-tips-and-tricks-for-color-formatting?tabs=powerbi-desktop).

Feel free to experiment and make your reports shine!

Data Bear’s website is a valuable resource for anyone seeking [Power BI training](https://databear.com/power-bi-training/) and other data-related services. Their expertise, practical workshops, and commitment to empowering users make them a top choice for enhancing data skills and leveraging Power BI effectively.

Don’t forget to check out our [training](https://databear.com/power-bi-training/) page and become a Power BI expert.