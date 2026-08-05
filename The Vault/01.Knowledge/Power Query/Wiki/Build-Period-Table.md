---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [power-query, calendar-table, date-dimension, M-code]
related: [EDATE, SELECTEDVALUE, TOTALYTD]
---

# Build a Period Table (Power Query)

Create a static `Period` lookup table in Excel or Power Query to drive time period slicers. The table maps period names to an ordering column for correct sort sequence.

## Pattern

**Excel source (imported to Power BI):**

| Period | Order |
|--------|-------|
| 1W | 1 |
| 1M | 2 |
| 6M | 3 |
| 1Y | 4 |

**Power Query equivalent:**
```m
= let
    Source = Table.FromRows(Json.Document("[
        {""1W"", 1},
        {""1M"", 2},
        {""6M"", 3},
        {""1Y"", 4}
    ], type table[Period = text, Order = Int64.Type]),
    ChangedType = Table.TransformColumnTypes(Source, {{"Period", type text}, {"Order", Int64.Type}})
in
    ChangedType
```

## Sort Column by Another Column

In Power BI, sort the `Period` column by the `Order` column so the slicer displays in the correct sequence (1W → 1M → 6M → 1Y) instead of alphabetical order:

1. Select the `Period` column in the table view.
2. Go to **Column tools → Sort by column → Order**.

This ensures `SELECTEDVALUE(Period[Period])` returns values in the intended sequence.

## Usage

Feed `Period[Period]` into a slicer. Use `SELECTEDVALUE(Period[Period])` in DAX measures to drive the time range:

```dax
Minimum Date =
VAR _MaxDate = [Maximum Date]
VAR _SelectedPeriod = SELECTEDVALUE(Period[Period])
VAR _MinimumDate =
    SWITCH(
        TRUE(),
        _SelectedPeriod = "1W", _MaxDate - 7,
        _SelectedPeriod = "1M", EDATE(_MaxDate, -1),
        _SelectedPeriod = "6M", EDATE(_MaxDate, -6),
        _SelectedPeriod = "1Y", EDATE(_MaxDate, -12)
    )
RETURN _MinimumDate
```

## Notes

- Build the Period table once as a static lookup — do not refresh from live data sources.
- `Order` column must be an integer type (not text) for Power BI to sort correctly.
- Period table should have no active relationship to the fact table — it is used only as a slicer lookup.
- The same pattern extends to fiscal periods, quarters, or custom date ranges.

## Related

- [[EDATE]] — subtract months in DAX for the minimum date calculation
- [[SELECTEDVALUE]] — read the user's period selection
- [[totalytd]] / [[totalqtd]] — time intelligence functions that work with the resulting date range
