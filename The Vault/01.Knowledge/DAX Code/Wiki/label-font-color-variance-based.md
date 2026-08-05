---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, conditional-formatting, color, font, switch, chart]
---

# Label Font Color — Variance-Based Color

Assigns a hex font color based on variance direction. Used alongside [[label-variance-if-arrow-format]] for fully styled data labels.

## Pattern

```c
// Color constants (stored in dedicated measures)
_Color Dark Green := "#31D286"
_Color Dark Red  := "#F05660"
_Color Text Secondary := "#79797C"

// Font color measure
Label Font Color =
    SWITCH(
        TRUE(),
        [Variance] > 0, [_Color Dark Red],   // up = worsening (turnover example)
        [Variance] < 0, [_Color Dark Green], // down = improving
        [_Color Text Secondary]              // no change
    )
```

> Note: In the HR turnover example, `> 0` (more leavers) → red because higher turnover is bad. Flip the logic for sales/profit scenarios where `> 0` → green.

## Applying

Set **Data label → Font color → fx → Field value** → point to `Label Font Color`.

## Config

`// 🔧` — Swap red/green logic based on whether increases are good or bad for your metric.

## Related

- [[label-variance-if-arrow-format]]
- [[dual-measure-label-background-trick]]
- [[color-palette-measures-static-hex-strings]]
