---
title: "The Power BI Chart That Breaks All the Rules (And Why You’ll Love It)"
source: "https://medium.com/learning-data/the-power-bi-chart-that-breaks-all-the-rules-and-why-youll-love-it-72de231a4571"
author:
  - "[[Ankann Bandyopadhyay]]"
published: 2025-09-06
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
*How to combine monthly data, averages, and totals in one stunning stacked column chart that actually makes sense*

— — — — — — — — — — — *🎁PBIX included at the end — — — — — — — — — —*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DBicj7kxpnqUYp4lBL7PEA.png)

The All-in-One Frankenstein Chart

**Picture this:** Your boss walks into the Monday morning meeting and asks, “Can you show me the monthly injury trends, the overall average, AND the total count all in one chart? And split by gender, too?”

Most analysts would either create three separate visuals or politely explain why that’s impossible. But what if I told you there’s a way to do exactly that — and make it look amazing?

Welcome to the world of **hybrid stacked column charts** in Power BI. Today, we’re going to break some conventional charting rules and create something that’s both visually stunning and incredibly informative.

## The Challenge: Three Stories, One Chart

Traditional charts force us to choose between showing monthly trends, totals, or averages. But real business questions don’t work that way. Stakeholders want to see the forest AND the trees, all at once.

Our sports injury dataset presents exactly this challenge:

- **Monthly injury counts** (the trend story)
- **Average injuries per month** (the performance benchmark)
- **Total injuries** (the big picture number)
- All split by **Male vs Female** athletes

## The Data

The dataset used for this presentation is taken from the [**FP20 Analytics Challenge 29 Sports Injury Analysis**](https://fp20analytics.com/datasets/)

## The Data Model

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UmkLXQ9Lk-cM9IEZvz-rnA.png)

The original Data model didn’t have Date\_Table, Month\_Table and Measures Tables

## The Secret Sauce: A Custom Month Table

Here’s where we get creative. Instead of using a standard date table, we’re going to create a hybrid table that includes both actual months AND our summary metrics.

```c
Month_Table = 
DISTINCT(
    UNION(
        SELECTCOLUMNS(DateTable,
            "Month Name", [Month],
            "Month Number", [MonthNo]
        ),
        DATATABLE(
            "Month Name", STRING, 
            "Month Number", INTEGER, 
            {
                {" ", 13}, 
                {"Average", 14}, 
                {"Total", 15}
            }
        )
    )
)
```

**What’s happening here?** We’re creating a Frankenstein table that combines:

- Months 1–12 (Jan through Dec)
- A blank space (month 13) for visual separation
- Average (month 14)
- Total (month 15)

This provides us with a continuous x-axis that seamlessly transitions from monthly data to summary metrics — genius!

## The Foundation: Your Basic Building Blocks

Before we get fancy, let’s establish our base measures:

```c
Total Injuries = COUNTROWS(FactInjuries)
```
```c
AvgNoofInjuries = 
  DIVIDE(
    [Total Injuries], 
    DISTINCTCOUNT(DateTable[Month])
  )
```

Nothing revolutionary here — just clean, simple measures that do what they say.

## The Magic Measure: Making It All Work Together

Now comes the fun part. We need a measure that can display monthly values, averages, AND totals, all while keeping the chart proportions readable:

```c
Injuries_New = 
VAR Total_ = 
    CALCULATE([Total Injuries], ALL(Month_Table)) 
VAR Average_ = 
    CALCULATE([AvgNoofInjuries], ALL(Month_Table)) 
VAR MaxMonthly = 
    MAXX(
        FILTER(
            ALL(Month_Table),
            Month_Table[Month Number] <= 12
        ),
        [Total Injuries]
    )
VAR ProportionalMultiplier = 
    IF(Total_ > 0 && MaxMonthly > 0, (MaxMonthly * 1.5) / Total_, 0.12)
VAR Result_ = 
    SWITCH( 
        SELECTEDVALUE(Month_Table[Month Name]), 
        "Total", Total_ * ProportionalMultiplier, 
        "Average", Average_, 
        [Total Injuries] 
    ) 
RETURN 
    IF(Result_ = BLANK(), " ", Result_)
```

