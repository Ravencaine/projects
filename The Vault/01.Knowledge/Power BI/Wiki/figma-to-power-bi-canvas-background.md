---
created: 2026-08-02
updated: 2026-08-05
source: Figma Meets Power BI Revolutionizing Report Design.md
note_type: workflow
tags: [powerbi, figma, design, svg, visualization, background]
---

# Figma to Power BI Canvas Background

Export a Figma design as SVG and import it as the report canvas background in Power BI, then layer native visuals on top to create polished, custom-styled report pages.

## Prerequisites

- Figma account (free tier is sufficient)
- Power BI Desktop
- A Figma design file with a frame sized to 1280 × 720 (the standard Power BI canvas size — Figma's "TV" preset)

## Steps

### 1. Build the design in Figma

Design the visual layout — KPI card backgrounds, buttons, logos, text placeholders — using Figma's shape, text, and image tools. Rename and group all elements in the Layers panel for clarity.

Key Figma tools used:
- **Frame** tool — set to `1280 × 720` (TV size) as the canvas
- **Rounded rectangle:** for KPI card backgrounds (Corner Radius: 16, gradient fill, drop shadow)
- **Rectangle** with corner radius — for oval buttons
- **Text tool** (T) — for labels and headers; Inter font used by default, adjustable in Properties panel
- **Image:** import logo images, resize via Width (W) and Height (H) in Properties panel

### 2. Export as SVG

1. Select the frame in Figma.
2. In the Properties panel, under **Export**, click the `+` icon.
3. Choose **SVG** as the export format.
4. Click **Export**.

### 3. Import into Power BI

1. Open the Power BI report.
2. In the **Format** pane for the report page, find **Canvas background**.
3. Set **Transparency** to 0%.
4. Import the SVG file exported from Figma.

The Figma design now sits behind all native Power BI visuals on the page.

### 4. Layer Power BI visuals

Add KPI cards, charts, slicers, and other native Power BI visuals on top of the Figma background. Position them to align with the design layout (card backgrounds, button areas, etc.).

## Key Rules

- Export format must be **SVG:** not PNG or JPG — for crisp scaling on any display density.
- Set canvas background transparency to **0%** in Power BI; otherwise the SVG may appear washed out.
- Figma canvas size **1280 × 720** matches the Power BI default page size exactly.
- Group and name Figma layers for easier alignment in Power BI.

## Variations

- **Iterative design with clients:** Share Figma prototype links for client feedback before building in Power BI.
- **Reduce Power BI shape count:** Move background shapes (card backgrounds, dividers) into the Figma SVG so they don't need to be rebuilt with Power BI shape objects — improves report performance.
- **Export PNG/JPG instead:** For reports that don't need scaling, PNG at 2× resolution is a simpler alternative.

## Related

- [[figma-power-bi-design-stack]]
