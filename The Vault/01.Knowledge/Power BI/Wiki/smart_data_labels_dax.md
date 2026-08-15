---
created: 2026-08-09
updated: 2026-08-09
source: 10 Ways to Instantly Improve Your Power BI Charts
note_type: pattern
tags: [data-labels, dax, minx, maxx, power-bi]
---

# Smart Data Labels DAX (Min/Max Highlight)

<!-- show data labels only on the maximum and minimum values in a chart using MAXX, MINX, and ALL -->

## Purpose

Display data labels on a chart only for the highest and lowest values (or anomalies) rather than all values. This guides attention to the extremes without cluttering the visual with redundant axis information.

## Components

- `MAXX` — iterate over a table expression and return the maximum value
- `MINX` — iterate over a table expression and return the minimum value
- `ALL` — remove filters from a table/column to calculate across the full context
- `IF` — return the measure value only when the current value equals max or min, otherwise BLANK

## Structure

```dax
Turnover Data Label =
VAR _MaxValue =
  MAXX(
    ALL('Turnover'[Department]),
    [Turnover Last 12 months]
  )
VAR _MinValue =
  MINX(
    ALL('Turnover'[Department]),
    [Turnover Last 12 months]
  )
RETURN
  IF(
    [Turnover Last 12 months] = _MaxValue || [Turnover Last 12 months] = _MinValue,
    [Turnover Last 12 months]
  )
```

## Example

1. Create the `Turnover Data Label` measure
2. Assign it to the Data labels property of the column chart
3. Enable data labels on the visual — the measure returns BLANK for all non-extreme values, so no label is shown
4. Only the department with the highest and lowest turnover rate display a label

## Variations

- Highlight latest period only: swap MAXX/MINX for `CALCULATE(MAX(...), PARALLELPERIOD(...))`
- Highlight anomalies: replace the IF condition with a test against the anomaly detection result
- Show delta from average: replace the RETURN value with `[Turnover Last 12 months] - AVERAGE(...)`

## Related

- [[smart_data_labels]]
- [[anomaly-detection-data-requirements]]
