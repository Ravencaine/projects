---
created: 2026-08-04
updated: 2026-08-05
source: "How to Build a Gantt Chart in Power BI Using Only Core Visuals.md"
note_type: pattern
tags: [powerbi, dax, pattern, conditional-measures, status-coloring, color-by-status]
---

# Status-Conditioned Measure Family (One Measure Per Status)

When you want a single bar (or KPI, or icon, or label) to take on a different value or color for each member of a categorical field — but conditional formatting on one measure is too clumsy — build a family of measures, one per category value, each gated by `IF(SELECTEDVALUE(<category>) = "<value>", <base value>)`. Drop the whole family on the visual's value axis; assign each measure a colour manually.

## Purpose

Power BI's conditional formatting on a single measure gives you colour-by-value (a gradient) but not colour-by-category reliably when the value axis is a measure (not a column). For categorical encoding — "Not Started = grey, Delayed = orange, Completed = green" — the cleanest path is **one measure per status**, dropped as siblings in the same visual field bucket. Each measure evaluates to the base value only when the row matches its status, and BLANK otherwise. The visual draws each series in its assigned colour; BLANK rows draw nothing.

Use when:

- A bar chart, KPI card, or matrix needs a **categorical colour code** (status, severity, priority, region, etc.).
- The category is a **slicer-driven filter** (not a row-level dimension) — i.e., the chart already aggregates across rows, so the per-row measure approach won't work.
- The number of distinct categories is small (≤ ~7) — otherwise the measure family becomes unwieldy.

Do NOT use when:

- The category is on rows/columns of the visual (then `SWITCH` colour formatting on a single measure works directly).
- You need **colour-by-measure-value** (a gradient), not colour-by-category — use conditional formatting instead.
- The category has dozens of values — the measure-family pattern doesn't scale past ~7.

## Components

- A **base value measure:** what every status-conditioned measure wraps (e.g., `Task Duration`, `Sales Amount`, `Open Ticket Count`).
- A **category column** with a small fixed set of string values (e.g., `Projects[Status]`).
- `SELECTEDVALUE(<category column>)` — returns the active category for the current filter context, or BLANK if multiple/no values are selected.
- `IF(SELECTEDVALUE(...) = "<status>", <base value>)` — the gating wrapper for each measure in the family.

## Structure

```DAX
// Base value — the value every status measure returns when its status matches
Base Value = <whatever the chart shows when unfiltered>

// One measure per status value — repeat this template for each
<Metric> - <status value> =
IF(
    SELECTEDVALUE(<table>[<status column>]) = "<status value>",
    [<Base Value>]
)
```

Five-measure example from the Gantt article:

```DAX
Task Duration = DATEDIFF([Task Start Date], [Task End Date], DAY)

Task duration - completed   = IF(SELECTEDVALUE(Projects[Status]) = "Completed",   [Task Duration])
Task duration - delayed     = IF(SELECTEDVALUE(Projects[Status]) = "Delayed",     [Task Duration])
Task duration - in progress = IF(SELECTEDVALUE(Projects[Status]) = "In Progress", [Task Duration])
Task duration - not started = IF(SELECTEDVALUE(Projects[Status]) = "Not Started", [Task Duration])
Task duration - pending     = IF(SELECTEDVALUE(Projects[Status]) = "Pending",     [Task Duration])
```

Drop all five into the bar chart's X-axis (or Y-axis, depending on orientation). Power BI treats each as a separate series; assign each its own colour via the Format pane.

## Example

Gantt chart colour-by-status: each task gets a bar in its status colour, with only the matching measure returning a value for that row. The bar chart shows five series, but each task row only has a non-BLANK value from one of the five — so visually, you see one coloured bar per task, coloured by its status.

## Variations

- **Numeric value family.** The `IF` can wrap a numeric expression per status — e.g., one measure per status returns `Sales * 1.0`, another returns `Sales * 0.85`, another returns `Sales * 1.15`. Same scaffolding, different value per status.
- **Layered with emoji/icon.** Pair with a `SWITCH(SELECTEDVALUE(Status), ...)` measure that returns an emoji or icon glyph per status — gives visual plus label in one move.
- **Replacing conditional formatting.** When conditional formatting on a card or KPI doesn't support the granularity you need, drop a single status-conditioned measure that returns one value when its status matches, BLANK otherwise, and assign the colour manually.
- **Two-column category keys.** When a category is composed of two fields (e.g., `Priority × Region`), the measure can gate on both: `IF(SELECTEDVALUE(Priority) = "High" && SELECTEDVALUE(Region) = "EMEA", <value>)`. Use sparingly — the measure count grows multiplicatively.

## Related

- [[Gantt-Chart-Native-Visuals-Overlay-Pattern]] — the headline use of this pattern (5 status measures on a Gantt bar chart).
- [[SWITCH-Color-Assignment]] — alternative for cases where the category is on rows/columns (single measure, `SWITCH` colour).
- [[Dynamic-Color-Coding-Bar-Charts]] — broader bar-chart colour-coding strategies; the status-conditioned family is one of them.
- [[Status Border Color]] (embedded in the Gantt atomic) — sibling `SWITCH(SELECTEDVALUE(...), "...")` measure for label colours, same SELECTEDVALUE idiom.
- [[Task Label]] (embedded in the Gantt atomic) — sibling emoji-composition measure, same SELECTEDVALUE-driven pattern.