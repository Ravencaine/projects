---
created: 2026-07-29
updated: 2026-08-02
source: "Crafting Data Narratives: The Art of Power BI Reporting"
note_type: workflow
tags: [data-narrative, report-design, ux, perspective, lo-fi, hi-fi]
related: [Visual-Design-Principles, The-3-30-300-Rule]
source_url:
---

# Data Narratives Report Design (7-Step Process)

A structured UX/design process for building Power BI reports that tell a story rather than just display data.

## The 7 Steps

### 1 — Identify the Perspective

Who is the audience? What decisions do they need to make?

- **C-suite:** Overview metrics, trends, alerts
- **Operations:** Process status, bottlenecks, exceptions
- **Sales:** Pipeline, performance vs target, regional breakdown
- **HR:** Headcount, turnover, hiring pipeline

### 2 — Define the Question Hierarchy

| Tier | Question Type | Time |
|------|-------------|------|
| 3 seconds | "How are we doing?" | Overview |
| 30 seconds | "What's different / what's the trend?" | Explore |
| 300 seconds | "Why is this happening?" | Analyse |

This maps directly to the [[The-3-30-300-Rule]].

### 3 — Build a Lo-Fi Wireframe

Sketch the report layout on paper before touching Power BI:
- Which visuals go on page 1 (overview), page 2 (explore), page 3 (analyse)?
- What is the dominant visual on each page?
- Where are filters/slicers placed?

### 4 — Identify Data Requirements

- Which tables are needed?
- Do relationships exist, or are they missing?
- Are calculated columns or measures needed?

### 5 — Develop the High-Fidelity Prototype

Build the report in Power BI, following the wireframe:
- Start with the dominant visual.
- Add supporting visuals.
- Apply consistent formatting (colors, fonts, spacing).

### 6 — Test with Real Users

- Watch a real user interact with the report.
- Note where they hesitate or get confused.
- Validate that they can answer the 3/30/300-second questions.

### 7 — Iterate Post-Publication

- Set up a feedback loop (email, Teams, comments).
- Track which filters are used most.
- Publish usage metrics from Power BI Service.

## Notes

- Bittar's process draws from the **Double Diamond design framework**: divergent exploration followed by convergent solution-building.
- The [[FORMAT]] (overview first, zoom/filter, details-on-demand) applies at the visual level within each page.
- [[The-3-30-300-Rule]] operationalises the time-budget concept for dashboard design.

## Structural Integrity as a Design Foundation

Bittar's 7-step process can be preceded by a **Step 0 — Structural Integrity Check** before wireframing:

Althea Van Zyl identifies three structural practices that apply before any visual design begins:

1. **Lucid introduction:** every report page should have a clear opening: what question does this page answer?
2. **Logical content sequencing:** sections follow a reading order that matches the user's decision process (overview → trend → exception)
3. **Uniform formatting:** consistent fonts, colors, and spacing across all pages signals professionalism and reduces cognitive load

> Source: [[Source-Crafting-Compelling-Impactful-Power-BI-Reports]] — Althea Van Zyl, 2024-07-09

## Related

- [[The-3-30-300-Rule]] — time-budget framework
- [[Visual-Design-Principles]] — Gestalt principles and visual hierarchy
- [[Visual-Information-Seeking-Mantira]] — visual design framework
