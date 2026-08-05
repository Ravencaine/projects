---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, formatting, number-format, humanize, k, m, b, power-bi]
---

# Humanize — Short-Scale Number Formatting

Converts large values to K/M/B strings. Handles negatives and blanks. Returns a string — use for tooltips, card text, narrative.

## Signature

```c
UDF Humanize = ( x : NUMERIC ) => SWITCH(TRUE(),
    ISBLANK(x),  BLANK(),
    ABS(x) >= 1e9, FORMAT(x/1e9, "0.##") & "B",
    ABS(x) >= 1e6, FORMAT(x/1e6, "0.##") & "M",
    ABS(x) >= 1e3, FORMAT(x/1e3, "0.##") & "K",
    FORMAT(x, "#,0")
)
```

## HumanizeWithDecimals

```c
UDF HumanizeWithDecimals = ( x : NUMERIC, decimals : INT64 ) => ...
// decimals: 0..3 — controls decimal places
```

## Usage

```c
Total Sales := SUM(Sales[SalesAmount])

// As text (for tooltips, cards, narrative)
Total Sales (Humanized)        := Humanize([Total Sales])
Total Sales (Humanized 1dp)    := HumanizeWithDecimals([Total Sales], 1)
```

## Pro Tip: Dynamic Format String

Keep the measure numeric and switch only the format string for sorting:

```c
VAR v = [Total Sales]
RETURN SWITCH(TRUE(),
    ABS(v) >= 1e9, "0.##,,,'B'",
    ABS(v) >= 1e6, "0.##,,'M'",
    ABS(v) >= 1e3, "0.##,'K'",
    "#,0"
)
```

Format string approach preserves numeric sort order.

## Related

- [[FORMAT]]
