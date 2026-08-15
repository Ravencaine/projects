---
created: 2026-08-02
updated: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, number-format, humanize, k, m, b]
---

# Humanize + HumanizeWithDecimals — K/M/B Number Abbreviation

Short-scale number abbreviation: `1,234,567` → `"1.23M"`.

```dax
DEFINE
    FUNCTION Humanize =
        ( x : NUMERIC ) =>
        VAR ax = ABS(x)
        RETURN SWITCH(TRUE(),
            ISBLANK(x), BLANK(),
            ax>=1000000000, FORMAT(x/1000000000,"0.##")&"B",
            ax>=1000000,    FORMAT(x/1000000,"0.##")&"M",
            ax>=1000,       FORMAT(x/1000,"0.##")&"K",
            FORMAT(x,"#,0"))

    FUNCTION HumanizeWithDecimals =
        ( x : NUMERIC, decimals : INT64 ) =>
        VAR ax  = ABS(x)
        VAR fmt = "0."&REPT("#",MIN(3,MAX(0,decimals)))
        RETURN SWITCH(TRUE(),
            ISBLANK(x), BLANK(),
            ax>=1e9, FORMAT(x/1e9,fmt)&"B",
            ax>=1e6, FORMAT(x/1e6,fmt)&"M",
            ax>=1e3, FORMAT(x/1e3,fmt)&"K",
            FORMAT(x,"#,0"))
```

**Usage:**
```dax
Total Sales (Humanized)     = Humanize([Total Sales])
Total Sales (Humanized 1dp) = HumanizeWithDecimals([Total Sales],1)
```
