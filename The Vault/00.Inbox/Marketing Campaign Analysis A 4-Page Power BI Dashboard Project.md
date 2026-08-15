---
title: "Marketing Campaign Analysis: A 4-Page Power BI Dashboard Project"
source: "https://medium.com/@kudehinbusamad/marketing-campaign-analysis-a-4-page-power-bi-dashboard-project-458617f52780"
author:
  - "[[Abdulsamad Kudehinbu]]"
published: 2025-09-25
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
## Introduction / Context

Most of my past projects were focused on sales data. That was good practice, but after a while, I felt stuck in one lane. I wanted to branch out into something new.

That’s what inspired this project — a **4-page Power BI dashboard** analyzing **40,000 rows of marketing campaign data** from 2020 to 2025. It was an opportunity to work with new metrics, address new business questions, and tell a different kind of story.

To make it even more exciting, I didn’t stop at Power BI. After building the dashboard, I also [**wrote SQL queries in Microsoft SQL Server**](https://github.com/Samadkudehinbu/Data-Portfolio/blob/main/Marketing%20Campaign%20Analysis%20Project%20by%20Abdulsamad%20Kudehinbu.sql) to replicate the same results and confirm the accuracy of my analysis. This way, I could validate my insights across both tools.

📊 Click [**here**](https://app.powerbi.com/view?r=eyJrIjoiZGRkYTEzYmUtYjZhMS00ODQ5LWE0M2QtYzEyMzBmZWYwOGYyIiwidCI6IjgxMTQ1ZWNkLTc5NTAtNDk4Ny1hOGFmLTJhMDY1YTgwMWVhYyJ9) to interact with the Dashboard on Power BI Fabric.

## Objective / Problem Statement

The goal was to answer the kind of questions every marketing team asks:

- How do campaigns perform across time?
- Which channels bring the best ROI and CTR?
- How do product categories and regions differ?
- Which audience segments respond best?

## Dataset Description

The dataset included **40,000 rows** with details such as:

- Campaign ID, Manager, Start & End Dates
- Channel, Country, Product Category, Target Audience
- Impressions, Clicks, Conversions, Spend, Revenue

Since 2025 only had January and February, I filtered those out and focused on **2020–2024** for a complete view.

## Data Cleaning & Preparation

I prepared the data in **Power Query** within Power BI:

- Removed incomplete 2025 records
- Checked and removed duplicates
- Standardized date formats and created a calendar table
- Built new metrics with DAX (ROI, CTR, CPC, CPA)

💻 [**See SQL Queries**](https://github.com/Samadkudehinbu/Data-Portfolio/blob/main/Marketing%20Campaign%20Analysis%20Project%20by%20Abdulsamad%20Kudehinbu.sql)

## Exploratory Data Analysis (EDA)

Before building visuals, I explored:

- Annual trends in spend and revenue
- Which channels performed best
- Audience engagement across age groups
- ROI differences between regions
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BV_WU-PR8GMJH53zG7zm7w.png)

Campaign Performance Overview

## Analysis / Modeling

This project wasn’t about machine learning — it was about **data storytelling**.

I created DAX measures for the core KPIs:

- ROI → `(Revenue - Spend) / Spend`
- CTR → `Clicks / Impressions`
- CPC → `Spend / Clicks`
- CPA → `Spend / Conversions`

To stay organized, I wireframed my visuals in PowerPoint before building them in Power BI.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GSPtr8QXMIyG74QQldiJ8g.png)

Channel Effectiveness

After completing the dashboard, I also went one step further:  
I **wrote SQL queries in Microsoft SQL Server** to replicate the same calculations and check whether I’d get the same numbers as Power BI. This gave me extra confidence in my results and helped me strengthen my SQL skills.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*9HKZ6lwbkgKmFLbXz70Ryw.png)

Geographical Insights

## Key Insights & Findings

Here’s what stood out the most:

1. **Google Ads, Social Media, and Influencer campaigns** had the highest click-through rates and conversions.
2. **USA, Australia, and Argentina** showed strong ROI, proving the value of regional targeting.
3. **Millennials engaged more with digital campaigns**, while **Baby Boomers responded to print and radio**.
4. Campaigns grew steadily each year, with conversions up by over **5% in the last year**.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jOUn0iosh63d6WyLUDO9lw.png)

General Summary Table

## Business / Real-World Implications

If this dataset reflected a real business, here’s what the team could do:

- Invest more in Google Ads and Social Media.
- Target Millennials with digital-first strategies.
- Use print and radio more effectively for Baby Boomers.
- Prioritize strong markets like the USA and Australia.

## Limitations

No project is perfect. Some limits here were:

- The dataset only covered 2020–2024.
- Missing context on campaign creativity or competitor activity.
- No direct customer feedback, only performance metrics.

## Conclusion

This project pushed me beyond sales dashboards and into the realm of **marketing analytics**. I built a 4-page dashboard that not only shows performance but also answers strategic questions. And by validating those same results in **SQL**, I proved that my findings were accurate no matter the tool I used. It was both a Power BI and SQL learning experience in one.

## Want to explore further?

- **🔗** [**View Dashboard**](https://app.powerbi.com/view?r=eyJrIjoiZGRkYTEzYmUtYjZhMS00ODQ5LWE0M2QtYzEyMzBmZWYwOGYyIiwidCI6IjgxMTQ1ZWNkLTc5NTAtNDk4Ny1hOGFmLTJhMDY1YTgwMWVhYyJ9)
- **🔗** [**Explore SQL Queries**](https://github.com/Samadkudehinbu/Data-Portfolio/blob/main/Marketing%20Campaign%20Analysis%20Project%20by%20Abdulsamad%20Kudehinbu.sql)
- **🔗** [**Check My Portfolio**](https://www.datascienceportfol.io/kudehinbusamad)
- **🔗** [**Connect with Me on LinkedIn**](https://www.linkedin.com/in/abdulsamad-kudehinbu/)
- **📧 Email Me @kudehinbusamad@gmail.com**