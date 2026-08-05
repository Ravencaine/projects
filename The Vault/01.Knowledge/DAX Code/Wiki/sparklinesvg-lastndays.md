---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, svg, sparkline, visualization]
---

# SparklineSVG_LastNDays — Gradient SVG Sparkline

Renders the last N days of any measure as a gradient-filled SVG polyline, styled red or green based on first→last direction.

```dax
DEFINE
    FUNCTION SparklineSVG_LastNDays =
        ( valueExpr : AnyRef expr,
          nDays     : INT64,
          posStroke : STRING, posBg1 : STRING, posBg2 : STRING,
          negStroke : STRING, negBg1 : STRING, negBg2 : STRING,
          width     : NUMERIC, height : NUMERIC ) =>
        VAR _maxDate = MAX('Crypto Data'[timestamp])
        VAR _minDate = _maxDate-(nDays-1)
        VAR _datesWin = CALCULATETABLE(VALUES('Crypto Data'[timestamp]),
            KEEPFILTERS('Crypto Data'[timestamp]>=_minDate && 'Crypto Data'[timestamp]<=_maxDate))
        VAR _seriesRaw = ADDCOLUMNS(_datesWin,"val",CALCULATE(valueExpr))
        VAR _n    = COUNTROWS(_seriesRaw)
        VAR _vMin = MINX(_seriesRaw,[val])
        VAR _vMax = MAXX(_seriesRaw,[val])
        VAR _den  = _vMax-_vMin
        VAR _midY = height/2
        VAR _seriesXY = ADDCOLUMNS(_seriesRaw,
            "idx",RANKX(_seriesRaw,'Crypto Data'[timestamp],,ASC),
            "x",IF(_n<=1,0,DIVIDE(([idx]-1)*width,_n-1)),
            "y",IF(_den=0,_midY,height*(1-DIVIDE([val]-_vMin,_den))))
        VAR _firstVal = MINX(TOPN(1,_seriesXY,'Crypto Data'[timestamp],ASC),[val])
        VAR _lastVal  = MAXX(TOPN(1,_seriesXY,'Crypto Data'[timestamp],DESC),[val])
        VAR _pctVar  = IF(_firstVal=0,BLANK(),DIVIDE(_lastVal-_firstVal,_firstVal))
        VAR _stroke  = IF(_pctVar<0,negStroke,posStroke)
        VAR _bg1     = IF(_pctVar<0,negBg1,posBg1)
        VAR _bg2     = IF(_pctVar<0,negBg2,posBg2)
        VAR _points  = CONCATENATEX(_seriesXY,
            FORMAT([x],"0")&","&FORMAT([y],"0")," ",'Crypto Data'[timestamp],ASC)
        RETURN "<svg xmlns='...' viewBox='0 0 "&width&" "&height&"'>"
          &"<defs><linearGradient id='g' x1='0%' y1='0%' x2='0%' y2='100%'>"
          &"<stop offset='0%' style='stop-color:"&_bg1&";stop-opacity:1'/>"
          &"<stop offset='100%' style='stop-color:"&_bg2&";stop-opacity:0'/>"
          &"</linearGradient></defs>"
          &"<polyline fill='url(#g)' points='" &_points&" "&width&","&height&" 0,"&height&"'/>"
          &"<polyline fill='none' stroke='" &_stroke&"' stroke-width='1.5' points='" &_points&"'/>"
          &"</svg>"
```

**Usage:**
```dax
Sparkline (7D) = SparklineSVG_LastNDays(
    [Current Price], 7,
    "#2E7D32","#A5D6A7","#E8F5E9",   -- positive: stroke, bg1, bg2
    "#C62828","#FFCDD2","#FFEBEE",   -- negative: stroke, bg1, bg2
    70, 30                              -- width, height
)
```

Display via **Conditional formatting → Field value** or as an image field. CONFIG: change date column to your Date table.