**Breaking it down:**

- **Total\_**: Gets the grand total across all months
- **Average\_**: Gets our average calculation
- **MaxMonthly**: Finds the highest monthly value
- **ProportionalMultiplier**: Here’s the secret sauce! This scales down the total bar so it doesn’t dwarf the monthly bars
- **SWITCH**: Routes the right calculation to the right “month”

The proportional multiplier ensures your total bar is always visible and meaningful compared to monthly values — no more microscopic monthly bars!

## The Values Behind the Bars

Users love to see actual numbers, not just bar heights. That’s where our companion measure comes in:

```c
Injuries_Value = 
VAR Total_ = CALCULATE([Total Injuries], ALL(Month_Table)) 
VAR Average_ = CALCULATE([AvgNoofInjuries], ALL(Month_Table)) 
VAR Result_ = 
    SWITCH( 
        SELECTEDVALUE(Month_Table[Month Name]), 
        "Total", Total_, 
        "Average", Average_, 
        [Total Injuries] 
    ) 
RETURN 
IF( 
    Result_ = BLANK(), " ", 
    Result_ 
)
```

This gives you the *actual* values to display as data labels while `Injuries_New` handling the visual proportions. Clean separation of concerns!

## Bringing It All Together

Now for the assembly:

1. **X-Axis**: Month Name from Month\_Table
2. **Y-Axis**: Injuries\_New measure
3. **Legend**: Gender from DimPlayer
4. **Data Labels**: Injuries\_Value measure
5. **Slicer**: Year from DateTable

The result? A chart that flows seamlessly from January through December, then shows your average and total with perfect visual proportions.

## Why This Approach Wins

**For Stakeholders:**

- One chart tells three stories
- Easy to spot trends AND see big picture numbers
- Gender comparison is crystal clear
- Professional, polished appearance

**For Developers:**

- Flexible framework for similar requirements
- Clean, maintainable DAX
- Reusable across different datasets
- No complex custom visuals required

**For Performance:**

- Efficient calculations
- Minimal data model impact
- Fast rendering

## Pro Tips for Implementation

1. **Test your proportional multiplier**: The 1.5 factor works well for most datasets, but adjust based on your data range
2. **Consider your blank space**: The empty “month 13” creates visual breathing room — experiment with this
3. **Color coordination**: Use consistent colors for male/female across all chart sections
4. **Data labels**: Always show actual values, not the proportionally adjusted ones

## The Bottom Line

Sometimes the best solutions come from breaking conventional rules. This hybrid approach proves that with creative DAX and smart data modeling, you can build charts that are both beautiful and brilliantly functional.

Your stakeholders get their comprehensive view, you get to showcase advanced Power BI skills, and everyone wins with clearer insights.

Ready to revolutionize your reporting? Give this technique a try and watch your audiences react when they see monthly trends, averages, and totals all dancing together in perfect harmony.

**Now, as promised, here is the link to the** [***PBIX file***](https://github.com/Ankan2508/All-in-One-Frankenstein-Chart)

*What creative charting challenges are you facing? Drop a comment below — I’d love to help you break more rules and build better visuals!*

**About the Author**: Hi, I’m **Ankan Bandyopadhyay,** a data visualization enthusiast/ Power BI Developer who believes that the best charts are the ones that disappear, leaving only the insights behind. Connect with me on [**LinkedIn**](http://www.linkedin.com/in/bandyopadhyay-ankan) to discuss data storytelling and visualization design.

***If you like my work, then*** [***buy me a coffee***](https://buymeacoffee.com/ankanbandyopadhyay) ***💓***

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*