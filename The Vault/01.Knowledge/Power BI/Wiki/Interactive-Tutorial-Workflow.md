---
created: 2026-08-06
updated: 2026-08-06
source: Building Interactive Tutorials That Stick in Power BI (Isabelle Bittar, 2024-02-12)
note_type: workflow
tags: [powerbi, bookmarks, selection, buttons, ux, onboarding, tutorial]
---

# Building Interactive Tutorials in Power BI

A step-by-step guide for creating a guided, multi-step interactive tutorial overlaid on a Power BI report page using the Selection and Bookmarks panels — no DAX required.

## Prerequisites

- A completed report page you want to add the tutorial to
- View → Selection pane (renaming and grouping)
- View → Bookmarks pane
- Report can contain shapes, text boxes, images, and buttons (all available natively)

## Steps

### 1. Plan the tutorial structure

Map out all the features you want to highlight. Keep each step focused on one interaction. Recommended: 4–8 steps maximum — tutorial length is inversely correlated with completion rate.

### 2. Create the first info bubble

For each bubble, add these elements on top of your existing report:

1. **Persona image:** use a human face or avatar image; increases engagement
2. **Instruction text box:** short, verb-led ("Click the filter button to narrow results")
3. **Highlight shape:** a rectangle or oval placed over the UI element being described
4. **"Next" button:** advances to the next bubble
5. **"End tutorial" button:** closes the tutorial and returns to normal use

Rename every element in the Selection pane. Group all elements together (multi-select → right-click → Group). Name the group (e.g., `Info Filter`).

### 3. Create subsequent info bubbles

Copy the first group (Ctrl+C / Ctrl+V). Hide the original group, then modify the copy (update text, image, highlight shape). Repeat for every step. Rename and regroup under a parent heading (e.g., `Tutorial`) in the Selection pane.

### 4. Open the Bookmarks pane (View → Bookmarks)

Create one bookmark per tutorial step plus one close bookmark:

**Close bookmark:** Select the `Tutorial` group → hide it → create bookmark → name it `Tutorial Close` → right-click → deselect **Data** → select **Selected visuals**.

**Step bookmarks:** For each info bubble, make its group visible, create a bookmark (e.g., `Tutorial Filter`), deselect **Data**, select **Selected visuals**. Group all bookmarks under `Tutorials` in the Bookmarks pane.

> **Key setting:** Deselecting **Data** in bookmark options is critical — it prevents the bookmark from resetting slicer or date filter state when the user navigates through the tutorial. See [[bookmarks-in-power-bi-complete-guide]].

### 5. Assign bookmarks to buttons

**Close button:** Select "End tutorial" button → Format pane → Action → Type: Bookmark → select `Tutorial Close`.

**Next button:** Select "Next" button → Format pane → Action → Type: Bookmark → select the bookmark for the *next* bubble (e.g., `Tutorial Date`).

Apply to all bubble "Next" buttons in sequence.

### 6. Add transparent click targets (optional but recommended)

Place a transparent button over the text and image area of each bubble so the whole bubble is clickable, not just the visible "Next" button.

## Variations

- **Per-page tutorial** vs. persistent overlay: place tutorial bubbles on every page for page-specific guidance
- **Bookmark Navigator** approach: replace individual buttons with a Bookmark Navigator visual for cleaner navigation UI
- **Exit state bookmark:** create a final bookmark that hides all bubbles and returns to clean page state

## Common Errors

- Bookmark captures wrong state because Selection pane was not open when bookmark was created — always open Selection pane before creating bookmarks
- Slicer state resets when navigating bubbles — fix: deselect **Data** in bookmark options
- Bubble shows on top of visuals you want visible — use Selection pane z-order or place bubbles on a dedicated layer/page

## Related

- [[bookmarks-in-power-bi-complete-guide]] — full bookmark reference
- [[bookmark-navigator-visual-switching]] — uses the same deselect-Data technique
- [[Info-Bubble-Pattern]] — the reusable UI pattern for grouping elements
- [[source-interactive-tutorials-that-stick]] — source article
