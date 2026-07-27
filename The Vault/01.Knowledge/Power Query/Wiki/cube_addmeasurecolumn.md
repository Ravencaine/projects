---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["cube", "m-function"]
---


# Cube.AddMeasureColumn

Adds a column with the name column to the cube that contains the results of the measure measureSelector applied in the row context of each row. Measure application is affected by changes to dimension granularity and slicing. Measure values will be adjusted after certain cube operations are performed. --- PAGE 331 ---

## Signature

```m
Cube.AddMeasureColumn(
cube as table,
column as text,
measureSelector as any
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| cube | table | |
| column | text | |
| measureSelector | any | |

## Returns

table

