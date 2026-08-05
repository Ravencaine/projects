---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [data-narrative, report-design, UX, perspective, lo-fi, hi-fi]
related: [Visual-Design-Principles, The-3-30-300-Rule]
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

## Related

- [[The-3-30-300-Rule]] — time-budget framework
- [[Visual-Design-Principles]] — Gestalt principles and visual hierarchy
- [[Visual-Information-Seeking-Mantira]] — visual design framework
