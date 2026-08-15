---
title: "A Simple Trick to Always Display the Latest Month in Power BI (Even After Refresh)"
source: "https://medium.com/microsoft-power-bi/a-simple-trick-to-always-display-the-latest-month-in-power-bi-even-after-refresh-0630fef5e2f3"
author:
  - "[[Isabelle Bittar]]"
published: 2026-02-12
created: 2026-08-09
description: "A practical slicer pattern that automatically updates to the latest data"
Processed: "Unprocessed"
---
## A practical slicer pattern that automatically updates to the latest data

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hQSIFLZGPmre2v_UeROueA.png)

By Isabelle Bittar for KI Data Science

*PBIX available for download at the end of this article! 🥳*

So this is more of a micro-tip — I’ve had to use it recently so thought it could be a good idea to share the idea with others in case you run into the same situation. 🤓

In many reports, users need to:

- View **current data by default**
- But still be able to **go back in time** using a slicer

In those cases, the report usually contains **both current and historical data**, and a slicer defines which time period is being displayed.

### The problem?After a dataset refresh, slicers do not automatically move to the latest period.

If the slicer was initially set to, say, *March 2024*, the report will still open on *March 2024* after refresh — even if new data for *April 2024* is now available.  
Unless you manually change the slicer selection and republish, users won’t see the most recent data.

Here’s a short demo with the visual from the cover image of this article:

[https://youtube.com/shorts/2F\_AiLxL7jo?feature=share](https://www.youtube.com/shorts/2F_AiLxL7jo)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## My usual way of avoiding this problem

In most of my reports, I avoid relying on slicers for “current period” logic altogether.

Instead, my DAX calculations are explicitly based on the **latest available data**. For example, if I have a basic KPI like total profit:

```c
Profit =
SUM ( Sales[Profit] )
```

I’ll often create a second measure that explicitly calculates the value for the **current month**, and use *that* measure in visuals:

```c
Current Profit =
VAR _MaxMonth =
    MAX ( Dates[First Day of Month] )
RETURN
    CALCULATE (
        [Profit],
        FILTER (
            Dates,
            Dates[First Day of Month] = _MaxMonth
        )
    )
```

This way:

- The KPI always reflects the latest month
- No slicer interaction is required
- Refreshing the dataset automatically updates the value

This approach works very well… **as long as you control the measures**.

## But what if the report already relies on slicers?

When I’m doing a **report makeover** 🎨 on an existing report, I don’t always have that luxury.

Sometimes:

- The report already uses slicers extensively
- Users expect to control the time period themselves
- Rewriting all KPIs to bypass slicers would be too disruptive

In those cases, the slicer *is* the mechanism that defines “current” vs “historical” — and we need a way for it to **automatically point to the latest month after refresh**.

That’s where this simple trick comes in.

## The idea: a “sticky” slicer value

Power BI slicers can’t truly be driven by measures.  
But they *can* remember a **text value** that stays selected across refreshes.

So instead of trying to dynamically select *“April 2024”*, we do this:

- Create a column that displays:
- **“This Month”** for the current month
- The **regular Month + Year label** for all other months
- Select **“This Month” once**
- Let the underlying data change on refresh

After refresh:

- The slicer is still set to **“This Month”**
- But *which month* is tagged as “This Month” has changed
- The report automatically opens on the latest data 🎉

## Example: Date table setup

In my Date table that I usually like to create in Power Query, I add:

- A Month + Year label (e.g. *Jan 2026*)
- A First Day of Month column
- A “This Month” column

Conceptually, the logic looks like this:

- If the date belongs to the current month → `"This Month"`
- Otherwise → `"MMM yyyy"`

That single column is what I use in the slicer.

In the case of this demo, here is the Power Query code of the table:

```c
let
    // Reference your fact table
    Source = Sales,

    // Get min and max dates from the fact
    MinDate = Date.StartOfMonth( List.Min( Source[Date] ) ),
    MaxDate = Date.EndOfMonth( List.Max( Source[Date] ) ),

    // Generate continuous date range
    DateList =
        List.Dates(
            MinDate,
            Duration.Days( MaxDate - MinDate ) + 1,
            #duration(1, 0, 0, 0)
        ),

    // Convert to table
    DateTable =
        Table.FromList(
            DateList,
            Splitter.SplitByNothing(),
            {"Date"},
            null,
            ExtraValues.Error
        ),

    // Change type
    ChangeType =
        Table.TransformColumnTypes(
            DateTable,
            {{"Date", type date}}
        ),

    // Add Year
    AddYear =
        Table.AddColumn(
            ChangeType,
            "Year",
            each Date.Year([Date]),
            Int64.Type
        ),

    // Add Month Number
    AddMonthNumber =
        Table.AddColumn(
            AddYear,
            "Month Number",
            each Date.Month([Date]),
            Int64.Type
        ),

    // Add First Day of Month
    AddFirstDayOfMonth =
        Table.AddColumn(
            AddMonthNumber,
            "First Day of Month",
            each Date.StartOfMonth([Date]),
            type date
        ),

    // Add Month + Year label (e.g. Jan 2026)
    AddMonthYear =
        Table.AddColumn(
            AddFirstDayOfMonth,
            "Month",
            each Date.ToText([Date], "MMM yyyy"),
            type text
        ),

    // Add "This Month" column (with year fallback)
    AddThisMonthOrMonthYear =
        Table.AddColumn(
            AddMonthYear,
            "This Month",
            each
                if Date.StartOfMonth([Date])
                    = Date.StartOfMonth(Date.From(DateTime.LocalNow()))
                then "This Month"
                else [Month],
            type text
        )

in
    AddThisMonthOrMonthYear
```

This Date table is fully dynamic and automatically adjusts to the data in the model.

First, it looks at the **minimum and maximum dates** in the Sales table and expands them to the start of the first month and the end of the last month. This ensures the calendar always covers the full range of available data — even after refresh.

It then generates a **continuous daily date list** and adds useful time columns like:

- Year
- Month Number
- First Day of Month
- A formatted Month + Year label (e.g., *Jan 2026*)

Finally — and most importantly — it creates a **“This Month”** column.

If a row belongs to the current month, it’s labeled `"This Month"`. Otherwise, it displays the regular Month + Year label.

Because this column updates on refresh, the slicer can stay selected on **“This Month”**, while the underlying month automatically moves forward.

## Why this works so well

This approach has a few big advantages:

- ✅ No need to republish after every refresh
- ✅ Users still have full control over historical periods
- ✅ The report always opens in the *right* context
- ✅ Very easy to explain and maintain

Most importantly, it makes the dashboard feel **smarter and calmer** — users see the most relevant data immediately, without having to click anything.

## Final thoughts

This isn’t a complex DAX trick or a fancy visual hack — it’s just a small UX improvement.  
But in practice, it’s one of those details that makes a report feel **thoughtful** instead of annoying.

If you often build reports where:

- Data grows over time
- Users want both “latest” and “historical” views
- Slicers are part of the experience

…this is a pattern worth keeping in your toolbox.

**PBIX available of this demo available** [**here**](https://drive.google.com/file/d/1cIPmptceR3Ggg2Wt35ZkUCKtyYZmehY4/view?usp=sharing)**! 🥳**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----0630fef5e2f3---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization, DAX

**Tags:** Tips & Tricks, Tutorial, Data Visualization, DAX