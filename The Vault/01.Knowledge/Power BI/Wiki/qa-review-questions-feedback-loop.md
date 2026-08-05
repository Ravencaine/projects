---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [qa-visual, review-questions, feedback, qa-setup, learning]
---

# Q&A Review Questions — Feedback Loop

The Q&A Setup pane's "Review Questions" feature shows what questions users have asked — enabling continuous improvement of the model.

## Purpose

After publishing a report with Q&A, users type questions. The Review Questions pane captures every asked question, showing which were answered correctly and which failed — giving the analyst a direct feedback loop.

## Components

| Status | Meaning |
|--------|---------|
| **Translated** | Q&A successfully answered this question |
| **Not translated** | Q&A could not parse or find a matching field |
| **Under review** | Analyst is evaluating the failure |

## Steps

1. In Power BI Service: open the report → Q&A visual → Settings ⚙ → Set up Q&A → Review Questions
2. See all questions users have asked since publishing
3. For failed questions:
   - **Add synonyms** to map the missing term
   - **Rename columns** to match user language
   - **Add missing relationships** if the question spans tables
4. Save changes — the model improves on next publish

## Key Points

- The feedback loop is what makes Q&A improve over time
- Review questions regularly (weekly/monthly) to catch new terminology users introduce
- Failed questions are a goldmine of domain-specific vocabulary that should be added as synonyms

## Related

- [[qa-best-practices]]
- [[qa-field-synonyms]]
- [[language-model-improves-over-time]]
