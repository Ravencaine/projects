---
title: "Mastering Supply Chain Analytics: Building a Comprehensive Power BI Dashboard"
source: "https://medium.com/@mohamedaasir1992/mastering-supply-chain-analytics-building-a-comprehensive-power-bi-dashboard-37f9ed408a03"
author:
  - "[[Aasir Waseer]]"
published: 2024-10-13
created: 2026-08-12
description: "In today’s fast-paced business environment, 79% of companies with high-performing supply chains achieve revenue growth superior to the average within their industries. This statistic underscores a critical truth: mastering supply chain analytics is no longer optional — it’s imperative for business success. As supply chains grow increasingly complex, the need for data-driven insights has never been more pressing. In this post, we’ll walk through the process of creating a powerful supply chain dashboard using Power BI, a tool that’s revolutionizing the way we visualize and analyze data."
Processed: "Unprocessed"
---
## In today’s fast-paced business environment, 79% of companies with high-performing supply chains achieve revenue growth superior to the average within their industries. This statistic underscores a critical truth: mastering supply chain analytics is no longer optional — it’s imperative for business success. As supply chains grow increasingly complex, the need for data-driven insights has never been more pressing. In this post, we’ll walk through the process of creating a powerful supply chain dashboard using Power BI, a tool that’s revolutionizing the way we visualize and analyze data.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Gk0ybQl7tg0YmLp6UeqaMg.png)

## Understanding the Data

Our journey begins with the **SCMS\_Delivery\_History\_Dataset**, sourced from [Kaggle’s Supply Chain Shipment Pricing Data](https://www.kaggle.com/datasets/divyeshardeshana/supply-chain-shipment-pricing-data/data). This dataset provides a wealth of supply chain information, including key fields such as delivery dates, shipping modes, product details, and costs. However, like many real-world datasets, it came with its challenges. For instance, the ‘PO Sent to Vendor Date’ field contained inconsistencies, including null values and non-standard date formats. Addressing these data quality issues was our first step toward building a reliable dashboard.

## Data Preparation: Cleaning and Transforming

Before diving into analysis, we needed to address several data quality issues. This crucial step ensures the reliability and accuracy of our insights. Here’s how we tackled some key challenges:

### Cleaning the PO Sent to Vendor Date:

Our dataset had inconsistencies in the ‘PO Sent to Vendor Date’ column, including null values and non-standard formats. We addressed this in Power Query Editor:

- Replaced “Date Not Captured” and “N/A — From RDC” with null values.
- Created a new “Clean PO Date” column using this formula:
```c
if [PO Sent to Vendor Date] = null then null
else if Text.Contains([PO Sent to Vendor Date], "/") then
    try Date.FromText(
        if Text.Length(Text.BeforeDelimiter([PO Sent to Vendor Date], "/")) = 1 
        then "0" & [PO Sent to Vendor Date] 
        else [PO Sent to Vendor Date]
    )
    otherwise null
else null
```

This formula standardizes date formats and handles single-digit months.

**Formatting Other Date Columns:** We ensured all date columns (like ‘Delivered to Client Date’ and ‘Scheduled Delivery Date’) were in a consistent date format.

**Handling Null Values:** For numerical columns, we replaced null values with 0 where appropriate (e.g., in ‘Line Item Insurance (USD)’), and created measures that account for nulls to avoid skewing calculations.

These data cleaning steps, while time-consuming, are crucial for building a trustworthy dashboard. They help prevent misleading insights and ensure that our KPIs accurately reflect the business reality.

### Defining Key Performance Indicators (KPIs)

Choosing the right KPIs is crucial for meaningful supply chain analysis. After careful consideration, we focused on four key metrics:

- **On-Time Delivery Rate**: A critical measure of service quality and reliability.
- **Average Freight Cost per Shipment**: Essential for monitoring cost efficiency.
- **Stock Turnover Rate**: Indicates how efficiently inventory is managed.
- **Days Inventory Outstanding**: Provides insight into the cash conversion cycle.

These KPIs offer a balanced view of supply chain performance, touching on service quality, cost efficiency, and inventory management.

## Dashboard Structure

To present our insights clearly, we opted for a multi-sheet approach:

1. **Overview**: Provides a high-level summary of supply chain performance.
2. **Delivery Performance**: Focuses on delivery timeliness and efficiency.
3. **Cost & Inventory Analysis**: Dives deep into financial and inventory metrics.

This structure allows users to grasp the big picture quickly while also providing the option to explore specific areas in detail.

## Deep Dive: Key Visualizations

Let’s explore two key visualizations that form the backbone of our dashboard:

### On-Time Delivery Trend Line Chart

This chart tracks the On-Time Delivery Rate over time, allowing us to identify trends and seasonality in delivery performance. We used a line chart for this visualization, with time on the x-axis and the On-Time Delivery Rate on the y-axis. This provides an immediate visual cue of performance trends, making it easy to spot improvements or declines in delivery reliability.

### Stock Turnover Rate

This metric required some creative thinking due to limitations in our dataset. We calculated it using the following formula:

```c
Stock Turnover Rate = 
VAR TotalSales = [Total Sales Value]
VAR AvgInventory = [Avg Monthly Inventory Value]
RETURN
    IF(
        NOT ISBLANK(AvgInventory) && AvgInventory <> 0,
        TotalSales / AvgInventory,
        BLANK()
    )
```

We visualized this metric using a multi-row card, displaying both the Enhanced Stock Turnover Rate and the related Days Inventory Outstanding. This provides a quick yet comprehensive view of inventory efficiency.

## Addressing Data Quality

Data quality is paramount in analytics. We incorporated data quality indicators into our dashboard, including a multi-row card showing the percentage of records with valid dates for key fields. This transparency helps users interpret the data with appropriate context and confidence.

Our data cleaning efforts didn’t stop at preparation. We built ongoing data quality monitoring into the dashboard itself. For example, we created a measure to track the percentage of records with valid dates:

```c
Valid Date Percentage = 
DIVIDE(
    COUNTROWS(
        FILTER(
            SCMS_Delivery_History_Dataset,
            NOT ISBLANK(SCMS_Delivery_History_Dataset[Clean PO Date])
        )
    ),
    COUNTROWS(SCMS_Delivery_History_Dataset)
)
```

This measure, visualized as a card on our dashboard, provides users with immediate insight into the completeness of our date data, crucial for time-based analyses.

## Making the Dashboard Interactive

To enhance user experience and allow for deeper insights, we incorporated several interactive elements:

- **Date Range Slicer**: Allows users to focus on specific time periods.
- **Product Group Slicer**: Enables analysis by product category.
- **Shipment Mode Slicer**: Facilitates comparison between different shipping methods.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eUH7z_Ru0gLJHjei4t74hg.png)

