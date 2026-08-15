---
title: "Agent Skills for Power BI Just Shipped. Here’s What Actually Changed Since I Compared These Tools."
source: "https://medium.com/@mohamedaasir1992/agent-skills-for-power-bi-just-shipped-heres-what-actually-changed-since-i-compared-these-tools-9f1119a906c8"
author:
  - "[[Aasir Waseer]]"
published: 2026-07-15
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
*A follow-up to my Power BI Copilot vs. Tableau Pulse vs. Qlik Answers piece — because the ground moved under that comparison faster than I expected.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MI2_zZ_kkih9F3uEln1uWg.jpeg)

I wrote a comparison of the major BI AI assistants a couple of weeks ago, and even then I knew the category was moving fast. I didn’t expect it to move fast enough that part of the piece would need an update this soon. Microsoft’s latest release wave introduces something categorically different from what I compared before, and the distinction matters enough that I think it’s worth walking through explicitly, rather than just tacking a footnote onto the old piece.

**What I was actually comparing before**

When I wrote the original comparison, the Copilot experience I evaluated was fundamentally a *question-answering* layer sitting on top of reports that a human had already built. You’d ask “what were sales in Q4,” and it would find the right report, filter it, and hand you an answer inline. Useful, genuinely time-saving, but bounded — the AI was operating inside a structure a person had designed.

That’s still true of the core “chat with your data” experience, and it’s still a fair way to evaluate that specific feature. What’s new is a second, much more ambitious capability sitting alongside it, and conflating the two is where I think a lot of coverage is currently getting sloppy.

**The actual shift: from answering questions to building the report itself**

The new capability lets an AI agent go end-to-end: design a report, build the underlying semantic model, author the actual report files, validate the result, and publish it — from a natural language description or even a screenshot as a design reference. That’s a meaningfully different claim than “ask a question about an existing report.” It’s “skip building the report yourself entirely.”

There’s also a companion piece that matters just as much and gets less attention: an AI-powered assistant that can analyze an existing semantic model and directly apply structural changes — renaming tables and columns, creating relationships, generating DAX measures — from a plain-language instruction like “improve table relationships.” That’s not answering a question about the data. That’s an agent making schema-level modeling decisions that used to require someone who actually understood the data model.

Put those two together and the honest read is: the tools I compared a few weeks ago were assistants. This release is closer to an autonomous report-building and modeling agent, with a human reviewing the output rather than authoring it.

**Why this connects directly to the context-engineering piece I wrote**

I spent a full piece a few weeks back arguing that a gold layer designed for AI consumption has to be modeled differently than one designed purely for human dashboards — because the agent inherits every ambiguity a human would normally paper over with context they already have in their head. Microsoft’s own messaging around this release makes almost exactly that argument, in different words: a pretty report built on bad assumptions is just a faster way to be wrong, and that’s precisely why the agent is being positioned to work through the governed semantic layer — where business logic, relationships, and measure definitions are supposed to already be correct — rather than freelancing its own assumptions about what a metric means.

That’s a tacit admission of the same risk I flagged in the SQL piece: an AI system that’s fast at producing plausible output is only trustworthy to the extent the structure underneath it was already correct. Speeding up report *creation* doesn’t fix a badly modeled semantic layer — it just means bad assumptions get published faster and with a more convincing coat of paint on top.

**The part I think is genuinely underrated: the continuous edit-verify loop**

One detail buried in the announcement that I think matters more than the headline capability: a new bridge that lets an agent connect directly to a running desktop session and read, update, and verify a report in a continuous loop — rather than generating something once and handing it over blind. That loop is the difference between “AI guesses and you find out later” and “AI iterates against a live, checkable target.” It’s a meaningfully more conservative design than a single-shot generation, and it’s the piece that makes me somewhat more comfortable with the broader agentic claim than I would be otherwise.

**Where I’d revise my original comparison**

Going back to the framing of my earlier piece, here’s what I’d actually change:

- **The comparison needs a second axis, not just a winner.** It’s no longer just “which assistant answers questions best” — it’s now also “which platform lets an agent build and modify the underlying model, not just query it.” Those are genuinely different capabilities, and a tool can be strong on one and weak on the other.
- **“Trust the governed model” becomes the load-bearing caveat for the whole category.** Any AI-driven report-building capability is only as trustworthy as the semantic model it’s grounded in. That was true before this release too, but it matters more now that the AI is touching the model itself, not just querying around it.
- **The deprecation of the old, simpler Q&A feature by the end of this year is worth flagging.** It’s a signal that this generative, agentic approach isn’t an add-on option anymore — it’s becoming the only path forward, which raises the stakes on getting the semantic layer right before leaning on it.

**What I’m actually doing differently because of this**

Practically, this pushes me toward spending more time up front on the semantic model itself — naming conventions, relationships, measure definitions — treating that layer as the thing an agent will eventually be modifying directly, not just something a human occasionally tunes. If an AI agent is going to be trusted to rename columns and create relationships based on a plain-language instruction, the existing model needs to be clean enough that “improve table relationships” doesn’t have multiple plausible, contradictory interpretations for the agent to choose between.

That’s the same lesson from the SQL piece and the context-engineering piece showing up a third time in a different tool: the unglamorous modeling work underneath the AI layer keeps turning out to be the actual bottleneck, not the AI’s capability itself.

**Where I’m staying cautious**

I want to be honest that I haven’t run this capability against a real production model yet — this is a first read based on the announcement and documentation, not a hands-on verdict. The continuous edit-verify loop is a genuinely reassuring design choice on paper, but “agent modifies your live semantic model based on natural language” is exactly the kind of capability I’d want to see fail a few times in a sandboxed environment before trusting it against anything a leadership team is actually going to look at. I’ll follow up once I’ve actually tried it against something real, rather than just reacting to the release notes.

*I compare BI tooling as I actually use it, and update when the ground moves — which, this year, is apparently every few weeks. If you’ve already tried the new Agent Skills against a real model, I’d like to hear whether the edit-verify loop held up.*