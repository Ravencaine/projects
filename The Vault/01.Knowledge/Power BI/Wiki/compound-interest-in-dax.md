---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, finance, compound-interest, growth, investment]
note_type: pattern

---

# Compound Interest in DAX

Calculating compound growth over time.

## Formula

```
Future Value = Principal * (1 + rate)^periods
```

## DAX Pattern

```dax
Future Value :=
VAR __Principal = [Amount]
VAR __Rate = [AnnualRate]
VAR __Years = [Years]
VAR __CompoundsPerYear = [CompoundsPerYear]
RETURN
__Principal
    * POWER( 1 + DIVIDE( __Rate, __CompoundsPerYear ), __Years * __CompoundsPerYear )
```

## Notes

- POWER(x, n) is DAX's exponentiation operator (x^n)
- For continuous compounding, use EXP(rate * years)

## Related

- [[npv-and-irr-calculations-in-dax]]
- [[linear-interpolation-in-dax]]
