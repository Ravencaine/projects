---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "accounts-payable", "turnover"]
note_type: pattern

---

# Accounts Payable Turnover in DAX

Measuring how quickly a company pays its suppliers.

## Formula

```
AP Turnover = COGS / Average Accounts Payable
Days Payable Outstanding = 365 / AP Turnover
```

## DAX Pattern

```dax
AP Turnover :=
DIVIDE(
    SUM( 'AP'[COGS] ),
    AVERAGEX(
        SUMMARIZECOLUMNS( 'Dates'[Month], "AP", SUM( 'AP'[Balance] ) ),
        [AP]
    )
)

Days Payable Outstanding := DIVIDE( 365, [AP Turnover] )
```

## Notes

- Higher DPO means the company holds onto cash longer (generally favorable)
- Compare DPO to payment terms agreed with suppliers
- Very high DPO may indicate financial stress

## Related

- [[accounts-receivable-turnover-in-dax]]
- [[current-ratio-and-quick-ratio-in-dax]]
