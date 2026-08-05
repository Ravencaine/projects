---
created: 2026-08-05
source: 4 Tips Work Efficiently Power BI (Isabelle Bittar)
note_type: atomic
tags: [power-bi, dax, color, theme, hex, conditional-formatting, best-practice]
---

# Color Measures: Consistent Theme Values

Storing hex color values in named DAX measures instead of hard-coding them in conditional formatting expressions — enabling single-point palette updates across a report.

## Definition

Creating one-row DAX measures that return a hex string:

```dax
Color Green = "#2C6D6A"
Color Red   = "#D8404A"
```

Then referencing these measures in conditional formatting rules instead of typing the hex values directly.

## How to Use

### In conditional formatting (field-based)

1. Select a visual → **Format → Data colors**
2. Click the **fx** button → **Based on field**
3. Select the DAX color measure (e.g., `[Color Green]`) as the field value
4. Apply to the relevant measure

### In DAX expressions

```dax
Score Variation Color =
IF(
    [Score Variation] > 0,
    [Color Green],
    [Color Red]
)
```

The color measure is referenced as a value, not called as a function — it returns the hex string which DAX then uses as the output.

## Benefits

| Benefit | Detail |
|---------|--------|
| **Single-point update** | Change one measure's value, every visual that uses it updates |
| **Consistency** | Same shade used everywhere — no accidental variation |
| **Theme alignment** | Updating a brand palette requires changing only the color measures |
| **Auditability** | Color intent is in a named measure, not buried in a visual's format pane |

## Example Color Measure Set

```dax
// Semantic palette
Color Green   = "#2C6D6A"
Color Red     = "#D8404A"
Color Amber   = "#F5A623"
Color Blue    = "#1B65A6"
Color Grey    = "#888888"

// Conditional status colors
Color Good    = "#2C6D6A"
Color Bad     = "#D8404A"
Color Neutral = "#888888"
```

## Related

- [[Parameter-File-No-Hard-Coding]]
- [[Power-BI-JSON-Theme]]
