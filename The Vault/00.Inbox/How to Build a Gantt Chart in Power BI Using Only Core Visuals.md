---
title: "🗂️ How to Build a Gantt Chart in Power BI (Using Only Core Visuals!)"
source: "https://medium.com/the-bi-corner/%EF%B8%8F-how-to-build-a-gantt-chart-in-power-bi-using-only-core-visuals-6d27e1e56d13"
author:
  - "[[Isabelle Bittar]]"
published: 2025-08-02
created: 2026-08-04
description: "A step-by-step guide to building interactive project timelines in Power BI using bar and column charts."
Processed: "Unprocessed"
---
## A step-by-step guide to building interactive project timelines in Power BI using bar and column charts.

![](99.System/Attachments/1!svZTvNwCEQ843FWE0QR-Bg.png.webp)

By Isabelle Bittar for KI Data Science

**🎁PBIX available at the end of this article!**

### Introduction

Gantt charts are key visuals in project management, but Power BI doesn’t provide a native visual to easily display projects or tasks over a selected time period. And of course, I had to build one recently — so yeah, I needed to figure out an effective workaround 😅.

In my case, the Gantt chart needed to:

- Show tasks and their statuses (*Not Started, Delayed, Pending, In Progress, Completed*)
- Allow dynamic project selection via a slicer
- Display today’s date with a reference line

You can view a quick demo of what the final Gantt chart looks like in action 📽️.

I achieved this by overlaying and syncing two native Power BI visuals:

- A **bar chart** to display project tasks and their durations
- A **column chart** to visualize the project timeline
![](99.System/Attachments/1!8mvlsduLvL1kQEQ-Xk1mLA.png.webp)

📊 Bar Chart and Column Chart Used in Power BI to Build the Gantt Chart

### Step 1: Getting Started

My main table, `Projects`, listed tasks by project, lead, group, status, start date, and end date:

![](99.System/Attachments/1!cMJN_Cvd6eoWGZUuVjFAMA.png.webp)

📄 Projects Table in Power BI

From this, I built a `Dates` table in Power Query that generated all dates between the min and max project dates, including the start of each week:

![](99.System/Attachments/1!E0-oIkiC2c4zijkfGkwb1g.png.webp)

📆 Dates Table in Power BI

These two tables were connected in the model using the `Date` column.

### Step 2: Creating the Project Timeline View

![](99.System/Attachments/1!XOS6sv2tADWaheqxbL49Qw.png.webp)

Creating the Project Timeline View

Once both tables were loaded, I started by creating a **Clustered Column Chart** to represent the timeline.

I first created a simple measure to count project tasks:

```c
Number of tasks = COUNT(Projects[Task])
```

I dropped the `Start of Week` field from the `Dates` table onto the X-axis (making sure it was not the date hierarchy), and added `Number of tasks` to the Y-axis.

![](99.System/Attachments/1!W_161skLasfKC_jA6xBGrQ.png.webp)

📊 Clustered Column Chart Start in Power BI

Next, to sync this with the upcoming bar chart, I created two measures and set them as the X-axis minimum and maximum:

```c
Min Calendar Date = 
    CALCULATE(
        CALCULATE(
            MIN(Dates[Start of Week]),
            FILTER(
                Projects,
                [Number of projects] >= 1
            )
        ),
        ALL(Projects[Task])
    )

Max Project Date = 
    CALCULATE(
        MAX(Projects[Date]),
        ALL(Projects[Task])
    )
```
![](99.System/Attachments/1!r9rhsJgvyzqDsussbZS1kQ.png.webp)

🛠️ Assigning Min and Max X-Axis Range to the Clustered Column Chart in Power BI

This slightly shifts the bars to the right — this is to accommodate tasks that end later.

![](99.System/Attachments/1!LvIEMJQQJYDyYhJnmJwoSw.png.webp)

Clustered Column Chart with Min and Max X-axis Range Set in Power BI

