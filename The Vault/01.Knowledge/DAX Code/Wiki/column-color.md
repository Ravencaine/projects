---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, color, conditional-formatting, switch]
---

# Column Color

A SWITCH-TRUE measure that returns a hex color code for conditional data colors on a clustered column chart, based on the active highlight and threshold comparisons.

## Signature

```dax
Column Color =
    SWITCH(
        TRUE(),
        SELECTEDVALUE(Highlights[Order]) = 1
            && [High OT Employees (Last 7 Days)] = [Most Employees Flagged for High OT per Unit],
            [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 2
            && [OT Hours per FTE Variance %] <= 0,
            [_Color Green],
        SELECTEDVALUE(Highlights[Order]) = 2
            && [OT Hours per FTE Variance %],
            [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 3
            && [OT Hours This Week] = [Highest OT Hours per Unit],
            [_Color Red],

        SELECTEDVALUE(Highlights[Order]) = 4
            && [Filled Rate % This Week] = [Lowest Fill Rate],
            [_Color Red],

        [_Color Medium Blue]
    )
```

## Parameters

None — reads `SELECTEDVALUE(Highlights[Order])` and a threshold comparison measure per highlight.

## Returns

A color name or hex string — `_Color Red`, `_Color Green`, `_Color Medium Blue`. The color names are defined as separate measures in the model (`_Constants/Colors` folder).

## Notes

`SWITCH(TRUE(), ...)` evaluates each condition as a boolean and returns the result of the first matching branch. This is the standard DAX idiom for multi-condition logic. Each highlight has its own color logic: for OT metrics, red = bad (high OT); for variance, green = decrease (improvement). A neutral blue is the default for all other bars.

## Related

- [[Column-Value]]
- [[Graph-Title]]
- [[Graph-Subtitle]]
