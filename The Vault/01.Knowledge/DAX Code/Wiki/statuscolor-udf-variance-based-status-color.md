---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, conditional-formatting, color, variance, kpi, power-bi]
---

# StatusColor — Variance-Based Status Color

Assigns a hex color code based on variance magnitude vs. symmetric or asymmetric thresholds. Use with conditional formatting by field value.

## Signature

```c
UDF StatusColor =
    ( variance : NUMERIC,
      tolLow  : NUMERIC,   // below this → red
      tolHigh : NUMERIC    // above this → green
    ) => SWITCH(TRUE(),
        variance < tolLow,  "#E15759",   // red — underperformance
        variance > tolHigh, "#59A14F",   // green — exceeding
        "#BAB0AC"                   // gray — neutral
      )
```

## Usage

```c
// Fixed absolute thresholds
Sales Status Color := StatusColor([Sales Variance], -5000, 5000)

// Proportional thresholds (5% of total)
Sales Status Color (MoM) :=
    StatusColor(
        [Sales Variance (MoM)],
        -0.05 * [Total Sales],
         0.05 * [Total Sales]
    )
```

Apply via **Conditional formatting → Field value** on any visual, pointing at the Status Color measure.

## Config

`// 🔧 CONFIG` — adjust `tolLow`/`tolHigh` thresholds and hex codes to match your design system.

## Pairs With

- [[varabs-udf-variance-from-reference]]
- [[rolling-total-udf]] / [[rolling-average-udf]] for rolling variance comparisons
