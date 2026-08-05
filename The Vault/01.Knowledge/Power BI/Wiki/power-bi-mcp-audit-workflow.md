---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
note_type: pattern
tags: [power-bi, ai, mcp, auditing, semantic-model, workflow, dax-studio]
---

# AI-Assisted Power BI Model Audit Workflow (MCP)

A three-phase workflow for using Claude + Microsoft Power BI Modeling MCP server in a semantic model audit engagement. Combines AI exhaustive scanning with human judgment for every finding.

## Prerequisites

Before any MCP query runs:
- ✅ Confirm data governance: model metadata only, sanitised or synthetic copies for sensitive environments
- ✅ Explicit client approval (for client-facing engagements)
- ✅ MCP is preview — all findings independently validated before delivery
- ✅ Test environment used, never production (for sensitive clients)

## Phase 1 — Sanitise and Scope (10 minutes)

1. Obtain a sanitised or reconstructed copy of the semantic model
2. Confirm no live client data will be sent to the AI provider API
3. Document the trust posture in the engagement scope
4. Note: model structure (table names, relationships, measure definitions, M code) is what AI needs — not row-level data

## Phase 2 — AI Investigation (30–60 minutes)

Run Claude + MCP with deliberately open framing:

> *"Inspect this semantic model and tell me anything that structurally questionable, performance-risky, or business-logic suspicious. Don't make assumptions about correctness — flag what catches your attention."*

Claude will systematically scan:
- Measure definitions for inconsistencies across namespaces
- Relationships for unexpected cross-filtering or cardinality issues
- Power Query M code for data quality anomalies
- Calculated columns vs measures for modelling appropriateness

For focused engagements, use a targeted prompt:
> *"Look at the [specific table] and related dimensions. Flag any data quality concerns, modelling concerns, or anomalies."*

## Phase 3 — Human Validation (ongoing)

For every AI flag, apply the **conversation trigger** protocol:

```
AI flag → Ask "Is this real, and if not, why does the data look this way?"
         → The question surfaces the real risk (may be unrelated to AI's proposed cause)
         → Document the finding with root cause
         → Do NOT treat AI's proposed cause as the conclusion
```

**For mature models:** AI serves as a validation pass — compare AI findings against your own audit conclusions. Convergence = stronger signal. Divergence = investigate.

## Output Structure

| Section | Content |
|---------|---------|
| Trust disclosures | What data left the environment, where, and who approved |
| AI findings | Flags grouped by type (structural, performance, naming, data quality) |
| Human validation | Per-flag: real / false positive / conversation trigger |
| Model maturity assessment | Discovery tool vs confirmation tool (based on what AI found) |
| Recommendations | Actionable items from validated findings only |

## When MCP Adds Most Value

| Model Characteristic | MCP Value |
|---------------------|-----------|
| 50+ measures, multiple authors | High — cross-namespace matching finds buried inconsistencies |
| New analyst onboarding | High — AI catches what the previous audit missed |
| Pre-Fabric migration review | High — surfaces architectural risks before migration |
| Mature model by experienced team | Medium — serves as independent validation layer |
| Small single-author model | Low — human review is sufficient |

## Model Maturity Rule

> **For a junior analyst's first model: AI is a discovery tool.**
> **For an experienced practitioner's review of mature work: AI is a confirmation tool.**
> Both are useful. They are just different uses.

## Related

- [[ai-assisted-audit-vs-manual-audit]] — combining AI and human strengths
- [[ai-cross-namespace-pattern-matching]] — AI's strongest use case
- [[ai-flag-as-conversation-trigger]] — how to handle every AI flag
- [[mcp-power-bi-modeling-preview-caveats]] — preview constraints and trust requirements
