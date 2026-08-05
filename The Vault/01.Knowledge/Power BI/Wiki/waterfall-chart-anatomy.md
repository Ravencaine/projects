---
created: 2026-08-02
updated: 2026-08-05
source: Why a Waterfall Chart is a Diagnostic Tool, Not Just a Dashboard Decoration
note_type: pattern
tags: [powerbi, pattern, data-visualization, waterfall-chart, anatomy, labeling]
---

# Waterfall Anatomy: Anchors, Floating Bricks, Faint Connectors, Subtotals, Labeling Convention

Waterfall = starting baseline + steps up/down + ending result. Makes the mathematical journey from point A to B visible.

**Anatomy:**

- **Anchors** (first and last bars) — sit firmly on the baseline. Represent absolute reality at fixed points in time. If the ending total is floating, the mathematical model is broken.
- **Floating bricks** (steps) — each block starts exactly where the previous one left off. These are the changes.
- **Connectors:** thin, neutral-colored lines linking corners of adjacent steps. Keep faint so they don't become visual noise. Guide the eye through the running total.
- **Subtotals** (optional checkpoints, e.g., Gross Profit) — full bars grounded to the baseline. Visually distinct from floating steps. Give the reader a visual rest.

**Labeling rule:** Label deltas with plus/minus signs. Label totals with absolute values. Mixing these creates instant confusion.

**Design:** Plus/minus on deltas, absolute values on totals — never reverse this.
