---
title: "⚡How to Build a Correlation Matrix in Power BI Using Only DAX"
source: "https://medium.com/microsoft-power-bi/how-to-build-a-correlation-matrix-in-power-bi-using-only-dax-ab611a19a194"
author:
  - "[[Isabelle Bittar]]"
published: 2025-08-24
created: 2026-08-02
description: "A hands-on guide to calculating correlations, formatting visuals, and adding interactivity — no external tools needed."
Processed: "Unprocessed"
---
## A hands-on guide to calculating correlations, formatting visuals, and adding interactivity — no external tools needed.

![](99.System/Attachments/1!TDvC6p5QftYeDDiaji_w9g.png.webp)

By Isabelle Bittar for KI Data Science

*🎁PBIX available for download at the end of this article!*

## Introduction

Recently, I wrote a few articles on how you can leverage Python in Power Query to access more advanced analytic methods, such as forecasting or anomaly detection. But DAX alone can also take your analysis much further than you might expect — for example, by building a **fully dynamic correlation matrix**.

I recently worked on a tactical HR dashboard designed to help HR advisors identify links and relationships between key indicators such as **Engagement**, **Performance**, and **Overtime hours**. One of the most valuable visuals we developed was a **correlation matrix**. I figured out a way to build it **100% in DAX**, making it fully interactive: users could apply filters and slicers to customize the view, and even explore details with an interactive tooltip that displayed additional context about the observations.

This visual proved to be a game-changer for advisors, helping them understand how metrics interact and providing clear, data-backed recommendations for leadership. For instance, as shown in the screenshot below, we identified that **Overtime hours were negatively correlated with Engagement in the IT department**. From this insight, we could recommend **keeping overtime under 10 hours per week** to help raise the average Engagement score closer to 6.

![](99.System/Attachments/1!0TXEMs0wlSEkMz5Opz5zHw.png.webp)

Overtime Hours vs. Engagement Survey Score Correlation Results

Here is a short demo video:

In this article, I’ll walk you through how I built this visual in Power BI, so you can replicate or adapt it to your own projects. But before diving into the DAX details, let’s take a closer look at **what a correlation matrix is and how it works**.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## What is a Correlation Matrix and How it Works

A **correlation matrix** is a table that displays the **correlation coefficients** between multiple numeric variables. Each cell shows a value between **\-1 and +1**, indicating both the **strength** and **direction** of the relationship:

- **+1** → perfect positive correlation (as one variable increases, the other always increases)
- **0** → no linear relationship
- **\-1** → perfect negative correlation (as one variable increases, the other always decreases)

Behind the scenes, the calculation uses the **Pearson correlation coefficient**, defined as:

![](99.System/Attachments/1!hrBG5gioayf-8Nt1tsrrUw.png.webp)

This formula standardizes the covariance of two variables by their standard deviations, producing a consistent measure that ranges from **\-1 to +1**.

### What does this mean? 😅

1. **Calculate the mean** of each variable.
2. **Subtract the mean** from each observation to center the data.
3. **Multiply the deviations** for each pair of values and find their average (this is the covariance).
4. **Divide by the product of the standard deviations** of the two variables.

At the end of this process, you get a value that is easy to interpret:

- If it’s **close to +1** (e.g., *performance rating* and *engagement survey score* = **0.84**), it means those metrics tend to rise and fall together strongly.
- If it’s **close to -1** (e.g., *overtime hours* and *engagement survey score*), it means as one goes up, the other consistently goes down.
- If it’s **close to 0**, there’s **little to no linear relationship** between those variables.

Now, let’s get into how I actually used this concept in Power BI! 🤓

## Step 1: Getting Started

To begin this project, I started with a table of HR performance indicators for each employee — such as their performance rating, number of training hours completed, absenteeism rate, and more. This is what my initial **HR Data** table looked like in Power BI:

![](99.System/Attachments/1!Z0HjREQw-litkvDBD7-hBg.png.webp)

Initial HR Data Table in Power BI

