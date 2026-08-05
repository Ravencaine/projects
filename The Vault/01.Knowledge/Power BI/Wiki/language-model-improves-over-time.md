---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [language-model, qa-visual, learning, child-analogy, continuous-improvement]
---

# Language Model Improves Over Time — Child Learning Analogy

A language model's accuracy improves through exposure — just as a child learns vocabulary from context and correction.

## Definition

The Q&A visual's language model starts with general English vocabulary and domain knowledge. Through two mechanisms, it improves:

1. **Synonym additions**: the analyst maps domain-specific terms
2. **User corrections**: thumbs-down feedback adds new mappings

## The Child Learning Analogy

A child first learns "food" broadly. Through correction ("that's not food, that's a toy") and context, they learn the specific category. The Q&A model works the same way: "sales" might initially map to the wrong field, but correction and synonym addition teach it the right mapping.

## Key Points

- The model starts **general** and becomes **specific** through correction
- Without correction and synonym additions, Q&A stays at general English accuracy
- The most valuable additions are **domain-specific terms** not in general English vocabulary
- The model remembers synonym mappings across sessions — improvements persist on republish

## What Improves Accuracy Most

| Action | Impact |
|--------|--------|
| Human-readable column names | High |
| Explicit synonyms | High |
| User corrections via thumbs-down | Medium |
| Review Questions feedback | Medium |
| Adding Q&A suggestions | Low |

## Related

- [[qa-visual-power-bi]]
- [[qa-field-synonyms]]
- [[qa-review-questions-feedback-loop]]
