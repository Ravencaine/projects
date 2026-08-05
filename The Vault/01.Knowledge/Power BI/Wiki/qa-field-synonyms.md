---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [qa-visual, synonyms, exclusions, qa-setup, terminology]
---

# Q&A Field Synonyms — Adding and Excluding Terms

The Q&A Setup pane lets you map business terms to data model fields and exclude ambiguous words.

## Purpose

Users ask questions using business language ("revenue", "turnover", "total sales"). The data model uses technical language ("TotalSalesAmount"). Synonyms bridge the gap.

## Synonym Types

| Type | Effect |
|------|--------|
| **Include term** | Maps a word/phrase to a field (e.g., "revenue" → TotalSalesAmount) |
| **Exclude term** | Prevents a word from mapping to a field (e.g., exclude "sales" from mapping to UnitPrice) |

## Steps in Power BI Desktop

1. Click the Q&A visual
2. Settings (⚙) → Set up Q&A
3. Select the field to add a synonym for
4. Add terms to the Synonyms box (comma-separated)
5. Add exclusions if needed (Exclude box)

## Examples

| Field | Include | Exclude |
|-------|--------|--------|
| TotalSalesAmount | revenue, turnover, sales, income | — |
| UnitPrice | price, unit price | — |
| SalesUnits | units, quantity sold | — |

## Notes

- Synonyms are stored with the model and persist when published
- Too many synonyms for the same field can cause ambiguity — use exclusions to disambiguate
- Test synonyms by typing the question in the Q&A visual after saving

## Related

- [[qa-best-practices]]
- [[qa-visual-power-bi]]
- [[semantic-matching-qa-visual]]