To prepare the setup for the matrix, I then created two simple calculated tables, `VariablesX` and `VariablesY`, to represent each of the variables:

```c
VariablesX = 
DATATABLE (
    "Variable", STRING,
    {
        { "Performance Rating" },
        { "Training Hours Completed" },
        { "Absenteeism Rate (%)" },
        { "Engagement Survey Score" },
        { "Overtime Hours" },
        { "Tenure in Role (months)" }
    }
)

VariablesY = 
DATATABLE (
    "Variable", STRING,
    {
        { "Performance Rating" },
        { "Training Hours Completed" },
        { "Absenteeism Rate (%)" },
        { "Engagement Survey Score" },
        { "Overtime Hours" },
        { "Tenure in Role (months)" }
    }
)
```

Once those tables were in place, I created the **correlation measure**. This DAX formula calculates the Pearson correlation coefficient dynamically based on the variables selected in the rows and columns of the matrix:

```c
Correlation = 
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )

-- One row per employee, respecting all report filters (e.g., Department)
VAR Base =
    SUMMARIZE (
        'HR Data', 'HR Data'[Employee ID],
        "Perf",   MAX ( 'HR Data'[Performance Rating] ),
        "Train",  MAX ( 'HR Data'[Training Hours Completed] ),
        "Abs",    MAX ( 'HR Data'[Absenteeism Rate (%)] ),
        "Eng",    MAX ( 'HR Data'[Engagement Survey Score] ),
        "OT",     MAX ( 'HR Data'[Overtime Hours] ),
        "Tenure", MAX ( 'HR Data'[Tenure in Role (months)] )
    )

-- Map selected variable names to numeric series
VAR WithXY =
    ADDCOLUMNS (
        Base,
        "X",
            SWITCH (
                TRUE(),
                XName = "Performance Rating",           [Perf],
                XName = "Training Hours Completed",     [Train],
                XName = "Absenteeism Rate (%)",         [Abs],
                XName = "Engagement Survey Score",      [Eng],
                XName = "Overtime Hours",               [OT],
                XName = "Tenure in Role (months)",      [Tenure],
                BLANK ()
            ),
        "Y",
            SWITCH (
                TRUE(),
                YName = "Performance Rating",           [Perf],
                YName = "Training Hours Completed",     [Train],
                YName = "Absenteeism Rate (%)",         [Abs],
                YName = "Engagement Survey Score",      [Eng],
                YName = "Overtime Hours",               [OT],
                YName = "Tenure in Role (months)",      [Tenure],
                BLANK ()
            )
    )

VAR Clean = FILTER ( WithXY, NOT ISBLANK ( [X] ) && NOT ISBLANK ( [Y] ) )
VAR N     = COUNTROWS ( Clean )
VAR AvgX  = AVERAGEX ( Clean, [X] )
VAR AvgY  = AVERAGEX ( Clean, [Y] )
VAR Num   = SUMX ( Clean, ( [X] - AvgX ) * ( [Y] - AvgY ) )
VAR Den   =
    SQRT (
        SUMX ( Clean, ( [X] - AvgX ) ^ 2 ) *
        SUMX ( Clean, ( [Y] - AvgY ) ^ 2 )
    )
RETURN IF 0
, Num / Den )
```

With that measure ready, I now had everything I needed to build the correlation table using **Power BI’s Matrix visual**.

## Step 2: Building the Correlation Matrix Visual

Next, I inserted a **Matrix visual** and added the `VariablesX[Variable]` field to the **Rows** and the `VariablesY[Variable]` field to the **Columns**. Under **Values**, I used the **Correlation** measure we built in the previous step.

The initial result gave me this table:

![](99.System/Attachments/1!rKlxyaJx0uHZod8ph4LZRg.png.webp)

Initial Matrix Visual presenting the correlation between HR variables in Power BI

To make the table easier to interpret — especially for users who aren’t as comfortable with statistics — I wanted to remove the **redundancy** of repeating the same correlation values across both sides of the matrix and hide the correlation of a variable with itself (e.g., *Absenteeism Rate vs. Absenteeism Rate = 1*).

