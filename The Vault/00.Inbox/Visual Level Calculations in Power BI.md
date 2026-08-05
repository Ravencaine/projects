---
title: "Visual Level Calculations in Power BI"
source: "https://databear.com/visual-level-calculations-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-02-24
created: 2026-08-04
description: "Visual level calculations are a game-changer, especially for new Power BI users or those who struggle with DAX."
Processed: "Unprocessed"
---
Many Power BI users enjoy the initial thrill of working with the platform and discovering its potential. However, that thrill can fade quickly when they encounter the need to write their first DAX measure. Understanding concepts like filter context, row context, and context transition can be a major hurdle, especially for users who don’t code on a regular basis. That’s where the new visual level calculations come to the rescue, simplifying DAX for everyone!

![Visual Level Calculations in Power BI](99.System/Attachments/Visual_Level_Calculations_in_Power_BI.png)

### What are Visual Level Calculations?

Visual level calculations introduce a new, intuitive way to create DAX formulas directly within Power BI visuals. With a simplified interface and helpful templates, these calculations eliminate the complexities of traditional DAX, allowing users to perform common tasks like running totals, moving averages, and comparisons with just a few clicks.

### Getting Started (Prerequisites) with Visual Level Calculations

To start using visual level calculations:

1. **Update:** Make sure you’re using Power BI Desktop (February 2024 update or later).![Power BI Updated Feb 2024](99.System/Attachments/Power_BI_Updated_Feb_2024.png)
2. **Enable:** Go to **File** > **Options and Settings** > **Options** > **Preview features** and enable the **Visual calculations** option.![New Visual Calculation](99.System/Attachments/New_Visual_Calculation.png)

**Let’s Try It Out!**

Imagine a Matrix visual showing sales actuals over time. Here’s how to add a visual level calculation:

1. **Home Tab:** In the **Calculations** group, click **New calculation**.![New Calculation ](99.System/Attachments/New_Calculation_.png)
2. **Formula Bar:** At the top, you’ll see your visual. At the bottom, you can add your calculation.![Formula Bar: ](99.System/Attachments/Formula_Bar!_.png)
3. **Templates:** For first-time users, the provided templates are a great guide.![Template](99.System/Attachments/Template.png)

### Templates for Common Calculations

#### ● Running Calculations (Running Sum)

- **Purpose**: Tracks the cumulative total of a value over time.
- **Example**:
	- Monthly sales figures with a column showing the year-to-date running sales total.
		- Number of new customers each week, with a column showing the total customers acquired thus far.

#### ● Rolling Calculations (Moving Average)

- **Purpose**: Smooths out fluctuations in data by calculating the average over a specified previous period.
- **Example**:
	- A line chart of daily website traffic, with a moving average line showing the trend over a 7-day period.
		- Stock prices with a 30-day moving average to help identify trends and filter out short-term noise.

#### ● Level of Detail Calculations

##### Percent of Parent/Subtotal

- **Purpose**: Calculates what percentage an individual value makes up of a larger group (subcategory vs. category)
- **Example**: A breakdown of sales by product. A column displaying each product’s contribution to the overall category sales.

##### Percent of Grand Total

- **Purpose**: Shows what percentage an individual value contributes to the overall total across all categories.
- **Example**: Sales by region, with a column indicating each region’s percentage of the total sales for the company.

#### ● Comparisons

##### Versus Previous/Next

- **Purpose**: Calculates the difference between the current period and the previous/next period.
- **Example**: Monthly sales with change vs. the previous month.

##### Versus First/Last

- **Purpose**: Calculates the difference between the current period and the first/last period within a defined range.
- **Example**: Quarterly earnings figures with a column showing the difference from the first quarter of the year.

**Key Benefits of Visual Level Calculations**

- **Intuitive Interface:** Replace complex DAX syntax with simple references and templates.
- **Faster Calculations:** Create common calculations in seconds.
- **Easier to Understand:** Improve readability and maintainability of your calculations.

### Additional Tips and Observations on Visual Level Calculations

**Formatting**

- **Importance:** While visual level calculations help with the logic, you may still need to fine-tune how the results are displayed (currency, percentages, number of decimal places, etc.).
- **The** FORMAT **Function:** Use the FORMAT function within your calculations to control the display format.
	- Example: FORMAT(\[Sales Difference\], “Currency”)
- **Resources:** Find a list of common formatting strings for the FORMAT function on [Microsoft’s documentation or DAX guide websites.](https://learn.microsoft.com/en-us/dax/)

**Conditional Actions**

- **Beyond Basic Calculations:** IF statements let you customize how values are displayed based on conditions.
- **Example 1:** Showing “N/A” when there’s no previous period for comparison:

IF(ISBLANK(PREVIOUS(\[Sales Actual\])), “N/A”, \[Sales Actual\] – PREVIOUS(\[Sales Actual\]))

- **Example 2:** Highlight values with a background color based on a threshold:
	- (This would be for conditional formatting, currently not directly supported, but a workaround exists using measures)

**New Functions**

- PREVIOUS**:** Retrieves the value from a previous row within the same partition (e.g., by month, by product category).
- COLLAPSE**:** Calculates aggregates at a higher level, excluding certain details. Think of it as the opposite of “drill-down”.
- EXPAND**:** Works in tandem with COLLAPSE to calculate values at a more detailed level than the current visual.

**Custom Visuals**

- **Compatibility:** Most well-developed custom visuals from reputable sources should support visual level calculations. This greatly expands your visualization options!
- **Testing:** It’s always a good practice to check the custom visual’s documentation to confirm compatibility or test it first.

**Calculation Groups**

- **Time Intelligence:** Calculation groups provide a robust way to create time-based calculations (YTD, MTD, etc.) with a single measure that can be reused.
- **Synergy:** Combine them with visual level calculations for even more sophisticated analysis. For example:
	- Calculate a moving average with a visual level calculation.
		- Use a calculation group to easily view the moving average YTD, MTD, etc.

**Limitations and Future Developments**

Visual level calculations are still in their early stages. Here’s what to expect and hope for in the future:

- **Advanced Calculations:** More functions for running averages, sums, maximums, etc.
- **Number Formatting:** Built-in options for controlling formatting.
- **Integration:** Better connections with measures, field parameters, conditional formatting, and reference lines.

Visual level calculations are a game-changer, especially for new Power BI users or those who struggle with DAX. While there are still improvements to be made, this feature is a giant leap forward in making Power BI more accessible to everyone!

Remember to check out the Data Bear training **[page](https://databear.com/power-bi-training/)** for some awesome courses.