---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, narrative, kpi, insight, top-change]
---

# NarrativeTopChangeCore + Wrappers — Auto-Generated KPI Insight Text

Produces one-line narrative insights for the biggest rise/drop: `"🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)"`.

```dax
DEFINE
    FUNCTION NarrativeTopChangeCore =
        ( varianceExpr : AnyRef expr,
          shareCutoff  : NUMERIC,
          risePrefix   : STRING,
          dropPrefix   : STRING,
          metricName   : STRING,
          dimLabelSing : STRING,
          attrLabelSing: STRING,
          mode         : STRING,
          dimAll  : TABLE, dimName : STRING,
          attrAll : TABLE, attrName: STRING ) =>
        VAR _mode = UPPER(mode)
        VAR _extremeVar = SWITCH(_mode,"RISE",MAXX(dimAll,varianceExpr),"DROP",MINX(dimAll,varianceExpr),MAXX(dimAll,varianceExpr))
        VAR _extremeDim = CALCULATE(FIRSTNONBLANK(dimName,1),FILTER(dimAll,varianceExpr=_extremeVar))
        VAR _attrTbl = ADDCOLUMNS(attrAll,"Var",CALCULATE(varianceExpr))
        VAR _topAttrVar  = IF(ISEMPTY(_attrTbl),BLANK(),
            SWITCH(_mode,"RISE",MAXX(_attrTbl,[Var]),"DROP",MINX(_attrTbl,[Var]),MAXX(_attrTbl,[Var])))
        VAR _topAttrName= IF(ISEMPTY(_attrTbl),BLANK(),
            MAXX(TOPN(1,_attrTbl,[Var],IF(_mode="DROP",ASC,DESC)),attrName))
        VAR _share = IF(OR(ISBLANK(_topAttrVar),_extremeVar=0),BLANK(),DIVIDE(ABS(_topAttrVar),ABS(_extremeVar)))
        VAR _prefix = SWITCH(_mode,"RISE",risePrefix,"DROP",dropPrefix,risePrefix)
        VAR _attrText = IF(ISEMPTY(_attrTbl)||ISBLANK(_topAttrVar),"",
            SWITCH(TRUE(),
                _mode="RISE" && _topAttrVar>0 && _share>=shareCutoff," — mainly on "&_topAttrName&" ("&FORMAT(_topAttrVar,"+0.0%")&")",
                _mode="RISE" && _topAttrVar>0 && _share<shareCutoff, " — spread across "&attrLabelSing&"s (top: "&_topAttrName&" "&FORMAT(_topAttrVar,"+0.0%")&")",
                _mode="DROP" && _topAttrVar<0 && ABS(_share)>=shareCutoff," — mainly on "&_topAttrName&" ("&FORMAT(_topAttrVar,"+0.0%")&")",
                _mode="DROP" && _topAttrVar<0 && ABS(_share)<shareCutoff, " — spread across "&attrLabelSing&"s (top: "&_topAttrName&" "&FORMAT(_topAttrVar,"+0.0%")&")",
                ""))
        RETURN _prefix&metricName&": "&_extremeDim&" "&FORMAT(_extremeVar,"+0.0%")&_attrText
```

**Wrapper pattern** (binds dimension + attribution columns):
```dax
FUNCTION NarrativeTopChange_UnitShift =
    ( varianceExpr, shareCutoff, risePrefix, dropPrefix, metricName, mode ) =>
    VAR _dimAll  = ALL(Units[Unit])
    VAR _dimName = Units[Unit]
    VAR _attrAll = ALL('Scheduling Data'[Shift])
    VAR _attrName= 'Scheduling Data'[Shift]
    RETURN NarrativeTopChangeCore(varianceExpr,shareCutoff,risePrefix,dropPrefix,
        metricName,"unit","shift",mode,_dimAll,_attrAll,_dimName,_attrName)
```

**Usage:**
```dax
Biggest Rise (Narrative) =
    NarrativeTopChange_UnitShift(
        [OT Hours per FTE Variance %],
        0.60, "🔺 Biggest rise in ","🔻 Biggest drop in ","OT/FTE","RISE"
    )
-- Output: "🔺 Biggest rise in OT/FTE: ICU +12.6% — mainly on Evening (+7.4%)"
```
