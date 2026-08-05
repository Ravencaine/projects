---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: atomic
tags: [Gestalt, visual-perception, design-principles, proximity, similarity, closure]
related: [Visual-Design-Principles, Color-Theory-for-Dashboards]
---

# Gestalt Principles (5 Named Laws)

Five perceptual principles from Gestalt psychology that explain how users visually group and interpret dashboard elements.

## The 5 Principles

### 1 — Figure-Ground

Users perceive elements as either in the foreground (figure) or background (ground). On a dashboard:

- **KPI cards** should be the figure — the dominant visual on a page.
- **Background shapes and grid lines** are the ground — present but not distracting.
- **Avoid** placing important metrics on busy backgrounds.
- **Tip:** Use subtle backgrounds (light grey, #F5F5F5) to push decorative elements back.

### 2 — Similarity

Elements that share visual properties (color, size, shape, font) are perceived as belonging to the same group:

- **Color-code** related metrics (all financial metrics in blue, all operational metrics in green).
- **Use consistent font sizes** for same-level elements (all KPI values = 28pt, all labels = 10pt).
- **Shape** conveys relationship — rounded corners on one group of cards, sharp corners on another.

### 3 — Proximity

Elements close to each other are perceived as a group:

- **Group** related visuals together — a KPI card and its supporting trend chart should be adjacent.
- **Leave whitespace** between visual groups — a 24px gap between pages or sections communicates "these are separate topics."
- **Use consistent spacing** within groups (12px between a title and its visual, 24px between visual groups).

### 4 — Continuity

The eye follows lines, curves, and directional cues:

- **Connector lines** in a process tracker guide the eye through steps.
- **Line charts** draw the eye along a temporal path.
- **Avoid** sudden direction changes within a visual sequence.
- **Use** gridlines and alignment to create implied directional flow.

### 5 — Closure

Users mentally complete incomplete shapes:

- **Use background shapes** (rounded rectangles) to create the illusion of a card without drawing full borders.
- **Icons** (a partial checkmark) imply completion without needing a full visual.
- **Partial data bars** in table cells suggest the full value range without needing a full axis.

## Application to Power BI Dashboards

| Principle | Power BI Implementation |
|-----------|------------------------|
| Figure-Ground | KPI cards as dominant visuals; background shapes subdued |
| Similarity | Consistent color per category; same font size per tier |
| Proximity | Visual grouping; whitespace gaps between sections |
| Continuity | Process trackers with connector lines; aligned grids |
| Closure | Partial backgrounds; icon-based status indicators |

## Notes

- Bittar's "Unlocking the Power of Visual Design" article introduces all five principles specifically for dashboard design.
- These principles are the design foundation — they explain *why* the [[Color-Theory-for-Dashboards]] and [[The-3-30-300-Rule]] guidelines work.
- [[Visual-Design-Principles]] extends these with hierarchy, balance, and scale.

## Related

- [[Visual-Design-Principles]] — broader visual design framework
- [[Color-Theory-for-Dashboards]] — applying color with perceptual grounding
- [[The-3-30-300-Rule]] — time-budget framework informed by Gestalt perception
