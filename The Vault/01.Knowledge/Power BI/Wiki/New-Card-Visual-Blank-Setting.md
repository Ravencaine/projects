---
created: 2026-08-05
updated: 2026-08-05
source: Blank Values in Power BI Reports (Boniface Muchendu)
note_type: atomic
tags: [power-bi, card-visual, blank, no-dax, built-in]
---

# New Card Visual: Show Blank Value As

The Power BI New Card Visual has a built-in "Show blank value as" property that replaces blank values with custom text — no DAX required.

## How to Enable

1. Add a **Card** (New Card) visual to the report
2. Drop the measure into the visual
3. In the **Format** pane: **Visual → Blank state → Show blank value as**
4. Enter the desired display value: `N/A`, `null`, `—`, `0`, or any text

## What It Looks Like

- Default: blank space in the card when no data
- With setting: displays the entered text instead of blank

## When to Use

- Card or multi-row card visuals showing single measures
- Quickest solution when DAX is not desired
- Works for all measure types without modifying the measure itself

## Limitations

- Only available on the **Card (New Card)** visual — not on the classic card or other visual types
- Applies to the visual level, not the model — other visuals on the same measure still show blanks
- The setting is per-visual, not per-measure

## Related

- [[Plus-Zero-Blanks-Atomic]]
- [[IF-Implicit-Blank-Check-Pattern]]
- [[Choosing-Blank-Value-Strategy]]
