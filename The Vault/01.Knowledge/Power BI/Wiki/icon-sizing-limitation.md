---
created: 2026-08-09
updated: 2026-08-09
source: "Elevate Your Power BI Tables with Custom Icons 🥳 1.md"
note_type: atomic
tags: [power-bi, custom-icons, svg, sizing, limitation, atomic]
---

# Icon Sizing Limitation Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-custom-icons-power-bi-tables]]

Icons embedded in the JSON theme and applied via cell element formatting always render at a small fixed size. Avoid designing icons that require detail or embedded text.

## The constraint

Theme icons render at a relatively small size — there is no control over scaling them up for detail. This makes them unsuitable for:

- Detailed icons with fine lines or small elements
- Icons with embedded text (e.g., pills with labels like "NEW", "SALE", "HOT")
- Complex multi-color illustrations
- Icons that need to convey meaning through small text

## Design guideline

> Keep theme icons simple: single-color glyphs, geometric shapes, status indicators. Do not attempt to replicate detailed badges.

## Alternatives for complex icons

| Icon type | Approach |
|-----------|----------|
| Detailed / text-based | SVG column or measure |
| Scalable detailed | Image data column |
| Simple status | Theme icon ✓ |

## Practical rule

If the icon needs to be readable at a glance at small size, theme icons work well. If it needs text, fine detail, or branding, use SVG/image columns instead.
