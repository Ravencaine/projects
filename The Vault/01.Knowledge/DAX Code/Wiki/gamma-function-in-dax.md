---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, math, gamma, statistics, lanczos]
note_type: function

---

# GAMMA — Gamma Function via Lanczos Approximation

DAX has no native GAMMA function. It can be implemented using the Lanczos numerical approximation.

## Purpose

The gamma function extends factorials to non-integer values: GAMMA(n) = (n-1)! for integer n. Used in statistics (gamma distribution, beta distribution) and advanced mathematics.

## Formula (Lanczos Approximation)

```
GAMMA(z) = sqrt(2*pi) * (z + g + 0.5)^(z+0.5) * e^-(z+g+0.5) * L(z)
```

## DAX Implementation

```dax
GAMMA :=
VAR __z = [z]
VAR __g = 5.65
VAR __c = {
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7
}
VAR __t = __z + __g + 0.5 - 1
VAR __p =
    SUMX(
        __c,
        [Value] / ( __z + INDEX( __c, ROW() ) )
    )
RETURN
SQRT( 2 * PI() )
    * POWER( __t, __z + 0.5 )
    * EXP( -__t )
    * __p
```

## Notes

- Requires generating a series table with __c coefficients
- Accurate to ~15 significant digits for z > 0.5
- Used internally by BETA.DIST and CHISQ.DIST

## Related

- [[regression-analysis-in-dax]]
- [[stdevx.p]]
