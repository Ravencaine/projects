---
title: "Exploring Data Analysis with Power BI's Decomposition Tree"
source: "https://databear.com/power-bi-decomposition-tree/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-05-19
created: 2026-08-04
description: "Let's dive right in and explore how you can leverage the Decomposition Tree to uncover insights in your data."
Processed: "Unprocessed"
---
Today, I want to delve into one of the AI visuals within Power BI Desktop: the Decomposition Tree. This powerful tool can significantly enhance your data analysis capabilities. Let’s dive right in and explore how you can leverage the Decomposition Tree to uncover insights in your data.

#### Understanding the Decomposition Tree Visual

The Decomposition Tree visual in Power BI allows you to break down a measure across multiple dimensions, providing a clear hierarchical view of your data. This visual can automatically aggregate your data, enabling you to drill into various dimensions in any order you prefer.

![Understanding the Decomposition Tree Visual](99.System/Attachments/Understanding_the_Decomposition_Tree_Visual.png)

#### Setting Up the Decomposition Tree Visual

To get started, you’ll need to locate the Decomposition Tree visual in your visualization pane. It’s a few rows down and a couple of columns over. Here’s what you need to do to set it up:

1. **Analyze Field:** Drag the metric you want to analyze into this field. This should be a measure or an aggregate to work correctly.
2. **Explain By:** Add the dimensions you want to break down the metric by. These dimensions will help explain the metric in more detail.

For example, let’s use the Adventure Works dataset, a popular bike retailer dataset. We’ll analyze the ‘Profit’ measure and explain it by several dimensions such as ‘Color,’ ‘Model Name,’ ‘Region,’ and ‘Country.’

#### Exploring the Decomposition Tree

Once you have your measure and dimensions set, you can start exploring the data:

1. **Add a Dimension:** Click on the plus sign next to your measure to add a dimension. For instance, if you choose ‘Country,’ you’ll see which countries contribute most to the profit.
2. **Drill Down:** You can further drill down by selecting additional dimensions. For example, after ‘Country,’ you might choose ‘Region’ to see the contribution by different regions within a country.
3. **AI Splits:** Utilize the AI splits to let Power BI’s AI suggest the most significant dimensions. You can choose ‘High Value’ or ‘Low Value’ to see which factors contribute the most or least to your measure.

![Exploring the Decomposition Tree](99.System/Attachments/Exploring_the_Decomposition_Tree.png)

#### Analyzing Specific Scenarios

Let’s break down our profit by ‘Country,’ ‘Region,’ ‘Model Name,’ and ‘Color’:

- **Country**: Shows which countries contribute the most to overall profit.
- **Region**: Within a country, identifies the regions contributing most.
- **Model Name:** Reveals which product models are driving profits in a region.
- **Color**: Indicates which product colors are popular among top-selling models.

For instance, analyzing profit by ‘Country’ might show the US as the top contributor, followed by Australia and the UK. Drilling down into the US, the ‘Southwest’ region might emerge as the highest contributor. Further drilling by ‘Model Name’ and ‘Color’ can reveal specific product trends.

![Analyzing Specific Scenarios](99.System/Attachments/Analyzing_Specific_Scenarios.png)

#### Utilizing AI Splits for Deeper Insights

Instead of manually selecting dimensions, you can let AI do the heavy lifting:

- **High Value:** AI identifies the dimension contributing most to high profit values.
- **Low Value:** AI pinpoints the dimension contributing least.

For example, if the AI split shows ‘Model Name’ as the highest contributing factor over ‘Country,’ it indicates the importance of specific product models in driving profit.

![Utilizing AI Splits for Deeper Insights](99.System/Attachments/Utilizing_AI_Splits_for_Deeper_Insights.png)

#### Responsive Nature of the Decomposition Tree

One of the exciting features of the Decomposition Tree is its responsiveness to filters:

- Filter by Year or Month: The visual updates dynamically based on your selections, allowing you to focus on specific time periods.
- Drill Through: You can set up a drill-through page to see detailed information on a specific data point. For example, drilling through on ‘Mountain 200’ model name can provide more granular insights.

![Responsive Nature of the Decomposition Tree](99.System/Attachments/Responsive_Nature_of_the_Decomposition_Tree.png)

#### Practical Tips

- **Maximum Levels:** The Decomposition Tree supports up to 50 levels, ensuring you can dive deep into your data.
- **Data Points Limit:** It can handle up to 5,000 data points, making it suitable for large datasets.
- **AI Splits Support:** Note that AI splits are not supported for on-premises Analysis Services, Azure Analysis Services, Power BI Report Server, or when published to the web.

![Decomposition Tree](99.System/Attachments/Decomposition_Tree.png)

#### Conclusion

The Decomposition Tree visual in Power BI is a robust tool for dissecting and understanding complex data. Whether you manually select dimensions or leverage AI splits, this visual can provide valuable insights into your dataset.

Visit our [training page](https://databear.com/power-bi-training/) to learn more and take advantage of special discounts on our learning subscriptions. Happy analyzing!