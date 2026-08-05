---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "project", "roi", "payback-period", "finance"]
note_type: pattern

---

# Project ROI and Payback Period in DAX

Calculating the financial return and break-even timeline for projects.

## Return on Investment (ROI)

```
ROI = ( Net Benefits / Total Investment ) * 100
```

```dax
Net Benefits :=
SUM( 'CashFlows'[Benefit] ) - SUM( 'CashFlows'[Cost] )

ROI :=
DIVIDE( [Net Benefits], SUM( 'CashFlows'[Cost] ] ) * 100
```

## Payback Period

The time it takes for cumulative benefits to equal cumulative costs.

```dax
Payback Period :=
MAXX(
    FILTER(
        SUMMARIZECOLUMNS(
            'Dates'[Year],
            "CumCost", SUM( 'CashFlows'[Cost] ),
            "CumBenefit", SUM( 'CashFlows'[Benefit] )
        ),
        [CumBenefit] >= [CumCost]
    ),
    'Dates'[Year]
)
```

## Net Present Value (NPV)

```dax
NPV :=
SUMX(
    'CashFlows',
    DIVIDE( [CashFlow], POWER( 1 + [DiscountRate], [Year] - 1 ) )
)
```

## Notes

- Use DATESYTD() or SUMMARIZECOLUMNS() to accumulate cash flows by period
- Discount rate should reflect the organization's cost of capital
- IRR can be found using DAX's financial functions (XIRR, RRI)

## Related

- [[npv-and-irr-calculations-in-dax]]
- [[gross-margin-calculation-in-dax]]
