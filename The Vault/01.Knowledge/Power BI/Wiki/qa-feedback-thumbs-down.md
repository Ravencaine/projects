---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [qa-visual, feedback, thumbs-down, correction, synonym]
---

# Q&A Feedback — Thumbs Down Correction

End users can correct Q&A answers directly from the visual using a thumbs-down button — the analyst then maps the correction in Q&A Setup.

## Purpose

When a user gets a wrong answer, the thumbs-down button logs the correction intent. The analyst uses the logged feedback to add synonyms or rename fields.

## Steps

### User Side

1. User types a question in Q&A
2. Gets a visualisation they believe is wrong
3. Clicks the thumbs-down icon below the answer
4. Types the correct interpretation (e.g., "I meant total revenue, not unit count")

### Analyst Side

1. Open Q&A Setup → Q&A Suggestions
2. Find the feedback entry
3. Add the term as a synonym to the correct field
4. Republish the report

## Key Points

- The thumbs-down does not fix the answer automatically — it surfaces the correction for analyst review
- Corrections are surfaced in Q&A Setup → Q&A Suggestions
- This is the most direct user-driven improvement mechanism for Q&A

## Related

- [[qa-review-questions-feedback-loop]]
- [[qa-field-synonyms]]
- [[qa-best-practices]]
