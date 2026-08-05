---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "accounts-receivable", "turnover"]
note_type: pattern

---

# Accounts Receivable Turnover in DAX

Measuring how quickly a company collects payment from customers.

## Formula

```
AR Turnover = Net Credit Sales / Average Accounts Receivable
Days Sales Outstanding = 365 / AR Turnover
```

## DAX Pattern

```dax
AR Turnover :=
DIVIDE(
    SUM( 'Sales'[NetCreditSales] ),
    AVERAGEX(
        SUMMARIZECOLUMNS( 'Dates'[Month], "AR", SUM( 'AR'[Balance] ) ),
        [AR]
    )
)

Days Sales Outstanding := DIVIDE( 365, [AR Turnover] )
```

## Notes

- Lower DSO means faster collection (generally favorable)
- DSO above payment terms suggests collection problems
- Use customer segment slicers to identify slow payers

## Related

- [[accounts-payable-turnover-in-dax]]
- [[npv-and-irr-calculations-in-dax]]
