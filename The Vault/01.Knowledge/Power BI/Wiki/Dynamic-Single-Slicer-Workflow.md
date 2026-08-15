---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Single Slicer using DAX logic.md"
note_type: workflow
tags: [power-bi, slicer, dynamic-slicer, disconnected-table, measures-table, workflow]
---

# Dynamic Single Slicer — 5-Step Implementation Workflow

> **Type:** workflow
> **Routed to:** Power BI
> **Primary source:** Boniface Muchendu, Data Bear — 2022-10-30

## Overview

Combine multiple column slicers into one dynamic slicer using a disconnected measures table with an index column and SELECTEDVALUE/SWITCH DAX logic.

## Steps

### Step 1: Import Dataset

1. Connect Power BI to data source (e.g., SQL Server)
2. Select table(s) to import (e.g., FactInternetSales)
3. Click **Transform Data** → Power Query Editor
4. Perform any data manipulations
5. Load into model

### Step 2: Create Calendar Table

1. Go to **Modeling** tab → **New table**
2. Write CALENDAR DAX:

```
DateTable =
CALENDAR(
    MIN(FactInternetSales[OrderDate]),
    MAX(FactInternetSales[OrderDate])
)
```

3. Set DateTable as a date table (**Mark as date table**)
4. Create relationship between DateTable and fact table on the date column

### Step 3: Create Measures Table (Disconnected)

1. **Home** → **Enter Data** (manual table)
2. Add columns: `MeasureName` (metric display names) and `Index` (integer order)
3. Example rows:

| MeasureName    | Index |
|----------------|-------|
| Sales Amount   | 1     |
| Order Quantity | 2     |
| Unit Price     | 3     |
| Freight        | 4     |
| Total Cost     | 5     |
| Standard Cost  | 6     |

4. Load table — **no relationship** to other tables (disconnected table)

### Step 4: Create DAX Measures

For each metric, create an aggregation measure:

```dax
SalesAmtCal = AVERAGE(FactInternetSales[SalesAmount])
OrderQtyCal = AVERAGE(FactInternetSales[OrderQuantity])
-- ... repeat for each metric
```

Create the dynamic selector measure:

```dax
DynamicMetric =
VAR SelectedIdx = SELECTEDVALUE(AllMeasuresTable[Index])
RETURN
    SWITCH(
        SelectedIdx,
        1, [SalesAmtCal],
        2, [OrderQtyCal],
        -- ... add all metrics
    )
```

### Step 5: Build Slicer and Visual

1. Add a **Clustered Column Chart**
2. Put date hierarchy column in **Axis**
3. Put `DynamicMetric` in **Values**
4. Add **Slicer** visual → put `AllMeasuresTable[MeasureName]` in the slicer field
5. Select any measure name → chart updates automatically

## Verification

- Chart is blank before first selection (expected — no default)
- Selecting a metric name shows that metric's values in the chart
- Switching selection updates chart instantly
- Multiple metrics combined into one slicer control

## Limitations

- Requires SELECTEDVALUE — if multi-select is possible, add a fallback: `SELECTEDVALUE(..., "Multiple")`
- Disconnected table cannot be filtered by other slicers

## See Also

- [[Source-Dynamic-Single-Slicer-using-DAX-logic]] — source article
- [[Dynamic-Single-Slicer-Pattern]] — pattern note with full DAX
