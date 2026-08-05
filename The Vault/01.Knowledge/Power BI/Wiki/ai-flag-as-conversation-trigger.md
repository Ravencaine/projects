---
created: 2026-08-01
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught - and What It Got Wrong.md"
note_type: atomic
tags: [power-bi, ai, false-positive, conversation, audit, critical-thinking]
---

# AI Flag as Conversation Trigger

Every AI audit flag should be treated as a question, not an answer. The question the flag generates is almost always more valuable than the flag itself.

## The Pattern

Claude flagged a 1.2% inventory gap and proposed it was a missing Power Query adjustment record. The analytics lead investigated. The gap was real — but the cause was completely different: intra-day stock transfers between distribution centres not reflected in the daily snapshot. This was known to the business, handled manually, and never documented.

The wrong response would have been to spend a week looking for a Power Query bug. The right response was to ask "is this real, and if not, why does the data look this way?"

That question revealed two things the standard audit would not have surfaced:
1. The manual reconciliation process was one person's undocumented responsibility — that person was planning to retire within 12 months
2. The Fabric migration the client was evaluating would change snapshot timing, exposing the 1.2% gap in ways the current architecture had absorbed

The "false positive" became the most valuable finding of the engagement.

## The Rule

> **False positives are not failures if they generate the right next question.**

An AI flag that points at nothing still generates a question. That question may surface a real risk that was unrelated to what AI proposed — but would never have been asked in a standard manual audit.

## What This Means for Audit Practice

| AI Flag Response | Value |
|----------------|-------|
| Treat as conclusion → act on the proposed cause | Wasted effort, possible misdiagnosis |
| Treat as trigger → ask "is this real, and why?" | Surfaces real risks regardless of AI's proposed cause |

## The Meta-Pattern

The best use of AI in audit is not "AI finds bugs." It is "AI surfaces questions I wasn't going to ask." The questions compound. The flags themselves are just the entry point.

## Related

- [[ai-assisted-audit-vs-manual-audit]] — human judgment interprets what AI flags
- [[ai-cross-namespace-pattern-matching]] — where AI flags come from
- [[power-bi-mcp-audit-workflow]] — workflow that treats flags as triggers
