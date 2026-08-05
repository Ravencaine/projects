---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [power-query, stock-data, data-prep, investing-com]
related: [EDATE, SELECTEDVALUE, Table.ExpandListColumn]
---

# Import and Prep Stock Data (Power Query)

Load stock price data from Investing.com into Power BI and shape it for time period slicer analysis.

## Import Data

1. Export CSV from Investing.com (or another financial data source).
2. Load via **Get Data → Text/CSV** in Power BI.
3. In Power Query Editor, inspect the data types.

Typical `Stock Data` table shape:

| Date | Price | Open | High | Low | Volume |
|------|-------|------|------|-----|--------|
| 2024-01-02 | 185.40 | 184.20 | 186.10 | 183.90 | 45,230,000 |
| 2024-01-03 | 186.20 | 185.40 | 187.00 | 184.80 | 42,100,000 |

## Shape Steps

```m
= let
    Source = Csv.Document(File.Contents("...\stock_data.csv"), [Delimiter=",", Columns=6]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedType = Table.TransformColumnTypes(
        PromotedHeaders,
        {
            {"Date", type date},
            {"Price", type number},
            {"Open", type number},
            {"High", type number},
            {"Low", type number},
            {"Volume", Int64.Type}
        }
    ),
    // Sort by date ascending
    SortedRows = Table.Sort(ChangedType, {{"Date", Order.Ascending}})
in
    SortedRows
```

## Key M Functions Used

| Function | Purpose |
|----------|---------|
| `Csv.Document` | Parse CSV file |
| `Table.PromoteHeaders` | Use first row as headers |
| `Table.TransformColumnTypes` | Set explicit data types |
| `Table.Sort` | Sort by date |
| `Table.SelectColumns` | Keep only needed columns |

## Notes

- Setting explicit `type date` and `type number` on import prevents Power BI from inferring incorrect types.
- Sort the table ascending by date before loading — Power BI does not auto-sort date columns.
- If the source has multiple tickers (wide format), unpivot to a long table with columns: `Date`, `Ticker`, `Price`.
- Bittar loads this table then uses `MAX('Stock Data'[Date])` in DAX to anchor the time period slicer to the latest available data point.

## Related

- [[EDATE]] — subtract time periods in DAX for the minimum date
- [[Build-Period-Table]] — create the period lookup table to pair with this data
- [[SELECTEDVALUE]] — read user's period selection to drive dynamic axis
