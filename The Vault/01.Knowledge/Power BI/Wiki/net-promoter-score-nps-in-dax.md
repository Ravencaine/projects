---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, marketing, nps, customer-satisfaction, survey]
note_type: pattern

---

# Net Promoter Score (NPS) in DAX

Measuring customer loyalty using survey response data.

## NPS Formula

```
NPS = % Promoters - % Detractors
```

Where:
- Promoters: score 9-10
- Passives: score 7-8
- Detractors: score 0-6

## DAX Pattern

```dax
Total Responses := COUNTROWS( 'Survey' )

% Promoters :=
DIVIDE(
    COUNTROWS( FILTER( 'Survey', 'Survey'[Score] >= 9 ) ),
    [Total Responses]
)

% Detractors :=
DIVIDE(
    COUNTROWS( FILTER( 'Survey', 'Survey'[Score] <= 6 ) ),
    [Total Responses]
)

NPS :=
( [% Promoters] - [% Detractors] ) * 100
```

## Notes

- NPS ranges from -100 to +100
- Zero or above is generally acceptable
- Segment by product, region, or time period for insights

## Related

- [[value_add]]
- [[employee-satisfaction-in-dax]]
