---
created: 2026-08-10
updated: 2026-08-10
source: ChatGPT Thinks. Copilot Builds. Power BI Proves.
source_url: https://medium.com/@Jamesabryant/chatgpt-thinks-copilot-builds-power-bi-proves-827a505d5b36
note_type: pattern
tags: [dax, firstdate, lastdate, improvement, percent-change, trend, athlete-analytics]
---

# Endurance Improvement: FIRSTDATE + LASTDATE Percentage Change

Compare an entity's first recorded value against its most recent value, then return the percentage improvement. A useful pattern for any scenario where you want to track individual progress over time.

## The Pattern

```dax
Endurance Improvement (%) =
VAR FirstEndurance =
    CALCULATE(
        AVERAGE('AthletePerformance'[Endurance (min)]),
        FIRSTDATE('AthletePerformance'[Date])
    )
VAR LastEndurance =
    CALCULATE(
        AVERAGE('AthletePerformance'[Endurance (min)]),
        LASTDATE('AthletePerformance'[Date])
    )
RETURN
    DIVIDE(LastEndurance - FirstEndurance, FirstEndurance) * 100
```

## How It Works

- `FIRSTDATE()` returns the first date in the current filter context — the earliest recorded event for the selected entity
- `LASTDATE()` returns the last date — the most recent
- `CALCULATE(..., FIRSTDATE(...))` applies context transition so it returns values from the first date
- `DIVIDE(a - b, b) * 100` gives the percentage improvement from first to last

## Limitations and Edge Cases

This pattern makes assumptions that may not hold:

1. **ALL records vs one entity:** If the visual shows all athletes at once, `FIRSTDATE()` / `LASTDATE()` operate over all records, not per-athlete. Wrap in an `ITERATOR` (SUMX) or use `FILTER` to iterate per entity.

2. **First event ever vs first in filter period:** Should the baseline reset when a time filter is applied? Or always use the entity's lifetime first record?

3. **Blank first value:** If `FirstEndurance` is BLANK or zero, `DIVIDE` returns BLANK — may silently hide data. Guard with `IF(FirstEndurance = 0 || ISBLANK(FirstEndurance), BLANK(), ...)`.

4. **Compare to previous period instead:** First-to-last measures growth from an arbitrary start. Some use cases need comparison to the previous month or quarter, not the earliest record.

5. **One-time event vs time series:** Works best with regular time-series data. Single-event snapshots produce meaningless percentages.

## The ChatGPT Review Prompt

After drafting this measure, ask:
*Explain this DAX formula in plain language. What assumptions does it make, and how could it produce misleading results?*

This surfaces the edge cases the measure author may have missed.

## Related

- [[Time-Intelligence-Functions-Reference]] — overview of FIRSTDATE, LASTDATE, and related time functions
- [[DIVIDE-Safe-Division-Reference]] — safe division with BLANK handling
- [[Two-Layer-AI-Workflow-ChatGPT-Copilot-Power-BI]] — using ChatGPT to challenge DAX assumptions before deployment