Then, I formatted the visual:

- Removed axis titles
- Removed Y-axis values
- Set column color to **100% transparent**
![](99.System/Attachments/1!N54EVC4WZiw13RNWSK1fBg.png.webp)

🎨 Setting the Chart’s Columns Color to Transparent in Power BI

Finally, I needed to add a reference line for today’s date. I created the following measure (very complex 😂) and assigned it to the **X-Axis Constant Line**.

```c
Today = TODAY()
```

Here are some formatting touches I made to the default line:

- Renamed to “Today”
- Set color to purple `#4947CC`
- Width: 1px
- Enabled shade area with 97% transparency
- Turned on data label to show name underneath
![](99.System/Attachments/1!m3UyiAVtOiXbG0ln8n25jw.png.webp)

📌 Setting the Chart’s X-Axis Constant Line in Power BI

Now that the timeline was done, I moved on to building the bar chart for task durations.

### Step 3: Displaying the Project Tasks

![](99.System/Attachments/1!DBpIa_zv_hffGzbgd4z29w.png.webp)

Displaying the Project Tasks

For this step, I started by creating the following two measures: Task Start Date and Task End Date.

```c
Task Start Date = 
    CALCULATE(
        MAX(Projects[Date]),
        FILTER(
            Projects,
            Projects[Date Type] = "Start Date"
        )
    )

Task End Date = 
    CALCULATE(
        MAX(Projects[Date]),
        FILTER(
            Projects,
            Projects[Date Type] = "End Date"
        )
    )
```

From there, I calculated the task duration:

```c
Task Duration = DATEDIFF([Task Start Date], [Task End Date],DAY)
```

Adding the `Task Duration` measure to the X-axis of a bar chart with `Task` on the Y-axis gave me the following view:

![](99.System/Attachments/1!X_C4qawm3o7xQ5bUFA0iZA.png.webp)

📊 Initial Bar Chart Displaying Task Duration for Each Project Task

To align everything with the project timeline, I added a buffer to represent the gap before each task begins.

```c
Number of projects = COUNT(Projects[Project])

Date Start Buffer = 
VAR _MinCalendarDate = 
    CALCULATE(
        CALCULATE(
            MIN(Dates[Start of Week]),
            FILTER(
                Projects,
                [Number of projects] >= 1
            )
        ),
        ALL(Projects[Task])
    )
VAR _MinProjecDate = CALCULATE([Min Project Date], ALL(Projects[Task]))
RETURN DATEDIFF(_MinCalendarDate, [Min Project Date], DAY) + DATEDIFF([Min Project Date], [Task Start Date], DAY)
```
![](99.System/Attachments/1!-3W3MQZgfuxeWg7kU48TIw.png.webp)

Adding the Date Start Buffer Measure to the Bar Chart’s X-Axis in Power BI

I then dropped the `Date Start Buffer` into the X-axis:

- Set its series color to **100% transparent**
- Sorted the axis in ascending order by this field
![](99.System/Attachments/1!RYgJCEhvRSFHBKTYLDGfNQ.png.webp)

✨ Setting the Date Start Buffer Series Color and Sorting in Power BI

Next, to color the task bars by status, I created 5 status-specific measures and replaced the original **Task Duration** measure on the X-axis with these. Then I manually set the color of each series.

```c
Task duration - completed = 
    IF(
        SELECTEDVALUE(Projects[Status]) = "Completed",
        [Task Duration]
    )

Task duration - delayed = 
    IF(
        SELECTEDVALUE(Projects[Status]) = "Delayed",
        [Task Duration]
    )

Task duration - in progress = 
    IF(
        SELECTEDVALUE(Projects[Status]) = "In Progress",
        [Task Duration]
    )

Task duration - not started = 
    IF(
        SELECTEDVALUE(Projects[Status]) = "Not Started",
        [Task Duration]
    )

Task duration - pending = 
    IF(
        SELECTEDVALUE(Projects[Status]) = "Pending",
        [Task Duration]
    )
```
![](99.System/Attachments/1!oQani_DASTFZOlmL7cIIhA.png.webp)

