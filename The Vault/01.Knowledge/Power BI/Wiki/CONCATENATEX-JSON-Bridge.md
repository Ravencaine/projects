---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: snippet
tags: [dax, concatenatex, json, html-content, data-transfer]
---

# CONCATENATEX JSON Bridge

DAX pattern that serialises a table into a JavaScript-readable JSON array, enabling DAX measures to pass data into the HTML Content visual's JavaScript context.

## Code

```dax
VAR JsonData =
    CONCATENATEX(
        MyTable,
        "{key:'" & MyTable[Column] & "',value:" & MyTable[Value] & "}",
        ","
    )
RETURN
"
var rawData = [" & JsonData & "];
// rawData is now a JS array of {key, value} objects
"
```

## When to Use

- Passing date-series data from a DAX measure into the HTML Content visual for JavaScript charting
- Any scenario where a visual needs data that DAX alone cannot render (custom JS visuals, D3, Plotly, Google Charts)
- Bridges tabular DAX output to JSON-consuming web libraries

## Key Mechanics

- **`CONCATENATEX`** iterates every row in `MyTable` (respecting current filter context)
- The delimiter `","` separates objects; the trailing delimiter is stripped automatically
- **String interpolation** via `&` concatenates column values into the JSON template
- The result is embedded in the HTML string via `[" & JsonData & "]` — this injects the raw string value at measure-evaluate time

## Variations

```dax
-- Date format: use "yyyy-mm-dd" for JS Date() constructor compatibility
VAR JsonData = CONCATENATEX(
    calendar_table,
    "{date:'" & FORMAT([Date], "yyyy-mm-dd") & "',value:" & [Measure] & "}",
    ","
)

-- Multiple measures
VAR JsonData = CONCATENATEX(
    calendar_table,
    "{date:'" & FORMAT([Date], "yyyy-mm-dd") &
    "',actual:" & [Sales] &
    ",target:" & [Target] & "}",
    ","
)
```

## Related

- [[GitHub-Style-Calendar-Heatmap-Pattern]] — full working example with Plotly
- [[Dynamic-Alerts]] — CONCATENATEX + HTML Content for alert list rendering
