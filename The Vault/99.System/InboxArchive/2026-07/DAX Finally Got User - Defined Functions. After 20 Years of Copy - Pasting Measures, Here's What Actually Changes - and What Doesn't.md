---
title: "DAX Finally Got User-Defined Functions. After 20 Years of Copy-Pasting Measures, Here’s What Actually Changes — and What Doesn’t."
source: "https://medium.com/@t.gulab/dax-finally-got-user-defined-functions-d58e022379ca"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-07-06
created: 2026-07-27
description: "DAX user-defined functions went generally available in the June 2026 Power BI release, after nine months in preview. It’s the biggest change to how DAX code gets organized since calculation groups. But having spent two decades watching “game-changing” features land in the Microsoft BI stack — and having written a 577-formula DAX library along the way — I’ve learned to ask a more precise question than “is this exciting?” The question is: which specific problems does this solve, which does it not touch, and where will it quietly create new ones? Here’s the honest practitioner breakdown."
Processed: "Unprocessed"
---
## DAX user-defined functions went generally available in the June 2026 Power BI release, after nine months in preview. It’s the biggest change to how DAX code gets organized since calculation groups. But having spent two decades watching “game-changing” features land in the Microsoft BI stack — and having written a 577-formula DAX library along the way — I’ve learned to ask a more precise question than “is this exciting?” The question is: which specific problems does this solve, which does it not touch, and where will it quietly create new ones? Here’s the honest practitioner breakdown.

![](99.System/Attachments/1!D9qlURLKRdhi9_Q8YRb0qw.png.webp)

DAX Finally got Functions

Earlier this year, I wrote about an audit where Claude flagged two measures in a client’s model: *Net Revenue* and *Net Revenue (Final)*. Structurally similar. One filter different. Both in active use across different reports. Sales managers in two regions had been seeing different revenue numbers for months, and nobody knew.

When I traced how that happened, the story was painfully ordinary. A new analyst needed the revenue logic, couldn’t find where it lived, and rebuilt it from a half-remembered screenshot. The model had roughly 80 measures. At least a dozen of them were variations of the same three business rules — margin logic, net revenue logic, and a fiscal-period adjustment — copy-pasted and lightly mutated over three years by four different authors.

That’s not a bad team. That’s what DAX has forced on every team since 2010: the language had no way to define logic once and reuse it. Every measure was an island. The only “reuse” mechanism was copy-paste, and copy-paste is how one business rule becomes twelve slightly different business rules.

The June 2026 Power BI release changed that. DAX user-defined functions are now generally available in Power BI Desktop and the Power BI Service. For the first time, DAX has real functions — named, parameterized, documented, living in the model as first-class objects.

This matters. It also fixes less than the excitement suggests. Both things are true, and this post covers both.

*(Client details in this post are generalized to protect confidentiality. The technical scenarios are real.)*

## What Actually Shipped (Verified Facts First)

Before the opinions, the baseline from Microsoft’s documentation:

- DAX UDFs are **generally available starting with the June 2026 release**, in both Power BI Desktop and the Service. They’d been in preview since September 2025.
- Your model needs **database compatibility level 1702 or higher** — Power BI can upgrade this automatically.
- You define functions in **DAX query view or TMDL view**, and they appear under a **Functions node in Model Explorer**. In a Power BI Project (PBIP), they live in their own `functions.tmdl` file — which matters more than it sounds, because it means functions are now version-controllable objects.
- Functions can be called from **measures, calculated columns, visual calculations, and other functions**. Nesting works.
- Parameters support optional **type hints** — scalar subtypes like Int64, Decimal, String, DateTime — and two evaluation modes, **VAL and EXPR**, which we need to talk about seriously in a moment.
- A triple-slash comment (`///`) above the function becomes its description in the model. Documentation as part of the definition.

The basic shape looks like this:

```c
DEFINE
/// Returns amount including 10% tax
FUNCTION AddTax = ( amount : NUMERIC ) =>
    amount * 1.1

EVALUATE { AddTax ( 10 ) }  // Returns 11
```

Name, parameters, arrow, body. If you’ve written a function in any language in the past forty years, nothing here will surprise you. The surprise is that DAX went fifteen years without it.

One more piece worth knowing: SQLBI launched daxlib, an open-source repository of model-independent DAX functions you can import into your own models. A community library for the calculation layer now exists. That’s a structural change to how DAX knowledge spreads, not just a convenience.

![](99.System/Attachments/1!VenLEuJY9F_eUjh6n__V6w.png.webp)

What Shipped

## The Disease This Actually Cures

Let me be precise about the problem UDFs solve, because it’s a specific one.

