---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: snippet
tags: [power-bi, dax, slicers, disconnected-table, highlight, conditional-formatting]
related:
  - "[[Slicer-Highlight-vs-Filter]]"
  - "[[Disconnected-Table-Slicer-Pattern]]"
---

# Slicer Highlight Measure: SELECTEDVALUE + IN VALUES

DAX measure that detects whether a row's value is selected in a disconnected table slicer, returning 1 if selected (for use in conditional formatting) or 0 if not.

## Code

```dax
Highlight =
VAR Check =
    COUNTROWS(
        FILTER(
            'Products',                          -- connected dimension table
            'Products'[Product]                  -- dimension column
                IN VALUES('Products_Disconnected'[Product])  -- disconnected table column
        )
    )
RETURN
    IF(Check >= 1, 1, 0)
```

## When to Use

- In a table, matrix, or chart visual where you want to highlight matching rows instead of filtering them out
- As a conditional formatting field value applied to Background Color or Font Color
- In combination with a disconnected table slicer to enable multi-select highlighting without affecting filter context

## Variations

- **Count-based threshold:** `IF(Check >= 2, ...)` to only highlight when 2+ rows match
- **Text output:** Replace `1` and `0` with color names or text strings
- **Dual column:** Check against two disconnected tables simultaneously with nested `IN VALUES()`
- **Blank handling:** Add `&& NOT(ISBLANK(...))` to the filter condition to exclude blank rows

See also [[calculate]] for the core DAX function reference.

## Related

- [[Slicer-Highlight-vs-Filter]] — full worked example of the pattern
- [[Disconnected-Table-Slicer-Pattern]] — how to create the disconnected table
