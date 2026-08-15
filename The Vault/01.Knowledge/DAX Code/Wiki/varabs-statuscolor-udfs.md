---
created: 2026-08-02
updated: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, variance, color, conditional-formatting, threshold]
---

# VarAbs + StatusColor — Variance and Conditional Status Color UDFs

Two complementary UDFs: one computes the gap, one maps it to a hex color based on thresholds.

```dax
DEFINE
    FUNCTION VarAbs =
        ( actual : NUMERIC, reference : NUMERIC ) =>
        actual - reference;

    FUNCTION StatusColor =
        ( variance : NUMERIC, tolLow : NUMERIC, tolHigh : NUMERIC ) =>
        SWITCH( TRUE(),
            variance < tolLow,  "#E15759",  -- red = underperformance
            variance > tolHigh, "#59A14F",  -- green = exceeding
            "#BAB0AC"                   -- gray = neutral
        )
```

**`VarAbs`:** reference can be a target (budget) or a prior-period value from `CompareOverPeriodRange`.

**`StatusColor`:** two thresholds (`tolLow`, `tolHigh`) define the neutral band. Below low = red, above high = green, between = gray.

**Usage with target:**
```dax
Sales Variance      = VarAbs([Total Sales],[Sales Target])
Sales Status Color  = StatusColor([Sales Variance],-5000,5000)
```

**Usage with prior period:**
```dax
Sales Variance (MoM) =
    VarAbs([Total Sales], CompareOverPeriodRange([Total Sales],"MoM","VALUE"))

Sales Status Color (MoM) =
    StatusColor([Sales Variance (MoM)], -0.05*[Total Sales], 0.05*[Total Sales])
```