To do that, I replaced the original **Correlation** measure with this adjusted version:

```c
Correlation (Lower Triangle, No Diagonal) = 
VAR r = [Correlation]
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
RETURN
    IF (
        ISBLANK ( r ) || ISBLANK ( XName ) || ISBLANK ( YName ),
        BLANK (),
        IF ( XName <= YName, BLANK (), r )   -- hides upper triangle AND diagonal
    )
```

This gave me a cleaner matrix — showing only the **lower triangle** of the correlation table — which was much easier to read and aligned with the layout I wanted for the final dashboard:

![](99.System/Attachments/1!AbTx_hzmnHgKhrYOYI0_VQ.png.webp)

Matrix Visual using the “Correlation (Lower Triangle, No Diagonal)” measure in Power BI

## Step 3: Formatting and Adding Conditional Colors

Once the matrix was working, I moved on to **formatting it a bit to improve readability,** and make it look a bit more **polished 😅**. I made the following adjustments:

- Set the **Style preset** to “None.”
- Removed **row and column subtotals**.
- Changed **all borders to white** and added thin white gridlines.
- Increased the **row padding** for a cleaner layout.
- Adjusted the **font size and weight** for both values and headers.
- Resized columns for a balanced, uniform look.

With these tweaks, my matrix started to look much cleaner and easier to interpret:

![](99.System/Attachments/1!zfPVnIaO4eYGAkT7bly6kw.png.webp)

Reformatted matrix visual in Power BI

### Applying Conditional Formatting

To make the correlations **intuitive at a glance**, I applied **conditional formatting** to both the background and the font color of the matrix cells.

Instead of using Power BI’s built-in gradient, I created **DAX measures** for the colors. This gave me more control, ensuring that strong positive and negative correlations stood out — even when applying filters or slicers — and avoided misleading gradients when a department-level view had a narrower range of values.

I first defined my **color palette** in simple measures:

```c
_Color Black = "#4B4B4B"

_Color Dark Green = "#008080"

_Color Dark Grey = "#605E5C"

_Color Dark Orange = "#E76F51"

_Color Light Green = "#DFF5F2"

_Color Light Grey = "#F5F5F5"

_Color Light Orange = "#FFEDE7"

_Color Mid Green = "#00BFB2"

_Color Mid Grey = "#E0E0E0"

_Color Mid Orange = "#F4A896"

_Color White = "#F5F5F5"
```

Then, I used those colors in two measures: one for the **cell background** and another for the **font color**.

```c
Correlation Color (Buckets) = 
VAR r0  = [Correlation (Lower Triangle, No Diagonal)]
VAR r   = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR abs = IF ( ISBLANK ( r ), BLANK(), ABS ( r ) )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    SWITCH (
        TRUE(),
        abs < 0.10,         [_Color White],        -- very weak/none
        r <= -0.70,         [_Color Dark Orange],    -- high negative
        r <= -0.50,         [_Color Mid Orange],     -- med negative
        r <= -0.30,         [_Color Light Orange],   -- low negative
        r >=  0.70,         [_Color Dark Green],     -- high positive
        r >=  0.50,         [_Color Mid Green],      -- med positive
        r >=  0.30,         [_Color Light Green],    -- low positive
                            [_Color White]         -- default for (-0.30, 0.30)
    )
)

Correlation Font Color = 
VAR r0 = [Correlation (Lower Triangle, No Diagonal)]
VAR r  = IF ( ISBLANK ( r0 ), BLANK(), r0 )
VAR absr = ABS ( r )
RETURN
IF (
    ISBLANK ( r ),
    BLANK(),
    IF ( absr >= 0.5,  "#FFFFFF",  [_Color Black] )   
)
```

I applied these measures to the **cell background** and **font color** under **Cell elements → Field Value** in the matrix visual.

![](99.System/Attachments/1!t4RuLyy_aZv75T0dMctERA.png.webp)

