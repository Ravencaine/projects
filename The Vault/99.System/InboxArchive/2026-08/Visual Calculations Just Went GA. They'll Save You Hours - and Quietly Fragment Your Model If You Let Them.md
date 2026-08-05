---
title: "Visual Calculations Just Went GA. They’ll Save You Hours — and Quietly Fragment Your Model If You Let Them."
source: "https://medium.com/towards-artificial-intelligence/visual-calculations-just-went-ga-9a5940244b34"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-07-02
created: 2026-07-27
description: "With the May 2026 release, visual calculations and custom totals reached general availability in Power BI. Running sums, moving averages, and percent-of-parent without writing a measure — directly on the visual. It’s a genuinely good feature. It’s also the most governance-relevant change to where calculation logic lives since calculated columns. Here’s the decision framework for when a visual calculation is the right tool, and when it’s tomorrow’s audit finding."
Processed: "Unprocessed"
---
## With the May 2026 release, visual calculations and custom totals reached general availability in Power BI. Running sums, moving averages, and percent-of-parent without writing a measure — directly on the visual. It’s a genuinely good feature. It’s also the most governance-relevant change to where calculation logic lives since calculated columns. Here’s the decision framework for when a visual calculation is the right tool, and when it’s tomorrow’s audit finding.

![](99.System/Attachments/1!m_fUEAgZVe8VhYQAcV0TQg.png.webp)

Visual Calculation are GA

There’s a conversation I’ve had in some form at every client for fifteen years. An analyst needs a running total, or a percent-of-parent, or “this month versus previous” — something that’s awkward in classic DAX because it depends on what’s *visible in the visual*. They fight filter context for an hour, write a measure with three CALCULATE wrappers, and it breaks the moment someone adds a slicer.

Visual calculations exist because that conversation happened at every other company too. And as of the May 2026 Power BI release, they’re generally available — along with custom totals, which finally let you control what a total row actually shows.

Used well, they eliminate a whole genre of painful DAX. Used carelessly, they scatter business logic across report visuals where no governance process will ever find it. Both outcomes are now GA. Let’s take them in order.

## What a Visual Calculation Actually Is

![](99.System/Attachments/1!nOigB70snT4W2EQb4e79YQ.png.webp)

DAX on the Visual, Not in the Model

Microsoft’s definition is precise and worth quoting: a visual calculation is “a DAX calculation defined and executed directly on a visual.”

Three properties follow from that, and all three drive the decision framework later:

**It lives on the visual, not in the model.** Add it in edit mode; it’s stored with that visual. Delete the visual, the calculation goes with it.

It can only see what’s on the visual. Visual calculations operate on the *visual matrix* — the data grid behind the visual, with whatever aggregation has already happened. Not the model, not hidden columns, not other tables.

**It works on aggregated data.** Because aggregation already happened, visual calculations often perform *better* than equivalent measures — they’re doing arithmetic over a small grid instead of scanning a fact table.

**The toolkit is purpose-built for visual-shaped problems.** Templates: running sum, moving average, percent of parent, percent of grand total, versus previous/next/first/last. Functions you won’t find in classic DAX: `RUNNINGSUM`, `MOVINGAVERAGE`, `PREVIOUS`, `NEXT`, `FIRST`, `LAST`, `COLLAPSE`, `EXPAND`, `LOOKUP`, `ISATLEVEL` — plus Axis and Reset parameters that control how calculations traverse a hierarchy.

The one-liner that sells the feature:

```c
Running sum = RUNNINGSUM([Sales Amount])
```

That replaces a windowing measure most intermediate developers get wrong on the first try. And custom totals, built on the same engine, end the ancient “the total row is lying” argument — you can now tell a matrix total to show a sum, average, min, max, or count of the displayed rows, regardless of what the measure does.

## When Visual Calculations Genuinely Win

Three scenarios where they’re the *correct* choice, not just the convenient one:

**1\. Logic that’s about the visual, not the business.** A running total down a table. Percent-of-parent in a matrix. Rank within the displayed rows. These were never model semantics — we just had nowhere else to put them. Forcing them into measures polluted models with `Sales Running Total (for the quarterly view)` style debris. Visual calculations put presentation logic where presentation lives.

**2\. Performance on heavy visuals.** Because they compute over already-aggregated data, visual calculations can outperform measures that re-scan the model to reproduce what the visual already knows. For dense matrices doing comparative arithmetic, this is sometimes the difference between responsive and not.

**3\. Analyst velocity without model write access.** In a governed environment where the semantic model is locked, analysts can build their running comparisons without filing a ticket against the modeling team. That’s a real workflow improvement — with a caveat I’ll get to.

## The Limitations That Actually Matter

![](99.System/Attachments/1!esyRPfa5bn2iv-wExscM_A.png.webp)

The limitation that actually bite

The Considerations and Limitations list is long; these are the entries that bite in practice:

**No reuse. None.** A visual calculation cannot be copied to another visual, referenced from another visual, or promoted to the model. Need the same running sum on five visuals? You write it five times. They drift independently. Remember this one — it’s the heart of the governance problem.

**Exports exclude them.** Data exports don’t include visual calculation results. The number a user sees in the matrix is *not in the Excel file they export*. I’ve already heard one “the export doesn’t match the report” support ticket that traced to exactly this. (Underlying-data exports show hidden fields, but the calculation results themselves don’t export.)

**They don’t travel.** No pinning to dashboards. No publish-to-web. Limited availability in embedded scenarios (no IntelliSense there either).

**Visual coverage has gaps.** No slicers (expected), but also no key influencers, decomposition trees, small multiples, Q&A, metrics — and notably, no custom visuals.

