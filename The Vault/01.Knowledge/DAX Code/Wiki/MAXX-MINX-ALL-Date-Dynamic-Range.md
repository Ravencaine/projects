---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
note_type: atomic
tags: [dax, maxx, minx, all, remove-context, over-all, date, dynamic, range, y-axis, max-vital, min-vital]
---

# MAXX/MINX + ALL over Date for Dynamic Range

`MAXX(ALL('Vital Stats'[Date]), [Max Vital])` computes the overall maximum across all dates regardless of the current visual context. ALL strips the date filter; MAXX iterates over the resulting single-column table and returns the maximum measure value.

## Formula

```dax
Max Graph Area =
VAR _MaxVital =
    CALCULATE(
        MAXX(
            ALL('Vital Stats'[Date]),
            [Max Vital]
        )
    )
RETURN _MaxVital + 0.05 * _MaxVital

Min Graph Area =
VAR _MinVital =
    CALCULATE(
        MINX(
            ALL('Vital Stats'[Date]),
            [Min Vital]
        )
    )
RETURN _MinVital - 0.05 * _MinVital
```

## How It Works

| Step | Expression | Role |
|------|-----------|------|
| 1 | `ALL('Vital Stats'[Date])` | Removes all filters from Date; returns one row per unique date |
| 2 | `MAXX(ALL(...), [Max Vital])` | Iterates over each date row; evaluates [Max Vital] in that date's context; returns max |
| 3 | Outer `CALCULATE(...)` | Ensures the outer context (e.g. slicer selection) does not bleed into the range calculation |

## Why ALL over Date Column

The Y-axis needs a fixed range regardless of what dates are currently selected. Without ALL, MAXX would only see dates visible in the current context — the range would shrink when a date range is selected.

## MAXX vs MAX

| | MAXX | MAX |
|--|------|-----|
| Type | Iterator | Aggregator |
| Can use expressions | Yes | No |
| Works with measures | Yes | No |
| Context | Iterates a table/expression | Single column |

Use MAXX when you need to evaluate a **measure** (not just a column) across all values.

## Related

- [[Source-Oblique-Area-Chart-Native-Visuals-Isabelle-Bittar]] — source
- [[Measure-Type-Filter-Pattern]] — the [Max Vital] measure that MAXX evaluates
- [[Dynamic-Graph-Area-Buffer]] — uses this atomic to build the ±5% buffer pattern
