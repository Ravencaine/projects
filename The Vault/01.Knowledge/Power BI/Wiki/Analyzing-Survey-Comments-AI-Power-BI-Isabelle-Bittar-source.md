---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
source_url: https://medium.com/the-bi-corner/analyzing-survey-comments-in-power-bi-using-ai-ea0ca35ff98b
note_type: source
tags: [power-bi, gpt-4, sentiment-analysis, python, openai, survey, csv, text-analysis]
---

# Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)

End-to-end workflow: Python/GPT-4 enrichment (theme extraction + sentiment scoring) → Power BI interactive dashboard. Includes Colab notebook, PBIX with SVG sentiment icons, cost analysis.

> **Type:** article + Colab notebook + PBIX
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-07-12
> **URL:** https://medium.com/the-bi-corner/analyzing-survey-comments-in-power-bi-using-ai-ea0ca35ff98b
> **Colab:** https://colab.research.google.com/drive/1Z59S89qWHEcy4JcqqSZRKXbzT_lrhM90
> **PBIX:** [Survey_Comments_AI_Power_BI.pbix](file:///C:/Users/krlsa/Documents/00%20Projects/The%20Vault/99.System/Attachments/Survey_Comments_AI_Power_BI.pbix) (440 KB)
> **Routed to:** Power BI, DAX Code

## Summary

Isabelle Bittar demonstrates using GPT-4 to enrich raw survey free-text comments — extracting 12–15 themes, tagging each comment, and scoring sentiment 1–5 — then building a fully interactive Power BI dashboard with theme overview, sentiment distribution, trend analysis, and search. Key DAX patterns: `AVERAGE(SentimentScore)`, `SWITCH(TRUE(), ...)` with `REPT(UNICHAR(8203), n)` for sortable custom sentiment labels. Cost: $2.99 for ~500 comments via ChatGPT API.

## Key Claims

- Word clouds are insufficient for executive survey summaries — structured themes + sentiment scores are far more actionable
- GPT-4 can reliably extract 12–15 domain-relevant themes from a corpus of open-ended survey comments
- Theme tagging and sentiment scoring per comment requires one GPT-4 call per comment (batch-extract themes first, then tag individually)
- GPT-4 API with temperature=0.3 for theme extraction, temperature=0 for sentiment scoring
- `REPT(UNICHAR(8203), n)` creates zero-width spaces for sorting non-numeric text columns in Power BI visuals
- SVG conditional formatting on a table column can display sentiment as colour-coded icons without a custom visual

## Notable Details

- Colab notebook uses `openai>=1.0`, `pandas`, `openpyxl`, `tqdm`
- GPT-4 rather than GPT-4o — deliberately chosen for this use case
- CSV output columns: Comment, Theme, SentimentScore (1–5 integer)
- Sentiment labels: Very Negative / Slightly Negative / Neutral / Slightly Positive / Positive
- SWITCH thresholds: >4 = Positive, >3.2 = Slightly Positive, >2.8 = Neutral, >1.5 = Slightly Negative, ≤1.5 = Negative
- PBIX includes example visuals: Theme Overview table, donut chart, bar chart, line trend, search slicer, detailed answers table

## Related Notes

Links to notes derived from this source:

- [[Python-GPT4-Survey-Enrichment-Workflow]] — `atomic` — Colab notebook workflow: install, auth, theme extraction, tagging, scoring, export
- [[SWITCH-REPT-UNICHAR-Custom-Sorting]] — `atomic` — REPT(UNICHAR(8203)) zero-width space sorting trick in DAX
- [[Survey-Sentiment-Scorecard]] — `atomic` — AVERAGE(SentimentScore) + SWITCH measure for sentiment classification
- [[Survey-AI-Dashboard-Components]] — `atomic` — Power BI dashboard sections: theme overview, sentiment distribution, trends, search, detailed table
- [[REPT-UNICHAR-Measure-Sorting-Isabelle]] — `reference` — Isabelle's Medium article on custom measure sorting
- [[GPT4-API-Survey-Cost]] — `atomic` — $2.99 for ~500 comments, cost factors, ROI vs manual tagging
- [[Author-Isabelle-Bittar]] — `author` — Isabelle Bittar, KI Data Science (4 sources)
