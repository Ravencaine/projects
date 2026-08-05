---
created: 2026-08-05
updated: 2026-08-05
source: Power BI Dashboards Decision-Making (Boniface Muchendu)
note_type: atomic
tags: [power-bi, dashboard, kpi, alert, card-visual, threshold, notification]
---

# KPI Alert Setup in Power BI

Setting up proactive KPI alerts on card visuals so that critical metric shifts trigger email or push notifications — no DAX, built directly into the card visual settings.

## Definition

A KPI alert fires when a metric crosses a defined threshold (greater than, less than, percentage change) and notifies a designated individual or distribution list via email or Power BI mobile push notification.

## How to Set Up

1. Add a **Card visual** to the dashboard and pin it
2. On the dashboard tile, click the **ellipsis (⋯) → Manage alerts**
3. In the Alert rules pane: click **+ Add alert**
4. Set the **condition**: value is greater than / less than / percentage change exceeds X
5. Set the **notification method**: email or Power BI mobile push
6. Assign recipients (individual emails or distribution list)

## Visual Recommendations

| Visual | Why |
|--------|-----|
| **Card** | Single metric per tile — ideal for alert targets (sales, conversion rate, stock) |
| **Gauge** | Shows current value against threshold visually before alert fires |

## Smart Threshold Design

- Set thresholds based on business logic, not arbitrary round numbers
- Avoid thresholds that fire on every refresh — tune to meaningful change
- Review and update thresholds quarterly as baselines shift

## Limitations

- KPI alerts only work on **dashboard tiles**, not on report page visuals
- Alerts check on refresh — not real-time; frequency depends on dataset refresh schedule
- Applies to the **published dashboard** in the Power BI Service, not Desktop

## Related

- [[Executive-One-Pager-Dashboard-Design]]
- [[KPI-Alert-Setup-Power-BI]] — same concept, see also
- [[Dashboard-Bonus-Tips]]
