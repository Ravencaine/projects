---
created: 2026-08-06
updated: 2026-08-06
source: Building Interactive Tutorials That Stick in Power BI (Isabelle Bittar, 2024-02-12)
note_type: pattern
tags: [powerbi, bookmarks, selection, buttons, ux, onboarding, pattern]
---

# Info Bubble Pattern in Power BI

A reusable UI pattern for surfacing contextual guidance on a Power BI report page using grouped shapes + text boxes + transparent buttons + bookmarks. Each bubble is a self-contained, clickable instruction card that highlights a specific report feature.

## Purpose

Power BI reports often include features users never discover (drill-downs, slicers, tooltips). Static info panels are ignored. The Info Bubble pattern delivers guidance inline — one bubble per feature, step-by-step — without cluttering the permanent report layout.

## Components

| Component | Role |
|----------|------|
| **Persona image** | Human/avatar image to increase engagement and guide attention |
| **Instruction text box** | Short verb-led text describing the interaction |
| **Highlight shape** | Rectangle/oval overlay on the feature being described |
| **"Next" button** | Transparent button with bookmark action → advances to next bubble |
| **"End tutorial" button** | Closes the tutorial entirely |
| **Group** | All elements grouped in the Selection pane for single-click selection |

## Structure

```
Report Page
└── Info Bubble N (group)
    ├── Highlight shape (overlay on feature)
    ├── Persona image
    ├── Instruction text box
    ├── [Next button] → bookmark: Tutorial Step N+1
    └── [End button] → bookmark: Tutorial Close
```

Each bubble is a sibling group under a parent `Tutorial` group. All bubbles live on the same report page, layered over the existing content.

## Anatomy

The anatomy of a single bubble (from Bittar 2024):

```
┌─────────────────────────────────┐
│  [Persona image]                │
│  "You can hover over the chart  │
│   to see tooltips."             │
│                                 │
│   [Next ▶]   [End tutorial ✕]  │
└─────────────────────────────────┘
```

## Example

From the FP20 Analytics Challenge report:

1. **Bubble 1 (Info Filter):** Highlights where the filter controls are; persona + instruction + Next button
2. **Bubble 2 (Info Date):** Highlights the date picker; persona + instruction + Next button
3. **...6 bubbles total**, then close bookmark returns to clean page

Each bubble is independently visible or hidden via its corresponding bookmark.

## Bookmark Configuration

| Setting | Value | Reason |
|---------|-------|--------|
| **Data** | Unchecked | Preserves current slicer/filter selections during tutorial navigation |
| **Selected visuals** | Selected | Captures only the bubble group visibility — not all page state |
| **Background** | Optional | Leave unchecked during editing for clarity |

## UX Design Rules

- Use persona images (not abstract icons) — human faces increase engagement
- Lead with verbs: "click", "hover", "drag", "apply"
- Avoid BI jargon: say "filter" not "slicer"
- Keep text under 2 sentences per bubble
- Cap total bubbles at 6–8; shorter tutorials have higher completion rates
- Use consistent button placement across all bubbles

## Variations

- **Stacked overlay bubbles:** All bubbles at the same screen position, toggled by bookmarks (cleaner than repositioning each one)
- **Bookmark Navigator instead of individual buttons:** Replaces "Next"/"End" with a native Power BI bookmark navigator visual for a polished look
- **Per-page guide:** Place tutorial bubbles on each page, scoped to that page's features

## Related

- [[Interactive-Tutorial-Workflow]] — full step-by-step implementation
- [[bookmarks-in-power-bi-complete-guide]] — bookmark reference including Data-setting rationale
- [[bookmark-navigator-visual-switching]] — same deselect-Data technique for visual switching
- [[custom-slicer-filter-pane-bookmarks]] — related bookmark + shape pattern for filter panels
- [[source-interactive-tutorials-that-stick]] — source article
