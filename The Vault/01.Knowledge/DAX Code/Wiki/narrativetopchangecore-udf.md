---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, kpi, narrative, insight, text, formatting, power-bi]
---

# NarrativeTopChangeCore — KPI Narrative Formatter

Core formatter for the [[kpi-narrative-text-udf-pattern]]. Finds the extreme variance across a dimension, optionally attributes to a sub-dimension, and formats as an insight string.

## Signature

```c
UDF NarrativeTopChangeCore =
    ( varianceExpr : AnyRef expr,
      shareCutoff  : NUMERIC,
      risePrefix   : STRING,
      dropPrefix   : STRING,
      metricName   : STRING,
      dimLabelSing : STRING,
      attrLabelSing: STRING,
      mode         : STRING,   // "RISE" or "DROP"
      dimAll  : TABLE,
      attrAll : TABLE,
      dimName : STRING,
      attrName: STRING
    ) => ...
```

## Parameters

| Param | Purpose |
|-------|---------|
| `varianceExpr` | Measure/column returning % or numeric variance |
| `shareCutoff` | If top attribution ≥ this fraction of total, say "mainly on" |
| `risePrefix` | Text prefix for rises (e.g., `"🔺 Biggest rise in "`) |
| `dropPrefix` | Text prefix for drops |
| `metricName` | Name to insert in the narrative |
| `dimLabelSing` | Singular label for dimension (e.g., `"unit"`) |
| `attrLabelSing` | Singular label for attribution (e.g., `"shift"`) |
| `mode` | `"RISE"` or `"DROP"` |

## Output Shape

```
[Prefix][Metric]: [DimMember] [±pct] — [mainly on/spread across] [AttrMember] ([±pct])
```

## Related

- [[kpi-narrative-text-udf-pattern]]
