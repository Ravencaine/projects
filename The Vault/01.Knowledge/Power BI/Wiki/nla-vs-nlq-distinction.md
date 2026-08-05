---
created: 2026-08-01
updated: 2026-08-02
source: "Natural Language Analytics Instant Dashboard Answers.md"
note_type: atomic
tags: [power-bi, natural-language, nlq, nla, ai, beginner]
---

# NLA vs NLQ: The Distinction

NLQ and NLA are often used interchangeably but describe different depths of capability.

## NLQ: Natural Language Query (Retrieval)

NLQ interprets a plain-English question and returns the matching data — a number, a filtered table, a single chart.

**Example:** "What was our revenue last quarter?" → Returns a table of Q3 revenue figures.

NLQ answers: *what happened?*

## NLA: Natural Language Analytics (Analysis)

NLA goes a step further. It analyses the retrieved data to identify trends, compare periods, calculate variance against a target, and package the result with context.

**Example:** "What was our revenue last quarter?" → Returns revenue figures + explanation: "Revenue was $4.8M, 12.4% above target, driven primarily by enterprise software sales which grew 18% vs prior quarter."

NLA answers: *what happened, why, and what's notable?*

## The Hierarchy

Every NLA platform relies on NLQ underneath. But not every NLQ tool performs full analytics.

```
NLQ ⊂ NLA
All NLA = NLQ + analysis + contextualisation
```

## Why the Distinction Matters

When evaluating platforms, asking "does it support natural language?" isn't specific enough. You need to know:
- Does it only return raw data, or does it interpret it?
- Does it explain *why* a result is notable?
- Does it surface context that a manual query wouldn't?

NLQ is table stakes. NLA is the differentiator.

## In Power BI Context

Power BI Q&A is NLQ — it returns filtered data from the semantic model based on natural language questions. NLA extends this by adding AI-generated explanations, trend analysis, and context-aware insights.

## Related

- [[natural-language-analytics-how-it-works]] — the 4-step pipeline that powers both
- [[bold-bi-ai-features]] — Bold BI's NLA features (AI Agent, AI Copilot, Smart Narrations)
