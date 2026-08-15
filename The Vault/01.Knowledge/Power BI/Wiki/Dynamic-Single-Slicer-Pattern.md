---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Single Slicer using DAX logic.md"
note_type: pattern
tags: [power-bi, slicer, dynamic-slicer, disconnected-table, measures-table, selectedvalue, boniface-muchendu]
---

# Dynamic Single Slicer — DAX Measures Table Pattern

> **Type:** pattern
> **Routed to:** Power BI
> **Primary source:** Boniface Muchendu, Data Bear — 2022-10-30

## Problem

Multiple column slicers clutter a report. Users need to switch between different metrics (Sales Amount, Order Quantity, Unit Price, etc.) in a single visual without multiple slicers visible.

## Solution

Use a disconnected measures table + SELECTEDVALUE to create a single slicer that drives which metric is displayed.

## Pattern

```
┌─────────────────────────────────────────────┐
│  AllMeasuresTable (Enter Data)               │
│  ┌─────────────────┬───────┐               │
│  │ MeasureName     │ Index │               │
│  ├─────────────────┼───────┤               │
│  │ Sales Amount    │   1   │               │
│  │ Order Quantity  │   2   │               │
│  │ Unit Price      │   3   │               │
│  │ Freight         │   4   │               │
│  │ Total Cost      │   5   │               │
│  │ Standard Cost   │   6   │               │
│  └─────────────────┴───────┘               │
│                                             │
│  User selects from MeasureName slicer       │
│         ↓                                   │
│  SELECTEDVALUE(AllMeasuresTable[Index])     │
│         ↓                                   │
│  SWITCH on Index → shows corresponding      │
│  metric value in chart                      │
└─────────────────────────────────────────────┘
```

## DAX Pattern

```dax
-- Disconnected table: AllMeasuresTable
-- Columns: MeasureName (text), Index (integer)

-- Step 1: Individual aggregations per metric
SalesAmtCal   = AVERAGE(FactInternetSales[SalesAmount])
OrderQtyCal   = AVERAGE(FactInternetSales[OrderQuantity])
UnitPriceCal  = AVERAGE(FactInternetSales[UnitPrice])
FreightCal    = AVERAGE(FactInternetSales[Freight])
TotalCostCal  = AVERAGE(FactInternetSales[TotalProductCost])
StdCostCal    = AVERAGE(FactInternetSales[StandardCost])

-- Step 2: Dynamic measure selector
DynamicMetric =
VAR SelectedIdx = SELECTEDVALUE(AllMeasuresTable[Index])
RETURN
    SWITCH(
        SelectedIdx,
        1, [SalesAmtCal],
        2, [OrderQtyCal],
        3, [UnitPriceCal],
        4, [FreightCal],
        5, [TotalCostCal],
        6, [StdCostCal]
    )
```

## Visual Setup

1. Clustered column chart → Date hierarchy in Axis
2. Dynamic measure in **Values** section
3. AllMeasuresTable[MeasureName] as a **slicer**
4. Selecting a measure name → chart updates via SWITCH logic

## When to Use

- Multiple metrics competing for slicer space
- Metric switcher in a single visual
- Alternative to Dynamic M Query Parameters (when M params unavailable)

## Key Points

- Measures table is **disconnected** from the model (no relationships)
- Index column controls order and SWITCH logic
- SELECTEDVALUE returns blank if no selection or multi-select

## See Also

- [[Source-Dynamic-Single-Slicer-using-DAX-logic]] — full source article
- [[Slicer-Panel-Workflow]] — slicer grouping and UX patterns
- [[Field-Parameters-Pattern]] — alternative: native field parameters (may replace this pattern in newer PBIX files)
