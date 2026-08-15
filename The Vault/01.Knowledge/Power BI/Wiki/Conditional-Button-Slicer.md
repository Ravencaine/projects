---
created: 2026-08-06
updated: 2026-08-06
source: Button Slicer Level Up Your Power BI Reports!
note_type: pattern
tags: [button-slicer, conditional-formatting, power-bi, dynamic-styling]
---

# Conditional Button Slicer

A Button Slicer whose appearance changes dynamically based on the underlying data values — using Power BI conditional formatting rules.

## Purpose

Use conditional formatting on a Button Slicer to create visual hierarchies, draw attention to top performers, and dim underperformers. The button's color, image saturation, or border changes automatically based on thresholds in the data.

## Components

- **Button Slicer:** the New Card visual in slicer mode
- **Underlying measure or column:** the data field driving the conditional rules
- **Conditional formatting rules:** threshold-based or value-based rules applied to Fill, Font color, Border, or Image saturation

## Structure

No code — this is a UI-driven pattern:

1. Configure the Button Slicer with the desired field.
2. Open the conditional formatting dialog (paint roller → Colors section).
3. Set rules based on a measure (e.g., Sales Amount):
   - `value > 50000` → Gold fill (#FFD700)
   - `value <= 50000` → Dim gray fill (#CCCCCC)
4. Apply separate rules for image saturation on hover.

## Example

A regional sales Button Slicer where each country button:
- Turns **gold** when that region's sales exceed the target threshold
- Turns **faded** when sales are below the threshold
- Has **reduced image saturation on hover** for a subtle feedback effect

## Variations

| Variation | Trigger | Effect |
|-----------|---------|--------|
| Threshold highlight | Value > X | Button fill changes to gold/green |
| Underperformer dim | Value < X | Button fades to gray |
| Hover saturation | Mouse hover | Image saturation decreases |
| Data bar overlay | All states | Mini bar chart inside each button |

## Related

- [[Button-Slicer]] — concept overview
- [[Create-a-Button-Slicer]] — setup steps
- [[New-Power-BI-Slicer-Features]] — button state formatting details