These interactivity features transform the dashboard from a static report into a dynamic analytical tool.

## Design Considerations

In designing the dashboard, we prioritized a clean, intuitive layout. We chose a color scheme that’s easy on the eyes for prolonged use, using contrasting colors to highlight key metrics and trends. The consistent layout across sheets helps users navigate the dashboard effortlessly.

## Insights and Action Items

This dashboard opens up numerous possibilities for supply chain optimization. For instance:

1. Sum of Freight Cost (USD):
- Shows significant fluctuations throughout the year
- Peaks around September, with costs exceeding 7M USD
- Lowest point appears to be in April, with costs around 4M USD
- Overall trend seems cyclical, possibly influenced by seasonal factors

2\. Stock Turnover Rate:

- Highly variable throughout the year
- Starts high in January (around 80), drops sharply to April (below 40)
- Recovers and peaks again in September (about 80)
- Ends the year with another sharp rise in December

3\. On-Time Delivery Rate:

- Fluctuates between approximately 0.90 and 0.98 (90% to 98%)
- Lowest point in February, highest in April
- Generally maintains a rate above 0.95 for most of the year
- Slight downward trend visible in the latter half of the year

4\. Freight Cost by Country:

- Nigeria has the highest sum of freight costs
- Followed by Zambia, Côte d’Ivoire, and Rwanda
- There’s a significant drop-off after the top few countries

5\. On-Time Delivery Rate by Shipment Mode:

- Ocean shipments have the highest on-time delivery rate
- Followed closely by air shipments
- Truck shipments have a noticeably lower on-time delivery rate
- N/A category (possibly for mixed or unspecified modes) has the lowest rate

6\. Geographical Distribution:

- Shipments are primarily concentrated in Africa
- Some activity in South America, Middle East, and South Asia
- Little to no activity shown in North America, Europe, East Asia, and Australia

7\. Product Group Analysis:

- ARV dominates in terms of line item quantity
- Other product groups (ACT, ANTM, HRDT, MRDT) show minimal quantities in comparison

These trends suggest seasonal variations in shipping demand and costs, with performance metrics fluctuating accordingly. The focus on African countries and specific product groups (like ARV) implies this could be related to a healthcare or pharmaceutical supply chain, possibly for an international aid organization or a company specializing in medical supplies for developing regions.

## Conclusion

Building an effective supply chain dashboard is both an art and a science. It requires a deep understanding of the business, careful selection of KPIs, thoughtful data preparation, and strategic visualization choices. The dashboard we’ve created not only provides a comprehensive view of supply chain performance but also serves as a launchpad for deeper analysis and data-driven decision-making.

As you embark on your own data visualization journey, remember that the true power of a dashboard lies not just in its ability to display data, but in its capacity to inspire action and drive improvement.

Have you created a supply chain dashboard for your organization? What challenges did you face, and what insights did you uncover? Share your experiences in the comments below — let’s learn from each other and continue to push the boundaries of what’s possible with data analytics.