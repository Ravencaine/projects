---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: atomic
tags: [dax, average, switch, sentiment, score, survey, rept, unichar, classification]
---

# Survey Sentiment Scorecard: `AVG + SWITCH`

Two DAX measures that take the `SentimentScore` column (1–5 integer, output from the GPT-4 Python enrichment workflow) and produce a numeric average and a human-readable classification label with correct sort order.

## Measure 1: Average Sentiment Score

```dax
Sentiment score = AVERAGE(Comments[SentimentScore])
```

Returns the mean of all `SentimentScore` values in the current filter context. Automatically respects slicers and cross-filters — e.g., filtering to a specific theme shows average sentiment for that theme only.

## Measure 2: Sentiment Classification (Sortable)

```dax
Sentiment value =
    SWITCH(
        TRUE(),
        [Sentiment score] > 4,
            REPT(UNICHAR(8203), 5) & "Positive",
        [Sentiment score] > 3.2,
            REPT(UNICHAR(8203), 4) & "Slightly Positive",
        [Sentiment score] > 2.8,
            REPT(UNICHAR(8203), 3) & "Neutral",
        [Sentiment score] > 1.5,
            REPT(UNICHAR(8203), 2) & "Slightly Negative",
        REPT(UNICHAR(8203), 1) & "Negative"
    )
```

Returns a text label with zero-width space prefix for correct alphabetical sort order.

## Threshold Rationale

| Threshold | Label | Reasoning |
|-----------|-------|-----------|
| > 4.0 | Positive | Strong positive feedback |
| > 3.2 | Slightly Positive | Above neutral, leaning positive |
| > 2.8 | Neutral | Near centre of 1–5 scale |
| > 1.5 | Slightly Negative | Below neutral but not severely negative |
| ≤ 1.5 | Negative | Significant negative sentiment |

Thresholds are asymmetrical around 3 (neutral) because the GPT-4 scale tends to skew positive — adjust based on your corpus's actual distribution.

## Cross-Filter Behaviour

Both measures respect Power BI's filter context:

| Slicer selection | `Sentiment score` result | `Sentiment value` result |
|-----------------|------------------------|------------------------|
| No filter | Average across all comments | Overall classification |
| Theme = "Speed" | Average for Speed theme only | Classification for Speed |
| Date = "November" | Average for November only | Classification for November |

## Display in Visuals

| Visual | Measure | Purpose |
|--------|---------|---------|
| Card | `Sentiment score` | Numeric average (e.g., 3.7) |
| Table column | `Sentiment value` | Sortable text label (e.g., "Slightly Positive") |
| Donut chart | `Sentiment value` (by count) | Distribution of sentiment labels |
| Bar chart | `Sentiment score` by Theme | Average sentiment per theme |

## Related

- [[SWITCH-REPT-UNICHAR-Custom-Sorting]]
- [[Python-GPT4-Survey-Enrichment-Workflow]]
- [[Survey-AI-Dashboard-Components]]
