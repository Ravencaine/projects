---
created: 2026-08-01
updated: 2026-08-02
source: "Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md"
note_type: atomic
tags: [dax, date-table, calendar-table, time-intelligence, beginner]
---

# Date Table: Requirements for Time Intelligence

DAX doesn't see dates like humans do — `Sales[Date]` is just numbers to it. A Date table teaches DAX to think in periods.

## What DAX Needs from a Date Table

DAX can calculate anything but doesn't inherently "see" that 01-Jan-2025 and 31-Jan-2025 belong to the same month. The Date table bridges that gap.

## Minimum Requirements

| Requirement | Why it matters |
|-------------|---------------|
| **Continuous date range** | Gaps break SAMEPERIODLASTYEAR and DATESYTD |
| **Year column** | YTD and YoY comparisons need it |
| **Month column** | MTD and month-level filtering |
| **Quarter column** | QTD and quarter-level analysis |
| **Week column** (optional) | WTD and week-based reporting |
| **DateKey / unique key** | Relationship anchor to fact tables |
| **No missing dates** | Even one gap corrupts time intelligence |

## Mark as Date Table

In Power BI Desktop:

```
Right-click Date table → Mark as date table → Select the Date column
```

This tells Power BI which column represents dates — without it, time intelligence functions can give unexpected results.

## Star Schema: One Date Table

Rule: build **one central Date table** and relate all fact tables to it.

```
        ┌─────────────────┐
        │    Date Table   │
        │  (DateKey, Y/M/Q)│
        └────────┬────────┘
                 │ (1-to-many)
     ┌───────────┼──────────────┐
     ▼           ▼              ▼
┌─────────┐ ┌─────────┐ ┌──────────┐
│  Sales  │ │ Orders  │ │ Payments │
└─────────┘ └─────────┘ └──────────┘
```

Do NOT use separate date columns from each fact table for time intelligence — create one shared Date dimension.

## The Intern Gotcha

Using `TransactionDate` instead of the official `'Date'` table breaks ALL time intelligence:
- YTD shows wrong totals
- YoY comparisons misalign
- QTD/MTD calculations produce incorrect results

Always verify: every time intelligence measure references the **central Date table**, not individual fact date columns.

## Related

- [[ytd-qtd-mtd-functions]] — using Date table with DATESYTD/DATESQTD/DATESMTD
- [[sameperiodlastyear-yoY]] — Date table as prerequisite for SAMEPERIODLASTYEAR
- [[time-intelligence-star-schema]] — single Date dimension connecting all facts
