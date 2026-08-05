---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
source_url: "https://medium.com/towards-artificial-intelligence/i-connected-claude-to-3-real-client-power-bi-models-via-mcp-cc75289f859a"
note_type: source
tags: [power-bi, ai, mcp, auditing, semantic-model, claude, agentic-ai]
---

# Tejwani — Claude + MCP Power BI Model Auditing

> **Type:** article / case study
> **Author:** Gulab Chand Tejwani
> **Published:** 2026-05-18
> **URL:** https://medium.com/towards-artificial-intelligence/i-connected-claude-to-3-real-client-power-bi-models-via-mcp-cc75289f859a
> **Routed to:** Power BI

## Summary

Three real client engagements using Claude + Microsoft's Power BI Modeling MCP server (public preview) for semantic model auditing. One genuine catch (inconsistent measure pair), one false positive that revealed a real risk, one mature model where AI served as a validation layer. Honest scorecard: AI value depends on model maturity and framing.

## The Setup

- **Tool:** Claude (Anthropic) + Microsoft Power BI Modeling MCP server (public preview)
- **Trust model:** No live client data sent to API; sanitized or synthetic model copies used throughout
- **Clients:** Manufacturing distributor (Gujarat), pharma supply chain, financial services firm
- **Disclosure:** MCP is preview — findings independently validated before any client decision

## Three Engagement Outcomes

| Client | Model Maturity | Finding Type | Value Delivered |
|--------|--------------|--------------|----------------|
| Manufacturing | Low (~80 measures, new analyst) | Genuine catch | Caught duplicate measure pair with different filter contexts — inconsistent revenue figures across regions |
| Pharma supply chain | Medium | False positive → real risk | Flagged 1.2% inventory gap (wrong cause); revealed undocumented manual reconciliation + Fabric migration risk |
| Financial services | High (mature team, excellent model) | Confirmation | Independent validation of audit conclusions; added credibility for regulated environment |

## Key Claims

- Claude + MCP catches naming and structural inconsistencies across the full model namespace — things humans miss during long manual audits
- AI flags are conversation starters, not audit conclusions — every flag led to a question; the questions were more valuable than the flags
- AI produces less new value on mature models — on excellent work it serves as a validation layer, not a discovery tool
- False positives are not failures if they generate the right next question

## Honest Scorecard

- **Best for:** Cross-namespace pattern matching, finding similarly-named but differently-defined measures, catching things humans miss in long audits
- **Needs:** Human in the loop on every flag; independent validation before client delivery
- **Limitation:** Preview MCP; not ready for production audit workflows
- **Model maturity effect:** More value on messy/aging models; less on mature well-built ones

## Recommendations

1. Sort the data governance question before the technology question
2. Manage expectations: AI on mature models = confirmation, not discovery
3. Treat AI findings as conversation triggers, not audit conclusions

## Extracted Notes

- [[ai-assisted-audit-vs-manual-audit]] — `atomic` — AI catches what humans miss after hour 7; humans catch what AI misinterprets
- [[ai-cross-namespace-pattern-matching]] — `atomic` — strength: finding similarly-named but differently-defined measures across the full namespace
- [[ai-flag-as-conversation-trigger]] — `atomic` — every AI flag should start a question; the question is the value
- [[mcp-power-bi-modeling-preview-caveats]] — `atomic` — preview constraints, trust posture, data governance requirements
- [[power-bi-mcp-audit-workflow]] — `pattern` — 3-step workflow for AI-assisted semantic model auditing

## Metadata

| Field | Value |
|-------|-------|
| Source file | I Connected Claude to 3 Real Client Power BI Models Via MCP. Here’s What It Caught — and What It Got Wrong.md. Here’s What It Caught — and What It Got Wrong.md |
| Ingestion date | 2026-08-01 |
| Word count | ~540 |
