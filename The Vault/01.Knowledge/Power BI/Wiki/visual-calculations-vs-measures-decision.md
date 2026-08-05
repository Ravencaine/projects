---
created: 2026-08-01
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md"
note_type: atomic
tags: [power-bi, visual-calculations, measures, decision-framework, governance]
---

# Visual Calculations vs Measures — Decision Framework

## Five-Question Decision Tree

```
Should this be a visual calculation or a measure?

1. Does it define a business term (margin, growth, attainment, share)?
   → MEASURE. Always. No exceptions for convenience.

2. Will it be needed on more than one visual?
   → MEASURE. (Visual calcs can't be reused — N copies drift.)

3. Will users export this number, pin it, or consume via
   publish-to-web / custom visuals?
   → MEASURE. Visual calcs don't travel.

4. Does it need data not displayed on the visual, relationships,
   or dynamic format strings?
   → MEASURE. The visual matrix can't see any of that.

5. Is it presentation arithmetic over what's already displayed —
   running sum, moving average, % of parent, vs-previous,
   rank-as-shown, custom totals?
   → VISUAL CALCULATION. Right tool, and likely faster too.
```

The first four questions all route to measures. That's not anti-feature bias — it's the feature's own architecture defining its scope.

## When Visual Calculations Genuinely Win

| Scenario | Why |
|----------|-----|
| Logic about the visual, not the business | Running totals, percent-of-parent, rank within visual rows |
| Performance on heavy visuals | Arithmetic on pre-aggregated grid vs. fact table re-scan |
| Analyst velocity without model write access | Semantic model locked → visual calc works without ticket |

## When to Use Measures

| Scenario | Action |
|----------|--------|
| Business definition | Measure — it defines what "growth %" *means* |
| Multi-visual reuse | Measure — visual calcs can't be referenced |
| Export/dashboard/publish-to-web | Measure — visual calcs don't travel |
| Needs model data/relationships | Measure — visual matrix is isolated |
| Dynamic format strings | Measure — not available in visual calcs |

## The Governing Rule

> **Visual calculations for presentation arithmetic; measures for business definitions.**

If the calculation defines what a business term *means*, it goes in the model — however convenient the alternative.
