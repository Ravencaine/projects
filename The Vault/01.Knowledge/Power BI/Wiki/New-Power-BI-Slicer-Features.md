---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [new-slicer, slicer-options, image-slicer, callout-label, button-formatting]
related: [Market-Watch-Dashboard, SELECTEDVALUE]
---

# New Power BI Slicer Features (November 2023+)

The new Power BI slicer (released November 2023) adds substantial formatting capabilities beyond the legacy slicer.

## Feature Summary

| Feature | Description |
|---------|-------------|
| **Callout values** | Display formatted values prominently above the list |
| **Image support** | Show images alongside each slicer item |
| **Label descriptions** | Add a second line of text below each value |
| **Button state formatting** | Format Default, Hover, Pressed, Selected states independently |
| **Layout control** | Specify rows × columns (grid layout) |
| **Shape options** | Apply background, border, font formatting per state |
| **Background images** | Tile images as background (with opacity) |

## Setup: Image Slicer (Bittar Pattern)

1. Create a dimension table with an image URL column.
2. Set the URL column's **Data category → Image URL** in the model view.
3. Create a new **Slicer** visual.
4. Add the key column to the slicer's **Field** well.
5. Add the image URL column to the slicer's **Image** field well.
6. Format:
   - `Image fit` → `Normal`
   - `Position` → `Left`
   - `Image area size` → `10%`
   - `Space between image and callout` → `10px`

## Setup: Description Labels

```dax
Description =
    SELECTEDVALUE('Key'[Full Name]) & " - " & SELECTEDVALUE('Key'[Description])
```

Add `Description` to the slicer's **Callout values → Label** field well.

## Button State Formatting

Format the `Selected` state to highlight the chosen item:
- `Fill` → your accent color
- `Font color` → white
- `Border` → off

Format the `Hover` state:
- `Fill` → slightly lighter shade
- `Border` → 1px accent color

## Notes

- The new slicer is available on the visualizations pane alongside the legacy slicer — select the new one explicitly.
- Image URL columns require the column's **Data category** to be set to `Image URL` in the model view.
- The new slicer renders as a button/list hybrid — each item behaves like a button with four states.
- Bittar's Market Watch dashboard combines the new slicer with Field Parameters to create a fully customized asset selector.

## Related

- [[Market-Watch-Dashboard]] — full workflow using new slicer + field parameters
- [[SELECTEDVALUE]] — build description labels from dimension columns
- [[Field-Parameters]] — combine with the new slicer for multi-dimensional filtering
