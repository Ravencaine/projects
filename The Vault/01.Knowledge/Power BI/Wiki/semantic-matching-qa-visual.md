---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [semantic-matching, qa-visual, synonyms, relationships, nlp]
---

# Semantic Matching in the Q&A Visual

Q&A maps question words to data model fields using synonyms, relationships, and context — not exact string matching.

## Definition

Semantic matching is the process of mapping words in a user's question to the correct table, column, and measure in the data model. It goes beyond exact string matching: "revenue" maps to "TotalSalesAmount" if a synonym is defined, and "total sales" maps to the SUM aggregation of that column.

## Key Points

- The Q&A engine builds a **semantic model** of the data at publish time
- It uses:
  - **Column and table names** (direct matches)
  - **Synonyms** (defined in the Q&A suggestions pane)
  - **Relationship context** (navigation paths between tables)
  - **Aggregation conventions** ("total" → SUM, "average" → AVERAGE)
- **Underline states** indicate matching confidence:
  - `revenue` (single underline) = understood
  - `rev` (dashed underline) = uncertain
  - `revnue` (wavy underline) = not understood

## Implications

- Human-readable column names improve Q&A accuracy more than any other single change
- Adding synonyms is the most effective way to handle business terminology (e.g., "revenue" = "total sales" = "turnover")
- Q&A respects model relationships — a question about "revenue by region" works only if Region and Revenue are linked in the model

## Related

- [[qa-visual-power-bi]]
- [[qa-best-practices]]
- [[qa-field-synonyms]]
- [[qa-underline-states]]
