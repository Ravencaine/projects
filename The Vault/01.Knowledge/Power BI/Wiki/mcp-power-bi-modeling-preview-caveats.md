---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
note_type: atomic
tags: [power-bi, mcp, ai, preview, data-governance, trust, security]
---

# MCP Power BI Modeling Preview: Key Caveats

Microsoft's Power BI Modeling MCP server is in public preview. Using it for production audit work requires understanding what is and isn't supported, and what the trust model demands.

## What MCP Does

The Power BI Modeling MCP server connects an AI agent (Claude, etc.) directly to a Power BI semantic model via the XMLA endpoint. The agent can:
- List tables, columns, measures, and relationships
- Read measure definitions and Power Query M code
- Run DAX diagnostic queries against the model
- Inspect model structure without exporting .bim files

## Preview Constraints

- **Implementation may change** before general availability — prompts and workflows that work now may not work after the API stabilises
- **Not production-ready** for automated recurring audit workflows
- **Support boundaries unclear**: Microsoft documentation does not yet define the production support posture for MCP-derived findings
- **Not appropriate for production audit workflows** until GA with documented support commitments

## Data Governance Requirements

Using MCP requires a defensible trust posture before any engagement begins:

| Question | Required Answer |
|----------|----------------|
| Can model metadata be sent to the AI provider's API under your organisation's data policies? | Yes → direct use; No → sanitised copies only |
| Are you using a production or test workspace? | Test/reconstruction only for sensitive environments |
| Is any sensitive row-level data transmitted? | No — only model structure and measure definitions |
| Have you anonymised or masked sensitive identifiers? | Yes — customer names, account IDs, pricing details |
| Has the client approved this approach? | Explicit approval required for client-facing work |

## Trust Disclosure Template

When using AI-assisted auditing in client engagements, disclose:
1. What data leaves the organisation (model metadata only — no row-level data)
2. Where it goes (AI provider API)
3. Who can access it (governed by AI provider's own access controls)
4. What environment is used (sanitised copy, reconstructed model, or synthetic data)

## Bottom Line

MCP is a genuinely useful investigation tool in its current state. It is not ready for automated production audit pipelines. The trust disclosures are non-negotiable — without clear answers on data governance, the engagement does not proceed.

## Related

- [[power-bi-mcp-audit-workflow]] — structured workflow respecting these constraints
- [[ai-assisted-audit-vs-manual-audit]] — combining MCP with human judgment
