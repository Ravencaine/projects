---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI Multi-Row Card Visuals
note_type: atomic
tags: [conditional-formatting, multi-row-card, power-bi, dax, visual-design]
---

# Conditional Formatting in Multi-Row Card Visuals

Power BI's Multi-Row Card visual does not expose conditional formatting in its Format pane — unlike tables and matrices, there is no right-click → Conditional Formatting option. The workaround is to bake conditional formatting into the measure itself using DAX + UNICHAR, rendering icons (circles, arrows) directly as text within the card values.

<!-- one-line description: Workaround DAX measure using UNICHAR to add conditional formatting icons to Multi-Row Card visuals, which natively lack conditional formatting support -->

## Definition

The Multi-Row Card visual shows field values in a compact card layout, but its Format pane omits the conditional formatting section available in tables and matrices. The standard UI workaround is to create a separate DAX measure that returns an icon character (via UNICHAR) based on the conditional logic, then display that measure alongside or instead of the raw number.

## Key Points

- Multi-Row Card has no built-in conditional formatting — the Format pane simply lacks the option
- The workaround creates a DAX measure that outputs an icon + optional formatted number
- UNICHAR() converts Unicode code points to characters: UNICHAR(11044) = 🟢 green circle, UNICHAR(128308) = 🔴 red circle, UNICHAR(9650) = ▲ up arrow, UNICHAR(9660) = ▼ down arrow
- ISBLANK() guard prevents misleading icons for missing data
- FORMAT() formats numbers as percentages, currency, etc. before concatenation
- The measure can be used in any visual that supports text/card display — not just Multi-Row Cards
- Contrast with [[conditional-formatting-via-dax]] — that note covers the built-in "field value" conditional formatting approach (using a measure to drive color via the Format pane); this note covers the icon-via-measure workaround for visuals that lack conditional formatting UI
- Contrast with [[UNICHAR]] — that note covers UNICHAR as a general DAX function with all code points; this note focuses on the Multi-Row Card application and the specific icon pattern for profit/variance indicators

## Related

- [[conditional-formatting-via-dax]] — general pattern for DAX-driven conditional formatting in Power BI
- [[Add-Conditional-Formatting-to-Multi-Row-Card]] — step-by-step workflow
- [[UNICHAR-Icon-Codes-Reference]] — quick reference for icon codes used in this pattern
- [[UNICHAR]] — the DAX function underpinning this technique
- [[conditional-formatting-via-dax]] — dynamic color via measures (Format pane field-value approach)
