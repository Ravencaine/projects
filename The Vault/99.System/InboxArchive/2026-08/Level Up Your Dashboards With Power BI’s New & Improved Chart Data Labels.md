---
title: "Level Up Your Dashboards With Power BI’s New & Improved Chart Data Labels"
source: "https://medium.com/microsoft-power-bi/level-up-your-dashboards-with-power-bis-new-improved-chart-data-labels-2e9a09d2b329"
author:
  - "[[Isabelle Bittar]]"
published: 2024-01-21
created: 2026-08-02
description: "Discover How to Utilize the New Features from Power BI’s December 2023 Release"
Processed: "Unprocessed"
---
## Discover How to Utilize the New Features from Power BI’s December 2023 Release

![](99.System/Attachments/1!0VBSwWnHjxnk7ssqU4WO_g.png.webp)

By Isabelle Bittar for KI Data Science

*PBIX file available for download at the end of this article.*

Power BI introduced an exciting update in its December 2023 features release: new and improved chart data labels 🥳! Since early 2023, Power BI has allowed us to customize chart data labels, enabling them to display values different from those of the measure used in chart lines or columns. However, this latest update elevates the functionality by adding more detail to the data labels of columns and offering advanced formatting options.

![](99.System/Attachments/0!Sm8B3ZcMF12j62Ka.png.webp)

Power BI’s New Customizable Chart Data Labels (Read December 2023 Feature Summary Here )

In building a (yes, another! 🙈) talent acquisition dashboard, I started leveraging this new functionality — and it rocks! The danger for me is to go crazy with all the possibilities these data labels offer and start creating heavy charts with way too much data label information😅. Just because we can, doesn’t mean we should!

In the following article, I will provide an overview of these new chart data labels and guide you through how I integrated them in the development of my dashboard to give you a sense of how you can use them in your projects.

### Overview of the New Chart Data Labels

Below is the anatomy of the new chart data label:

![](99.System/Attachments/1!N47CWNBwwSpzZ5CxVk7Ehw.png.webp)

Anatomy of Power BI’s New Chart Data Labels

What I like about these new labels is all the customizations options available. Here are a few examples of what can be achieved with them:

- **Customize the Value**: The displayed value doesn’t have to match the measure used in the chart. While this capability existed before December, it now leads to a range of other options.
- **Add/Remove or Customize the Title**: The title, which can default to the name of the value’s measure, offers flexibility. You can alter it manually or use the `fx` option for dynamic adjustments.
- **Add Detail**: The detail ‘sub-values’ are my favorite part. You can add more relevant information on the main metric presented in your chart. In the example presented above, 2 detail sub-values are provided: the total amount and percentage variation from a previous period.
- **Customize the Value and Detail Format**: Not only can you modify formatting settings for the main value, but you can also apply diverse formatting styles to different sub-values, such as varying color schemes.

While all these features are very exciting, I was slightly disappointed 🤔that we can’t customize the detail background like showcased in the official Microsoft documentation. Maybe a next feature to come? 🤞

![](99.System/Attachments/1!X7WaMhhIs9ka5GU28NjX2Q.png.webp)

Screenshot of Microsoft’s Documentation of the New Chart Data Labels (see here )

Another challenge with these new data labels is their increased space requirement, which can lead to more frequent overlapping with chart elements, such as data label text partially covering the bars in a chart. I address how to manage this issue in Step 4.

### Case Study: Talent Acquisition Dashboard

Here’s a dashboard I’m currently working on. So far, most of it has been designed in Figma, and now I’m bringing it to life in Power BI. If you’re interested in learning how to leverage Figma and Power BI, you can read my article: [**Figma Meets Power BI: Revolutionizing Report Design**](https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7)

## [Figma Meets Power BI: Revolutionizing Report Design](https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7?source=post_page-----2e9a09d2b329---------------------------------------)

### Unleashing Creativity and Efficiency in Data Visualization

medium.com

As I develop this dashboard, I’ve identified several charts where I want to leverage the new data labels. In the next section, I will demonstrate how I used them in creating a specific chart. This chart showcases the current month’s process duration in talent acquisition, along with a comparison to the previous month.

![](99.System/Attachments/1!mR1skml9puGSdrQzDAkpZA.png.webp)

Chart Built Using Power BI’s New Data Labels

### Step 1: Setting Up the Initial Bar Chart

The first step involved developing the main DAX measures to calculate the current and previous month’s process duration and setting up the bar chart.

I started with my initial data table titled `Process Duration`, loaded into Power BI. This table provides the average number of days spent on each process step for each period.

