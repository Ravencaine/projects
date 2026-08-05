---
title: "Power Graphing: Unleashing Multi-Dimensional Insights in One Power BI Visual"
source: "https://medium.com/microsoft-power-bi/power-graphing-unleashing-multi-dimensional-insights-in-one-power-bi-visual-a8c4e4a9b5e4"
author:
  - "[[Isabelle Bittar]]"
published: 2023-10-07
created: 2026-07-29
description: "Maximizing Information in a Single Graph in Power BI"
Processed: "Unprocessed"
---
## Maximizing Information in a Single Graph in Power BI

![](99.System/Attachments/1!runKobNZB9x3A_0bx_5VOw.png.webp)

By KI Data Science

### Introduction

In the sophisticated realm of data-driven decision-making, the visual presentation of information often dictates the impact of insights. Power BI stands as a testament to the fusion of analytical prowess with artistic design, offering a platform where raw data metamorphoses into powerful stories. However, a common pitfall is the overcomplication of dashboards, leading to cognitive overload and obscured insights. As the modern zeitgeist gravitates towards minimalistic yet potent designs, the challenge is to craft a single graph that resonates with multifaceted depth, akin to the example we delve into below.

This demonstration reveals how a company’s HR application metrics can be elegantly conveyed through a single, well-crafted visualization, encapsulating various dimensions of the data landscape.

![](99.System/Attachments/1!p2wDQIDYtGnnAhJ8WCDs6w.png.webp)

By KI Data Science

The information found in 1 graph includes:

- The total number of applications received (in the title).
- The nominal distribution of application per sourcing channel (each bar of the chart).
- The percentage variation between 2023 and 2022 of applications received in total (in the title) and per channel (at the end of each bar).
- The ranking of each channel and comparaison to the previous year (at the beginning of each bar).
- Insight on where the greatest nominal variation occurred (in the subtitle).

Below is a summary on how each step was achieved.

As a starting point, here is our initial data table:

![](99.System/Attachments/1!J2H9L7M59WsBRBgYTuSVCQ.png.webp)

Initial Data Table

### 1) Getting the Chart Started

A) Select the Table visual and add the Recruitment Sourcing Channels as the first column.

B) Create the measure for the total number of applications received in 2023.

```c
Applications 2023 = SUM('Applications Sourcing'[2023])
```

C) Create a measure calculating the percentage variation of applications received between 2022 and 2023.

```c
Applications 2022 = SUM('Applications Sourcing'[2022])

Variation 2022 - 2023 = [Applications 2023] - [Applications 2022]

Percentage Variation 2022 - 2023 = 
VAR _Percentage = 
    DIVIDE(
        [Applications 2023] - [Applications 2022],
        [Applications 2022]
    )
VAR _ValueToReturn = 
    IF(
        _Percentage>0, 
        "+" & FORMAT(_Percentage, "0.0%"),
        FORMAT(_Percentage, "0.0%")
    )
RETURN _ValueToReturn
```

D) Create a measure to display the sourcing channels ranking compared to last year.

```c
Ranking 2023 = 
    RANKX(
        ALL('Applications Sourcing'),
        [Applications 2023]
    )

Ranking 2023 Text = "# " &[Ranking 2023]

Ranking 2022 = 
    RANKX(
        ALL('Applications Sourcing'),
        [Applications 2022]
    )

Ranking Variation 2022 - 2023 = 
VAR _Rank2023 = [Ranking 2023]
VAR _Rank2022 = [Ranking 2022]
VAR _Variation = _Rank2022 - _Rank2023
RETURN _Variation  

Ranking Variation 2022 - 2023 Text = 
VAR _Variation = [Ranking Variation 2022 - 2023]
VAR _ValueToReturn = 
    SWITCH(
        TRUE(),
        _Variation<0, UNICHAR(128899) & " " & ABS(_Variation),
        _Variation>0, UNICHAR(128897) & " " & _Variation
    )
RETURN _ValueToReturn
```

C) Add these measures as columns to the table visual in the following order:

![](99.System/Attachments/1!MCK5TQ109N8s3VE9WA_JSQ.png.webp)

Fields for the Table Visual

The graph should look like this at this point:

![](99.System/Attachments/1!SYAzVjC-ijucBwdqg4HgTQ.png.webp)

