---
created: 2026-08-13
source: Top Use Cases of Multi-Row Cards in Power BI
source_url: https://medium.com/write-a-catalyst/top-use-cases-of-multi-row-cards-in-power-bi-19934e239698
note_type: atomic
tags: [power-bi, multi-row-card, profile-card, drill-through, detail-panel]
---

# Multi-Row Card as Profile/Detail Panel

Show a complete entity profile — Employee Name, Department, Designation, Performance Score — when a user selects a row, region, or record.

## Purpose

Functions as a dynamic profile card or info panel. Acts as a lightweight drill-through without requiring a separate report page. The card updates contextually based on the current filter/selection.

## When to Use

- HR or workforce dashboards (employee profiles)
- Selection-driven detail panels in any report
- Sidebar context beside a main visual
- Tooltip panels for drill-through pages

## Design Notes

- Works best when the visual is synced to a slicer or selection via drill-through
- Keep field count to 4–5 to avoid clutter
- Use consistent label:value formatting for scannability

## Related

- [[Multi-Row-Card-as-KPI-Summary]]
- [[Multi-Row-Card-for-Customer-Information]]
- [[Multi-Row-Card-Best-Practices]]
