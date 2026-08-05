---


title: "KPI Design in PowerPivot"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, dax, kpi, pattern]
note_type: pattern
description: "Creating KPIs in PowerPivot — calculated field as base, goal threshold, status indicators (green/yellow/red). From Dunlop Chapter 7."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# KPI Design in PowerPivot

A Key Performance Indicator (KPI) compares a calculated field (the **Actual** value) against a **Target** (absolute value, field, or threshold). Status shown as green/yellow/red.

## Step-by-Step: KPI in PowerPivot

### 1. Create the Base Calculated Field

```dax
Average of Profit/Sales := AVERAGE( 'Sales'[Profit/Sales] )
```

This becomes the **indicator value**: what is being measured.

### 2. Create the KPI

```
Right-click the calculated field → Create KPI
```

### 3. Set Thresholds

| Threshold | Status | Meaning |
|-----------|--------|---------|
| Green (above 53%) | On target | Profit/Sales ≥ 53% |
| Yellow (40-53%) | Warning | Marginally acceptable |
| Red (below 40%) | Below target | Underperforming |

Sliders define the boundary values.

### 4. Display in Pivot Table

Drag the KPI field to Values → it automatically shows three columns:
- **Value**: the actual metric
- **Goal**: the target value
- **Status**: visual indicator (color)

## KPI Components

| Element | Description |
|---------|-------------|
| Indicator value | The calculated field being measured |
| Target type | Absolute value, another measure, or threshold |
| Status thresholds | Green/yellow/red boundaries |

## Source Reference

Chapter 7, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
