---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: pattern
tags: [dax, udf, kpi, narrative, insight, text, power-bi]
---

# KPI Narrative Text UDF Pattern

Generates auto-insight narrative text for KPI cards (e.g., "🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)"). Standardizes the "voice" of KPI narratives across reports.

## Architecture

```
NarrativeTopChangeCore  → core formatter (no columns)
  ↕ callbacks
NarrativeTopChange_UnitShift  → wrapper: Units × Shifts
NarrativeTopChange_ProductRegion  → wrapper: Product × Region
```

The core controls thresholds and wording; wrappers bind dimension/attribution columns.

## How It Works

1. Finds the dimension member with the extreme variance (max for rise, min for drop)
2. Optionally attributes to a sub-dimension if it explains ≥ `shareCutoff` (e.g., 60%) of the variance
3. Formats: `🔺 [Prefix]: [DimMember] [±pct] — mainly on [AttrMember] ([±pct])`

## Usage

```c
OT Hours per FTE Variance % :=
    DIVIDE(
        [OT Hours per FTE] - [OT Hours per FTE PrevWeek],
        [OT Hours per FTE PrevWeek]
    )

Biggest Rise (Narrative) := NarrativeTopChange_UnitShift(
    [OT Hours per FTE Variance %],
    0.60,                        // shareCutoff
    "🔺 Biggest rise in ",       // risePrefix
    "🔻 Biggest drop in ",       // dropPrefix (not used)
    "OT/FTE",                    // metricName
    "RISE"                       // mode
)
```

## Output Examples

- `🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)`
- `🔻 Biggest drop in Gross Margin %: Widgets −3.1% — spread across regions (top: West −1.4%)`

## Config

`// 🔧 BIND` — change dimension/attribution tables and column names inside each wrapper.

## Related

- [[narrativetopchangecore-udf]]
- [[humanize-udf-short-scale-number-formatting]] — for number formatting in narratives