Every mature semantic model I audit — and I’ve done these audits across manufacturing, pharma, retail, and financial services — has the same pathology. Somewhere between 15% and 40% of the measures are near-duplicates of each other. The same margin calculation with a different filter. The same currency conversion with a hardcoded rate that was updated in three places but not the fourth. The same “exclude inter-company transactions” pattern implemented four slightly different ways by four different authors.

None of this happened because anyone was careless. It happened because the language offered no alternative. When business logic can’t be defined once, it gets defined everywhere, and every copy drifts independently.

UDFs attack exactly this. The margin rule becomes one function. The inter-company exclusion becomes one function. When finance changes the rule — and finance always changes the rule — you update one definition and every measure that calls it inherits the fix. The *Net Revenue (Final)* problem from my audit doesn’t disappear entirely, but its most common cause does: the new analyst doesn’t rebuild the logic from a screenshot, because the logic has a name, a description, and a home in Model Explorer where they can find it.

There’s a second-order benefit I care about even more as someone who reviews other people’s models for a living: **functions make intent readable**. A measure that calls `Sales.NetRevenue ( ... )` tells me what it's doing. Three hundred characters of nested CALCULATE tells me nothing until I've reverse-engineered it. Multiply that by 80 measures and you understand why model audits take days.

![](99.System/Attachments/1!M26iViC-CN_jjUEqFxixxw.png.webp)

The Copy Paste Disease

## The VAL vs EXPR Trap (Where People Will Get Hurt)

Now the part most of the celebration posts skip, and the part that will generate the production incidents.

Every UDF parameter has an evaluation mode. **VAL** means the argument is evaluated immediately, before the function runs, and the resulting value is passed in. **EXPR** means the unevaluated expression is passed in, and the function decides when — and in what filter context — to evaluate it. VAL is the default.

Why does this matter? Because DAX is a language where *when* something is evaluated determines *what* it returns. Filter context and context transition are the entire game. A function that receives a pre-evaluated value cannot re-evaluate it under a different filter — so if your function tries to do something like “compute this expression, but only for red products,” a VAL parameter silently gives you the wrong answer. The expression was already evaluated in the outer context before your CALCULATE ever ran. No error. No warning. Just a plausible-looking wrong number.

SQLBI’s early deep-dive on UDFs made this exact point, and it matches what I’ve seen in preview-period experiments: the difference between a function written by a newcomer and one written by a professional is whether it handles context transition deliberately — choosing EXPR where the function manipulates context, and forcing the transition explicitly with CALCULATE inside the function body where needed.

Here’s my blunt prediction. Over the next year, teams will build function libraries where half the functions have subtly wrong parameter modes. The functions will work in the scenario their author tested. Then someone will call them from a different context — a calculated column instead of a measure, an iterator instead of a card visual — and the numbers will shift quietly. This is the SUM-vs-SUMX class of error all over again: not a syntax error, a semantics error, invisible until someone reconciles against the source system.

If you take one technical thing from this post: **decide VAL or EXPR explicitly for every parameter, and test every function from at least two different calling contexts before you trust it**. The default is not a decision. It’s a deferral.

![](99.System/Attachments/1!jJfuzUF3fk1bmMJW_WpjdQ.png.webp)

The VAL Vs EXPR Trap

## What UDFs Don’t Fix

I’ve written before about why I stopped publishing “best practice” lists — patterns without context create worse developers than no advice at all. So in that spirit, here is what this feature genuinely does not touch.

**UDFs don’t fix your model.** If your grain is wrong, your relationships are ambiguous, or your fact table is a flat export from the ERP, wrapping the compensating DAX in a tidy function just gives the problem a nicer name. I said it about Fabric, I said it about Copilot, and it’s still true here: the bottleneck in most broken models is upstream of the calculation layer.

**UDFs don’t automatically improve performance.** A function is a reusable expression, not a faster one. In fact, the stakes go up: a function called by thirty measures multiplies its inefficiency by thirty. SQLBI’s guidance is right — optimize function code more aggressively than you’d optimize a single measure, precisely because it’s shared infrastructure now.

**UDFs don’t replace calculation groups.** Time intelligence variations across many measures — YTD, PY, YoY% applied to everything — is still calculation group territory. UDFs shine for business logic: the rules with parameters, the calculations that differ by input rather than by filter-context transformation. Most serious models will end up using both, deliberately.

**UDFs don’t govern themselves.** You can now build a shared function library — which means you now need ownership, naming conventions (the community has settled on PascalCase, with dots for namespacing like `Sales.NetRevenue`), a review process for changes, and version control. The `functions.tmdl` file plus Git handles the mechanics. The discipline is on you. A shared library nobody governs becomes the new copy-paste problem, just centralized.

