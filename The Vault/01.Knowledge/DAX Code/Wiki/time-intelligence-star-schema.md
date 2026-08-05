---
created: 2026-08-01
updated: 2026-08-02
source: "Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md"
note_type: atomic
tags: [dax, time-intelligence, star-schema, data-modeling, date-table, beginner]
---

# Time Intelligence Star Schema: Single Date Dimension

Build one central Date table and relate every fact table to it. Multiple date columns (InvoiceDate, ShipDate, DueDate) need one shared Date dimension — not separate date columns for time intelligence.

## The Problem: Multiple Date Columns

Fact tables often have multiple date columns:

```
Sales
├── OrderDate
├── ShipDate
├── InvoiceDate
└── DueDate
```

Using `OrderDate` for one measure and `InvoiceDate` for another — each pointing to different date references — breaks the unified time intelligence model.

## The Solution: Star Schema with One Date Dimension

```
                    ┌──────────────────┐
                    │   DimDate        │
                    │ (central Date    │
                    │  dimension)      │
                    │                  │
                    │ DateKey          │
                    │ Year             │
                    │ Quarter          │
                    │ Month            │
                    │ Week             │
                    │ FiscalYear       │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │  Sales   │   │  Orders  │   │ Payments │
        │Fact table│   │Fact table│   │Fact table│
        │InvoiceDt │   │ OrderDt  │   │  DueDate │
        └──────────┘   └──────────┘   └──────────┘
```

Every fact table relates to the **same Date dimension** via its respective date key.

## Why This Matters for Time Intelligence

Time intelligence functions reference ONE Date table:

```c
// References DimDate — but which column?
Sales YTD = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
```

If you use `InvoiceDate` for Sales YTD but `ShipDate` for Shipping YTD — and each has its own mini date table — the measures don't align. Slicers won't sync, YoY comparisons will be off.

With one central Date table: every time intelligence measure uses the same Date column, slicers work across all visuals, and YoY comparisons are consistent.

## The Gotcha: Intern Duplicated the Wrong Table

Tejwani's story: an intern duplicated the report but used `TransactionDate` instead of the official `'Date'` table. YTD broke because:
- The official Date table was marked as the date table
- `TransactionDate` was not
- SAMEPERIODLASTYEAR returned wrong/blank results

**Lesson: verify every measure references the marked Date table, not a fact column.**

## Checklist for Time Intelligence Models

- [ ] One central Date dimension table
- [ ] Date column marked as Date Table in Power BI
- [ ] Continuous date range (no gaps)
- [ ] All fact tables related to Date dimension via date keys
- [ ] All time intelligence measures use the Date dimension, not fact date columns
- [ ] Fiscal year column included if using non-calendar fiscal years

## Related

- [[time-intelligence-date-table-requirements]] — Date table requirements
- [[ytd-qtd-mtd-functions]] — measures that use the central Date table
- [[sameperiodlastyear-yoY]] — YoY that depends on unified date context
