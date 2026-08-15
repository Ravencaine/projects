---
created: 2026-08-13
source: "Level Up with Custom Visuals Power BI HTML Calculation Groups Deneb"
source_url: https://www.youtube.com/watch?v=QXMMpabHPS4
note_type: workflow
tags: [remixicon, html-visual, svg, power-query, dynamic-icons]
---

# Dynamic SVG Icons via HTML + RemixIcon

Import 2,271 free SVG icons from RemixIcon into a Power BI table, expose them as a slicer, and color them dynamically through the HTML custom visual.

## Prerequisites

- [remixicon.com](https://remixicon.com) account (free, no attribution required but appreciated)
- Power BI Desktop with an HTML custom visual installed (e.g. HTML Content by Daniel Marsh Patrick)

## Steps

### 1 — Download the Icon Pack

Go to remixicon.com → Download all icons → unzip the folder locally.

### 2 — Import Folder as Binary Table

In Power BI: **Get Data → Folder** → point at the unzipped icon folder → load. Power BI produces a table with one row per file; the `Content` column holds binary SVG data.

### 3 — Convert Binary to Text in Power Query

Right-click the `Content` column → **Transform → Transform to Text**. The column now holds the raw SVG markup as text.

### 4 — Keep Only the SVG Column and the Name

Drop the metadata columns (path, extension, etc.). Keep:

- `Name` — e.g. `ri-bar-chart-line`, used for the icon picker
- `Content` — the SVG markup

> The `Name` column is essential: filtering an HTML visual by raw SVG text is impractical because the markup is long and unique per icon. Filtering by name is instant.

### 5 — Use As-Is (Static Color)

Drop the `Content` column into the **Values** field of an HTML visual. The icon renders with its default (black) fill.

### 6 — Substitute the Color for Dynamic Theming

```dax
IconWithColor =
VAR _Color = [ColorText]            // shared measure from [[dynamic-color-themes-via-html-rgb]]
VAR _SVG   = SELECTEDVALUE('Icons'[Content])
RETURN
SUBSTITUTE(
    SUBSTITUTE(
        _SVG,
        "fill=""currentColor""", 1),
    "<path", "<path fill='" & _Color & "'"
)
```

A typical Remix Icon SVG starts with `<path d="..."` and inherits color from `currentColor`. Substituting `currentColor` (or wrapping `<path`) with a hex value lets the same icon wear different colors across reports.

### 7 — Pick Icons from a Slicer

Add the `Name` column to a slicer with **Single-Select** enabled. Each selection drives both `Content` (icon shape) and `Content`-derived measures in any HTML visual on the page.

## Variations

- **Static variant** — drop `Content` directly into Values; skip step 6.
- **Indexed info panel** — Injae Park uses an information-button report with all 2,271 icons in one page so users can browse and copy the exact `Name` for their slicer.
- **Color-graded variant** — the substitute measure above lets the same icon render in primary, secondary, gradient, or RGB-derived colors driven by the same controls as the rest of the report.

## Gotchas

- The `Content` column for all 2,271 icons can inflate PBIX size noticeably. Be aware of file size.
- RemixIcon SVGs may use `currentColor` or hardcoded color values; check that the substitution target exists in the markup.

## Related

- [[dynamic-html-text-via-calculation-groups]] — same HTML visual + DAX approach
- [[dynamic-color-themes-via-html-rgb]] — for sourcing the dynamic color
