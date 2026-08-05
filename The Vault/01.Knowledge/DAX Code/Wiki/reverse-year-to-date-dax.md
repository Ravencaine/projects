---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, finance, revenue, forecasting]
---

# Reverse Year-to-Date

## Purpose

Reverse Year-to-Date (*Reverse YTD*) decomposes a **cumulative YTD figure**
back into its **individual monthly values** by subtracting consecutive YTD rows.
This is the inverse of a standard YTD accumulation.

**Why it matters:** Many financial systems store revenue and cost figures as
cumulative YTD totals rather than monthly figures. To do any meaningful
month-over-month analysis, you must first "de-accumulate" the data.

> **Alexis Olson notes:** This technique assumes YTD data exists for *every*
> month with no gaps. If your source system has missing months, prepend logic
> to fill the gaps before applying Reverse YTD.

## Formula

```dax
Reverse YTD =
    VAR __Year        = MAX( 'Year To Date'[Year] )
    VAR __Month       = MAX( 'Year To Date'[Month] )
    VAR __CurrentYTD  = MAX( 'Year To Date'[Revenue YTD] )
    VAR __PreviousYTD = MAXX(
                            FILTER(
                                ALL( 'Year To Date' ),
                                [Year] = __Year && [Month] = __Month - 1
                            ),
                            [Revenue YTD]
                        )
    VAR __Result = __CurrentYTD - __PreviousYTD
    RETURN __Result
```

## Components

| Variable | Role |
|----------|------|
| `__Year` | Current year context from the visual/report |
| `__Month` | Current month context |
| `__CurrentYTD` | Revenue YTD value for the current year/month row |
| `__PreviousYTD` | YTD value for the *prior month* — found by removing all filters<br/>with `ALL()` then re-filtering to `Month = current − 1` |
| `__Result` | Difference = individual month's revenue |

## Data Layout

| Year | Month | Revenue YTD |
|------|-------|------------|
| 2024 | 10    | $110,000,000 |
| 2024 | 11    | $122,000,000 |
| 2024 | 12    | $130,000,000 |
| 2025 | 1     | $12,000,000  |
| 2025 | 2     | $19,000,000  |
| 2025 | 3     | $31,000,000  |
| 2025 | 4     | $42,000,000  |

The YTD column **resets in January** (new fiscal year). Reverse YTD produces:

| Year | Month | Revenue (Reverse YTD) |
|------|-------|----------------------|
| 2024 | 10    | $110,000,000 |
| 2024 | 11    | $12,000,000  |
| 2024 | 12    | $8,000,000   |
| 2025 | 1     | $12,000,000  |
| 2025 | 2     | $7,000,000   |
| 2025 | 3     | $12,000,000  |
| 2025 | 4     | $11,000,000  |

## Key Insight: ALL() for Row-to-Row Comparison

The core trick is `ALL( 'Year To Date' )`, which **removes all filters** from
the table so that you can reach the *previous row's* YTD value regardless of
what the current visual is displaying. Without `ALL()`, the context of the
current row would block access to the prior row.

For the January reset row (where `__Month - 1 = 0`), `FILTER` returns no rows
and `MAXX` returns `BLANK()`, making `__Result` = `__CurrentYTD` — which is
correct, since January YTD *is* January revenue.

## Notes

- **Gap handling:** If months are missing, consider pre-processing with Power
  Query to add missing rows (e.g., using `List.Dates` or `CALENDARAUTO`).
- **Fiscal year resets:** The pattern automatically handles year-boundary resets
  because the prior-month lookup returns BLANK in January, yielding the correct
  monthly figure.
- This pattern generalizes: swap `Month` for any ordinal column (week, quarter)
  to reverse-accumulate at any granularity.

## Related

- [[dax-index-pattern-deckler]] — row-to-row comparison patterns
- [[project-burndown-chart-dax]] — cumulative vs. actual comparisons
