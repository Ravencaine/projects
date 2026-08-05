---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "liquidity", "ratio"]
note_type: pattern

---

# Current Ratio and Quick Ratio in DAX

Measuring a company's ability to pay short-term obligations.

## Current Ratio

```
Current Ratio = Current Assets / Current Liabilities
```

```dax
Current Ratio :=
DIVIDE(
    SUM( 'BalanceSheet'[CurrentAssets] ),
    SUM( 'BalanceSheet'[CurrentLiabilities] )
)
```

## Quick Ratio (Acid Test)

```
Quick Ratio = ( Current Assets - Inventory ) / Current Liabilities
```

```dax
Quick Ratio :=
DIVIDE(
    SUM( 'BalanceSheet'[CurrentAssets] ) - SUM( 'BalanceSheet'[Inventory] ),
    SUM( 'BalanceSheet'[CurrentLiabilities] )
)
```

## Interpretation

| Ratio | > 1.5 | 1.0-1.5 | < 1.0 |
|-------|--------|---------|-------|
| Current | Healthy | Acceptable | At risk |
| Quick | Strong | Acceptable | At risk |

## Notes

- Use a date table to show ratio trends over time
- Exclude illiquid assets from Quick Ratio (inventory, prepaid expenses)

## Related

- [[debt-to-equity-ratio-in-dax]]
- [[gross-margin-calculation-in-dax]]
