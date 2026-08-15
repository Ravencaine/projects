---
title: "Conditional Formatting in Power BI Multi-Row Card Visuals"
source: "https://databear.com/power-bi-multi-row-card-visuals/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-03-17
created: 2026-08-04
description: "Welcome to our blog! Today, we're diving into a common frustration for Power BI users: adding conditional formatting to a Multi-Row Card Visuals."
Processed: "Unprocessed"
---
### Introduction

Welcome to our blog! Today, we’re diving into a common frustration for Power BI users: adding conditional formatting to a Multi-Row Card Visuals. It’s a feature many have struggled with, including myself. But fret no more! In this post, I’ll walk you through a workaround solution that will change the way you use Power BI. So, let’s get started and make your data visualization more dynamic and intuitive!

### Understanding Conditional Formatting in Power BI

Conditional formatting in Power BI allows you to highlight important aspects of your data visually. For instance, when dealing with profit growth, we can easily apply conditional formatting in a table visual to see which numbers are above or below a certain threshold. Typically, you’d right-click on the desired field, choose conditional formatting, and set your rules. For example, setting a green arrow for positive growth and a red arrow for negative growth can quickly convey the performance trend at a glance.

### The Challenge with Multi-Row Card Visuals

However, when we switch to a Multi-Row Card Visual, the option for conditional formatting mysteriously disappears. This limitation can be a stumbling block if you prefer the clean layout of multi-row cards for dashboard summaries. The absence of conditional formatting in this visual type has been a notable gap in Power BI’s feature set.

### Innovative Workaround Using DAX and UNICHAR

Fear not, as there is a creative workaround to this issue! The solution involves the use of DAX, Power BI’s formula language, and a function called UNICHAR. By creating a new measure and applying UNICHAR, we can integrate icons (like green and red circles) to visually represent data trends directly within the Multi-Row Card Visual.

### Step-by-Step Guide to Implement the Solution

1. #### Creating Measures with DAX for Conditional Formatting in Power BI

In this section, we’ll delve into the process of creating a new measure in Power BI that employs DAX to enable conditional formatting within Multi-Row Card Visuals. Specifically, we will use green and red circles to signify positive and negative profit growth, respectively. This method leverages the UNICHAR function to integrate these color-coded indicators based on the performance metrics. Here’s how you can do it:

1. **Open Power BI Desktop** and navigate to your report.
2. **Create a New Measure:** Right-click on your data table in the Fields pane and select New measure.
3. **Enter the DAX Formula:** In the formula bar, start defining your measure. We will name it ProfitGrowthIndicator for clarity. Here’s the DAX formula you can use:

![ DAX for Conditional Formatting in Power BI](99.System/Attachments/_DAX_for_Conditional_Formatting_in_Power_BI.png)

In this formula:

- VAR is used to declare variables for the green and red circles, with UNICHAR function calls to get the respective circle symbols.
- IF statements are used to determine which color circle to display based on the Profit Growth measure. If the profit growth is positive, the green circle is shown; if negative, the red circle appears.

Apply the Measure to your Visual: Drag the ProfitGrowthIndicator measure into your Multi-Row Card Visual or any other visual where you want to see this conditional formatting.

### 2\. Incorporating the Measure into the Visual

Once the measure is created, you can incorporate it into a Multi-Row Card Visual in Power BI to display conditional formatting:

1. **Go to the report view** in Power BI Desktop.
2. **Create a Multi-Row Card Visual** if you haven’t already done so by selecting the Multi-Row Card icon from the Visualizations pane.
3. **Add the newly created measure** to the Multi-Row Card by dragging the Profit Growth Indicator measure into the Values field of the visual.

Initially, this will display just the green and red circles in the Multi-Row Card Visual. To add context and make the visual more informative, you also need to display the actual profit growth numbers alongside the colored circles:

1. **Drag the Profit Growth measure** into the Multi-Row Card Visual as well.
2. **Adjust the formatting** of the Multi-Row Card Visual to ensure that the data is clearly displayed, and the icons are correctly aligned with the numbers.

![Incorporating the Measure into the Visual](99.System/Attachments/Incorporating_the_Measure_into_the_Visual.png)

### 3\. Enhancing the Measure for Clarity

To make the measure more informative, we can enhance it by appending the actual profit growth percentage next to the visual indicator (circles). This step involves modifying the DAX formula to concatenate the visual indicator with the numerical profit growth data, ensuring the number is properly formatted as a percentage and rounded for better readability.

Here’s how you can enhance the DAX measure:

![Enhancing the Measure for Clarity Muticard](99.System/Attachments/Enhancing_the_Measure_for_Clarity_Muticard.png)

In this formula, FORMAT(\[Profit Growth\], “0.0%”) converts the profit growth number into a percentage format, rounding to one decimal place. The & ” ” operator is used to add a space between the circle and the percentage, making the display clearer.

### 4\. Final Adjustments for Usability

To ensure the visual remains clean and informative, especially in cases where there might be blank values or years without data, we ensure the measure handles these scenarios gracefully. This is already taken care of in the enhanced measure above with the ISBLANK(\[Profit Growth\]) condition, which returns a blank if the profit growth value is not available, avoiding misleading indicators.

### 5\. Expanding the Solution

The method is flexible and can be expanded to use different visual indicators, such as up and down arrows, instead of circles. This allows users to choose their preferred style for representing data trends.

To implement this with up and down arrows, you would use the respective UNICHAR codes for these symbols in the DAX measure:

![Expanding the Solution Multi-Row Card Visuals](99.System/Attachments/Expanding_the_Solution_Multi-Row_Card_Visuals.png)

This measure uses the up arrow (UNICHAR(9650)) to indicate positive growth and the down arrow (UNICHAR(9660)) for negative growth. Users can then choose between the circle indicators or arrow indicators based on their preference and the specific requirements of their Power BI reports.

### Conclusion

With this innovative approach, we’ve bridged the gap in Power BI’s functionality, enabling conditional formatting in Multi-Row Card Visuals. This method not only enhances the aesthetic appeal of your reports but also improves the ease of data analysis. I hope this guide helps you make the most of your Power BI dashboards.

Don’t forget to visit our [training page](https://databear.com/power-bi-training/) to learn all you can about Power BI. Also see our other blog posts [page](https://databear.com/blog/).