---
created: 2026-08-13
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: workflow
tags: [powerpoint, image-mask, overlay, merge-shapes, png, static-layout]
---

# Circular Overlay Mask (PowerPoint + Power BI)

Layer a circular "hole" PNG over a square image in Power BI to make it appear circular — useful for fixed-position images (e.g. card headers) where the original image file must stay as-is.

## When to Use

- Images always render in the same fixed position on a page (e.g. a profile card header).
- You can't or don't want to re-encode the original image.
- You can place a second visual precisely on top of the first.

## Limitations

- **Does not work inside tables/matrices** — when the user scrolls, the overlay visual stays put while the row image moves. Use only for static placements.

## Prerequisites

- PowerPoint (any modern version — 2016+)
- Power BI Desktop

## Steps

### Part A — Build the Mask PNG in PowerPoint

#### 1 — Set Up the Slide

Create a new slide. Resize the slide to match the aspect ratio of your image — e.g. **Design → Slide Size → Custom Slide Size → set to your image's dimensions**.

#### 2 — Draw the Background Rectangle

**Insert → Shapes → Rectangle.** Resize it to fill the entire slide.

#### 3 — Draw the Circle "Hole"

**Insert → Shapes → Oval.** Hold **Shift** while drawing to make a perfect circle. Resize and position it exactly where you want the image to appear.

#### 4 — Punch the Hole

Select both the rectangle and the circle (click the rectangle first, then shift-click the circle).

**Shape Format → Merge Shapes → Combine.** The rectangle now has a transparent circular hole.

#### 5 — Save the Mask

Set the rectangle's **Fill** to match the report background colour (e.g. white) and **Outline** to **No Outline**.

Right-click → **Save as Picture…** → save as PNG with transparency.

### Part B — Layer It in Power BI

1. **Insert → Image** → add the original (square) image.
2. **Insert → Image** → add the mask PNG. Resize and position it precisely over the original.
3. Align both visuals to the page grid so the mask sits perfectly on top of the image.

The mask's transparent area reveals the square image; the white (background-coloured) area covers everything outside the circle — producing a circular appearance.

## Variations

- **Background-coloured mask** — instead of white, paint the mask the exact background colour of your report page. Layer order: mask on top.
- **Frame / ring effect** — build a thinner ring (use the ring shape rather than the punched hole) to add a status border around a circular image.

## Gotchas

- **Scroll failure inside tables/matrices** — the overlay visual is anchored to the canvas, but row images move with scroll. Result: misalignment as soon as the user scrolls. Don't use this in any visual where the image moves.
- **Pixel alignment** — the overlay mask must align exactly with the image. Power BI's snap-to-grid helps; small DPI differences can cause sub-pixel gaps.
- **Theme changes** — if the report background colour changes, the mask colour must be updated and re-saved.

## Related

- [[pre-circularize-images-in-powerpoint]] — when the original image can be re-encoded
- [[batch-circularize-images-with-python]] — for large sets of original files
- [[circular-image-approaches-decision-guide]] — when to use which approach
