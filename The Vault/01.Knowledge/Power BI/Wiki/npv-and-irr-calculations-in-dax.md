---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "npv", "irr", "investment"]
note_type: pattern

---

# NPV and IRR Calculations in DAX

Evaluating the profitability of investments using time value of money.

## Net Present Value (NPV)

```
NPV = sum of ( Cash Flow / (1 + r)^n ) for all periods
```

```dax
NPV :=
SUMX(
    'CashFlows',
    DIVIDE(
        [Amount],
        POWER( 1 + [DiscountRate], [Period] )
    )
)
```

## Internal Rate of Return (IRR)

DAX has no native IRR function, but it can be approximated:

```dax
IRR Approximation :=
VAR __NPV = [NPV]
VAR __Slope =
    SUMX( 'CashFlows', [Amount] / POWER( 1.1, [Period] ) )
RETURN
DIVIDE( __NPV, __Slope ) + 0.1
```

For precise IRR, use XIRR for cash flows with actual dates.

## Notes

- Use a low discount rate (5-10%) for stable businesses
- IRR should exceed the cost of capital to create value
- XIRR is preferred when cash flow dates are irregular

## Related

- [[project-roi-and-payback-period-in-dax]]
- [[gross-margin-calculation-in-dax]]