Applying the DAX measures to the matrix cell elements in Power BI

Once this step was completed, my matrix looked like the following:

![](99.System/Attachments/1!0PtuO53G0mwSQ0DE-4pEVg.png.webp)

Correlation matrix after applying conditional background and font color in Power BI

Next, I took the visual a step further by **adding an interactive tooltip** that showed the individual data points for any two selected variables. This helped users quickly understand the distribution of those metrics and added context to each correlation.

## Step 4: Adding an Interactive Tooltip

![](99.System/Attachments/1!Z7RdgGpheNxV-3W0waJfxQ.png.webp)

Adding an Interactive Tooltip to the Correlation Matrix in Power BI

Once the correlation matrix was clean and color-coded, I wanted to take it a step further by creating an **interactive tooltip**. The idea was simple: let users hover over any cell in the matrix and instantly see a **scatter plot** of the two variables for that intersection. This extra layer of context made the visual far more insightful by showing the actual data distribution behind each correlation.

### 1\. Create a Tooltip Page

I started by adding a new page to the report and setting it up as a tooltip:

- In the page settings, I changed **Page Type** to **Tooltip**.
- Adjusted the size to something compact (around **400px by 500px**) to keep the layout focused and easy to read.

### 2\. Build the Scatter Plot

On the tooltip page, I added a **scatter chart** and configured it as follows:

- **X-Axis:** `X Value` (a measure that dynamically pulls the numeric values of the selected variable)
- **Y-Axis:** `Y Value` (the same concept, but for the second variable)
- **Details/Legend:** `Employee ID` from the HR Data table, to show individual data points.

To make this dynamic, I first created two helper measures to capture the currently selected variable names:

```c
Selected X Name = SELECTEDVALUE ( VariablesX[Variable] )

Selected Y Name = SELECTEDVALUE ( VariablesY[Variable] )
```

Then I created these measures to map each selection to its corresponding numeric values:

```c
X Value = 
VAR _name = [Selected X Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",               MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",      MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)

Y Value = 
VAR _name = [Selected Y Name]
RETURN
SWITCH (
    TRUE(),
    _name = "Performance Rating",           MAX ( 'HR Data'[Performance Rating] ),
    _name = "Training Hours Completed",     MAX ( 'HR Data'[Training Hours Completed] ),
    _name = "Absenteeism Rate (%)",         MAX ( 'HR Data'[Absenteeism Rate (%)] ),
    _name = "Engagement Survey Score",      MAX ( 'HR Data'[Engagement Survey Score] ),
    _name = "Overtime Hours",               MAX ( 'HR Data'[Overtime Hours] ),
    _name = "Tenure in Role (months)",      MAX ( 'HR Data'[Tenure in Role (months)] ),
    BLANK()
)
```

Finally, I added a **dynamic title** to make the plot self-explanatory:

```c
Scatter Title = [Selected X Name] & " vs " & [Selected Y Name]
```

### 3\. Add a Dynamic, Styled Subtitle

Since not all users were familiar with correlation coefficients, I wanted to include a subtitle that explained the relationship in **plain language** while still looking polished.

I built an **HTML-based measure** for the subtitle, letting me highlight strong correlations with color and bold text. Here’s the measure:

