---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into Power BI reporting with the new date picker slicer option (Preview).md"
note_type: workflow
tags: [power-bi, date-picker, slicer, compact, formatting, workflow]
---

# Compact Single-Line Date Picker Slicer — 9-Step Formatting Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Microsoft Fabric / DataZoe — 2026-07-16

## Goal

Format the Date Picker Slicer into a single-line minimal control — calendar button only, no header, no slider, no summaries. Takes up minimal report space while preserving all functionality.

## Steps

1. Select the **date slicer** on the canvas
2. Open the **Format pane**
3. **General** → turn OFF **Header** (also removes the clear all button — see step 8)
4. **Slider** → turn OFF
5. **Text** → expand → turn OFF **Summary**
6. **Date Range** → expand → change **font size to 18**
7. **Button** → expand:
   - Turn OFF **Border**
   - Expand **Icon** → set **Color** to Blue, **Size** to 30
8. **Insert ribbon** → **Buttons** dropdown → **Clear all slicers** → change to icon only
9. Position the **slicer** and **clear button** above the target visual

## Result

Single-line date picker: `18pt date range text | blue calendar icon button`

- Clicking the calendar icon opens the overlay calendar
- Full functionality preserved (relative range, manual range, single date, slider)
- Minimal report real estate
- Add a Clear All slicers button (icon) to compensate for lost header button

## Tip

Combine with a relative range default (e.g., Last 12 Months) so the single-line display shows meaningful dates immediately.

## See Also

- [[Source-Date-Picker-Slicer-Preview]] — source article
- [[Last-Full-Month-Date-Picker-Workflow]] — default relative range configuration
