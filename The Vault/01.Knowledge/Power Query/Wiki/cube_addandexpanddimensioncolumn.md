---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [cube, m-function]
---


# Cube.AddAndExpandDimensionColumn

Merges the specified dimension table, dimensionSelector, into the filter context of the cube and changes the dimensional granularity by expanding the specified set, attributeNames, of dimension attributes. The dimension attributes are added to the tabular view with columns named newColumnNames, or attributeNames if not specified. Last updated on 04/03/2026 --- PAGE 330 ---

## Signature

```m
Cube.AddAndExpandDimensionColumn(
cube as table,
dimensionSelector as any,
attributeNames as list,
optional newColumnNames as any
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| cube | table | |
| dimensionSelector | any | |
| attributeNames | list | |
| optional newColumnNames | any | |

## Returns

table

