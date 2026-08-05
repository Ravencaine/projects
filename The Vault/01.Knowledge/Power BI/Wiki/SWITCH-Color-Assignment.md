---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [color, bar-chart, conditional-formatting, SWITCH, SELECTEDVALUE]
related: [Color-Coding-4-Techniques, SWITCH, RANKX]
---

# SWITCH Color Assignment (Field Values)

Uses `SWITCH` + `SELECTEDVALUE` to return a hex color string for each distinct category value, then assigns the measure to the visual's field value color property.

## Pattern

**Step 1 — Create the color measure:**
```dax
Category Color =
    SWITCH(
        TRUE(),
        SELECTEDVALUE('Category'[Category]) = "High Priority", "#EE6064",
        SELECTEDVALUE('Category'[Category]) = "Medium Priority", "#F5A623",
        SELECTEDVALUE('Category'[Category]) = "Low Priority", "#76E3B4",
        "#B5C2CA"  // default
    )
```

**Step 2 — Assign to visual:**
1. Add the `Category` field to the legend or axis of the bar chart.
2. Go to **Format → Data colors**.
3. Select **Default color → fx → Field value**.
4. Select the `Category Color` measure.

**Step 3 — For each category value, set the color override to "By field value" and select the measure.**

## Application: Process Tracker Fill Color

```dax
Job Posting Fill Color =
    SWITCH(
        TRUE(),
        [Selected Stage Order] > 1, "#4059ad",   // completed
        [Selected Stage Order] = 1, "#fe5f55",  // in progress
        "#B5C2CA"                                // not started
    )
```

Assign to the oval shape's **Fill → fx → Field value → Category Color**.

## Application: Bubble Chart Vacancy Rate Color

```dax
Vacancy Rate Color =
VAR _No1 = CALCULATE([No.1 Ranking], ALL('NAICS Industry'[Industry]))
VAR _No2 = CALCULATE([No.2 Ranking], ALL('NAICS Industry'[Industry]))
VAR _No3 = CALCULATE([No.3 Ranking], ALL('NAICS Industry'[Industry]))
RETURN
    SWITCH(
        TRUE(),
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No1, "#EE6064",
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No2, "#EE6064",
        SELECTEDVALUE('NAICS Industry'[Industry]) = _No3, "#EE6064",
        "#76E3B4"
    )
```

## Notes

- `SELECTEDVALUE` reads the current row's category from the visual's filter context.
- The `TRUE()` as the first argument to SWITCH enables the boolean condition form — each condition is a boolean expression.
- Always include a final default color — SWITCH returns BLANK if no condition matches, which causes the visual to use its default color.
- Works on: bar charts, column charts, matrix, table, shapes, text boxes.
- In Bittar's articles, this pattern is the foundation of every color-coding technique — it adapts to the current visual context.

## Related

- [[SWITCH]] — conditional branching logic
- [[SELECTEDVALUE]] — read current category from visual context
- [[RANKX]] — identify top-N items for color assignment
- [[Color-Coding-4-Techniques]] — full reference
