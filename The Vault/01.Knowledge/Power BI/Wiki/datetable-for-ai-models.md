---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: snippet
tags: [dax, date-table, time-intelligence, ai, forecasting]
---

# DateTable DAX for AI Models

DAX snippet to create a dedicated date table — required for time intelligence features and AI forecasting to work correctly in Power BI.

## Code

```dax
DateTable =
CALENDAR(
    MIN(Sales[OrderDate]),
    MAX(Sales[OrderDate])
)
```

## When to Use

- Any Power BI model that uses time intelligence (YTD, QTD, YoY, etc.)
- AI forecasting features (Anomaly Detection, Python forecasting)
- Key Influencers or Copilot analysis involving date-based metrics

## Variations

Add fiscal year and additional columns:

```dax
DateTable =
ADDCOLUMNS(
    CALENDAR(
        MIN(Sales[OrderDate]),
        MAX(Sales[OrderDate])
    ),
    "Year", YEAR([Date]),
    "Month", FORMAT([Date], "MMMM"),
    "Month Number", MONTH([Date]),
    "Quarter", "Q" & QUARTER([Date]),
    "Year-Month", FORMAT([Date], "YYYY-MM"),
    "Day of Week", FORMAT([Date], "dddd"),
    "Day of Week Number", WEEKDAY([Date], 2)  -- Monday=1
)
```

Mark the table as a date table in Model View → mark as date table → select the Date column.

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[time-intelligence-functions-overview]] — DAX Code KB