```c
Scatter Subtitle (HTML) = 
VAR _x = [Selected X Name]
VAR _y = [Selected Y Name]
VAR _r = [Correlation]
VAR _abs = IF ( ISBLANK ( _r ), BLANK(), ABS ( _r ) )

-- Label bucket
VAR _labelRaw =
    SWITCH(
        TRUE(),
        _r <= -0.70, "high negative",
        _r <= -0.50, "medium negative",
        _r <= -0.30, "low negative",
        _r >=  0.70, "high positive",
        _r >=  0.50, "medium positive",
        _r >=  0.30, "low positive",
        "very weak/none"
    )
VAR _labelText = UPPER(LEFT(_labelRaw,1)) & MID(_labelRaw,2,LEN(_labelRaw)-1)

-- Background by label
VAR _bg_base =
    SWITCH(
        _labelRaw,
        "high negative",   [_Color Dark Orange],
        "medium negative", [_Color Mid Orange],
        "low negative",    [_Color Light Orange],
        "high positive",   [_Color Dark Green],
        "medium positive", [_Color Mid Green],
        "low positive",    [_Color Light Green],
        BLANK()
    )

-- White background if very weak or |r| < 0.10
VAR _bg = IF( _labelRaw = "very weak/none" || _abs < 0.10, [_Color White], _bg_base )

-- Font color on the badge:
-- White for HIGH & MEDIUM (±), dark grey otherwise
VAR _fg =
    SWITCH(
        TRUE(),
        _labelRaw IN { "high negative", "high positive", "medium negative", "medium positive" }, "#FFFFFF",
        [_Color dark grey]
    )

-- Bold, continuous badge for "<Label> correlation"
VAR _badgeFull =
    "<span style='background-color:" & _bg &
    "; color:" & _fg &
    "; padding:1px 6px; font-size:12px; font-family:Segoe UI Light; font-weight:600; display:inline-block; white-space:nowrap'>" &
    _labelText & " correlation</span>"

-- Headline with bold r
VAR _headline =
    _badgeFull & ", <b>r = " & FORMAT( _r, "0.00" ) & "</b>"

-- Second line sentence (bold all increase/decrease including plural)
VAR _sentenceRaw =
    _y & " tends to increase as " & _x & " increases"

VAR _sentenceBold =
    SUBSTITUTE(
        SUBSTITUTE(
            SUBSTITUTE( _sentenceRaw, "increases", "<b>increases</b>" ),
            "decreases", "<b>decreases</b>"
        ),
        "increase", "<b>increase</b>"
    )

VAR _sentenceFinal =
    IF( _r > 0,
        _sentenceBold,
        SUBSTITUTE( _sentenceBold, "<b>increase</b>", "<b>decrease</b>" )
    )

RETURN
IF(
    ISBLANK(_r) || ISBLANK(_x) || ISBLANK(_y),
    BLANK(),
    "<div style='color:" & [_Color dark grey] & "; font-family:Segoe UI Light; font-size:12px; line-height:1.4'>" &
        _headline & "<br/>" &
        _sentenceFinal &
    "</div>"
)
```

This measure uses the correlation value to:

- Show a badge (colored teal for positive, coral for negative).
- Highlight the correlation value.
- Provide a second line that explains the relationship, e.g.,  
	*“Engagement Survey Score tends to* ***decrease*** *as Overtime Hours* ***increases***.”

If you want to learn how to integrate HTML into your Power BI reports, I cover that in detail here:

## [Elevating Power BI Reports with HTML & CSS: Joining Forces 💪](https://medium.com/microsoft-power-bi/elevating-power-bi-reports-with-html-css-joining-forces-f90fbd654e8b?source=post_page-----ab611a19a194---------------------------------------)

### In It to Win It 🤠: Part 2 of Participating in the FP20 Analytics Challenge on Data-Driven Education Management

medium.com

### 4\. Refine the Scatter Chart

Under the **Analysis** pane, I enabled the **Trend line** to make the relationship even clearer at a glance.

![](99.System/Attachments/1!bXPRQcOKRGXvy5DiW4wMLg.png.webp)

Turning the scatter chart trend line on in Power BI

### 5\. Link the Tooltip to the Matrix

At the end, the scatter chart looked like the following on my tooltip page:

![](99.System/Attachments/1!-hnuKoxnIF9nKLmqmouoZw.png.webp)

Scatter Plot on Tooltip Page in Power BI

But after assigning this page to matrix visual, I was able to properly test and view the variables and their info in the graph.

![](99.System/Attachments/1!UrtpPzd9ur_ANIU5Ro66Rg.png.webp)

Assigning Tooltip Page to the the Matrix Visual in Power BI

