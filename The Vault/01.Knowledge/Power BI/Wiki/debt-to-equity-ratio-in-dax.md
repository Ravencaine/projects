---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, finance, leverage, ratio]
note_type: pattern

---

# Debt-to-Equity Ratio in DAX

Measuring the proportion of debt to shareholder equity.

## Formula

```
Debt-to-Equity = Total Liabilities / Total Equity
```

## DAX Pattern

```dax
Total Liabilities := SUM( 'BalanceSheet'[Liabilities] )
Total Equity := SUM( 'BalanceSheet'[Equity] )

Debt-to-Equity :=
DIVIDE( [Total Liabilities], [Total Equity] )
```

## Interpretation

- D/E < 1: More equity than debt (conservative)
- D/E 1-2: Moderate leverage
- D/E > 2: High leverage (higher risk)

## Notes

- Compare against industry benchmarks — capital-intensive industries carry more debt
- Track over time to detect deteriorating financial health

## Related

- [[current-ratio-and-quick-ratio-in-dax]]
- [[accounts-payable-turnover-in-dax]]
