---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [qa-visual, power-bi, nlp, question-answering, natural-language]
---

# Q&A Visual in Power BI

A Power BI visual that accepts free-text questions and returns visualisations — no DAX, no drag-and-drop required.

## Signature

Power BI visual: Q&A (in the Visualizations pane)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Question box | text input | The natural language question |
| Suggested questions | text list | Pre-configured questions shown before typing |
| Q&A Setup | pane | Define synonyms, manage terminology |

## Returns

A visualisation (chart, table, card) generated from the question. If the engine cannot answer, it shows "I couldn't find an answer to that."

## Steps

1. Insert → Q&A visual
2. Type a question or click a suggested question
3. Review the underlined terms (single = understood, dashed = uncertain, wavy = unknown)
4. Adjust synonyms if the mapping is wrong
5. Save the Q&A setup when publishing

## Notes

- Works on published datasets in Power BI Service
- Requires the dataset to be published to a workspace (not just saved locally)
- Q&A suggestions (suggested questions) help guide users to supported queries

## Related

- [[semantic-matching-qa-visual]]
- [[qa-best-practices]]
- [[natural-language-processing-data-exploration]]
