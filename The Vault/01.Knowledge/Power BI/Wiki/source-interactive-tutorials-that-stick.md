---
created: 2026-08-06
updated: 2026-08-06
source: Building Interactive Tutorials That Stick in Power BI
source_url: https://medium.com/microsoft-power-bi/power-bi-unleashed-building-interactive-tutorials-that-stick-95f97da8eef0
author:
  - Isabelle Bittar
published: 2024-02-12
note_type: reference
tags: [powerbi, bookmarks, selection, buttons, ux, onboarding, tutorial, navigation]
---

# Source — Building Interactive Tutorials That Stick in Power BI

*Isabelle Bittar · Medium · 2024-02-12 · [[Author-Isabelle-Bittar]]*

Describes how to build a guided, step-by-step interactive tutorial inside a Power BI report using the Selection and Bookmarks panels — no DAX required. Used the FP20 Analytics Challenge (Data-Driven Education Management) as the working example.

## Key Points

- Users miss drill-downs, slicers, and tooltips unless actively shown
- Static info windows are ignored; interactive step-by-step bubbles are more engaging
- Requires only: Selection panel + Bookmarks panel + transparent buttons
- Each "info bubble" is a group of shapes, text boxes, and images; grouped in the Selection panel
- One bookmark per bubble state (shows/hides the group); assigned to buttons on the bubble itself
- Deselect **Data** in bookmark options so slicer/filter state is preserved during navigation
- Select **Selected visuals** (not All visuals) so only the bubble shapes are captured

## UX Best Practices

- Use persona images to encourage engagement
- Use verbs ("click", "hover", "apply") to guide action
- Use simple language — non-BI users say "filter", not "slicer"
- Keep it short — inverse relationship between tutorial length and completion rate

## Anatomy of an Info Bubble

Each bubble contains: persona image, instruction text box, contextual highlight shape, "Next" button, "End tutorial" button — all grouped in the Selection panel.

## PBIX

[Download from Google Drive](https://drive.google.com/file/d/1mSXZTR7BnRPK0Di_WWDNQ_1keeUbeh_g/view?usp=sharing)

## Notes Extracted

- [[Interactive-Tutorial-Workflow]] — step-by-step workflow for building the tutorial
- [[Info-Bubble-Pattern]] — the reusable UI pattern for grouped elements + bookmark navigation

## Related

- [[bookmarks-in-power-bi-complete-guide]]
- [[bookmark-navigator-visual-switching]]
- [[custom-slicer-filter-pane-bookmarks]]
- [[Author-Isabelle-Bittar]]
