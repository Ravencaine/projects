---
created: 2026-08-01
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md"
note_type: atomic
tags: [power-bi, visual-calculations, governance, model-debt, copilot]
---

# Visual Calculations Governance

## The Risk: Logic Fragmentation

For two decades BI has migrated logic *toward the center* — out of Excel formulas, out of report-level calculated fields, into governed semantic models where definitions are versioned, certified, and shared.

Visual calculations move logic in the *opposite direction* — and without a policy, chaos follows:

```
Analyst A: "growth %" = visual calc on page 3, visual 2
Analyst B: "growth %" = slightly different visual calc on page 7
Neither in model documentation
Neither visible to lineage tools, BPA, or Copilot
18 months later: two executives see two different "growth %" numbers
Data team cannot find where either is defined
Answer: "page 4, third visual from the left"
```

We have seen this movie. It was called "the Excel formula in the hidden sheet." Industry spent 15 years recovering.

## Why AI/Copilot Is Now Directly Affected

Copilot reasons over the semantic model. Visual calculation logic is *not in the model*. So Copilot cannot see it, ground to it, or reason about it — even when users are looking at the numbers it produced.

## The One-Sentence Policy

> **Visual calculations for presentation arithmetic; measures for business definitions.**

If the calculation defines what a business term *means* — growth, margin, attainment, share — it goes in the model, however inconvenient. If it rearranges what's already on the visual — running totals, % of displayed parent, versus-previous — visual calculations are exactly right.

## What Belongs in the Model (Measures)

Every calculation that:
- Defines a business term
- Needs to appear on more than one visual
- Will be exported, pinned, or used in publish-to-web
- Needs model data, relationships, or dynamic formatting

## What Belongs as a Visual Calculation

- Running totals on a visual
- Percent of displayed parent/grand total
- Versus-previous / versus-next / versus-first / versus-last
- Rank-as-shown within the visual
- Custom totals (sum/avg/min/max/count of displayed rows)
