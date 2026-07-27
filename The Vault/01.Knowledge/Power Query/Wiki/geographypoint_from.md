---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["geographypoint", "m-function"]
---


# GeographyPoint.From

Creates a record representing a geographic point from its constituent parts, such as longitude, latitude, and if present, elevation (Z) and measure (M). An optional spatial reference identifier (SRID) can be given if different from the default value (4326). --- PAGE 883 ---

## Signature

```m
GeographyPoint.From(
longitude as number,
latitude as number,
optional z as nullable number,
optional m as nullable number,
optional srid as nullable number
) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| longitude | number | |
| latitude | number | |
| optional z | nullable number | |
| optional m | nullable number | |
| optional srid | nullable number | |

## Returns

record