![](99.System/Attachments/1!vqPvO6rhhHaM1rPJHGhSKQ.png.webp)

What UDFs Don’t Fix

## The 577-Formula Question

When UDFs hit GA, the first thing I did was reopen my own DAX formula library — 577 formulas across 26 chapters, built over years of client work — and ask an uncomfortable question: how much of this should now be functions?

The honest audit surprised me in both directions.

Roughly **60 to 80 formulas collapse naturally into maybe 15 to 20 functions.** These are the parameterized business rules: safe-divide-with-business-default patterns, tiered margin logic, currency normalization, working-day adjustments, text-cleanup rules for customer matching. The variations in my library were mostly the same skeleton with different inputs — exactly what parameters are for.

The **time intelligence chapters mostly stay as they are**. Not because functions couldn’t express them, but because calculation groups already solve that reuse problem better, and mixing both mechanisms for the same job makes models harder to reason about, not easier.

And a large share of the library **shouldn’t become functions at all** — because those formulas were never really about the DAX. They were about the modeling decision underneath: what grain, which relationship, which context. Turning them into functions would hide the decision that matters inside an abstraction that suggests it’s settled. Some code deserves to stay visible.

That ratio — call it a quarter of a mature DAX corpus genuinely wanting to become functions — is my honest expectation for most real models too. Meaningful. Not revolutionary. The models that benefit most will be the ones with the most duplicated business logic, which, not coincidentally, are the ones with the least governance. The feature helps most where discipline exists least. That’s either an opportunity or a warning, depending on your team.

![](99.System/Attachments/1!MVLtpY4PrksGmqyhiRMLHA.png.webp)

The 577- Formula Question

## How I’d Actually Start (If This Is Your Model)

Four moves, in order.

**Start with an inventory, not a function.** Search your model for near-duplicate measures — INFO.USERDEFINEDFUNCTIONS and the older INFO functions in DAX query view make model introspection straightforward now, and even a manual pass over Model Explorer will surface the repeated skeletons. You can’t consolidate what you haven’t counted.

**Convert your top three duplicated rules first.** Not thirty. Three. The ones where the business rule has changed in the past year are the highest-value candidates, because they’re the ones most likely to have drifted across copies already.

**Write the doc comment before the body.** The `///` description is what the next analyst reads in Model Explorer. If you can't describe the function in one sentence, the function is doing too much — split it.

**Test each function from two contexts minimum.** A measure and a calculated column at least. If it’s an EXPR-parameter function, add an iterator. The VAL/EXPR class of bug only shows itself when the calling context changes, so change the calling context before production does it for you.

![](99.System/Attachments/1!vJv7SfuE2BeeS1v8gRNEyg.png.webp)

Getting Started

## Where This Actually Lands

My verdict, three weeks into GA and nine months after first touching the preview:

This is the most important change to DAX-the-language in years — and it’s an organizational feature more than a calculation feature. Nothing you can compute today was impossible before. What changed is whether a team’s DAX can be maintained by people who didn’t write it. That’s not a small thing. Unmaintainable calculation layers are where BI projects go to die quietly; I’ve audited the corpses.

The community library angle may end up mattering most. Between daxlib and functions living in version-controllable TMDL files, DAX just gained the sharing infrastructure every real programming language has had for decades. The next generation of Power BI developers will import battle-tested functions the way Python developers import packages. The generation after that won’t believe we copy-pasted measures for fifteen years.

And the failure mode is already visible: libraries of confidently-wrong functions with untested parameter modes, spreading through models with the same speed the good ones do. The tool amplifies whatever discipline you bring to it.

Which — if you’ve read anything else I’ve written this year — is the same conclusion every powerful new capability in this space keeps teaching. The tools keep getting better. The thinking is still the job.

![](99.System/Attachments/1!CwqNzM76uXcCpscZzx6UFg.png.webp)

The Practitioner Verdict

*Have you started moving real business logic into DAX UDFs — or hit the VAL/EXPR wall in the process? I’d genuinely like to hear what you’re seeing. The patterns across many models teach more than any single writeup.*

*If your model has the duplicated-measure disease and you want a second pair of eyes on which logic deserves consolidation, reach out. The inventory usually takes an afternoon. The clarity lasts considerably longer.*

*Sources referenced: Microsoft Learn documentation for DAX user-defined functions (June 2026 GA), Power BI June 2026 Feature Summary, SQLBI’s “Introducing user-defined functions in DAX,” Tabular Editor’s UDF guidance, and daxlib. All technical claims grounded in official documentation.*