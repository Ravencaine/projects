---
created: 2026-08-02
updated: 2026-08-05
source: Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels
note_type: function
tags: [dax, measure, switch, formatting, string]
---

# Formatted Process Duration Variation

Formats the numeric variance as a human-readable string with ±sign and pluralized "day"/"days".

```dax
Formatted Process Duration Variation =
    SWITCH(
        TRUE(),
        [Process Duration Variation] = 1,  "+ " & [Process Duration Variation] & " day",
        [Process Duration Variation] > 0,  "+ " & [Process Duration Variation] & " days",
        [Process Duration Variation] = -1, [Process Duration Variation] & " day",
        [Process Duration Variation] < 0,  [Process Duration Variation] & " days"
    )
```

## Key Technique

SWITCH(TRUE(), ...) pattern for multi-condition branching on a numeric value. Each condition checked in order; first TRUE wins.

## Gotcha

SWITCH without a final `0` (or equivalent) returns BLANK when no condition matches — verify the data cannot produce an exact-zero variation, or add an explicit `0` condition returning `""`.

## Source

Isabelle Bittar — "Level Up Your Dashboards With Power BI's New & Improved Chart Data Labels", 2024-01-21
