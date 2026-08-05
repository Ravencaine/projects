---
created: 2026-08-01
updated: 2026-08-02
source: "Natural Language Analytics Instant Dashboard Answers.md"
note_type: atomic
tags: [power-bi, bold-bi, ai, nla, ai-agent, ai-copilot, smart-narrations, beginner]
---

# Bold BI AI Features for Natural Language Analytics

Bold BI implements NLA through three distinct AI features. Each targets a different part of the analytics workflow.

## AI Agent

Conversational data exploration. Users type plain-English questions and receive answers directly from connected data sources.

**What it does:** interprets the question → queries the semantic model → returns formatted result (chart, KPI, table, or explanation).

**Use case:** "Which region exceeded its revenue target this quarter?" → returns a KPI card with target vs actual + regional comparison chart + AI explanation of key drivers.

## AI Copilot

Prompt-based dashboard creation. Users describe what they want and AI Copilot generates the visualisation without manual field configuration.

**What it does:** turns a natural language prompt into a configured chart.

**Use case:** "Create a bar chart of units sold by category" → AI Copilot generates the bar chart with correct fields mapped.

**Value:** lowers the barrier for non-technical users to build their own charts. Analysts still validate and refine the output.

## Smart Narrations

Automatic plain-language summaries for dashboard visualizations. Instead of manually interpreting a chart, users get a concise written explanation of what the data shows.

**What it does:** analyses the data behind any dashboard visual → generates a narrative explanation → surfaces notable changes, trends, and anomalies.

**Where it appears:**
- On dashboard visuals (inline narration)
- In scheduled dashboard exports (AI-generated email summaries)

**Value:** stakeholders who don't read charts directly get the insight anyway.

## How They Work Together

| Feature | Target User | Action |
|---------|------------|--------|
| AI Agent | Any business user | Ask questions, get answers |
| AI Copilot | Non-technical users | Create visualisations from prompts |
| Smart Narrations | All dashboard viewers | Get explanations without analysing charts |

Together they cover: ad hoc questions (AI Agent), self-service visualisation (AI Copilot), and comprehension assistance (Smart Narrations).

## Comparison with Power BI Q&A

Power BI Q&A is NLQ — plain-English querying of the semantic model. Bold BI's AI Agent goes further with conversational context retention and AI-generated explanations. AI Copilot is a prompt-to-viz feature not available in standard Power BI. Smart Narrations are similar in concept to Power BI's AI Insights but implemented at the dashboard level.

## Related

- [[nla-vs-nlq-distinction]] — how these features map to NLQ vs NLA
- [[natural-language-analytics-how-it-works]] — the pipeline that powers AI Agent
- [[natural-language-analytics-platform-capabilities]] — evaluation criteria for these features
