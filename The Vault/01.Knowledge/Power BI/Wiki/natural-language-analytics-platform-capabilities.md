---
created: 2026-08-01
updated: 2026-08-02
source: "Natural Language Analytics Instant Dashboard Answers.md"
note_type: atomic
tags: [power-bi, natural-language, nla, evaluation, platform, beginner, intermediate]
---

# NLA Platform: Key Capabilities to Evaluate

Not every tool that accepts a typed question delivers real analytics. These capabilities separate genuine NLA from a basic keyword-search feature.

## Natural Language Understanding (NLU)

Interprets free-form questions, not just rigid keyword syntax matched to column names. A genuine NLU engine handles paraphrasing, implied context, and conversational follow-ups without requiring exact phrasing.

**Shallow:** keyword match → column name → return column
**Real NLU:** intent + entities + context → query

## Query Transparency

Shows the underlying data and logic behind every answer so users can verify it rather than take it on faith. Particularly important in regulated industries (finance, healthcare) where incorrect interpretations carry risk.

**What to look for:** ability to see the exact fields queried, the time period applied, and any filters active.

## Automated Visualization Selection

The platform picks the chart, KPI card, or table format that best fits the question — rather than returning a generic table every time.

**Example:** "How does revenue compare to last year?" → bar chart. "What's our current pipeline?" → KPI card.

## Narrative Generation (NLG)

Explains the "why" behind a result in plain language alongside the visual. A number with a story is more actionable than a number alone.

**Example output:** "Revenue was $4.8M, 12.4% above target. Growth was driven primarily by enterprise software sales, which increased 18% vs the prior quarter."

## Context Retention

Supports follow-up questions without repeating the full question from scratch.

**Example:** Q1: "Which region beat target this quarter?" → Northeast. Q2: "What drove that?" → follow-up understood as still about Northeast.

## Synonym and Vocabulary Handling

Understands that "revenue" and "sales" refer to the same metric and can learn organisation-specific terminology over time.

## Governed, Connected Data

Works against the organisation's existing data sources and permission model — not a siloed copy. Answers are consistent with what dashboards show.

**Red flag:** A tool that creates a separate "NLA data store" disconnected from the governed semantic model.

## Related

- [[nla-vs-nlq-distinction]] — the evaluation starting point
- [[natural-language-analytics-how-it-works]] — the pipeline these capabilities support
- [[bold-bi-ai-features]] — Bold BI's implementation of these capabilities
