---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [bar-chart, dynamic-color, conditional-formatting, threshold, IF-measure]
related: [Color-Coding-4-Techniques, SWITCH, FORMAT]
---

# Dynamic Color Coding for Bar Charts

Applies conditional color to bar chart segments based on thresholds, targets, or category comparisons — one of the four color-coding techniques.

## Step 1 — Create Color Measures

```dax
Color Green  = "#76E3B4"
Color Red    = "#EE6064"
Color Yellow = "#F5A623"
Color Grey   = "#B5C2CA"
```

## Step 2 — Build the Conditional Measure

**Threshold-based:**
```dax
Bar Color =
    IF(
        [Sales] >= [Target],
        [Color Green],
        [Color Red]
    )
```

**3-way threshold:**
```dax
Bar Color 3-Way =
    SWITCH(
        TRUE(),
        [Sales] >= [Target], [Color Green],
        [Sales] >= [Warning Threshold], [Color Yellow],
        [Color Red]
    )
```

**Rank-based:**
```dax
Rank Color =
VAR _TopSeller = CALCULATE(
        RANKX(ALL('Product'[Product]), [Total Sales]),
        REMOVEFILTERS()
    )
RETURN
    IF(_TopSeller <= 3, [Color Green], [Color Grey])
```

## Step 3 — Assign to Visual

1. Add a measure to the bar chart's **Legend** or **Y-axis** field well (the category).
2. Go to **Format → Data colors → Default color → fx**.
3. Select **Field value**.
4. Select the color measure.
5. For each category in the legend, set override to **By field value** → select the measure.

## Notes

- Assigning the color measure to the same field that is on the axis/legend ensures Power BI applies the color in the correct context.
- For clustered bar charts, assign the color measure to the series field.
- Always test with at least 3 data points to confirm all color states render correctly.
- For multi-page reports, create the color constants as a shared measure table (via Enter Data) so they can be reused across pages.

## Related

- [[Color-Coding-4-Techniques]] — full four-technique reference
- [[SWITCH]] — multi-condition color logic
- [[RANKX]] — rank-based coloring
