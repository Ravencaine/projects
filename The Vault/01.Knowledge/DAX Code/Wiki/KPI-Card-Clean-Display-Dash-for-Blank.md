---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 3
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-3-f152d1b500b5
note_type: pattern
tags: [dax, user-experience, display, blank, card]
---

# KPI Card Clean Display — Return " - " for Blank

KPI cards show BLANK as an empty space. Returning `" - "` makes it explicit that there is no data for the current filter context — cleaner and more informative.

## Problem

`BLANK()` in a KPI card renders as empty space. Users can't tell if there is genuinely no data, the measure is broken, or the visual is loading.

## Solution

```dax
MEASURE [Card_Sales] =
VAR _sales = CALCULATE(SUM(Transactions[NetAmount]))
RETURN
    IF(ISBLANK(_sales), " - ", _sales)
```

## Mechanics

| Condition | Return |
|-----------|--------|
| `_sales` is BLANK | `" - "` (text string) |
| `_sales` has a value | The numeric value |

Returning a text string forces the card to display the text. The visual automatically formats the number when a numeric value is returned.

## Conditional Formatting Rules

Pair with conditional formatting to reinforce meaning:

| Condition | Format |
|-----------|--------|
| `>= 0` | Green |
| `< 0` | Red |
| `BLANK()` | Grey |

## Related

- [[BLANK-vs-Zero]] — BLANK is "no data"; 0 is "explicitly zero"
- [[Sticky-Slicer-This-Month-Auto-Select]] — UX pattern for report defaults
