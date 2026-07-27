---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# CURRENTGROUP

Applies to: Calculated column Calculated table Measure Visual This function is discouraged for use in visual calculations as it likely returns Returns a set of rows from the table argument of a GROUPBY expression that belong to

## Return Value

meaningless results. Returns a set of rows from the table argument of a GROUPBY expression that belong to the current row of the GROUPBY result. Syntax DAX CURRENTGROUP ( ) Parameters None Return value The rows in the table argument of the GROUPBY function corresponding to one group of values of the

## Remarks

This function can only be used within a GROUPBY expression. This function takes no arguments and is only supported as the first argument to one of the following aggregation functions: AVERAGEX, COUNTAX, COUNTX, GEOMEANX, MAXX, MINX, PRODUCTX, STDEVX.S, STDEVX.P, SUMX, VARX.S, VARX.P.