---
created: 2026-08-04
source: "Analyzing Survey Comments in Power BI Using AI.md"
source_url: "https://medium.com/the-bi-corner/analyzing-survey-comments-in-power-bi-using-ai-ea0ca35ff98b"
note_type: source
tags: [powerbi, llm, gpt-4, openai, survey-comments, text-analytics, sentiment-analysis, theme-tagging, python, ki-data-science]
---

# Analyzing Survey Comments in Power BI Using AI

A two-part walkthrough on enriching free-text survey comments with an LLM (GPT-4, via OpenAI Python client in Google Colab) — extracting themes, tagging each comment with a theme, scoring each comment's sentiment — then building an interactive 5-section Power BI dashboard from the enriched CSV.

> **Type:** article
> **Author:** [[Author-Isabelle-Bittar|Isabelle Bittar]] (KI Data Science)
> **Published:** 2025-07-12
> **Routed to:** Power BI

## Summary

Word clouds are an inadequate answer to "what are customers telling us?" in their open-ended survey responses. The author demonstrates a hybrid pipeline: a Python script powered by GPT-4 performs three jobs (extract themes, tag each comment with a theme, score sentiment on a 1–5 scale) and exports a tagged CSV; Power BI then visualises the enriched data via a 5-section dashboard with theme overview, sentiment distribution, trend over time, free-text search, and a detailed table.

## Key Claims

1. Three LLM calls per comment (one for theme, one for sentiment, one shared theme-extraction prompt across the corpus) deliver structured-enough output to drive a meaningful dashboard — total cost was $2.99 for the example run.
2. The two-pass theme approach (extract a closed theme list once from the corpus, then tag every comment against that list) gives consistent, comparable tag assignments — much better than asking GPT-4 to "tag each comment freely".
3. A 5-tier sentiment scale (Very Negative / Negative / Neutral / Slightly Positive / Positive) paired with `REPT(UNICHAR(8203), N)` sort-prefix lets Power BI show categorical sentiment with implied severity ordering — see [[rept-unichar-8203-zwsp]] for the underlying trick.
4. Dashboard cross-filtering + a free-text search box + a detailed comments table are the three tools that turn raw counts into an explorable story.
5. Hybrid architectures (Python outside Power BI for heavy cognitive lifting, Power BI inside for visualisation + interactivity) deliver more than either alone — and at surprising cost efficiency.

## Notable Details

- **Stack:** Google Colab + `openai` Python client (model: `gpt-4`), `pandas`, `tqdm`, `openpyxl`.
- **Three prompts, temperature choices:** theme extraction at `temperature=0.3` (some creativity for theme names), per-comment tagging at `temperature=0.3` (consistency, but some room to break ties), per-comment sentiment scoring at `temperature=0` (maximum determinism on a numeric scale).
- **Robustness:** every per-comment call is wrapped in `try/except` returning `"Error"` or `None` — failures don't crash the whole pipeline; they just leave blank rows in the output.
- **Final dataset:** `Comment`, `Theme`, `SentimentScore` (1–5) — three columns; original submission date is implicit by row order in the source CSV.
- **Two referenced sibling articles** Bittar links to from this one:
  - [Power BI: Elevating Data Visualization with Custom Measure Sorting](https://medium.com/microsoft-power-bi/power-bi-elevating-data-visualization-with-custom-measure-sorting-b368fd382917) — covered by the vault as [[rept-unichar-8203-zwsp]].
  - [Step Up Your Power BI Game With SVGs](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d) — covered by the vault as [[svg-visualizations-in-power-bi]].
- **Cost reference:** $2.99 USD per full survey run quoted in the article.
- A downloadable PBIX is offered at the end of the original article (Google Drive link, not archived here).

## Extracted Notes

- [[LLM-Survey-Enrichment-GPT4]] — pattern (the multi-call Python pipeline that exports a tagged CSV)
- [[GPT-4-Thematic-Coding]] — pattern (the prompt-engineering pattern: closed-set theme extraction then per-comment tagging; sentiment scoring with low temperature)
- [[OpenAI-API-Cost-Audit]] — atomic (concrete cost datum + the "cost vs human time" framing)
- [[Survey-Comments-Dashboard]] — workflow (the 5-section Power BI dashboard layout: Theme Overview / Sentiment Distribution / Trend Analysis / Search + Cross-Filtering / Details Table)

## Metadata

| Field | Value |
|-------|-------|
| Source file | Analyzing Survey Comments in Power BI Using AI.md |
| Archived at | (not yet archived — file remains in `00.Inbox/`) |
| Ingestion date | 2026-08-04 |
| Word count | ~2,200 |
