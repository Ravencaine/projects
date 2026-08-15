---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: pattern
tags: [power-bi, html, dax, html-content-visual, integration, pattern]
---

# HTML Measure Integration Pattern

**Type:** Pattern · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

Return an HTML string from a DAX measure so the HTML Content visual renders it in Power BI. The measure combines static HTML/CSS with dynamic DAX expressions — values computed in DAX are substituted into HTML placeholders before the HTML is returned.

## When to use

When you need styled or dynamic content in a Power BI report that native visuals cannot achieve: dynamic text formatting, conditional icon colors, custom shapes with data-driven content, multi-line formatted labels.

## Formula structure

```dax
MeasureName =
"<html>...</html>"
```

All HTML tags inside double quotes in the measure. Combine with DAX string concatenation (`&`).

## Example: bold text + line breaks

```dax
Visualization Last Semester/Year Average Score =
"Last semester: " & "<b>" & FORMAT([Average Score Last Semester], "0.0") & "</b><br>" &
"Last year: " & "<b>" & FORMAT([Average Score Last Year], "0.0") & "</b>"
```

`<b>` bold, `<br>` new line — all inside double quotes.

## Example: conditional icon + color

```dax
VAR _BackgroundColor =
    IF([Variation] < 0, [Color Light Red], [Color Light Green])
VAR _Shape =
    SUBSTITUTE([Oval Set Up], "{BACKGROUND_COLOR}", _BackgroundColor)
RETURN
    IF([Score] <> BLANK(), _Shape)
```

DAX computes color, SUBSTITUTE injects it into HTML, IF gates output to avoid blanks.

## Key properties

- HTML must be quoted string in measure
- DAX FORMAT, IF, VAR all work inside concatenation
- Nested SUBSTITUTE for multiple placeholders
- IF-blank gates output when no data
- HTML Content visual renders the returned HTML

## Related

- [[html-shape-measure-template]] — placeholder template pattern
- [[font-awesome-dax-icon-measure]] — icon integration
- [[html-content-visual-setup-workflow]] — getting started
- [[dynamic-html-conditional-styling]] — conditional colors/icons/shapes
