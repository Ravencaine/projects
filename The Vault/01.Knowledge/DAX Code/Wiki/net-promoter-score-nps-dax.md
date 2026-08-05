---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, customers, nps, survey, satisfaction]
---

# Net Promoter Score (NPS) in DAX

NPS® measures how likely customers are to recommend a product or service. Scores range from −100 to +100. Industry standard for customer loyalty.

## Purpose

NPS is a customer loyalty metric based on a single survey question: "How likely are you to recommend our product/service to others?" Responses are on a 0–10 scale categorized as:

- **Detractors** (0–6): unhappy customers who may damage reputation
- **Passives** (7–8): satisfied but unenthusiastic, vulnerable to competitors
- **Promoters** (9–10): enthusiastic advocates who drive growth

NPS = (% Promoters × 100) + (% Detractors × −100)

Result range: −100 (all detractors) to +100 (all promoters). Passive responses are neutral.

## Formula

```dax
NPS =
    VAR __Table = ALL( 'Promoters' )
    VAR __Total = COUNTROWS( __Table )
    VAR __Detractors =
        COUNTROWS(
            FILTER( __Table, [Score] <= 6 )
        )
    VAR __Promoters =
        COUNTROWS(
            FILTER( __Table, [Score] >= 9 )
        )
    VAR __PercDetractors = DIVIDE( __Detractors, __Total, 0 )
    VAR __PercPromoters = DIVIDE( __Promoters, __Total, 0 )
    VAR __Result = ( __PercPromoters - __PercDetractors ) * 100
    RETURN
        __Result
```

## Example Data (Deckler)

```dax
Promoters =
    SELECTCOLUMNS(
        ADDCOLUMNS(
            GENERATESERIES( 1, 10 ),
            "Score",
            SWITCH( TRUE(),
                MOD( [Value], 2 ) = 0, 10,
                [Value] = 3, 6,
                [Value] = 5, 7,
                9
            )
        ),
        "Response", [Value],
        "Score", [Score]
    )
```

This creates 10 responses: scores 10, 6, 10, 10, 7, 10, 10, 10, 10, 9. Result = 70.

## Components

| Component | Count | Formula |
|-----------|-------|---------|
| Total responses | 10 | COUNTROWS |
| Detractors (0–6) | 1 | [Score] <= 6 |
| Passives (7–8) | 1 | [Score] IN {7, 8} |
| Promoters (9–10) | 8 | [Score] >= 9 |
| % Detractors | 10% | 1/10 |
| % Promoters | 80% | 8/10 |
| NPS | 70 | (80% − 10%) × 100 |

## Notes

- ALL() ensures full table scan regardless of visual context
- SWITCH(TRUE(), ...) pattern for cascading IF conditions
- NPS is often tracked over time (monthly, quarterly) to identify trends
- Net Promoter and NPS are registered trademarks of Bain & Company and Fred Reichheld

## Related

- [[customer-churn-rate-dax]] — customer retention
- [[customer-lifetime-value-ltv-dax]] — customer value
