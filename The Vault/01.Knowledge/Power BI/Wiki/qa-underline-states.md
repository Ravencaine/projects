---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [qa-visual, underline-states, understood, uncertain, unknown, reference]
---

# Q&A Underline States — What They Mean

Three underline styles in the Q&A text box indicate the model's confidence in matching each word to a data field.

## Quick Reference

| Underline | Style | Meaning | Action |
|-----------|-------|---------|--------|
| **Single** | `revenue` | Word is understood and mapped to a field | None — working correctly |
| **Dashed** | `revnue` | Partial match — the model is uncertain | Review synonyms; check for typos in column names |
| **Wavy** | `revn` | No match found — term is unknown | Add as a synonym or rename the column |

## When to Act

- **Dashed underline**: the model found a field but isn't confident. Check if there's a more direct synonym.
- **Wavy underline**: the model couldn't find a matching field at all. This question will likely fail. Add the term as a synonym or rename the underlying column.
- **Mixed underlines** (some words wavy, others single): the question is partially understood — address the wavy terms first.

## Related

- [[qa-field-synonyms]]
- [[semantic-matching-qa-visual]]
- [[qa-best-practices]]
