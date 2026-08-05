---
created: 2026-08-04
updated: 2026-08-05
source: "How to Build a Gantt Chart in Power BI Using Only Core Visuals.md"
note_type: atomic
tags: [powerbi, visualization, gantt, native-visuals, overlay-pattern]
---

# Gantt Chart — Native-Visuals Overlay Pattern

Power BI has no native Gantt-chart visual, but the appearance of one can be reproduced by overlaying two core visuals — a column chart and a bar chart — each made transparent where it shouldn't show, so only the timeline grid and the per-task bars remain visible.

## Definition

A **two-chart stack** in which a clustered column chart owns the date X-axis (with its columns rendered fully transparent) and a bar chart carries the per-task durations (with its left-side buffer made transparent), both aligned to the same X-axis coordinates so that each task bar visually sits on its true start–end span. A "today" reference line is added through the column chart's Analytics pane.

## Key Points

- **Two visuals, one chart.** The column chart is the timeline skeleton; the bar chart is the visible Gantt body. Each visual has formatting that hides the parts the other visual "owns" (column chart columns = transparent; bar chart's left-pad buffer = transparent series).
- **Axis bounds must be measured.** The column chart's X-axis min and max are wired to `Min Calendar Date` and `Max Project Date` measures so the chart adapts to whatever date range the slicer selects. Manual axis bounds break when data changes.
- **The bar chart needs a buffer.** Without a left-side buffer, bars start at X = 0 and float disconnected from the timeline. A `Date Start Buffer` measure (`DATEDIFF(min calendar date, task start) + DATEDIFF(min project date, task start)`) is dropped in as a second transparent series.
- **Color-by-status is a measure family.** Rather than fight conditional formatting on a single measure, build one measure per status (Not Started, Delayed, Pending, In Progress, Completed), each gated by `IF(SELECTEDVALUE(Status) = "...", [Task Duration])`. Drop the whole family on the X-axis and assign each series its own color.
- **Custom labels need two measures.** A vertical-bar `" | "` marker colored by status sits next to an emoji-prefixed task name (Planning = 🗂️, Design = 🎨, Execution = ⚙️, Testing = 🔍, Deployment = 🚀). Together they form the Gantt's Y-axis row content.

## Examples

```DAX
// Axis bound — minimum date of the project timeline window
Min Calendar Date =
CALCULATE(
    CALCULATE(
        MIN(Dates[Start of Week]),
        FILTER(Projects, [Number of projects] >= 1)
    ),
    ALL(Projects[Task])
)

// Axis bound — maximum project date (where timeline ends)
Max Project Date =
CALCULATE(MAX(Projects[Date]), ALL(Projects[Task]))

// Per-task start — pulled from a long-form Date Type column
Task Start Date =
CALCULATE(
    MAX(Projects[Date]),
    FILTER(Projects, Projects[Date Type] = "Start Date")
)

// Per-task end — same shape, filtered to end-date rows
Task End Date =
CALCULATE(
    MAX(Projects[Date]),
    FILTER(Projects, Projects[Date Type] = "End Date")
)

// Per-task duration in days
Task Duration = DATEDIFF([Task Start Date], [Task End Date], DAY)

// Transparent buffer that pushes each bar to its true horizontal position
Date Start Buffer =
VAR _MinCalendarDate =
    CALCULATE(
        CALCULATE(MIN(Dates[Start of Week]), FILTER(Projects, [Number of projects] >= 1)),
        ALL(Projects[Task])
    )
VAR _MinProjectDate = CALCULATE([Min Project Date], ALL(Projects[Task]))
RETURN
    DATEDIFF(_MinCalendarDate, [Min Project Date], DAY)
    + DATEDIFF([Min Project Date], [Task Start Date], DAY)

// Status-conditioned duration — one of five siblings
Task duration - completed =
IF(SELECTEDVALUE(Projects[Status]) = "Completed", [Task Duration])

// Today reference line — add via Analytics pane > X-Axis Constant Line
Today = TODAY()

// Y-axis row content: status-colored vertical bar
Task Status Bar = "|"

// Status-driven border color for the bar marker
Status Border Color =
SWITCH(
    SELECTEDVALUE(Projects[Status]),
    "Delayed", [_Color Dark Orange],
    "In Progress", [_Color Dark Blue],
    "Not Started", [_Color Dark Grey],
    "Pending", [_Color Dark Purple],
    "Completed", [_Color Dark Green]
)

// Emoji + task name composed label
Task Label =
VAR _Group = SELECTEDVALUE(Projects[Task Group])
VAR _Task  = SELECTEDVALUE(Projects[Task])
VAR _Icon  =
    SWITCH(
        _Group,
        "Planning",   "🗂️",
        "Design",     "🎨",
        "Execution",  "⚙️",
        "Testing",    "🔍",
        "Deployment", "🚀",
        "📌" -- default
    )
RETURN _Icon & " " & _Task
```

**Build order (from the article):**

1. Build a `Dates` table in Power Query covering every date between min and max project dates, including `Start of Week`. Connect it to `Projects` on the date column.
2. Add a clustered column chart with `Dates[Start of Week]` (NOT the date hierarchy) on the X-axis and `Number of tasks` on the Y-axis. Then wire the X-axis min/max to the bound measures.
3. Format the column chart: remove axis titles, hide Y-axis values, set column color to 100% transparent. Add the `Today` constant line in the Analytics pane.
4. Add a bar chart with `Projects[Task]` on the Y-axis. Drop in the `Date Start Buffer` first, set its series color to 100% transparent, sort Y-axis ascending by the buffer.
5. Drop in the five status-conditioned `Task duration - <status>` measures; assign each a color.
6. Add the `Task Status Bar` and `Task Label` to the Y-axis as custom label rows; remove axis titles/values/legend, set background transparent.
7. Verify the right end of the bar chart lines up with the right end of the column chart, and the left start with the first X-axis gridline. Add `Task Start Date` / `Task End Date` to the tooltip to confirm alignment.

## Related

- [[Source-Gantt-Chart-Native-Visuals]] — source article record.
- [[Status-Conditioned-Measure-Family-Pattern]] — the 5-measure family used for color-by-status is reusable beyond Gantt charts (segment-coloured bars, conditional KPIs, etc.).
- [[Chart-Alignment-Between-Stacked-Visuals-Gotcha]] — alignment between the two charts is the trickiest part of the build.
- [[Bar-to-Area-Conversion]] — related overlay trick where a bar chart is converted into an area chart with hidden borders to fake a modern shape.
- [[Error-Band-as-White-Out-Mask]] — another "hide the chart's own lines to fake a different shape" trick in the same native-visual-override family.