![](99.System/Attachments/1!qTMpa3RicfAjFb3ExW3DSg.png.webp)

Process Duration Table Loaded in Power Query

To calculate the process duration for the current month, I first needed to determine the current date, which is the `Maximum Date` of my dataset. I obtained this value using the following measure:

```c
Maximum Date = MAX('Process Duration'[Date])
```

Next, to calculate the `Process Duration`, I summed up the days for each process step for this maximum date, using this measure:

```c
Process Duration = 
VAR _MaxDate = [Maximum Date]
VAR _Duration = 
    CALCULATE(
        SUM('Process Duration'[Days]),
        FILTER(
            'Process Duration',
            'Process Duration'[Date] = _MaxDate
        )
    )
RETURN _Duration
```

I applied the same logic to calculate the process duration for the previous month by subtracting one month from the maximum date. Here are the measures:

```c
Date Last Month = EDATE([Maximum Date],-1)

Process Duration Previous Month = 
VAR _DateLastMonth = [Date Last Month]
VAR _Duration = 
    CALCULATE(
        SUM('Process Duration'[Days]),
        FILTER(
            'Process Duration',
            'Process Duration'[Date] = _DateLastMonth
        )
    )
RETURN _Duration
```

With the measures ready, I added the `Clustered column chart` to my report and dragged these two measures on the Y-axis, and then the `Process Step` column on the X-axis.

![](99.System/Attachments/1!MSYhucyA1uGuoca6eEuLLg.png.webp)

Inserting the Clustered Column Chart in Power BI

As you will notice, the steps weren’t displayed in the correct order. To fix this, I created a separate table in Excel, loaded it into Power BI, and connected it to the data model on the `Process Step` column.

![](99.System/Attachments/1!ns_Ik6gnTtUkrobqGv4iDw.png.webp)

Process Steps Table Loaded and Connected to Data Model in Power BI

I then sorted the `Process Step` column by the `Order` column in the `Process Steps` table.

![](99.System/Attachments/1!lyVgiL68ykMpVU90ntGfVw.png.webp)

Sorting a Column by Another Column in Power BI

Finally, I used the `Process Step` column from this new table as the X-axis of my chart, ensuring all steps were displayed in the correct order.

![](99.System/Attachments/1!iZSy775ufRc3eFfiJhpPTA.png.webp)

Changing the Chart’s X-Axis in Power BI

Next, I applied some initial formatting steps to the chart to achieve the desired look and feel. The detailed steps are available in the PBIX file for download at the end of this article.

![](99.System/Attachments/1!BOlxT9Qz_3GHUA3GboTMBw.png.webp)

Initial Formatting to Chart in Power BI

One thing I will mention here as it is important to understand the next steps, is that I simplified the measure names under the Y-axis by double-clicking on the fields and retyping over them.

![](99.System/Attachments/1!-FO9-W1BuCQFk-el1106oA.png.webp)

Changing the Y-axis Measures Names

### Step 2: Adding the Data Labels

Now that the initial chart was set up, I was ready to start adding the data labels and their detail. With the chart selected, I turned on the `Data labels` option in the Format visual panel. Since I only wanted to display the values of the current month, I selected the `Previous Month` series and turned off the `Show for this series` option.

![](99.System/Attachments/1!5UX2WpfNJYVZ-NiOVYh1dg.png.webp)

Adding Data Labels for the Current Month in Power BI

With the `Current Month` series selected, I then formatted the data label value by going under the `Value` tab and changing the font to `Segeo UI Semibold`.

![](99.System/Attachments/1!PycS80kIJ224spU3Gg0Kgg.png.webp)

Change the Chart Value Font Color in Power BI

As you can see in the `Value` tab of the previous screenshot, you can change the measure selected under the `Field` for any other DAX measure created in your model. You also have the option to dynamically change the font color using the `fx` option.

Before adding the detail, it’s worth mentioning the `Title` tab under data labels. I left it turned off for my chart, but if you turn it on, you can see how the series’ title appears. This title can be customized, and you can even apply dynamic font color to it.

![](99.System/Attachments/1!UCOmFkYMQ-LDPEUeiqI4dw.png.webp)

Turning on the Data Labels’ Title in Power BI

### Step 3: Adding the Detail Sub-Values to the Chart

Next, I wanted to add the process duration variation between the previous and current month. I first developed the DAX calculation, which is straightforward:

```c
Process Duration Variation = [Process Duration] - [Process Duration Previous Month]
```