First Iteration of the Graph

### 2) Assigning a Title

A) Create the title measure.

```c
Title = [Applications 2023] & " Applications Received in 2023, " & [Percentage Variation 2022 - 2023] & " Since 2022"
```

B) Add the title measure to the visualization’s Title dynamic field.

### 3) Assigning a Subtitle

A) Create the subtitle measure showcasing where the greatest variation occurred using the first measure created in step 1C.

```c
Subtitle = 
VAR MaxVariation = 
IF([Variation 2022 - 2023]<0,
    MINX(
        ALL('Applications Sourcing'),
        [Variation 2022 - 2023]
    ),
    MAXX(
        ALL('Applications Sourcing'),
        [Variation 2022 - 2023]
    )
)
VAR MaxChannel = 
    CALCULATE(
        FIRSTNONBLANK('Applications Sourcing'[Recruitment Sourcing Channels],1),
        FILTER(
            'Applications Sourcing',
            [Variation 2022 - 2023] = MaxVariation
        )
    )
VAR ValueToReturn = 
    IF(
        [Variation 2022 - 2023]>0,
        MaxChannel & " had the greatest increase with " & MaxVariation & " additionnal applications compared to 2022. ",
        MaxChannel & " had the greatest decrease with " & ABS(MaxVariation) & " less applications compared to 2022. "
    )
RETURN ValueToReturn
```

B) Assign this measure to the visualization’s Subtitle dynamic field.

The graph should look like this at this point:

![](99.System/Attachments/1!RL3Qf6-DqeEfin9GMAfydQ.png.webp)

Second Iteration of the Graph

### 4) Formatting

Let’s now start formating the graph to make it resemble more the inital one presented. Under the Format visual pain, apply the following steps:

A) **Format the title and subtitle**: Use the font “Segoe UI Semi Bold” and “Segeo UI Light” for the title and subtitle, respectively. Apply a font size 13 for both.

B) **Remove grid lines**: Go to Style presets and select “None”. Under Grid and Border, apply the white color.

C) **Remove column headers**: Go to Column headers and use white a the Text color. Turn off the Text wrap option and resize columns accordingly.

d) **Add the data bar**: Go to Cell elements, select the series Applications 2023 and turn on Data bars. You can also click the fx to apply a specific color or additional formating. On my end, I changed the axis color to white and a

e) **Add color to the ranking variation**: Create the following measure and retrieve it through Cell elements, select the Series Ranking Variation 2022–2023 Text, turn on Font color, click the fx button, select Field value under Format style.

```c
_Const Color Green = "#00CF84"

_Const Color Red = "#F03538"

Ranking Variation Color = 
    SWITCH(
        TRUE(),
        [Ranking Variation 2022 - 2023]<0, [_Const Color Red],
        [Ranking Variation 2022 - 2023]>0, [_Const Color Green]
    )
```

f) **Add color to the percentage variation**: Similar to the previous step, create the following measure and retrieve it through Cell elements, select the Series Percentage Variation 2022–2023, turn on Font color, click the fx button, select Field value under Format style.

```c
Applications Variation Color = 
    SWITCH(
        TRUE(),
        [Variation 2022 - 2023]<0, [_Const Color Red],
        [Variation 2022 - 2023]>0, [_Const Color Green]
    )
```

G) **Remove totals**: Under Totals, Turn off Values.

H) **Increase the row padding**: Under Grid, select Options and add 5 to the Row padding.

### Conclusion

In the rapidly evolving world of data visualization, Power BI remains a cornerstone tool for creating insightful dashboards. The process described here encapsulates the art of achieving clarity without sacrificing detail, emphasizing the importance of an intuitive graph that can impart a wealth of information at a glance. This specific example demonstrates how to present data pertaining to an HR team’s application metrics by channel. By cleverly using measures, titles, subtitles, and strategic formatting techniques, a single graph has been transformed to provide comprehensive insights spanning total applications, distribution by channel, year-over-year variations, channel rankings, and notable variations. Such an approach ensures that the audience, from senior leadership to operational teams, can swiftly understand trends, successes, and areas of concern. This efficient use of visualization real estate not only upholds modern design principles but also reaffirms the notion that less can indeed be more, especially when it’s meticulously crafted.

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)