---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, svg, dynamic-visual, image]
note_type: pattern

---

# SVG Visualizations in Power BI

Creating dynamic visual elements using SVG strings rendered in Power BI image fields.

## Purpose

Power BI has no native SVG visual, but SVG can be generated in DAX and displayed via the Image visual or as a measure in a table.

## Pattern

```dax
SVG Bar Chart :=
VAR __Value = [Sales]
VAR __Max = [Max Sales]
VAR __Width = INT( DIVIDE( __Value, __Max ) * 200 )
VAR __SVG = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='30'><rect width='" & __Width & "' height='20' fill='steelblue'/></svg>"
RETURN
__SVG
```

## Dynamic SVG with Color Coding

```dax
SVG KPI :=
VAR __Value = [KPI]
VAR __Color = IF( __Value >= 0, "green", "red" )
VAR __Arrow = IF( __Value >= 0, UNICHAR( 9650 ), UNICHAR( 9660 ) )
VAR __SVG = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='30'><text x='5' y='22' fill='" & __Color & "' font-size='20'>" & __Arrow & " " & FORMAT( __Value, "0.0%" ) & "</text></svg>"
RETURN
__SVG
```

## Notes

- Use UNICHAR() for dynamic icons within SVG text elements
- Requires the "Image" visual or rendering SVG as a measure column
- Encode SVG strings as data URIs: `data:image/svg+xml;utf8,<svg>...</svg>`

## Related

- [[UNICHAR]]
- [[dynamic-text-titles-in-power-bi]]
