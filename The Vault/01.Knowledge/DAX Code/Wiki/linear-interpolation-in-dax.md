---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, math, interpolation, approximation]
note_type: pattern

---

# Linear Interpolation in DAX

Estimating values between two known data points using a linear model.

## Purpose

When you have two known (x, y) pairs and want to estimate y at an intermediate x, linear interpolation provides a smooth estimate.

## Formula

Given two points (x1, y1) and (x2, y2), the interpolated value at x is:

```
y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
```

## DAX Implementation

```dax
Linear Interpolation :=
VAR __x1 = MIN( 'Data'[X] )
VAR __x2 = MAX( 'Data'[X] )
VAR __y1 = MINX( FILTER( 'Data', 'Data'[X] = __x1 ), 'Data'[Y] )
VAR __y2 = MINX( FILTER( 'Data', 'Data'[X] = __x2 ), 'Data'[Y] )
VAR __x = [TargetX]
RETURN
__y1 + ( __x - __x1 ) * DIVIDE( __y2 - __y1, __x2 - __x1 )
```

## Notes

- Works best when data points are evenly spaced
- For unevenly spaced data, nearest-neighbour interpolation may be more appropriate
- Useful in finance for interpolating exchange rates or yield curves

## Related

- [[regression-analysis-in-dax]]
- [[better-mod-workaround-in-dax]]
