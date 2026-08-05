---
title: "Power BI Time Hacks: Mastering Dynamic Date Views"
source: "https://medium.com/microsoft-power-bi/power-bi-time-hacks-mastering-dynamic-date-views-20c26275bd2e"
author:
  - "[[Isabelle Bittar]]"
published: 2024-01-14
created: 2026-08-02
description: "Unlock the Secrets to Flexible Daily, Weekly, Monthly Analysis in Your Dashboards"
Processed: "Unprocessed"
---
## Unlock the Secrets to Flexible Daily, Weekly, Monthly Analysis in Your Dashboards

![](99.System/Attachments/1!zy5Zexv8h-MnwqOp07EFvg.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

### Introduction

“Can we get the same chart but with a weekly view? And daily?” Do these requests sound familiar to you as well? 😅 As data analysis spreads through different business areas, our Power BI dashboards and reports are reaching more and more people inside organizations. More users mean more needs. Although it makes sense to create different reports for different groups (and I usually think that’s the best approach), we often don’t have the time or resources. So, we end up making Power BI projects that have to fit a lot of different needs at once, like showing data with varying date granularities.

The visuals you see at the start of this article are from a financial asset dashboard I’m working on. I chose this view to spotlight the buzz around this week’s US Bitcoin ETF approval. If you look at the bottom of these KPI cards, you’ll find a part that shows the trading volume for a chosen asset. Users can toggle between different date granularities to see this info in daily, weekly, or monthly formats. The dashboard dynamically adjusts the data aggregation based on the user’s selection.

![](99.System/Attachments/1!pMDC8CATgJ4p1MT0YzHBvw.png.webp)

Date Granularity of KPI Cards Dynamically Adjusts Based on User Selection

In this article, I’ll walk you through the steps of creating these visuals in the trading volume analysis section, showing you how to implement similar features in your own Power BI projects. This guide is designed to help you enhance the flexibility and functionality of your reports and dashboards.

### 1\. Setting Up The Initial Data Tables

The financial data used for this dashboard was retrieved from [Yahoo Finance](https://finance.yahoo.com/quote/BTC-USD/history?period1=1547078400&period2=1704758400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true) and loaded in Power BI. You can view the CSV as well as the detailed steps applied in Power Query by downloading the PBIX file available at the end of the article.

Once loaded in Power BI, the table was called `Asset Data`. Here is an extract so you can view the different columns available:

![](99.System/Attachments/1!knb6L83D009FyugbMxBJDg.png.webp)

Asset Data Table Loaded in Power BI

To support the analysis of this table and build a proper data model for this Power BI project, I also built the following Calendar table in Power Query and loaded it in Power BI. It takes the maximum and minimum dates available from the `Asset Data` table and generates the full list of dates in between them in the column `Daily`. I also created the columns `Weekly` and `Monthly` that provide the first date of the corresponding week and month, respectively.

Here are the steps that I applied in Power Query:

```c
let
    GetMinDate = Date.StartOfMonth(List.Min(#"Asset Data"[#"Date"])),
    GetMaxDate = Date.EndOfMonth(List.Max(#"Asset Data"[#"Date"])),
    Source = #table({"MinDate", "MaxDate"}, {{GetMinDate, GetMaxDate}}),
    AddDateColumn = Table.AddColumn(Source, "Daily", each {Number.From([MinDate])..Number.From([MaxDate])}),
    ExpandDates = Table.ExpandListColumn(AddDateColumn, "Daily"),
    SelectColumns = Table.SelectColumns(ExpandDates, {"Daily"}),
    ChangeType = Table.TransformColumnTypes(SelectColumns,{{"Daily", type date}}),
    AddMonthlyColumn = Table.AddColumn(ChangeType, "Monthly", each Date.StartOfMonth([Daily]), type date),
    AddWeeklyColumn = Table.AddColumn(AddMonthlyColumn, "Weekly", each Date.StartOfWeek([Daily]), type date)
in
    AddWeeklyColumn
```

And here is an extract of the table it generated:

![](99.System/Attachments/1!__1TjMUIsk1RnKrgT8Zrew.png.webp)

Calendar Table Built in Power Query

### 2\. Creating the Date Granularity Slicer

The second step was to set up the slicer that enables users to select whether they want to view the data in a daily, weekly or monthly format. To achieve this, I first built a field parameter named `Date Granularity`, selecting all the columns from the `Calendar` table.

![](99.System/Attachments/1!uuvpw5ioRHKKha1dbDUCcg.png.webp)

Building a Field Parameter in Power BI

As you can see, since the `Add slicer to this page` check-box from the `Parameters` window was selected, a slicer appears on the report page.

I actually changed this slicer to Power BI’s new slicer and applied a few formatting steps to get the look and feel I wanted (see PBIX file for details).

![](99.System/Attachments/1!t876ynaUfDCQV76QBcEUUw.png.webp)

Formatting the Date Granularity Slicer in Power BI

### 3\. Calculating the Maximum Selected Dates

Following the slicer creation, I created 3 DAX measures that give the maximum dates: `Maximum Date`, `Maximum Week`, `Maximum Month`. These measures are referenced in subsequent measures to calculate the trading volume, as well as to format the bar chart.

```c
Maximum Date = MAX('Asset Data'[Date])

Maximum Week = 
    CALCULATE(
        MAX('Calendar'[Weekly]),
        FILTER(
            'Asset Data',
            'Asset Data'[Date]<>BLANK()
        )
    )

Maximum Month = 
    CALCULATE(
        MAX('Calendar'[Monthly]),
        FILTER(
            'Asset Data',
            'Asset Data'[Date]<>BLANK()
        )
    )
```

### 4\. Creating the Date Granularity Bar Chart

The next step was to create a measure that calculated the trading volume that would be displayed in the bar chart. This measure was pretty straight forward:

```c
Trading Volume = SUM('Asset Data'[Vol.])
```

I then added a bar chart visual to the report and placed the `Date Granularity` field parameter under the X-axis, and the measure `Trading Volume` in the Y-axis.

![](99.System/Attachments/1!PFJXjZJdRkNf1Z3DGaIKjA.png.webp)

Creating the Trading Volume Bar Chart in Power BI

As you can see, if you select through the different date granularity slicer options, the bar chart will display the values aggregated by month, week or day.

![](99.System/Attachments/1!JJ9JqsIwHi_ErSDpI9kxSA.png.webp)

Trading Volume Bar Chart Based on Date Granularity Slicer Selection

However, I didn’t really like the daily and weekly views. I wanted to limit the number of bars per graph to 12 so that basically, if the user selects `Daily`, they can view the last 12 days, if they select `Weekly`, they view the last 12 weeks, and `Monthly`; the last 12 months.

To achieve this, I created a measure that gives the minimum date I want to display on each chart depending on the user’s selection and applied it to the chart’s Minimum X-axis.

Here is the DAX measure that was created:

```c
Starting X-axis = 
VAR _MaxDate = [Maximum Date]
VAR _MaxWeek = [Maximum Week]
VAR _MaxMonth = [Maximum Month]
VAR _MinDate = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Daily]", _MaxDate - 12,
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]", _MaxWeek - 84,
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]", EDATE(_MaxMonth,-12)
    )
RETURN _MinDate
```

I then added it to the bar chart’s `Minimum X-axis Range`.

![](99.System/Attachments/1!FGU4M0cdgmCEmxZYNc-iAQ.png.webp)

Setting the X-Axis Minimum Range in Power BI

Now if you retest with the different slicer selections, you see only the last 12 observations appear on the bar chart, wether they be daily, weekly or monthly.

Another option here could be to have another slicer where the user can select the timeframe they desire for the analysis. For example, the user can define they want to view the last 7 days, 2 weeks, 6 months, etc. I wrote an article how you can achieve this in Power BI titled [Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range](https://medium.com/microsoft-power-bi/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3).

## [Using Time Periods as Slicers to Enhance Power BI Line or Area Charts’ Range](https://medium.com/microsoft-power-bi/using-time-periods-as-slicers-to-enhance-power-bi-line-or-area-charts-range-de1abe76c6c3?source=post_page-----20c26275bd2e---------------------------------------)

### Enhancing Data Visualization: Mastering Time Frame Selection in Power BI Reports

medium.com

To get the desired look and feel to this bar chart, I added a few formatting steps you can view in detail by downloading the PBIX file available at the end of this article.

![](99.System/Attachments/1!2gmcQRaspcslXQfH4HK6jg.png.webp)

Formatting the Bar Chart in Power BI

### 5\. Creating the Trading Volume KPI Card

![](99.System/Attachments/1!UWoAQwNIFtCJd5Rv9COzAg.png.webp)

Trading Volume KPI Card

The last step was to create this KPI card that provided the information on the trading volume of the selected day, week or month, based on user selection. Here, we can’t simply drop the `Trading Volume` measure previously created in a card visual, as it will just provide the sum of the trading volumes of all the `Asset Data` observations.

So this KPI card has 3 parts: the trading volume, the maximum date selected and the variation.

![](99.System/Attachments/1!QvUt4NaqKzWU_ZZkGzbyOA.png.webp)

Components of the Trading Volume KPI Card

Starting with the trading volume, I built the following DAX measure to render the proper aggregation based on the user’s selection:

```c
Trading Volume Display Value = 
VAR _MaxDate = [Maximum Date]
VAR _MaxWeek = [Maximum Week]
VAR _MaxMonth = [Maximum Month]
VAR _TradingVolume =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Daily]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Daily] = _MaxDate
                )
            ),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Weekly] = _MaxWeek
                )
            ),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Monthly] = _MaxMonth
                )
            )
    )
RETURN _TradingVolume
```

Following this, I created the following DAX measure that provides the textual information on the maximum date selected:

```c
Time frame = 
VAR _IsInProgress = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]" && [Maximum Week] + 6 > [Maximum Date], " (In Progress)",
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]" && EOMONTH([Maximum Month],0) > [Maximum Date], " (In Progress)"
    )
VAR _TimeFrame = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Daily]", "As of " & FORMAT([Maximum Date], "mmm d yyyy"),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]", "For the week of " & FORMAT([Maximum Week], "mmm d yyyy"),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]", "For the month of " & FORMAT([Maximum Month], "mmm yyyy")
    )
RETURN _TimeFrame & _IsInProgress
```

Finally, to display the variation, I built the following set of DAX measures.

The first measure `Trading Volume Display Value Date Before` is built to calculate the trading volume of the previous observation, therefore if daily is selected, if calculates the trading volume of the previous day, if weekly is selected, it calculates the volume of the previous week and so on.

```c
Trading Volume Display Value Date Before = 
VAR _MaxDate = [Maximum Date] - 1
VAR _MaxWeek = [Maximum Week] - 7
VAR _MaxMonth = EDATE([Maximum Month],-1)
VAR _TradingVolume =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Daily]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Daily] = _MaxDate
                )
            ),

        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Weekly] = _MaxWeek
                )
            ),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]",
            CALCULATE(
                [Trading Volume],
                FILTER(
                    'Calendar',
                    'Calendar'[Monthly] = _MaxMonth
                )
            )
    )
RETURN _TradingVolume
```

Following this initial DAX measure, I built the following measures to arrive to the percentage variation that are pretty straight forward:

```c
Trading Volume Variation = [Trading Volume Display Value] - [Trading Volume Display Value Date Before]

Trading Volume Percentage Variation = 
    DIVIDE(
        [Trading Volume Variation],
        [Trading Volume Display Value Date Before]
    )
```

In my case, I wanted to add HTML icons to display the variation, so instead of leveraging a native Power BI card visual, I used the HTML content visual. Here is how to add this visual in Power BI desktop:

![](99.System/Attachments/1!RnnEgT1NpjHfmSqUma3tDQ.png.webp)

Adding the HTML Content Visual in Power BI Desktop

Finally, I created the measure `Trading Volume Information Formatted` to present the trading volume and its variation with icons and colors. The preliminary measures below are to set up the colors and icons:

```c
Color Red = "#EA3943"

Color Green = "#16C784"

Icon Font awesome icon set up = "<head><link rel=""stylesheet"" href=""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css""/></head><i style=""color:{COLOR}"" class=""{ICON_CODE} {SIZE}""></i>&nbsp;" 

Icon green triangle up = 
SUBSTITUTE(
        SUBSTITUTE(
            SUBSTITUTE(
                [Icon Font awesome icon set up],
                "{ICON_CODE}",
                "fa-solid fa-circle-chevron-up"
                ), 
            "{SIZE}", 
            "fa-lg"
        ),
        "{COLOR}",
        [Color Green]
    )

Icon red triangle down = 
SUBSTITUTE(
        SUBSTITUTE(
            SUBSTITUTE(
                [Icon Font awesome icon set up],
                "{ICON_CODE}",
                "fa-solid fa-circle-chevron-down"
                ), 
            "{SIZE}", 
            "fa-lg"
        ),
        "{COLOR}",
        [Color Red]
    )

Trading Volume Information Formatted = 
VAR _ValueToFormat = [Trading Volume Display Value]
VAR _FormattedValue = 
SWITCH(
        TRUE(),
        _ValueToFormat < 1000, FORMAT(_ValueToFormat, "$0"),
        _ValueToFormat  < 1000000, FORMAT(_ValueToFormat / 1000, "$0.##") & "K",
        _ValueToFormat < 1000000000, FORMAT(_ValueToFormat / 1000000, "$0.##") & "M",
        _ValueToFormat < 1000000000000, FORMAT(_ValueToFormat / 1000000000, "$0.##") & "B",
        FORMAT(_ValueToFormat / 1000000000000, "$0.##") & "T"
    )
VAR _FormattedVariation = FORMAT([Trading Volume Percentage Variation], "0.0%") & " " 
VAR _DateCompared = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Daily]", "(1d)",
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Weekly]", "(1w)",
        SELECTEDVALUE('Date Granularity'[Data Granularity Fields]) = "'Calendar'[Monthly]", "(1m)"
    )
VAR _TextVariation = 
    IF(
        [Trading Volume Variation]<0,
        _FormattedVariation & " " & _DateCompared & " "  & [Icon red triangle down],
        _FormattedVariation & " " & _DateCompared & " "  & [Icon green triangle up]
    )

VAR _FontVariation = 
    IF(
        [Trading Volume Percentage Variation]<0,
        "<font color = " & [Color Red] & ">",
        "<font color = " & [Color Green] & ">"
    )

RETURN _FormattedValue & "<font color = " & [Color Grey] & "><font size = ""-1"">" & "&nbsp;" & "&nbsp;" &   "US"  & "&nbsp;" & "&nbsp;" & "&nbsp;" & _FontVariation & _TextVariation
```

I used a distinct HTML visual to place the `Time Frame` measure right underneath the `Trading Volume Information Formatted` html visual.

### Conclusion

That’s it for our guide on spicing up your Power BI dashboards with dynamic date choices! As you’ve seen, the DAX part is pretty straightforward and the fun part comes from leveraging Power BI’s native visual and core functionalities. I hope this was helpful and it inspires you on cool ways to add flexibility to your users in your current or future Power BI projects.

**To see all these visuals and formatting options in action, as seen in the cover image of this article, you can download my report** [**here**](https://drive.google.com/drive/folders/1kN20nT-cgfSsI1Fd4c9IpM6HAQ9Pv2_h?usp=sharing)**.**

Love hearing what you think — it really sparks my next ideas. Feel free to share your thoughts in the comments — I’m eager to read them. If you’ve found this article helpful, a clap is greatly appreciated 😊! Thanks for your interest and for taking the time to read!

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X (Formerly Twitter)***](https://twitter.com/KI_Datascience)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)