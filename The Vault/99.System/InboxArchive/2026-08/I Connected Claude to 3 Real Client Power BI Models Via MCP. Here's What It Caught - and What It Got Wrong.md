---
title: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here’s What It Caught — and What It Got Wrong."
source: "https://medium.com/towards-artificial-intelligence/i-connected-claude-to-3-real-client-power-bi-models-via-mcp-cc75289f859a"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-05-18
created: 2026-07-27
description: "Over the past two months, I’ve used Claude + Microsoft’s Power BI Modeling MCP server (currently in public preview) on three real client engagements — a manufacturing distributor, a pharma supply chain client, and a financial services firm. Three different industries. Three different model maturities. Three very different findings. One was a genuine catch I would have missed in a manual audit. One was a false positive that pointed at a real issue elsewhere. One was simply faster validation of work I’d already done. Here’s what actually happened, what each finding teaches about how to use AI in BI workflows responsibly, and the honest disclosures about how I ran these without exposing client data."
Processed: "Unprocessed"
---
## Over the past two months, I’ve used Claude + Microsoft’s Power BI Modeling MCP server (currently in public preview) on three real client engagements — a manufacturing distributor, a pharma supply chain client, and a financial services firm. Three different industries. Three different model maturities. Three very different findings. One was a genuine catch I would have missed in a manual audit. One was a false positive that pointed at a real issue elsewhere. One was simply faster validation of work I’d already done. Here’s what actually happened, what each finding teaches about how to use AI in BI workflows responsibly, and the honest disclosures about how I ran these without exposing client data.

![](99.System/Attachments/1!XNTrKoqhSynjpSVcSrnS1A.png.webp)

Claude and MCP. 3 Real client Models

## First, The Trust Disclosures (Because They Matter)

Before I describe what Claude found, I need to be explicit about how I ran these engagements. If the trust questions aren’t answered first, none of the findings matter.

**No live client data was sent to Anthropic’s API**. I worked with anonymized or sanitized model copies in every case. Customer names, account identifiers, pricing details, and any sensitive transactional content were either masked or replaced with synthetic equivalents before any MCP query ran. The semantic model structure (table names, relationships, measure definitions, Power Query M code) is what Claude actually needed to investigate — and that is genuinely useful for finding model issues without requiring sensitive row-level data.

**Two of the three clients explicitly approved this approach**. The financial services client required additional safeguards: I worked with a reconstructed model in a test environment, never the production one. The pharma client allowed a sanitized copy of the actual model. The manufacturing client allowed direct connection to a development workspace that mirrored production but contained synthetic transaction data.

**MCP is in public preview**. Microsoft’s Power BI Modeling MCP server is explicitly marked as preview. Their documentation says the implementation may change before general availability. None of these engagements treated MCP-derived findings as the final word — every finding was independently validated before any client decision.

**Claude is not part of any client’s production workflow**. This was investigative work I did during audit and review engagements. The clients are not running Claude against their live models on a schedule. Whether they will after MCP hits general availability is a separate decision they each have to make based on their own compliance and procurement contexts.

With that stated, here’s what actually happened.

![](99.System/Attachments/1!sVgb33R1XMNkjpOcKvWqNg.png.webp)

Trust & Setup Disclosures

## Client 1: The Manufacturing Distributor (A Real Catch)

The first engagement was with a manufacturing and trading client in Gujarat. They’d been on Power BI for about three years. Their core model was a sales and inventory analytics setup serving 14 published reports. The CFO had asked me to do a model health review after their analytics lead had moved to a different role and a new hire was struggling to extend the existing reports.

I’d already done my standard manual audit — the 5-check framework I’ve written about before. I’d flagged the usual things: a few measures that needed simplification, two relationships that should have been single-direction instead of bidirectional, some calculated columns that should have been measures. Standard findings.

Then I ran Claude + MCP against a sanitized copy of the model and asked a deliberately open question: *“Inspect this semantic model and tell me anything that looks structurally questionable, performance-risky, or business-logic suspicious. Don’t make assumptions about correctness — flag what catches your attention.”*

Claude went through the model methodically. It listed the tables, read the measure definitions, ran a few diagnostic DAX queries, and inspected the Power Query M code. Most of what it surfaced confirmed my own audit findings — same bidirectional relationships I’d flagged, same calculated columns, same complex measures.

Then it flagged one thing I had missed.

There was a measure called something like *“Net Revenue (Final)”* that had been added to the model about eight months earlier — after the original analytics lead had built the core measures. The new measure was structurally similar to the existing *“Net Revenue”* measure, but with one filter removed. Both measures were in active use across different reports. They produced different numbers for the same time period.

I’d missed it because the model has roughly 80 measures, and I’d only spot-checked the ones used in the executive dashboard. The *“Net Revenue (Final)”* measure was buried in a regional report I hadn’t audited.

Claude flagged it because it noticed two measures with very similar names and asked, in effect, “are these meant to differ, and if so, which is the business definition?”

The answer turned out to be that the new analyst had created the second measure when they couldn’t find the original and didn’t realize the regional report’s version of “net revenue” was structurally different from the executive dashboard’s version. Sales managers in two regions had been seeing inconsistent revenue figures for months without flagging it because each manager only saw one number.

