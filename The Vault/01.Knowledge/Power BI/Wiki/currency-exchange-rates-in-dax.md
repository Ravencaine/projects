---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "finance", "currency", "exchange-rate", "conversion"]
note_type: pattern

---

# Currency Exchange Rates in DAX

Converting amounts between currencies using a rate table.

## Data Model

A rate table: Date, FromCurrency, ToCurrency, Rate.

## DAX Pattern

```dax
Converted Amount :=
VAR __Date = MAX( 'Dates'[Date] )
VAR __Currency = SELECTEDVALUE( 'Transaction'[Currency] )
VAR __Rate =
    LOOKUPVALUE(
        'ExchangeRates'[Rate],
        'ExchangeRates'[Date], __Date,
        'ExchangeRates'[FromCurrency], __Currency,
        'ExchangeRates'[ToCurrency], "USD"
    )
RETURN
DIVIDE( [Amount], __Rate )
```

## Notes

- Use a separate exchange rate table with daily rates
- For real-time rates, connect to an API data source

## Related

- [[gross-margin-calculation-in-dax]]
- [[modified-dietz-return-dax]]