**Model features don’t reach them.** No dynamic format strings, no drill-through to records, no “show items with no data,” no personalization. Relationship functions (`USERELATIONSHIP`, `RELATED`) aren't available — you're on the visual matrix, not the model graph.

None of these are bugs. They all follow from the architecture: the calculation lives on a visual, so anything that happens away from that visual — exports, dashboards, other visuals — doesn’t know it exists.

## The Governance Problem Nobody’s Writing About

Here’s the part that earns the second half of my title.

For two decades, the discipline of BI has been a slow migration of logic *toward the center*: out of Excel formulas, out of report-level calculated fields, into governed semantic models where definitions are versioned, certified, and shared. The entire “semantic model as single source of truth” doctrine — the same doctrine Microsoft’s AI story now depends on — rests on logic living in the model.

Visual calculations move logic in the *opposite direction*. Deliberately, and for good reasons. But consider what happens at scale without a policy:

An analyst defines “growth %” as a visual calculation on one report page. A colleague defines it slightly differently on another. Neither appears in the model documentation. Neither is visible to lineage tools, Best Practice Analyzer runs, or your Copilot/AI grounding — *Copilot reasons over the model, and this logic isn’t in the model*. Eighteen months later, two executives are in a meeting with two different “growth %” numbers, and the data team cannot find where either is defined, because the answer is “page 4, third visual from the left.”

We have seen this movie. It was called “the Excel formula in the hidden sheet,” and the industry spent fifteen years recovering from it.

**The policy that prevents it is one sentence:** *visual calculations for presentation arithmetic; measures for business definitions.* If the calculation defines what a business term *means* — growth, margin, attainment, share — it goes in the model, however convenient the alternative. If it rearranges what’s already on the visual — running totals, percent of displayed parent, versus-previous — visual calculations are exactly right.

## The Migration Question Nobody’s Asking Yet

There’s a second-order decision hiding behind GA that I want to surface before it surfaces itself: **what do you do with the measures you wrote because visual calculations didn’t exist?**

Every mature Power BI estate carries a sediment layer of visual-shaped measures. You know them by their names: `Sales RT (Quarterly View)`, `Pct of Parent - Region Matrix`, `Rank for Top10 Visual`. Each one exists because some visual needed presentation arithmetic, and the model was the only place to put it. I've audited models where a quarter of all measures were this species — single-visual, presentation-bound, polluting the measure list that every new analyst (and now every Copilot session) has to navigate.

GA makes those candidates for *demotion* — moving logic from the model down to the visual that was always its only consumer. The payoff is real: a shorter, cleaner measure list is easier for humans to navigate and materially better for AI grounding, since Copilot no longer has to guess which of four running-total variants is meaningful.

But demotion has the same governance physics as everything else in this post, so the rules I use:

**Demote only what’s provably single-use.** Before touching a measure, check its lineage — if it appears in two reports, it stays a measure. (Semantic Link’s `list_measures` plus a scan of report definitions makes this an afternoon, not a quarter.)

**Mind the export dependency.** If anyone exports that visual to Excel expecting the column, demotion silently deletes it from their workflow. Ask before you remove.

**Batch it with intent, don’t drip it.** A planned cleanup — twenty measures demoted, documented, announced — builds trust. Measures quietly vanishing one at a time generates tickets and fear.

**Never demote a business definition that happens to live on one visual.** The test from the framework below still rules: if it defines what a term *means*, it stays in the model even if only one visual uses it today.

Handled this way, GA isn’t just a new authoring option — it’s a one-time chance to repay model debt that accumulated for structural reasons that no longer exist.

## The Decision Framework

![](99.System/Attachments/1!X-Cj6K4VBTCFP4fOCHRQ-A.png.webp)

Visual Calculation or Measure? Five Questions

```c
Should this be a visual calculation or a measure?

1. Does it define a business term (margin, growth, share)?
   → Measure. Always. No exceptions for convenience.

2. Will it be needed on more than one visual?
   → Measure. (Visual calcs can't be reused — you'd be
     maintaining N copies that drift.)

3. Will users export this number, pin it to a dashboard,
   or consume it via publish-to-web / custom visuals?
   → Measure. Visual calcs don't travel.

4. Does it need data not displayed on the visual,
   relationships, or dynamic format strings?
   → Measure. The visual matrix can't see any of that.

5. Is it presentation arithmetic over what's already
   displayed — running sum, moving average, % of parent,
   vs-previous, rank-as-shown, custom totals?
   → Visual calculation. This is what it's for,
     and it'll likely be faster too.
```

Five questions, and the first four all route to measures. That’s not anti-feature bias — it’s the feature’s own architecture telling you its scope. Within that scope, it’s excellent.

## Practitioner Verdict

![](99.System/Attachments/1!CcTzWB0NQLjr0swbkQQBAA.png.webp)

![](99.System/Attachments/1!My5BQ51sr4m12PFrzKezCw.png.webp)

I like this feature considerably more than this post’s warnings might suggest. The DAX it replaces was genuinely miserable — window-function gymnastics that consumed afternoons and broke under slicers. For its intended scope, it’s the right tool, well executed, and GA-stable.

But every team adopting it should write the one-sentence policy *first*. The model-as-single-source-of-truth doctrine wasn’t bureaucracy — it’s what makes your reports auditable, your definitions consistent, and increasingly, your AI answers correct. Visual calculations are a great place for presentation math, and a terrible place for the meaning of your business to quietly go live.

*What’s your team’s policy line between visual calculations and measures? And has the export gotcha bitten you yet? Comments below.*