This was a real catch. Not a $180K disaster. Not dramatic. But genuinely useful. Without it, the inconsistency would have continued until someone — probably during a board meeting — compared two reports and found the gap.

**What this taught me:** Claude + MCP is genuinely good at catching naming and structural inconsistencies across a model that a human auditor might miss because the human is checking what they expect to find, not pattern-matching across the whole namespace. AI doesn’t get tired the way I do during the seventh hour of a manual audit.

![](99.System/Attachments/1!666Hc4KsXSKNNYS2aNmOGw.png.webp)

Client 1 — The Real Catch

## Client 2: The Pharma Supply Chain Client (A False Positive That Revealed Something)

The second engagement was with a pharma supply chain client. They’d been on Power BI for around five years and were in the middle of evaluating a Fabric migration. Part of my engagement was reviewing the readiness of their current model for migration.

I ran Claude against a sanitized copy of their inventory analytics model with a focused prompt: *“Look at the FactInventory table and the related dimensions. Flag any data quality concerns, modeling concerns, or anomalies that could affect downstream analytics.”*

Claude’s response was confident and specific. It identified what it described as a likely data quality issue in the inventory balance measure. The concern: it found that on certain dates, the sum of inventory balance across all products didn’t match the expected total based on opening balance plus movements. The discrepancy was small — around 1.2% — but consistent. Claude proposed it might be a missing inventory adjustment record or a Power Query issue with the inventory snapshot table.

This sounded plausible. I escalated it to the client’s analytics team for review.

It turned out to be a false positive — but a useful one.

The client’s analytics lead came back two days later with the actual explanation: the 1.2% gap was real, but it wasn’t a bug. It was caused by intra-day stock transfers between distribution centers that weren’t reflected in the daily snapshot table. The business knew about it. Their accounting team handled the reconciliation manually each month. It had never been a problem because nobody analyzed inventory balance at that level of precision in any production report.

So Claude flagged something. It just flagged the wrong cause.

But here’s why this still mattered: the conversation that followed revealed two things I would not have asked about in my standard audit. First, the manual reconciliation process was one person’s responsibility, undocumented anywhere, and that person was planning to retire within twelve months. Second, the Fabric migration the client was evaluating would change how snapshots were taken, which would expose the existing 1.2% gap in ways the current architecture absorbed.

The “false positive” became a real conversation about a real risk. The risk wasn’t where Claude had pointed, but the pointing itself was useful.

**What this taught me**: AI flags should be treated as triggers for conversation, not as conclusions. When Claude flagged the inventory anomaly, the wrong response would have been to spend a week looking for a Power Query bug. The right response was to ask “is this a real issue, and if not, why does the data look this way?” That question surfaced something genuinely worth discussing. False positives are not failures if they generate the right next question.

![](99.System/Attachments/1!Ykyt-PzmjxRudEAwQpcHBg.png.webp)

Client 2 — The False Positive

## Client 3: The Financial Services Firm (Faster Validation, Not New Findings)

The third engagement was with a financial services client. Highly regulated environment, careful data governance, mature analytics team. The engagement was a review of a new Fabric semantic model their team had built to replace a legacy Power BI dataset that had been in production for several years.

For this one, I worked exclusively against a reconstructed model in a test environment — never their production system. The reconstruction was based on the schema, measure definitions, and Power Query logic, but used synthetic data for any sensitive fields.

I’d already spent two days reviewing their work. The team had done an excellent job. Star schema, properly named measures, well-documented relationships, sensible Power Query design. My audit notes had a handful of minor suggestions and zero significant concerns.

I ran Claude + MCP partly to test the workflow on a high-quality model — to see what it would do when there was less to find. I asked the same kind of investigative question I’d used with the other two: *“Inspect the model and identify any concerns or improvements.”*

Claude’s response was different from the other two engagements. Instead of flagging issues, it largely confirmed the strengths of the model. It noted the same minor things I had — a few measure naming inconsistencies, two date-related calculations that could be simplified — but it didn’t surface anything I hadn’t already documented.

This sounds anticlimactic, but it was genuinely useful in a way I hadn’t expected. What Claude did, on this engagement, was give me independent confirmation of my own audit conclusions. Two separate analytical processes (mine, then Claude’s) reaching similar conclusions about a mature model is a stronger signal than either alone.

I included that in my final report to the client: I noted that an independent automated review using Claude + MCP had reached substantially the same conclusions. The client’s CTO appreciated the additional validation layer, particularly given the regulated environment they operate in.

**What this taught me:** AI is sometimes most valuable when it doesn’t find anything new. For mature, well-built models, Claude + MCP serves more as a validation pass than a discovery tool. That’s a different value proposition than “AI catches what you missed” — and it’s worth recognizing because it changes when and why you’d run it.

For a junior analyst’s first model, Claude + MCP probably IS a discovery tool. For an experienced practitioner’s review of a mature team’s work, it becomes a confirmation tool. Both are useful. They’re just different uses.

![](99.System/Attachments/1!xD_7kpc6iiV28JeqUB1QqA.png.webp)

