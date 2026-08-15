---
created: 2026-08-09
updated: 2026-08-09
source: "Elevating Power BI Reports with HTML & CSS Joining Forces 💪.md"
note_type: atomic
tags: [power-bi, html, dax, style-tags, atomic]
---

# HTML Style Tags in DAX Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-html-css-joining-forces-fp20]]

HTML style tags can be embedded directly in DAX measures (inside quotation marks) to style text rendered by the HTML Content visual.

## Core tags

| Tag | Effect | Example |
|-----|--------|---------|
| `<b>...</b>` | Bold | `"<b>" & [Value] & "</b>"` |
| `<i>...</i>` | Italic | `"<i>" & [Value] & "</i>"` |
| `<u>...</u>` | Underline | `"<u>" & [Value] & "</u>"` |
| `<br>` | Line break | `"Line1<br>Line2"` |
| `<span style="color:#FF5733;">...</span>` | Inline color | `"<span style=""color:#FF5733;"">" & [Value] & "</span>"` |
| `<div style="font-family:'Arial';">...</div>` | Font family | Changes font for enclosed text |

## Combining tags

Tags can be chained inside the same quotation marks:

```dax
"Last semester: " & "<b>" & FORMAT([Score], "0.0") & "</b><br>" &
"Last year: " & "<b>" & FORMAT([PriorScore], "0.0") & "</b>"
```

`</b><br>` appears together inside the same string.

## Applying to measures

```dax
"Variance: " & "<b>" & FORMAT([Variance], "0.0%") & "</b>"
```

DAX computes the value (FORMAT, IF, etc.), HTML tags wrap it with styling.

## Related

- [[html-measure-integration-pattern]] — using these tags in full measures
- [[dynamic-html-conditional-styling]] — conditional tag selection