Then I created a subsequent measure to format the display of the word “days” following the variation, only showing this value if the variation was positive or negative.

```c
Formatted Process Duration Variation = 
    SWITCH(
        TRUE(),
        [Process Duration Variation] = 1, "+ " & [Process Duration Variation] & " day",
        [Process Duration Variation] > 0, "+ " & [Process Duration Variation] & " days",
        [Process Duration Variation] = -1, [Process Duration Variation] & " day",
        [Process Duration Variation] < 0,[Process Duration Variation] & " days"
    )
```

Then, with the `Current Month` serie still selected under `Data labels`, I went to the `Detail` tab, turned it `On`, and added the measure `Formatted Process Duration Variation` under `Data`.

![](99.System/Attachments/1!HXXqihdAwrGNq7WmQyQ6_A.png.webp)

Adding the Detail to the Chart’s Data Labels in Power BI

I wanted the detail to appear green if the process duration variation was negative, and red if it was positive. To achieve this, I created the following measures, first specifying the color codes and then the logic to follow:

```c
Color Dark Green = "#3B952D"

Color Dark Red = "#D8404A"

Color Process Duration Variation = 
    IF(
        [Process Duration Variation]>0,
        [Color Dark Red],
        [Color Dark Green]
    )
```

I then assigned the `Color Process Duration Variation` measure to the font’s color `fx` option.

![](99.System/Attachments/1!YTLtbFXshXtfDJbmkDI6xA.png.webp)

Assigning a Dynamic Font Color to the Chart Data Label Detail in Power BI

I also changed the `Font` style to `Segeo UI Semibold` and the size to `8`. This gave me the following result:

![](99.System/Attachments/1!ueKS8iH5n0Ni1oo1S4MsbQ.png.webp)

I didn’t like the way the data value for `Management Interviews & Tests` was overlapping the data bar and noticed this would potentially always be a challenge using data labels with detail. Despite making the data labels appear on the `Outside end` under `Options` > `Position`, the overlapping was still present. To bring the required correction, I knew I had to set a maximum value to the Y-axis that was greater than the maximum value of the series to allow the full data label to appear.

### Step 4: Adjusting the Chart’s Axis Range To Allow the Data Label to Fully Appear Over the Bars

I first created a measure that calculates the maximum value to be displayed in this chart and added 35% to this value:

```c
Maximum Value = 
VAR _MaxProcessDuration = 
    MAXX(
        ALL('Process Steps'),
        [Process Duration]
    )
VAR _AxisValue = _MaxProcessDuration + 0.35*_MaxProcessDuration
RETURN _AxisValue
```

Then, I added this measure `Maximum Value` to the chart’s `Maximum Y-axis Range` using the `fx` option.

![](99.System/Attachments/1!eEWl5-xOhLPwKLiCqW6pxg.png.webp)

Setting the Maximum Y-Axis Chart Range in Power BI

This adjustment gave me the final desired final resul of this bar chart:

![](99.System/Attachments/1!c8D2FBWoGuhJlEUjC2tw8g.png.webp)

Bar Chart with Power BI’s New Data Labels

### Other Noteworthy Features

While I haven’t applied these options in my chart, here are some other features worth mentioning:

- You can add a background to the data labels using the `Background` tab. This provides a fixed background that is applied to the entire data label of the selected series. This relates to what I mentioned in the introduction about the potential usefulness of having a background option for the detail and the ability to customize its color with an `fx` option.
![](99.System/Attachments/1!q49uaK4eDaAU06XvgdIXxw.png.webp)

Adding a Background to the Chart Data Labels in Power BI

- Instead of having the detail presented beneath the values (the `Multi-line` option), you can select `Single line` under the `Layout` tab.
![](99.System/Attachments/1!wFbW6YjJdgwhclyJ1LZoGQ.png.webp)

Switching From Multi-Line to Single Line Layout

### Conclusion

The new Power BI chart data labels offer so many opportunities to enhance your charts by providing additional detailed information to support your report users in their analysis. From incorporating extra details to formatting how values appear, this feature from the December 2023 release can help provide more information in less report real estate. While all the possibilities with the new chart data labels are exciting, use them responsibly 😎.

**You can download my Power BI report** [**here**](https://drive.google.com/drive/folders/1lXuazFMTL0hdHLO6yk6uKpZ8c_ScDZFy?usp=sharing) **to continue experimenting on your own!**

I would love to know your feedback on this article and if you have other ideas for future reads! Please share your thoughts in the comments or clap if you found this helpful 😊. Thank you for your interest and taking the time to read 🙏.

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Be sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

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