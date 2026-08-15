---
created: 2026-08-02
updated: 2026-08-05
source: Figma Meets Power BI Revolutionizing Report Design.md
note_type: source
tags: [powerbi, figma, design, svg, tutorial]
---

# Source: Figma Meets Power BI — Revolutionizing Report Design

> Author: Isabelle Bittar
> Published: 2023-12-31
> URL: https://medium.com/microsoft-power-bi/figma-meets-power-bi-revolutionizing-report-design-420cce760aa7

## Introduction

Figma accelerates Power BI report design by providing a full vector design environment for creating report chrome (backgrounds, card shapes, buttons, layout). The workflow: design in Figma → export SVG → import as Power BI canvas background → layer native Power BI visuals on top.

Benefits:
- Sleek visuals not achievable in Power BI alone
- Reduced shape count in the published report (static background elements live in the SVG)
- Collaborative review via Figma shareable links
- Access to free community dashboard templates

## Figma Overview

Figma is a cloud-based design tool with:
- Toolbar, Layers Panel, Canvas, Properties Panel
- Vector shape tools, text, images, effects (gradients, drop shadows)
- Free tier with access to most important features
- Vibrant community with free dashboard templates

## Design Workflow

### Step 1: Low-Fidelity Wireframe

Start on paper or directly in Figma. Focus on information layout, element types, and overall composition. Share Figma links for client feedback.

### Step 2: Figma Canvas Setup

- Create a new Design File → Drafts.
- Add a **Frame** tool. For Power BI, set size to **1280 × 720** (use Figma's TV preset).
- Rename the frame (e.g., "Power BI Frame").

### Step 3: Sketching in Figma

Build the design using:
- **Rounded rectangles:** KPI card backgrounds. Format: Corner Radius 16, gradient fill, drop shadow (via Effects → +).
- **Rectangles with corner radius:** oval/circular buttons.
- **Text tool (T):** labels, headers. Inter font by default, adjustable weight and size.
- **Images:** import logos, resize via Width (W) and Height (H) in the Properties panel.

Group and rename elements in the Layers Panel before exporting.

### Step 4: Export and Import into Power BI

**To export:** Select the frame → Properties panel → Export → + → SVG → Export.

**To import in Power BI:** Page format pane → Canvas background → Set transparency to **0%** → Import the SVG file.

**To layer visuals:** Add KPI cards, charts, slicers on top of the background. Position to align with the Figma design.

## Figma Design Components Reference

| Component | Figma Tool | Key Settings |
|-----------|-----------|--------------|
| Canvas frame | Frame tool | 1280 × 720 (TV preset) |
| KPI card background | Rounded rectangle | Corner Radius: 16, gradient fill, drop shadow |
| Oval button | Rectangle | Corner Radius: max |
| Text label | Text tool (T) | Inter font, adjustable weight/size |
| Logo | Image import | Resize via W and H in Properties |

## PBIX and Figma Files

Download: https://drive.google.com/drive/folders/1jMFl_b8qLsUByBPEhOgj48qZ-jSveZcb
