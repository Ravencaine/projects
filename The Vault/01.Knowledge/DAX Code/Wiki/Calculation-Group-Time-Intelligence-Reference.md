---
created: 2026-08-10
updated: 2026-08-10
source: Calculation Groups for YoY, MoM & QoQ in Power BI — Powerful, but Maybe Not Worth It?
source_url: https://medium.com/microsoft-power-bi/calculation-groups-for-yoy-mom-qoq-in-power-bi-powerful-but-maybe-not-worth-it-86d996dbd471
note_type: pattern
tags: [dax, calculation-groups, selectedmeasure, dateadd, time-intelligence, mom, qoq, yoy]
---

# Time Intelligence via Calculation Groups — SELECTEDMEASURE() + DATEADD

Calculation groups eliminate the need for separate YoY/MoM/QoQ measures per KPI. One base measure per KPI; one calculation group for all time shifts. `SELECTEDMEASURE()` captures whichever measure the visual is rendering, and `DATEADD()` shifts the date context.

## Calculation Items

```dax
Current =
    SELECTEDMEASURE()

MoM =
VAR Prev =
    CALCULATE(
        SELECTEDMEASURE(),
        DATEADD('Dates'[Date], -1, MONTH)
    )
RETURN
    SELECTEDMEASURE() - Prev

QoQ =
VAR Prev =
    CALCULATE(
        SELECTEDMEASURE(),
        DATEADD('Dates'[Date], -1, QUARTER)
    )
RETURN
    SELECTEDMEASURE() - Prev

YoY =
VAR Prev =
    CALCULATE(
        SELECTEDMEASURE(),
        DATEADD('Dates'[Date], -1, YEAR)
    )
RETURN
    SELECTEDMEASURE() - Prev
```

## Pair with a Field Parameter

Use a **field parameter** for KPI selection (what to analyze) and the **calculation group** for time comparison (how to compare it). This combination — parameter + calculation group — is the most powerful pattern for flexible reporting.

```
Field Parameter:  [Burnout Risk] , [Absence Rate] , [Flight Risk Index] ...
Time Calc Group:  [Current] , [MoM] , [QoQ] , [YoY]
```

The visual shows one value at a time; users switch both KPI and time perspective via slicers.

## Limitations

- Calculation groups apply to all measures in the visual, including color measures and formatting labels — guard with `ISNUMBER(SELECTEDMEASURE())`
- Conditional formatting becomes fragile under calculation group context
- Requires Premium (AS/Tabular) for full authoring

## Related

- [[ISNUMBER-SelectedMeasure-Guard-Pattern]] — defensive guard for non-numeric measures
- [[SAMEPERIODLASTYEAR-YoY-Pattern]] — standalone YoY without calculation groups
- [[Time-Intelligence-Functions-Reference]] — full time intelligence function catalog
