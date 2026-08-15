---
title: "4 ways to use error bars in Power BI - small feature, big impact"
source: "https://datatraining.io/blog/4-clever-ways-error-bar-use-cases"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "Error bars in Power BI are hiding in plain sight. Most people set them up once for a standard chart and never think about them again - but there is a lot more going on under the hood. Used creatively, error bars can reshape a visual entirely, adding elements that would otherwise require custom visuals or complex workarounds."
Processed: "Unprocessed"
---
Error bars in Power BI are hiding in plain sight. Most people set them up once for a standard chart and never think about them again - but there is a lot more going on under the hood. Used creatively, error bars can reshape a visual entirely, adding elements that would otherwise require custom visuals or complex workarounds.

power bi error bars dax boxplot

Here are four ways to use Error bars creatively and to avoid custom visuals or complex DAX measures.  

Let’s dive in!**  
  
Example 1 - Data Flags**  
  
A data flag is a vertical line that pops up at a specific point in a chart, carrying a label with summary information. In this example, a flag appears at the start of each quarter showing the quarter name and total likes for that period. Clean, contextual, and built entirely with error bars.**  
  
What we are building  
  
**

A column chart showing monthly social media likes, with a vertical flag at the start of each quarter. Each flag shows the quarter label and the total likes for that quarter.

