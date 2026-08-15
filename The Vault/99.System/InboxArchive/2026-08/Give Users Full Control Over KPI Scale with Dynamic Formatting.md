---
title: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-17
created: 2026-08-08
description: "Executive Summary One of the most common friction points in BI reporting is number scaling. Executives often prefer high-level views in Millions or"
Processed: "Unprocessed"
---
**Executive Summary** One of the most common friction points in BI reporting is number scaling. Executives often prefer high-level views in **Millions** or **Billions** to spot trends, while analysts need **Actual** values to reconcile data or investigate anomalies.

Power BI’s default visual settings force us to choose: stick with "Auto" (which offers no user control) or hardcode display units to K, M, or B (which forces a single scale for everyone).  

In this post, I’ll show you how to use **Dynamic Format Strings** to give your users full, interactive control over how they view their data—without duplicating measures or cluttering your report.  

**The Problem: The "One-Size-Fits-None" Format**

Typically, we rely on the **Display units** setting in the visual options. While functional, it has significant limitations:

- **Auto** formatting is unpredictable and lacks user control.
- **Fixed units** (e.g., Millions) might look great for a full-year total but render smaller monthly values as $0.0M.
- **Duplicate Measures** (e.g., "Sales (M)" vs "Sales (Actual)") create technical debt and confuse self-service users.

**The Solution: User-Driven Dynamic Formatting**

By leveraging Dynamic Format Strings, we can change how a measure *looks* without changing the underlying calculation. This allows a single measure to toggle between Actuals, Thousands, Millions, and Billions based on a simple slicer selection.

Here is the step-by-step implementation guide.  

**Step 1: Create a Scale Dimension Table**

First, we need a disconnected table to feed our slicer. This table defines the scale options and an ID for sorting. You can create this directly in DAX:

```markup
Scale =

        DATATABLE

         (   

          "Scale Name", STRING,  

          "Scale ID", INTEGER, 

          { 

           { "Actuals", 1 },

           { "Thousands", 2 },

           { "Millions", 3 },

           { "Billions", 4 }

          }

         )
```

Tip: Sort the 'Scale Name' column by 'Scale ID' to ensure the slicer options appear in a logical order (Smallest to Largest) rather than alphabetically.

![Natarajan_M_0-1784122688237.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355639iE064926AF580DDEA/image-size/medium?v=v2&px=400 "Natarajan_M_0-1784122688237.png")

Control Scale Table  

**Step 2: Capture the User’s Selection**

Next, create a measure to read the slicer selection. This will drive our formatting logic:

```markup
Selected Scale = SELECTEDVALUE ( 'Scale'[Scale Name] )
```

**Step 3: Create Your Base Measure**

Write your KPI measure as you normally would. Do not divide it by 1000 or 1,000,000 inside the DAX logic. Keep the number whole.

```markup
Total Profit = SUM ( Financials[Profit] )
```

**Step 4: Apply the Dynamic Format String**

This is where the magic happens.

1. Select your measure (Total Profit) in the **Data** pane.
2. In the **Measure Tools** ribbon, change the **Format** dropdown from *General* (or Currency) to **Dynamic**.
3. A new DAX formula bar will appear for the format string. Paste in the following logic:
```markup
SWITCH (

        [Selected Scale],

         "Thousands", "$#,##0,.00",

         "Millions", "$#,##0,,.00",

         "Billions", "$#,##0,,,.00", 

         "Actuals", "$#,##0.00", 

         "$#,##0,,.00" -- Default fallback (e.g., Millions)

       )
```

Format: Dynamic

*Note the comma placement:,.00 divides by a thousand,,,.00 divides by a million, etc.  
  
*

**Why This Matters**

This technique offers immediate benefits for both developers and end-users:

- **Improved UX:** Users get a self-service experience where they control the granularity of the data.
- **Cleaner Semantic Models:** You no longer need separate measures for "Sales (M)" and "Sales (k)," reducing technical debt.
- **Consistency:** The underlying calculation remains the same across all visuals, ensuring data integrity.

![Natarajan_M_2-1784122688242.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355640iEEAA5A534A5E5569/image-size/medium?v=v2&px=400 "Natarajan_M_2-1784122688242.png")

Showing in Actual Dollars