🎨 Replacing Task Duration with Status-Based Measures in Power BI

Then, instead of displaying each task name directly on the Y-axis, I added two custom labels. First, I created a vertical bar “|” as a marker, conditionally colored by status, and then a label that includes a relevant icon per task group.

```c
Task Status Bar = "|"

Status Border Color = 
    SWITCH(
        SELECTEDVALUE(Projects[Status]),
        "Delayed", [_Color Dark Orange],
        "In Progress", [_Color Dark Blue],
        "Not Started", [_Color Dark Grey],
        "Pending", [_Color Dark Purple],
        "Completed", [_Color Dark Green]
    )

Task Label = 
VAR _Group = SELECTEDVALUE('Projects'[Task Group])
VAR _Task = SELECTEDVALUE('Projects'[Task])

VAR _Icon =
    SWITCH(
        _Group,
        "Planning", "🗂️",
        "Design", "🎨",
        "Execution", "⚙️",
        "Testing", "🔍",
        "Deployment", "🚀",
        "📌" -- default
    )

RETURN _Icon & " " & _Task
```
![](99.System/Attachments/1!UdSODDNoR93UksLZyqFD5w.png.webp)

📋 Adding Custom Labels and Icons to the Bar Chart in Power BI

Then, I:

- Turned off axis titles and values
- Removed the chart legend and title
- Set the background to transparent

This allowed me to overlay the bar chart cleanly on top of the timeline.

![](99.System/Attachments/1!66O--Hattv9equWF1fR0_w.png.webp)

Bar Chart After Making a Few Formatting Changes in Power BI

To ensure that dates from the timeline column chart aligned properly with the tasks from the bar chart, I needed to make sure that the **right end of the bar chart** was flush with the **right end of the column chart**, and that the **left start of the bar chart** was flush with the **first date (and vertical gridline) of the X-axis of the column chart**.

I also added **Task Start Date** and **Task End Date** to the tooltip to make sure alignment between the two charts was tight and properly synced.

![](99.System/Attachments/1!Mxofag2oYTgW0iV2T7WR7g.png.webp)

📐 Verifying Chart Alignment in Power BI

### Step 4: Final Formatting Touches

![](99.System/Attachments/1!Bq0ETiTNpIFuw46j_trj8A.png.webp)

Final Formatting Touches Brought to Gantt Chart in Power BI

Finally, I brought some last formatting touches to the combined visual, which included adding the following:

- Chart title in a text Box
- Slicer for project selection
- Status legend using a text box and shapes
- Custom tooltip page assigned to the visual
- Assigned task leads profiles using a HTML visual

You can see the detail in the PBIX available at the end of this article, but if you are interesting in learning more about how to create some of these components, such as the task leads profile pictures 🤩, here is one of my article that goes in more detail:

## [My Best Power BI KPI Card (So Far 😅)](https://medium.com/the-bi-corner/my-best-power-bi-kpi-card-so-far-deb7513ff3be?source=post_page-----6d27e1e56d13---------------------------------------)

### 🎁 PBIX available for download at the end of this article!

medium.com

### Wrapping Up

While not too complicated once you know how 😅, it took me a few tries to get everything aligned — especially syncing the task bars with the timeline.

Maybe someday Power BI will release native visuals for project management (🤞), especially since I’ve noticed more and more requests for this type of dashboard lately. Have you seen the same trend?

In the meantime, these were my hacks for building a Gantt chart — and if you’ve found another clever way to do it, I’d love to hear about it!

**👉You can download my report with all visuals and formatting as displayed in the cover picture of this article** [**here**](https://drive.google.com/file/d/1qG27MWuxNmHqePrRTYIahpaqm8VyrbzW/view?usp=sharing)**.**

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)