---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, svg, sparkline, visualization, power-bi]
---

# SparklineSVG_LastNDays — SVG Gradient Sparkline

Renders a gradient sparkline for the last N days of any measure. Chooses red/green styling based on first→last direction.

## Signature

```c
UDF SparklineSVG_LastNDays =
    ( valueExpr : AnyRef expr,
      nDays : INT64,
      posStroke : STRING, posBg1 : STRING, posBg2 : STRING,
      negStroke : STRING, negBg1 : STRING, negBg2 : STRING,
      width : NUMERIC, height : NUMERIC
    ) => "<svg ...>"
```

Returns raw SVG (not URL-encoded — apply `UDF_EncodeSVG` if embedding in an image field).

## How It Works

1. Window: `MAX(date) - (nDays-1)` → `MAX(date)`
2. Evaluates series via `CALCULATETABLE(VALUES(date_col), KEEPFILTERS(...))`
3. Normalizes x/y coordinates: `x = idx/(n-1) * width`, `y = height * (1 - (val - vMin)/(vMax - vMin))`
4. Direction: compares first→last value → picks pos or neg color set
5. Renders polyline + linear gradient fill

## Usage

```c
Current Price := AVERAGE('Crypto Data'[price])

Sparkline (7D) := SparklineSVG_LastNDays(
    [Current Price], 7,
    "#2E7D32", "#A5D6A7", "#E8F5E9",   // positive: stroke, bg1, bg2
    "#C62828", "#FFCDD2", "#FFEBEE",   // negative: stroke, bg1, bg2
    70, 30                              // width, height
)
```

Display via **Conditional formatting → Field value** or as an Image URL.

## Config

`// 🔧 CONFIG` — change `'Crypto Data'[timestamp]` to your date column.

## Related

- [[udf_encodesvg-url-encoder-for-svg]] — for URL-encoding this output
- [[svg-visualizations-in-power-bi]]
