---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [accessibility, color-contrast, alt-text, tooltips, colorblind, inclusive]
related: [Color-Theory-for-Dashboards, Bubble-Chart-Enhancement]
---

# Accessibility for Charts

Guidelines and techniques for making Power BI charts accessible to users with visual impairments, color blindness, or cognitive differences.

## Color Contrast

### WCAG Contrast Ratios

| Level | Minimum Ratio | Use |
|-------|--------------|-----|
| AAA | 7:1 | Body text, primary labels |
| AA | 4.5:1 | Secondary text, chart labels |
| AA Large | 3:1 | Large text (18pt+), UI components |
| Non-text | 3:1 | Chart elements, icons |

### Testing Tools

- **WebAIM Contrast Checker**: check foreground/background pairs.
- **Coblis Color Blindness Simulator**: upload screenshots to simulate deuteranopia, protanopia, tritanopia.
- **Colour Contrast Analyser**: desktop app for live checking.

## Colorblind-Safe Palettes

Avoid red/green as the only differentiator. Instead:

| Colorblind-Safe Pair | HEX |
|---------------------|-----|
| Blue + Orange | `#0077BB`, `#EE7733` |
| Blue + Yellow | `#0077BB`, `#EECC66` |
| Purple + Yellow | `#AA3377`, `#BBBBBB` |

## Alt Text (Report Descriptions)

In Power BI Desktop:
- Right-click the visual → **Edit alt text**.
- Write a concise description: *"Clustered bar chart showing monthly sales by product category. Healthcare leads at $2.3M."*
- Report-level: **File → Settings → Report settings → Alt text**.

## Screen Reader Support

- **Use table visuals** alongside charts for screen reader users — the table is inherently accessible.
- **Tooltips** must contain all data shown in the visual — never hide information that is only available visually.
- **Data labels** on charts provide a redundant channel.
- **Sort order** matters — consistent sorting helps screen reader navigation.

## Keyboard Navigation

- Ensure users can tab through all interactive elements (slicers, buttons, bookmarks).
- Test with keyboard-only navigation (**Tab**, **Enter**, **Arrow keys**).
- Visual focus indicators should meet 3:1 contrast ratio.

## Cognitive Accessibility

- **Consistent layout**: users learn where to find information.
- **Plain language** in labels and titles.
- **Progressive disclosure**: show overview first, details on demand (see [[The-3-30-300-Rule]]).

## Notes

- Bittar's bubble chart article includes an explicit accessibility section covering all four areas above.
- Accessibility is not optional in government, healthcare, and education sectors — check relevant standards (WCAG 2.1, Section 508).
- [[Color-Theory-for-Dashboards]] provides the full palette guidance that includes accessibility-safe choices.

## Related

- [[Color-Theory-for-Dashboards]] — accessible palette guidance
- [[Bubble-Chart-Enhancement]] — accessibility checklist embedded in workflow
- [[The-3-30-300-Rule]] — progressive disclosure for cognitive accessibility
