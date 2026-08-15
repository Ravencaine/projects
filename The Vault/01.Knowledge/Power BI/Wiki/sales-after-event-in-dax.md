---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, marketing, event, lift, attribution]
note_type: pattern

---

# Sales After Event in DAX

Measuring sales uplift in the period following a marketing event.

## Pattern

```dax
Sales After Event :=
VAR __EventDate = MAX( 'Events'[Date] )
VAR __WindowStart = __EventDate
VAR __WindowEnd = __EventDate + 30
RETURN
SUMX(
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Date] >= __WindowStart
        && 'Dates'[Date] <= __WindowEnd
    ),
    [Sales Amount]
)

Sales Before Event :=
VAR __EventDate = MIN( 'Events'[Date] )
VAR __WindowStart = __EventDate - 30
VAR __WindowEnd = __EventDate - 1
RETURN
SUMX(
    FILTER(
        ALL( 'Dates' ),
        'Dates'[Date] >= __WindowStart
        && 'Dates'[Date] <= __WindowEnd
    ),
    [Sales Amount]
)

Lift :=
DIVIDE( [Sales After Event] - [Sales Before Event], [Sales Before Event] )
```

## Notes

- Adjust the window (30 days above) based on the event type
- Use for marketing attribution analysis

## Related

- [[customer-lifetime-value-ltv-dax]]
- [[net-promoter-score-nps-dax]]
