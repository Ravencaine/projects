---
created: 2026-08-02
updated: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, time-intelligence, yoy, qoq, mom, rolling]
---

# CompareOverPeriodRange — Whole-Period Time Comparison (YoY/QoQ/MoM/WoW/DoD)

Compares a base measure over the full prior period vs. the current period (anchored to MAX visible date).

```dax
DEFINE
    FUNCTION CompareOverPeriodRange =
        ( base : AnyRef expr, shift : STRING, mode : STRING ) =>
        VAR _today    = MAX( 'Date'[Date] )
        VAR _s       = UPPER(shift)
        VAR _mode    = UPPER(mode)

        -- Current period start
        VAR _curStart = SWITCH( TRUE(),
            _s="YOY",  DATE(YEAR(_today),1,1),
            _s="QOQ",  STARTOFQUARTER(DATESBETWEEN('Date'[Date],_today,_today)),
            _s="MOM",  DATE(YEAR(_today),MONTH(_today),1),
            _s="WOW",  _today-6,
            _s="DOD",  _today,
            DATE(YEAR(_today),MONTH(_today),1)
        )
        VAR _curEnd  = _today

        -- Prior period
        VAR _priorStart = SWITCH( TRUE(),
            _s="YOY",  DATE(YEAR(_today)-1,1,1),
            _s="QOQ",  EDATE(_curStart,-3),
            _s="MOM",  EDATE(_curStart,-1),
            _s="WOW",  _curStart-7,
            _s="DOD",  _today-1,
            EDATE(_curStart,-1)
        )
        VAR _priorEnd = SWITCH( TRUE(),
            _s="YOY",  DATE(YEAR(_today)-1,12,31),
            _s="QOQ",  EOMONTH(_priorStart,2),
            _s="MOM",  EOMONTH(_priorStart,0),
            _s="WOW",  _curEnd-7,
            _s="DOD",  _today-1,
            EOMONTH(_priorStart,0)
        )

        VAR _currVal   = CALCULATE(base, DATESBETWEEN('Date'[Date],_curStart,_curEnd))
        VAR _priorVal  = CALCULATE(base, DATESBETWEEN('Date'[Date],_priorStart,_priorEnd))
        VAR _delta     = _currVal - _priorVal
        VAR _pct       = IF(NOT ISBLANK(_priorVal) && _priorVal<>0, DIVIDE(_delta,_priorVal), BLANK())

        RETURN SWITCH(_mode,
            "VALUE", _priorVal,
            "DELTA", _delta,
            "PCT",   _pct,
            _pct   -- default
        )
```

**Parameters:** `shift` = `"YOY"|"QOQ"|"MOM"|"WOW"|"DOD"`, `mode` = `"VALUE"|"DELTA"|"PCT"`

**Usage:**
```dax
YoY Sales %  = CompareOverPeriodRange([Total Sales],"YOY","PCT")
QoQ Sales Δ  = CompareOverPeriodRange([Total Sales],"QoQ","DELTA")
MoM Sales (prior) = CompareOverPeriodRange([Total Sales],"MoM","VALUE")
```

**Anchor:** `MAX('Date'[Date])` — change CONFIG comment if using a different Date table.
