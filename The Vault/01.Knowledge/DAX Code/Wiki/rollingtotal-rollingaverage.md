---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, rolling-window, average, time-intelligence]
---

# RollingTotal + RollingAverage — Rolling Window UDFs

Rolling totals and averages anchored to the latest visible date. Works with DAY/WEEK/MONTH/QUARTER/YEAR units.

```dax
DEFINE
    FUNCTION RollingTotal =
        ( base : AnyRef expr, n : INT64, unit : STRING ) =>
        VAR _u   = UPPER(unit)
        VAR _end = MAX('Date'[Date])
        VAR _span = SWITCH( TRUE(),
            _u IN {"DAY","DAYS"},     DATESINPERIOD('Date'[Date],_end,-n,DAY),
            _u IN {"WEEK","WEEKS"},   DATESINPERIOD('Date'[Date],_end,-(7*n),DAY),
            _u IN {"MONTH","MONTHS"}, DATESINPERIOD('Date'[Date],_end,-n,MONTH),
            _u IN {"QUARTER","QUARTERS"},DATESINPERIOD('Date'[Date],_end,-n,QUARTER),
            _u IN {"YEAR","YEARS"},   DATESINPERIOD('Date'[Date],_end,-n,YEAR),
            BLANK()
        )
        RETURN IF(ISBLANK(_span)||ISEMPTY(_span),BLANK(),CALCULATE(base,_span));

    FUNCTION RollingAverage =
        ( base : AnyRef expr, n : INT64, unit : STRING ) =>
        VAR _u   = UPPER(unit)
        VAR _end = MAX('Date'[Date])
        VAR _span = SWITCH( TRUE(),
            _u IN {"DAY","DAYS"},     DATESINPERIOD('Date'[Date],_end,-n,DAY),
            _u IN {"WEEK","WEEKS"},   DATESINPERIOD('Date'[Date],_end,-(7*n),DAY),
            _u IN {"MONTH","MONTHS"}, DATESINPERIOD('Date'[Date],_end,-n,MONTH),
            _u IN {"QUARTER","QUARTERS"},DATESINPERIOD('Date'[Date],_end,-n,QUARTER),
            _u IN {"YEAR","YEARS"},  DATESINPERIOD('Date'[Date],_end,-n,YEAR),
            BLANK()
        )
        VAR _total  = CALCULATE(base,_span)
        VAR _denom  = SWITCH(TRUE(),
            _u IN {"DAY","DAYS","WEEK","WEEKS"},   DISTINCTCOUNT('Date'[Date]),
            _u IN {"MONTH","MONTHS"},              DISTINCTCOUNT('Date'[Year]&"-"&'Date'[MonthNo]),
            _u IN {"QUARTER","QUARTERS"},          DISTINCTCOUNT('Date'[Year]&"-"&'Date'[Quarter]),
            _u IN {"YEAR","YEARS"},                DISTINCTCOUNT('Date'[Year])
        )
        RETURN DIVIDE(_total,_denom)
```

**Usage:**
```dax
Sales (30D)    = RollingTotal([Total Sales],30,"DAY")
Sales (12M)    = RollingTotal([Total Sales],12,"MONTH")
Sales (4Q)     = RollingTotal([Total Sales],4,"QUARTER")
Avg Daily 7D   = RollingAverage([Total Sales],7,"DAY")
Avg Monthly 6M = RollingAverage([Total Sales],6,"MONTH")
```

**Note:** Weeks implemented as `7*n` days (no native DAX week unit for `DATESINPERIOD`). Use ISO week columns for precise week-based windows.