![](https://lwfiles.mycourse.app/datatraining-public/b60e1eafe8a7379617d6528870325337.png)

**Step 1 - Create the measures  
**

You need five measures before touching the visual.  
**  
Monthly Max -** finds the highest likes value across all selected months and scales it up. This controls how tall the flag line appears.

![](https://lwfiles.mycourse.app/datatraining-public/e3feee2bbd32d066eca7d77b23ea67bf.png)

**Dummy0** - always returns zero. Used as the lower bound of the error bar so the line starts from the bottom.

![](https://lwfiles.mycourse.app/datatraining-public/043b5d3e930a316ecf4b976de440c7dd.png)

**Monthly Max - Start Quarter** - returns the Monthly Max value only at the start of each quarter. This is what controls where the flags appear.

![](https://lwfiles.mycourse.app/datatraining-public/191901f0dec944c5d4d1116621ca69e0.png)

**Data Labels Value** - returns the quarter label (Q1, Q2 etc.) only at quarter starts. This is the main text on the flag.

![](https://lwfiles.mycourse.app/datatraining-public/c2aa02cdb37c52193cf490bac47c13eb.png)

**Data Labels Detail -** returns the total likes for that quarter, formatted with thousand separators, only at quarter starts. This is the detail line below the quarter label on the flag.

![](https://lwfiles.mycourse.app/datatraining-public/e650567b893b96cac94d345a6867988d.png)

**Step 2 - Set up the visual  
  
**

Insert a clustered column chart.

- X-axis - Month
- Y-axis - add the three series in this order >> Monthly Max, Likes, Monthly Max - Start Quarter

![](https://lwfiles.mycourse.app/datatraining-public/3e61cd3a853a502443f03afedea151d9.png)

**Step 3 - Make the flag series transparent**  
  
The Monthly Max and Monthly Max - Start Quarter series need to be invisible - they are just anchors for the error bars and data labels.

- Go to Format - Columns - select Monthly Max series - set transparency to 100%
- Do the same for Monthly Max - Start Quarter series

Now only the Likes columns are visible.

**Step 4 - Reduce spacing to align the flag lines  
  
**

Attaching error bars directly to the Likes series centers the lines on the columns and they overlap the data labels. Instead, the error bars are attached to the Monthly Max series which sits alongside the columns. To make sure the flag lines land in the right position:

- Go to Format - Columns - Layout
- Reduce the space between series to around 25%

This overlaps the series so the Monthly Max series aligns closely with the Likes columns.

![](https://lwfiles.mycourse.app/datatraining-public/13f4d3312a6cb3cf38aeb5631449b100.png)

**Step 5 - Add error bars**  

Go to Format - Error bars.

- Select the Monthly Max series
- Turn on Enable
- Set Type to By Field
- Set Upper bound to Monthly Max - Start Quarter
- Set Lower bound to Dummy0
- Go to Bar - turn it on and style the color and width as you like
- Turn off borders and markers

![](https://lwfiles.mycourse.app/datatraining-public/ba28a1489c67eb390999da93e6fa7243.png) ![](https://lwfiles.mycourse.app/datatraining-public/f30d3dd8872f0d768016533c2504324b.png)

Because Monthly Max - Start Quarter only returns a value at January, April, July, and October, the error bar has nothing to draw for all other months - so the flags appear only at quarter starts automatically.

![](https://lwfiles.mycourse.app/datatraining-public/22784e18e3a5749d616640110d3f149a.png)

**Step 6 - Add data labels  
  
**

Go to Format - Data labels.

• Select the Monthly Max - Start Quarter series

• Turn on Show for this series

• Turn off Title

• Under Value - set Field to Data Labels Value, set font & color to your preference.

• Under Detail - turn it on and set Data to Data Labels Detail

• Under Background - turn it on and set a light background color to give the flag that card-like appearance

• Set text alignment to left

• Set layout to “Multi-line”

![](https://lwfiles.mycourse.app/datatraining-public/e3f35027d6c43edc4211b92b384961d2.png)

And we have a clean column chart where the monthly data speaks for itself, and the quarterly summary floats above it as a flag - no extra table, no tooltip hunting, no cluttered annotations. Just the right information, exactly where the eye naturally goes.

**  
Example 2 – Rounded Bars**

Power BI does not have a native rounded bar option. But with a small error bar trick, you can make it convincingly - a filled circle marker at each end of the bar creates the illusion of rounded caps, and the result looks polished enough!**  
  
What we are building  
**

A horizontal bar chart with rounded ends on both sides, giving each bar a clean, pill-like appearance.

![](https://lwfiles.mycourse.app/datatraining-public/d9b61d8d63a8cb0038d3441fd7cbc76a.png)

**Step 1 - Set up the base visual  
  
**

Insert a clustered bar chart.

- Y-axis - Category
- X-axis - Sales Actual

![](https://lwfiles.mycourse.app/datatraining-public/97fc1be3deb4ef20f74372ed7b0fce1b.png)

**Step 2 - Add error bars  
  
**

Go to Format - Error bars and select the Sales Actual series.

- Turn on Enable
- Set Type to By Percentage
- Set Upper bound to 0%
- Set Lower bound to 100%

This is what turns the plain error bar into a rounded cap.

![](https://lwfiles.mycourse.app/datatraining-public/478a839e33d0e2bc670fdda1dfac7a2b.png)

Under Bar:

- Turn on Bar
- Set bar color to match your main bar color
- Set width to 1
- Set border size to 0px  
	  
	Under Markers:
- Turn on Markers
- Set marker shape to filled circle
- Set size to 10px  
	  
	The filled circle at each end is what creates the rounded appearance. Make sure the marker color matches your bar color so it blends in seamlessly.

![](https://lwfiles.mycourse.app/datatraining-public/1063279090de05a693330375681c71a0.png) ![](https://lwfiles.mycourse.app/datatraining-public/b768bc74191002dc33fa2bfe7efb5ffb.png)

**Step 3 - Add Spacing  
  
**

Go to Format > Bars > Layout and increase the "Space between Categories".

Play around until it aligns with the error bar circles.

![](https://lwfiles.mycourse.app/datatraining-public/1fa5b567e82e54b0195445a3f9f1ee52.png)

**Step 4 - Adjust the x-axis range  
  
**

Go to X Axis and define your min and max range. You can create a measure for these values with a buffer - visual calculations are great for this.  

This creates just enough breathing room on the left for the rounded cap to show fully.

For the maximum, set it high enough that the right cap is not clipped either. Rather than hardcoding a number, consider using a dynamic measure that finds the maximum value in your data and adds a small buffer - that way the axis adjusts automatically as your data changes.  

A bar chart that looks like it came from a custom visual library but is built entirely with native Power BI formatting. Clean, smooth, and surprisingly simple once you know the trick.

**  
Example 3 – Dumbbell**

A dumbbell chart shows a range or spread between two points per category - great for before and after comparisons, price ranges, or any scenario where the gap between two values tells the real story. This one is built entirely with error bars on a clustered bar chart, with no actual bar values showing at all.**  
  
What we are building  
**

A horizontal dumbbell chart showing property price ranges by city, using only available properties. The connecting line spans from the minimum to the maximum price, with the interquartile range highlighted in the middle.

![](https://lwfiles.mycourse.app/datatraining-public/c5de44c8a1aff9881548606d1039d052.png)

**Step 1 - Create the measures  
  
**

All three starting point measures return zero - they are invisible anchors that carry the error bars.

The error bar measures filter only properties with Lead Status = "Available"

![](https://lwfiles.mycourse.app/datatraining-public/241cb93b50ec79011f826faa156153ae.png)

**Step 2 - Set up the visual  
  
**

Insert a clustered bar chart.

- Y-axis - City Name
- X-axis - add in this order >> starting point, starting point1, startingpoint3

![](https://lwfiles.mycourse.app/datatraining-public/2d7f148d70de8f3c754374faaa40a747.png)

**Step 3 - Declutter the visual  
  
**

- Turn off the title
- Turn off all axis titles
- Turn off the legend

**  
Step 4 - Set up the layout**

Go to Format - Bars - Layout:

- Space between categories - 50%
- Space between series - 100%
- Turn on Overlap

![](https://lwfiles.mycourse.app/datatraining-public/fda54865481cb0baa347c6a76dd1ab4e.png)

**Step 5 - Set up error bars**  
Three error bars are needed - one for the lower whisker, one for the upper whisker, and one for the IQR connecting bar in the middle.

**starting point - lower whisker (min to P25):**  
- Turn on Enable
- Upper bound - 25th Percentile Property Available
- Lower bound - Min Value Property Available
- Bar - on, match series color off, bar color light purple, width 1, border size 0px

**  
starting point1 - upper whisker (P75 to max):**

- Turn on Enable
- Upper bound - Max Value Property Available
- Lower bound - 75th Percentile Property Available
- Bar - on, match series color off, bar color light purple, width 1, border size 1px

**startingpoint3 - IQR connecting bar (P25 to P75):**

- Turn on Enable
- Upper bound - 75th Percentile Property Available
- Lower bound - 25th Percentile Property Available
- Bar - on, match series color off, bar color darker purple, width 2, border size 0px

![](https://lwfiles.mycourse.app/datatraining-public/dafb8656259a9950585746a9c70925d8.png) ![](https://lwfiles.mycourse.app/datatraining-public/3a0e0a4c5dd465c7b228388f1c638eb2.png) ![](https://lwfiles.mycourse.app/datatraining-public/4057d72aa7b4e95a27a221de24e23659.png)

A clean horizontal range chart. No custom visual, no complex DAX - just three invisible series and three carefully configured error bars doing all the work.

**  
Example 4 – Boxplot**

Power BI does not have a native boxplot visual, but you can build a convincing one using a line and stacked column chart combined with error bars. The result shows the full distribution - minimum, maximum, interquartile range, median, and average - all in one clean visual.**  
  
What we are building  
**

A horizontal dumbbell chart showing property price ranges by city, using only available properties. The connecting line spans from the minimum to the maximum price, with the interquartile range highlighted in the middle.

![](https://lwfiles.mycourse.app/datatraining-public/22ad465dde08eef7c2af76c821519c36.png)

**Step 1 - Create the measures**

![](https://lwfiles.mycourse.app/datatraining-public/7d303268d939b61d4001a998b53f9438.png)

AVG 2 is a duplicate of the AVG measure - needed because two different marker styles are applied to the same value to create the layered ring effect on the average marker.

**  
Step 2 - Set up the visual  
  
**

Insert a line and stacked column chart.

- X-axis - City
- Column y-axis - add in this order >> Sales Quantity PERCENTILE 25, Sales Quantity IQR 25-50, Sales Quantity IQR 50-75
- Line y-axis - add in this order >> AVG 2, Sales Quantity MIN, Sales Quantity MAX, Sales Quantity AVG

![](https://lwfiles.mycourse.app/datatraining-public/9a8934bf30d73401df6ab602b8420ab7.png)

**Step 3 - Declutter the visual**  
  

- Turn off the title
- Turn off all axis titles
- Turn off the lines for all line series
- Turn off gridlines
- Turn off the legend

**Step 4 - Format the columns  
**  
The stacked columns build the IQR box. The first series is invisible.

- Sales Quantity PERCENTILE 25 - set color to white (invisible spacer)
- Sales Quantity IQR 25-50 - set to a light shade of your chosen color
- Sales Quantity IQR 50-75 - set to the darker shade of the same color

Go to Layout:

- Set space between categories to 75%
- Set space between series to 3px

![](https://lwfiles.mycourse.app/datatraining-public/1b416e5eea5c163c9c2c36b4f10d1c4d.png)

**Step 5 - Set up markers  
**  
The average marker is built from two overlapping circles - a slightly larger outer ring and a smaller inner dot - giving it that distinctive ringed appearance.  
  

For AVG 2 (outer ring):

- Turn on markers
- Shape - filled circle, 7px
- Border - on, match line color off, border color purple, border width 1px

For Sales Quantity MIN:

- Turn on markers
- Shape - dash, 7px, rotation 0
- Color - purple, transparency 0%
- Border - off

For Sales Quantity MAX:

- Turn on markers
- Shape - dash, 7px, rotation 0
- Color - purple, transparency 0%
- Border - off

For Sales Quantity AVG (inner dot):

- Turn on markers
- Shape - filled circle, 6px
- Border - on, match line color off, border color white, border width 1px

![](https://lwfiles.mycourse.app/datatraining-public/3f0e0ae9d6f9b86528bb934825c8a72d.png)

**Step 6 - Add error bars  
**  
The whiskers - the vertical lines from minimum to maximum - are drawn using error bars on the MAX series.  
  

Go to Format - Error bars, select the MAX series:

- Turn on Enable
- Set Upper bound to Sales Quantity MAX
- Set Lower bound to Sales Quantity MIN
- Set Relationship to measure to Absolute

Under Bar:

- Turn on Bar
- Turn off Match series color
- Set bar color to your preferred color
- Set width to 1
- Set border size to 0px

Under Markers:

- Turn on markers
- Set marker shape to dash
- Set size to 5px

![](https://lwfiles.mycourse.app/datatraining-public/657102819b7b5e8c5595d0f2140520d7.png) ![](https://lwfiles.mycourse.app/datatraining-public/e36787afcd500e3d7d7f92e127b8d271.png) ![](https://lwfiles.mycourse.app/datatraining-public/75d039aea1042115da90d485a43c4a38.png)

A fully native boxplot showing the complete distribution of your data. No custom visual needed, no external dependencies - just a line and stacked column chart with a few clever tricks applied.  
  
And there you go, 4 really useful use cases!**  
  
Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI