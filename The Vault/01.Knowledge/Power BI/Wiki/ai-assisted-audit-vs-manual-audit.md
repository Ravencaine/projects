---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
note_type: atomic
tags: [power-bi, ai, auditing, human-ai-collaboration, model-review]
---

# AI-Assisted Audit vs Manual Audit

AI and human auditors bring different failure modes to model reviews. Understanding which tool catches which class of issues is the foundation of using AI responsibly in BI audit workflows.

## What Humans Do Well

- **Contextual judgment:** Understanding why a business uses a particular measure definition
- **Interpretive flags:** Recognising when a number is wrong based on domain knowledge, not just pattern
- **Causal reasoning:** When AI flags an anomaly, humans determine whether the cause is a model bug, a data issue, or expected business behaviour
- **Threshold calibration:** Deciding what level of discrepancy warrants escalation

## What AI Does Well

- **Exhaustive scanning:** Reading every measure definition, every relationship, every M script without getting tired
- **Cross-namespace pattern matching:** Finding similarly-named measures that differ structurally — a human spots this by chance; AI finds it systematically
- **Consistency checking:** Comparing all instances of the same concept across the full model
- **Persistence:** The seventh hour of a manual audit is error-prone; AI applies the same scrutiny at hour 1 and hour 8

## The Failure Modes

| | Human | AI |
|--|-------|-----|
| Misses | Things not expected during long audits (tiredness, familiarity) | Correct-sounding but contextually wrong interpretations |
| Mistakes | Rushing, familiarity bias | False positives that point at real issues but with wrong causes |
| Strength | Judgment, context, causality | Coverage, consistency, pattern matching across namespaces |

## Practical Implication

The manufacturing client case: Claude caught two similarly-named measures ("Net Revenue" and "Net Revenue (Final)") that produced different numbers for the same period. Both were in active use across different reports. The inconsistency had been present for months because neither regional manager saw the other's report. A human auditor had missed it (80 measures, spot-checked the executive dashboard only). AI found it systematically.

The pharma case: Claude flagged a 1.2% inventory gap and proposed a Power Query bug. The gap was real but had a completely different cause (intra-day stock transfers not in the snapshot). AI was wrong about the mechanism but right to flag the surface-level anomaly. Human judgment determined the real risk.

## Rule

AI catches what humans miss after hour 7 of a manual audit. Humans catch what AI misinterprets. Neither replaces the other — the combination is stronger than either alone.

## Related

- [[ai-cross-namespace-pattern-matching]] — AI's strongest use case
- [[ai-flag-as-conversation-trigger]] — what to do with AI flags
- [[power-bi-mcp-audit-workflow]] — structured workflow combining both