![Natarajan_M_0-1784122752277.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355641i568417B5718ADC3F/image-size/medium?v=v2&px=400 "Natarajan_M_0-1784122752277.png")

Showing in Thousands

![Natarajan_M_1-1784122762745.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355642i00042E00ACE84E91/image-size/medium?v=v2&px=400 "Natarajan_M_1-1784122762745.png")

Showing in Millions  

**Bonus Use Case: Multi-Currency Reporting**

You can extend this logic beyond just scaling numbers. This same pattern works perfectly for **Multi-Currency Reporting**. By creating a Currency table (USD, EUR, GBP) and using a similar SWITCH statement, you can dynamically change the currency symbol (e.g., $ vs €) based on user selection, all within a single measure.  

**Final Thoughts**

Dynamic format strings are a powerful, often underused feature in Power BI. By combining them with a simple parameter table, you can bridge the gap between executive summaries and analyst-level detail, delivering a truly modern and flexible BI experience.

Custom Formatting.pbix

Top Kudoed Posts

| Subject | Kudos |
| --- | --- |
| ## Data Days \| Create | 58 |
| ## Data Days \| Connect | 47 |
| ## Power BI Dataviz World Champs \| Round 3 | 29 |
| ## Power BI Dataviz World Champs Barcelona \| Round 2 | 26 |
| ## Power BI Dataviz World Champs Barcelona \| Round 1... | 23 |

[View All](https://community.fabric.microsoft.com/t5/forums/kudosleaderboardpage/board-id/community_blog/timerange/one_month/page/1/tab/posts)

Latest Articles

- [Need a Running Total for Just One Chart? Power BI'...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Need-a-Running-Total-for-Just-One-Chart-Power-BI-s-Visual/ba-p/5342327)
- [Data Days Contests | Announcing SQL + AI Promptath...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Data-Days-Contests-Announcing-SQL-AI-Promptathon-Winners/ba-p/5341906)
- [The Hidden Architecture of Power BI Publishing Exp...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/The-Hidden-Architecture-of-Power-BI-Publishing-Explained/ba-p/5333695)
- [Power BI Dataviz World Champs Barcelona | Round 2...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-2-Winners/ba-p/5332826)
- [Power BI Copilot Custom Instructions: Prep Data fo...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Custom-Instructions-Prep-Data-for-AI/ba-p/5332193)
- [Power BI Dataviz World Champs | Round 3](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Round-3/ba-p/5323477)
- [Community Sticker Challenge Barcelona 2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Community-Sticker-Challenge-Barcelona-2026/ba-p/5311346)
- [Power BI Copilot Set Limits](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Set-Limits/ba-p/5321290)
- [Tired of Viewers Clicking "+" on Every Row? Power...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Tired-of-Viewers-Clicking-quot-quot-on-Every-Row-Power-BI-s/ba-p/5322597)
- [Power Bi Alerts with DAX at Power Automate](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-Bi-Alerts-with-DAX-at-Power-Automate/ba-p/5314017)

Archives

- [08-02-2026 - 08-08-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/8-2-2026%2012%3A00%20AM)
- [07-26-2026 - 08-01-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-26-2026%2012%3A00%20AM)
- [07-19-2026 - 07-25-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-19-2026%2012%3A00%20AM)
- [07-12-2026 - 07-18-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-12-2026%2012%3A00%20AM)
- [07-05-2026 - 07-11-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-5-2026%2012%3A00%20AM)
- [06-28-2026 - 07-04-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-28-2026%2012%3A00%20AM)
- [06-21-2026 - 06-27-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-21-2026%2012%3A00%20AM)
- [06-14-2026 - 06-20-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-14-2026%2012%3A00%20AM)
- [06-07-2026 - 06-13-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-7-2026%2012%3A00%20AM)
- [05-31-2026 - 06-06-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-31-2026%2012%3A00%20AM)
- [05-24-2026 - 05-30-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-24-2026%2012%3A00%20AM)
- [05-17-2026 - 05-23-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-17-2026%2012%3A00%20AM)
- [05-10-2026 - 05-16-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-10-2026%2012%3A00%20AM)
- [View Complete Archives](https://community.fabric.microsoft.com/t5/blogs/blogarchivespage/blog-id/community_blog)