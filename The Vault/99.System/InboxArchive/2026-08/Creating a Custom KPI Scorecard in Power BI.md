---
title: "Creating a Custom KPI Scorecard in Power BI"
source: "https://databear.com/creating-a-custom-kpi-scorecard-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-03-23
created: 2026-08-04
description: "Unlock the potential of your data by creating a custom KPI scorecard in Power BI. Learn how to visualize your KPIs with unique symbols and thresholds for better reporting."
Processed: "Unprocessed"
---
In this post, we’ll explore how to build a custom KPI scorecard using Power BI. The goal is to give you control over how you visualize your KPIs, allowing you to set your own thresholds and utilize unique symbols. By the end, you’ll have a scorecard that not only informs you of trends but also enhances your reporting capabilities.

##### Why Build a Custom Scorecard?

You may wonder why you should create a custom scorecard when there are many pre-built visuals available. The answer lies in the need for control and flexibility. For instance, I recently worked with a client who wanted more control over their KPI thresholds. They desired to set specific thresholds in DAX without writing excessive DAX code and to use their own symbols instead of the standard ones. This need inspired the creation of a custom scorecard.

##### Setting Up Your Data

Before diving into the custom scorecard, let’s set up our data. Imagine you have a matrix filled with various KPI data. The stakeholders consuming these reports often find the sheer volume of numbers overwhelming. They prefer simple visual indicators like arrows to quickly understand trends. For example, they might want to see an up arrow for positive trends, a down arrow for negative trends, and a sideways arrow for stable trends.

![KPI data matrix](99.System/Attachments/KPI_data_matrix.png)

##### Creating Your KPI Value Measure

The first step in building your scorecard is to create a KPI value measure. This measure will be used to compare against your defined thresholds. For our example, let’s use a year-over-year sales calculation. Here’s how you can create the measure:

```
KPI Value = YEAROVERYEAR(SUM(Sales[Amount]))
```

This measure will serve as the basis for your KPI comparisons.

##### Defining KPI Status

Next, we need to define the KPI status. This is crucial for determining how the KPI value relates to the thresholds you’ve set. For instance, you might have a bottom threshold of -5% and a top threshold of 5%. Using the DAX SWITCH function, you can easily manage these thresholds:

```
KPI Status = SWITCH(TRUE(),
    [KPI Value] < -5, -1,
    [KPI Value] > 5, 1,
    0)
```

This setup allows you to manage your KPI statuses efficiently. If you need to change the thresholds later, you only need to update them in one place, and everything else will automatically adjust.

##### Using UNICHAR for Symbols

Now, let’s make our report more visually appealing by incorporating symbols using the UNICHAR function. This function enables you to display specific symbols based on the KPI status. Here’s how to create a measure for the KPI indicator:

```
KPI Indicator = 
VAR UpArrow = UNICHAR(8593)    // Up arrow
VAR DownArrow = UNICHAR(8595)  // Down arrow
VAR SidewaysArrow = UNICHAR(8596) // Sideways arrow
RETURN 
    SWITCH([KPI Status],
        -1, DownArrow,
        1, UpArrow,
        SidewaysArrow)
```

By using this measure, you can quickly show the trend direction with visual symbols.

##### Color Logic for Visual Representation

To enhance the readability of your scorecard, you should also define color logic for your KPI statuses. This logic will help users immediately understand the performance of KPIs:

```
KPI Color = 
SWITCH([KPI Status],
    -1, "Red",
    1, "Green",
    "Yellow")
```

This measure assigns colors based on the KPI status, allowing you to apply conditional formatting in your visuals.

##### Implementing Conditional Formatting

Once you have your KPI indicators and colors ready, the next step is to apply conditional formatting in your Power BI report. You can do this by going to the formatting pane and selecting the KPI value field. Here, set the font color based on the KPI color measure you created earlier. This will visually differentiate the performance of your KPIs.

![Conditional formatting in Power BI](99.System/Attachments/Conditional_formatting_in_Power_BI.png)

##### Adding the KPI Indicator to Your Matrix

Now that your measures are in place, it’s time to add the KPI indicator to your matrix. Copy the existing matrix and replace the KPI Value with the KPI Indicator measure. This change will allow you to see the arrows representing the trends instead of just numbers.

![KPI Indicator in matrix](99.System/Attachments/KPI_Indicator_in_matrix.png)

##### Finalizing Your Scorecard

After setting up the KPI indicators, the last step is to ensure everything is working as intended. You can hover over the KPI indicators to show tooltips with additional details, such as the actual KPI values. To do this, create a report tooltip that links to a detailed page:

```
Report Tooltip = 
    SELECTEDVALUE(Sales[Amount])
```

By implementing this, you give users the ability to delve deeper into the data while keeping the scorecard clean and focused.

##### Conclusion

Creating a custom KPI scorecard in Power BI is a powerful way to visualize your performance metrics. By using DAX measures for KPI values, statuses, and indicators, along with conditional formatting, you can create a dynamic and informative scorecard that meets your specific needs. Whether you’re tracking sales, customer retention, or any other metric, this approach allows for flexibility and clarity in reporting.

If you’re looking to enhance your skills in Power BI, consider checking out [expert-led Power BI training](https://databear.com/power-bi-training/) that can help you master these techniques.