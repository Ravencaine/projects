---
created: 2026-08-13
source: Top Use Cases of Multi-Row Cards in Power BI
source_url: https://medium.com/write-a-catalyst/top-use-cases-of-multi-row-cards-in-power-bi-19934e239698
note_type: atomic
tags: [power-bi, multi-row-card, transaction, invoice, audit]
---

# Multi-Row Card for Transaction/Invoice Details

Display transaction fields — Transaction ID, Date, Amount, Mode of Payment, Status — as a clear, single-record audit view.

## Purpose

Provides a clean way to surface and audit individual records. Works as a confirmation panel after a transaction is selected, replacing a modal or sub-report.

## When to Use

- Financial or accounts payable/receivable dashboards
- Audit or compliance reports
- Transaction history reports with drill-through to individual records

## Design Notes

- Format Amount with currency; format Date as a short date
- Color-code Status field (e.g., green = completed, red = failed, amber = pending)
- Keep Transaction ID clearly visible as the primary identifier

## Related

- [[Multi-Row-Card-as-Profile-Detail-Panel]]
- [[Multi-Row-Card-Best-Practices]]
