---
created: 2026-08-09
updated: 2026-08-09
source: "Document Power BI Dataflows Gen1 with Copilot Cowork (Before You Migrate).md"
note_type: atomic
tags: [power-bi, copilot-cowork, skill, quality-report, score, validation, atomic]
---

# CoWork Skill Quality Report

**Type:** Atomic · **KB:** Power BI · **Source:** [[Source-Document-Dataflows-Gen1-CoWork]]

CoWork generates a quality report for every skill it creates. The report scores the skill on four criteria and produces an overall score out of 100. A publish bar of 70 separates production-ready skills from those needing work.

## Quality report criteria

| Criterion | What it measures |
|-----------|----------------|
| **Timing** | Operates at the right pace — not too fast, not too slow |
| **Lanes** | Stays within its defined scope; does not overstep |
| **Surprise handling** | Handles unexpected inputs or edge cases safely |
| **Crowning / convergence** | Completes reliably; reaches a valid result |

## Scoring

- **Overall score:** 0–100
- **Publish bar:** 70
- Skills scoring **below 70** should not be published
- Individual criteria scores visible in the technical details view

## Example from this workflow

- **Skill:** Dataflow Documentation Skill
- **Score:** 96/100
- **Publish bar:** 70
- **Risk:** Medium
- **Result:** Passed — published

## What affects the score

Skills score higher when:
- Instructions are precise and unambiguous
- Guardrails are explicit about what NOT to do
- Input/output expectations are clear
- Edge cases are handled (no-JSON scenario, malformed input)
- The skill confirms outputs before declaring completion

## Accessing the quality report

After CoWork drafts a skill:
1. Click **Skill quality report** in the CoWork interface
2. Review the four individual criterion scores
3. Check the overall score against the 70 publish bar
4. Review technical details for per-criterion breakdowns

## Related

- [[CoWork-Skill-Guardrails]] — how to write guardrails that score well
- [[Skill-Guardrails-Design-Workflow]] — step-by-step guardrail design
- [[CoWork-vs-Copilot-Agent]] — why built-in validation matters