Client 3 — Validation Layer

## The Honest Scorecard Across Three Clients

![](99.System/Attachments/1!1eVhZb3oP9rRQmNNDEODtg.png.webp)

**Three engagements. Three different value patterns.** The headline insight isn’t “Claude is amazing” or “Claude is unreliable.” Both are too simple. The honest pattern is that AI investigation produces different value depending on the maturity of the work it’s looking at and the framing of the question being asked.

![](99.System/Attachments/1!1CKDT93kPx_J8JbkO9mQOQ.png.webp)

The Honest Scorecard

## What I’m Now Comfortable Saying About Claude + MCP for Real BI Work

After three engagements, here’s what I’d commit to in writing:

**It’s genuinely useful for cross-namespace pattern matching.** Catching things like inconsistent measure variants, similarly-named-but-differently-defined calculations, and structural patterns spread across many tables is something Claude does better than I do during long manual audits. This is its single strongest current use case.

**It needs a human in the loop on every flag.** None of the three findings were “deploy directly to client.” The manufacturing finding was real. The pharma finding was wrong about cause but right about flagging. The financial services finding was confirmatory. In every case, my judgment determined what to do with what Claude said. AI flags are conversation-starters, not conclusions.

**It produces less new value on mature models.** This is counterintuitive but matches what I observed. The financial services engagement, with the most mature model, generated the least new insight from MCP. The manufacturing engagement, with the least mature model, generated the most. If you’re an experienced practitioner working on excellent existing work, AI confirmation is the realistic value — not new findings.

**Trust disclosures matter as much as the findings.** Every conversation I’ve had with clients about MCP starts with “what data goes where, who sees it, how is it protected.” If I don’t have clear answers — sanitized copies, reconstructed models, no sensitive content sent to third-party APIs — the engagement doesn’t happen. The technology is only useful if the trust posture is defensible.

**MCP being preview is a real constraint.** I would not currently put Claude + MCP into a client’s production audit workflow. I’d use it during my engagement, validate every finding manually, and disclose the preview status clearly. When MCP hits general availability and Microsoft documents the support boundaries clearly, the calculus changes.

## What I’d Tell Someone Considering This For Their Own Models

If you’re an internal Power BI practitioner thinking about running Claude + MCP against your own organization’s models, three honest pieces of advice:

**First, sort out the data governance question before you sort out the technology.** Can you actually send your model metadata to Anthropic’s API under your organization’s data policies? If yes, proceed. If no, work with sanitized copies or wait for first-party Microsoft tools (the Power BI Agent in preview is one direction this might go). Don’t run technology you can’t defend.

**Second, manage your expectations about what AI investigation produces**. If your model is well-built, the AI will mostly confirm your work. That’s still valuable, but it’s a different value than “AI found a critical bug.” If your model is messy and aging, the AI will likely find more — but you’ll need to validate every flag because false positives are real.

**Third, treat AI findings as conversation triggers, not as audit conclusions.** Every Claude flag in my three engagements led to a question. The questions were almost always more valuable than the flags themselves. Use the AI to surface questions you weren’t going to ask. Then answer the questions yourself.

![](99.System/Attachments/1!8YJjVvb3Gg4k2iMV5ImBUA.png.webp)

Recommendations

## The Bigger Picture (Same Picture From Different Angles)

I’ve been writing about AI in Power BI for a while now, from different angles — Copilot’s limitations, ChatGPT vs Claude on diagnostic problems, how three different companies handled AI-driven team restructuring, what endures across tool generations. This post adds another angle: what happens when you actually use the strongest current AI investigation configuration on real client work.

The thread tying all of these posts together, after enough months of writing them, is honestly this: **AI is changing what experienced practitioners can do faster, but it isn’t changing what experienced practitioners need to know.**

Claude + MCP is genuinely useful for me. It catches things I miss. It surfaces conversations I wouldn’t have started. It validates conclusions in ways that strengthen my reports. It compresses the time I spend on certain audit tasks meaningfully.

It does not replace the part of my work that is “knowing what questions to ask,” “understanding the business well enough to interpret an anomaly,” or “having the judgment to tell a real finding from a false positive that points at something real.”

If you’re early in your BI career, the AI capability is rising fast — fast enough that the floor of what entry-level competence looks like is moving up. If you’re experienced, the AI capability is amplifying your existing judgment — which means you have more leverage than ever, IF you can stay credible about what AI is actually doing for you.

That credibility is the part I care about most right now. It’s why this post led with disclosures, why every finding included its context, and why “what it got wrong” got equal billing with “what it caught.”

The drama is the easy part to write. The honesty is what compounds.

![](99.System/Attachments/1!MQYYa6xonmGK30n-SAT0Ug.png.webp)

The Bigger Picture

*Have you used Claude + MCP, Copilot, or any AI investigation tool against real client or internal Power BI models? I’d genuinely value hearing what you’ve found — both the catches and the false positives. The pattern across many of these engagements will be more useful than any single test.*

*If you’re considering this for your own work and want to think through the data governance and disclosure questions before you start, reach out. The technology is straightforward. The trust posture is the part that takes work.*