---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, percentile, bucket, binning, quantile]
---

# PercentileBuckets UDF — Dynamic Quintile/Decile Bucketing

Computes dynamic percentile cutpoints and maps values to bucket labels that sort correctly in visuals.

```dax
DEFINE
    FUNCTION PercentileBoundsCustom =
        ( measureExpr : AnyRef expr, wholeTable : TABLE,
          q1 : NUMERIC, q2 : NUMERIC, q3 : NUMERIC, q4 : NUMERIC ) =>
        VAR T   = wholeTable
        RETURN ROW("Min",CALCULATE(MINX(T,measureExpr),T),
                   "P1", CALCULATE(PERCENTILEX.INC(T,measureExpr,q1),T),
                   "P2", CALCULATE(PERCENTILEX.INC(T,measureExpr,q2),T),
                   "P3", CALCULATE(PERCENTILEX.INC(T,measureExpr,q3),T),
                   "P4", CALCULATE(PERCENTILEX.INC(T,measureExpr,q4),T),
                   "Max",CALCULATE(MAXX(T,measureExpr),T));

    FUNCTION BucketIndexFromBounds =
        ( value : NUMERIC, minV,p1,p2,p3,p4,maxV : NUMERIC, includeZeroBlank : BOOL ) =>
        SWITCH(TRUE(),
            includeZeroBlank && (ISBLANK(value)||value=0), 0,
            value<=p1, 1, value<=p2, 2, value<=p3, 3, value<=p4, 4, 5);

    FUNCTION BucketLabelFromBounds =
        ( value,minV,p1,p2,p3,p4,maxV,includeZeroBlank ) =>
        VAR band  = BucketIndexFromBounds(value,minV,p1,p2,p3,p4,maxV,includeZeroBlank)
        VAR label = SWITCH(band,
            0,"No Value",
            1,FORMAT(minV,"#,##0")&" - "&FORMAT(p1,"#,##0"),
            2,FORMAT(p1,"#,##0")&" - "&FORMAT(p2,"#,##0"),
            3,FORMAT(p2,"#,##0")&" - "&FORMAT(p3,"#,##0"),
            4,FORMAT(p3,"#,##0")&" - "&FORMAT(p4,"#,##0"),
               FORMAT(p4,"#,##0")&" - "&FORMAT(maxV,"#,##0"))
        RETURN REPT(UNICHAR(8203),band+1)&label;

    -- Wrapper binds your table once
    FUNCTION QuantileBucketLabel =
        ( measureExpr : AnyRef expr, includeZeroBlank : BOOL,
          q1,q2,q3,q4 : NUMERIC ) =>
        VAR B = PercentileBoundsCustom(measureExpr,ALL(aggregate_risk),q1,q2,q3,q4)
        RETURN BucketLabelFromBounds(measureExpr,B[Min],B[P1],B[P2],B[P3],B[P4],B[Max],includeZeroBlank);

    FUNCTION QuantileBucketIndex =
        ( measureExpr : AnyRef expr, includeZeroBlank : BOOL,
          q1,q2,q3,q4 : NUMERIC ) =>
        VAR B = PercentileBoundsCustom(measureExpr,ALL(aggregate_risk),q1,q2,q3,q4)
        RETURN BucketIndexFromBounds(measureExpr,B[Min],B[P1],B[P2],B[P3],B[P4],B[Max],includeZeroBlank)
```

**Usage:**
```dax
Amount Bucket      = QuantileBucketLabel([Amount],TRUE, 0.2,0.4,0.6,0.8)
Amount Bucket Index= QuantileBucketIndex([Amount],TRUE, 0.2,0.4,0.6,0.8)
-- Sort axis by Bucket Index for correct order
```

Bucket labels include ZWSP prefix so they sort correctly without a separate sort column.
