---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["geometrypoint", "m-function"]
---


# GeometryPoint.From

Creates a record representing a geometric point from its constituent parts, such as X coordinate, Y coordinate, and if present, Z coordinate and measure (M). An optional spatial reference identifier (SRID) can be given if different from the default value (0). --- PAGE 886 ---

## Signature

```m
GeometryPoint.From(
x as number,
y as number,
optional z as nullable number,
optional m as nullable number,
optional srid as nullable number
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| x | number | |
| y | number | |
| optional z | nullable number | |
| optional m | nullable number | |
| optional srid | nullable number | |

## Returns

record