With this setup, the tooltip page provided a smooth, interactive way for users to drill deeper into the relationships between variables, making the correlation matrix more informative and actionable.

## Step 5: Final Touches

![](99.System/Attachments/1!GeQBMiDINVgdXn1e_qi4Iw.png.webp)

Final Touches to the Correlation Matrix in Power BI

To make the correlation matrix as **impactful and user-friendly** as possible, I added a few final touches:

- **Color legend:** Helped users quickly understand what the colors meant and how they mapped to correlation strengths.
- **Info tooltip:** Provided a short explanation of what a correlation matrix is and how to interpret the values, making the visual more approachable for non-technical users.
- **Visual-level slicer:** Allowed users to filter and explore correlations for specific departments, giving the analysis a more tailored and actionable feel.

You can find the details on how I implemented each of these enhancements in the **PBIX file** linked at the end of this article.

## Wrapping Up

Building this correlation matrix fully in DAX was more than just a technical exercise — it showed how a simple but well-designed visual can **unlock actionable insights** and make analytics more accessible to a wider audience.

Here are a few key takeaways from the experience:

- **Interactivity makes insights click** — Because the matrix responds to filters and slicers, users could instantly drill down into specific departments or roles. This flexibility helped advisors ask better questions, like why overtime’s impact on engagement was stronger in IT but less significant elsewhere.
- **Context is everything** — Pairing the matrix with the scatter plot tooltip transformed the analysis from a static table to an **interactive exploration tool**. It let users quickly spot outliers and better understand the drivers behind each correlation.
- **Design drives adoption** — Clean color coding, thoughtful layout, and supporting elements like a color legend and info tooltip made the matrix approachable, even for users without a stats background. The visual felt less like a “math-heavy” chart and more like a **decision-making tool**.
- **Maintenance is simple** — Because it’s built entirely in DAX, there are **no external scripts or refresh complexities**. The approach can be scaled or adapted to new datasets without additional technical overhead.
- **Broader applications** — This setup isn’t limited to HR data. The same logic can be applied to **sales, finance, operations, or marketing datasets** — anywhere you want to quickly uncover patterns and relationships between numeric variables.

With the interactive tooltip, thoughtful design, and DAX-driven calculations, the matrix became more than a visualization: it became a **conversation starter** that helped stakeholders move from simply seeing patterns to actually acting on them.

**👉** If you’d like to explore the setup in detail or adapt it to your own data, download the [**PBIX file**](https://drive.google.com/file/d/1YVedpU2inPKEDD-0PYsiZjbNNz4Z4w9O/view?usp=sharing) and start experimenting.

If you’re interested in exploring some of my more advanced Power BI data analytics projects, here are a few articles you might enjoy:

## [🚨 How to Do Anomaly Detection in Power BI (No External Tools Needed!)](https://medium.com/the-bi-corner/how-to-do-anomaly-detection-in-power-bi-no-external-tools-needed-b12973e58b2b?source=post_page-----ab611a19a194---------------------------------------)

### A hands-on case study using Python and Isolation Forest — run entirely inside Power Query to flag suspicious employee…

medium.com

## [✨ Analyzing Survey Comments in Power BI Using AI](https://medium.com/the-bi-corner/analyzing-survey-comments-in-power-bi-using-ai-ea0ca35ff98b?source=post_page-----ab611a19a194---------------------------------------)

### How I used GPT-4 to extract themes, score sentiment, and build an interactive dashboard in Power BI

medium.com

## [💡 My Favorite Way to Forecast in Power BI](https://medium.com/the-bi-corner/my-favorite-way-to-forecast-in-power-bi-634d1221df24?source=post_page-----ab611a19a194---------------------------------------)

### How I used Power Query and Python to build a reusable, customizable forecasting model — no Premium needed

medium.com

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

## Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

## Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-end) **🎁**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://powerbi-masterclass.short.gy/linktree?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----ab611a19a194---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

powerbi-masterclass.short.gy

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Visualization, DAX

**Tags:** Tutorial, PBIX, Data Visualization, DAX