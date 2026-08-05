---
created: 2026-08-01
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md"
note_type: atomic
tags: [power-bi, visual-calculations, measure-migration, demotion, model-cleanup]
---

# Visual Calculations — Measure Demotion Migration

## The Opportunity

GA is a one-time chance to repay model debt. Every mature Power BI estate has a sediment layer of "visual-shaped measures" — measures that exist because visual calculations didn't exist:

- `Sales RT (Quarterly View)`
- `Pct of Parent - Region Matrix`
- `Rank for Top10 Visual`

These are candidates for *demotion* — moving logic from the model down to the visual that was always its only consumer.

**Benefits of demotion:**
- Shorter, cleaner measure list
- Easier for analysts to navigate
- Better AI/Copilot grounding (fewer ambiguous running-total variants)
- Calculation now lives where it belongs (on the visual)

## Four Rules Before Demoting

### Rule 1: Demote Only What Is Provably Single-Use

Check lineage first. If the measure appears in two reports, it stays a measure.

```
Tool: Semantic Link's list_measures + scan of report definitions
Scope: afternoon audit, not a quarter of work
```

### Rule 2: Mind the Export Dependency

If anyone exports that visual expecting the column → demotion silently deletes it from their workflow. Ask before removing.

### Rule 3: Batch With Intent

- Planned cleanup: 20 measures demoted, documented, announced → builds trust
- Quiet drip demotion: one at a time → generates tickets and fear

### Rule 4: Never Demote a Business Definition

If it defines what a term *means*, it stays in the model — even if only one visual uses it today.

**The governance test still rules:** business definition → measure, regardless of use count.

## Demotion Checklist

```
Before demoting a measure:
□ Check lineage (is it used in more than one report?)
□ Ask visual owner: does anyone export expecting this column?
□ Confirm it qualifies as presentation arithmetic (not a business definition)
□ Plan for batch announcement, not silent removal
□ Verify equivalent visual calculation function exists
```

## Anti-Patterns to Avoid

| Don't do this | Because |
|---------------|---------|
| Demote a shared measure to "clean up" the model | Logic should live where it's needed |
| Demote without checking exports | Silent workflow breakage |
| Drip demote one at a time | Creates confusion and tickets |
| Demote business definitions for convenience | Violates the governance policy |
