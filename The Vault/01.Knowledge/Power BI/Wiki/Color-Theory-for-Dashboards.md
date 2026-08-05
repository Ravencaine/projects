---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [color-theory, dashboard, color-scheme, HSL, RGB, HEX, harmony]
related: [Color-Coding-4-Techniques, Gestalt-Principles]
---

# Color Theory for Dashboards

A practical guide to choosing and applying color in Power BI reports — covering color models, schemes, harmony rules, and common dashboard-specific patterns.

## Color Models

| Model | Format | Use in Power BI |
|-------|--------|----------------|
| HEX | `#RRGGBB` | DAX hex strings for conditional formatting |
| RGB | `rgb(r, g, b)` | CSS-compatible, used in HTML Content visual |
| HSL | `hsl(h, s%, l%)` | Intuitive hue/saturation/lightness control |
| Named | `Green`, `Red` | Power BI default theme colors |

## Color Schemes

| Scheme | Use |
|--------|-----|
| **Analogous** | Adjacent hues (blue + teal). Calm, professional. |
| **Complementary** | Opposite hues (blue + orange). High contrast, alerts. |
| **Triadic** | Three equidistant hues. Vibrant, playful. |
| **Monochromatic** | Single hue with lightness variations. Cohesive. |

## Dashboard-Specific Color Usage

| Color | Meaning | HEX |
|-------|---------|-----|
| Green | On track / positive / growth | `#76E3B4` |
| Red | Alert / negative / below target | `#EE6064` |
| Yellow/Amber | Warning / approaching threshold | `#F5A623` |
| Blue | Neutral / informational | `#4059ad` |
| Grey | Disabled / inactive / not started | `#B5C2CA` |
| White | Background / transparent | `#FFFFFF` |

## HSL Color Construction

For dashboard accents, build colors using HSL:
```dax
// Shift the hue by 15 degrees for analogous colors
_const Accent Blue   = "#4059ad"  // hsl(230, 50%, 45%)
_const Accent Teal   = "#40a49a"  // hsl(173, 47%, 45%)
_const Accent Purple = "#6b40a4"  // hsl(270, 48%, 45%)
```

## Principles for Dashboard Color

1. **Limit to 5 colors** in the active palette — more creates cognitive overload.
2. **Use color to encode meaning**, not decoration — each color must represent a distinct state.
3. **Maintain WCAG contrast ratios** (≥4.5:1 for text, ≥3:1 for large elements).
4. **Test with colorblind simulators** (deuteranopia, protanopia, tritanopia).
5. **Don't rely on color alone**: use icons, labels, and tooltips as redundant channels.

## Notes

- Bittar's "The Chromatic Canvas" article provides the full design rationale, including the psychology of warm vs. cool colors for different industries.
- The [[The-3-30-300-Rule]] uses color (traffic light system) as the primary 3-second overview signal.
- [[Accessibility-for-Charts]] extends these guidelines for inclusive design.

## Related

- [[Color-Coding-4-Techniques]] — applying color theory in DAX
- [[Gestalt-Principles]] — perceptual principles that explain why color groupings work
- [[Accessibility-for-Charts]] — contrast ratios and colorblind safety
