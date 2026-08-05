---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
note_type: atomic
tags: [power-bi, ai, mcp, measure-quality, naming-consistency, cross-namespace]
---

# AI Cross-Namespace Pattern Matching

AI's strongest current use case in semantic model auditing: finding structural inconsistencies across the full model namespace that humans miss due to fatigue, familiarity, or narrow spot-checking.

## The Problem

Large semantic models accumulate similarly-named but differently-defined measures over time — different analysts add measures to different reports, use slightly different filter contexts, and never compare them. When two measures with similar names produce different numbers for the same period, it causes confusion and erodes trust in the data.

Human auditors spot this by chance. They check what they expect to find. After hours of auditing, familiarity bias and fatigue narrow the scope of what gets compared. AI has no familiarity bias and no fatigue.

## The Mechanism

Claude + MCP reads:
- Every measure definition
- Every relationship
- Every Power Query M script

Then systematically compares structural patterns across the namespace — flagging measures that share names, prefixes, or semantic intent but differ in filter context, aggregation logic, or dimension scope.

## Real Example

Manufacturing client: 80 measures. Human auditor had reviewed the executive dashboard measures. Claude flagged two measures — "Net Revenue" and "Net Revenue (Final)" — that had the same apparent purpose but different filter contexts. The second measure had a filter removed by a new analyst who couldn't find the original and built a replacement without realising it was structurally different. Both measures were in active production use. Regional managers had been seeing inconsistent revenue figures for months.

Claude caught it because it compared all 80 measures systematically. A human would have needed to specifically look for this pattern.

## When It Works Best

| Model Characteristic | AI Value |
|---------------------|----------|
| Many measures (50+) | High — more surface area for inconsistencies |
| Multiple contributors over time | High — naming conventions drift |
| Complex calculated column / measure layering | Medium — structural differences are harder to compare |
| Small, single-author model | Low — namespace is small enough for human review |

## Limitations

Cross-namespace matching finds structural inconsistency but cannot determine which definition is "correct" — that requires business context. AI flags the symptom; human judgment interprets it.

## Related

- [[ai-assisted-audit-vs-manual-audit]] — where AI and human strengths differ
- [[ai-flag-as-conversation-trigger]] — what to do with the flag
- [[power-bi-mcp-audit-workflow]] — full workflow
