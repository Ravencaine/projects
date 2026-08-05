---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [slicer, dynamic-axis, time-period, EDATE, SELECTEDVALUE]
related: [EDATE, SELECTEDVALUE, Build-Period-Table, New-Power-BI-Slicer-Features]
---

# Time Period Slicers (Dynamic Chart Range)

Connects a period slicer to a line/area chart's X-axis minimum so the chart dynamically resizes its range when the user selects different time periods (1W, 1M, 6M, 1Y).

## Data Model

- `Stock Data` table: `[Date]`, `[Price]`
- `Period` table: `[Period]` ("1W", "1M", "6M", "1Y"), `[Order]`

No relationship between Period and Stock Data tables.

## DAX Measures

**Maximum date (latest data point):**
```dax
Maximum Date = MAX('Stock Data'[Date])
```

**Minimum date (calculated from period selection):**
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
RETURN
    _MinimumDate
```

## Chart Setup

1. Build an Area Chart: X-axis = `Date`, Y-axis = `Price`.
2. Go to **Format → X-axis → Minimum** → select **Field value**.
3. Select the `Minimum Date` measure.
4. Sort the Period slicer by the `Order` column so 1W → 1M → 6M → 1Y appears in order.

## Notes

- `SELECTEDVALUE(Period[Period])` returns the user's current selection from the slicer.
- `EDATE(_MaxDate, -N)` subtracts N months — it's more reliable than subtracting 30×N days for "1 month" periods.
- The X-axis minimum applies to the **visual** only — the data behind the chart remains unchanged, so other visuals on the same page can still show the full date range.
- If no period is selected (multi-select mode), `SELECTEDVALUE` returns its alternate value — set a default (e.g., "1M").
- Bittar's Market Watch article combines this pattern with the new slicer and Field Parameters for a complete stock analysis dashboard.

## Related

- [[EDATE]] — subtract months for the minimum date
- [[SELECTEDVALUE]] — read period from slicer
- [[Build-Period-Table]] — create the period lookup table
- [[New-Power-BI-Slicer-Features]] — use the new slicer for period selection
