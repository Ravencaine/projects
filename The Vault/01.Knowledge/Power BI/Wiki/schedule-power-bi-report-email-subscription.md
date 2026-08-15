---
created: 2026-08-15
source: "7 Powerful Ways to Share Your Power BI Reports Effectively.md"
source_url: https://medium.com/write-a-catalyst/7-powerful-ways-to-share-your-power-bi-reports-effectively-bbb33afe301f
note_type: pattern
tags: [power-bi, sharing, email, subscription, automation]
---

# Schedule Power BI Report Email Subscription

<!-- Send a recurring snapshot of a report to a list of recipients by email -->

## Purpose

Deliver a report to a fixed list of recipients on a schedule (daily, weekly, monthly) without requiring them to open Power BI. The recipient receives the snapshot — by default as a screenshot in the email body, or as an attached PDF.

## Components

- A Power BI report in a workspace
- One or more recipient email addresses (internal to the tenant)
- A subscription schedule: frequency, day-of-week / day-of-month, time

## Structure

```
Power BI Service → report → Subscribe
                                  ↓
                     recipients + frequency + time
                                  ↓
                    email with embedded snapshot
                            OR
                    email with PDF attachment
```

## Workflow

1. Open the report in Power BI Service.
2. Click **Subscribe** (or **Subscribe to report** in the menu).
3. Under **Subscribers**, add recipients (individuals or distribution groups).
4. Set **Frequency** (daily, hourly on weekdays, weekly, monthly) and a **Send time**.
5. Optionally include a link back to the report and a short message.
6. Choose the delivery format: **Report pages embedded** in the email body OR **PDF attachment** (if Power BI administrators allow PDF subscriptions).
7. Click **Save**. The subscription is active.

## Example

A retail operations team sends a daily sales summary to every regional manager:

- Open `Daily Sales Summary` report.
- **Subscribe** → add the regional-managers distribution group.
- Frequency: **Daily**, time: **06:00 local**.
- Delivery: **PDF attachment** so managers can archive or forward.
- Save. Each morning, the group receives a fresh PDF snapshot of the previous day's numbers.

## Variations

- **Per-page subscriptions** — subscribe to the whole report or to specific pages only.
- **Data-driven subscriptions** (paginated reports only) — generate per-recipient content using parameters from a database. See [[dynamic-subscriptions-with-email-in-power-bi-paginated-reports-part-2.md]] if it exists in your KB.
- **Manage centrally** — admins can view and edit subscriptions across the org in the Admin portal.

## License

- Sender: **Power BI Pro or Premium**.
- Recipients: must have access to the underlying report (workspace access or share). Recipients do **not** need a Pro license to view the embedded snapshot in their email; they only need Pro if they click through to the live report.

## Related

- [[power-bi-sharing-methods-compared.md]] — comparison
- [[export-power-bi-report-pdf-or-powerpoint.md]] — pattern (one-off export counterpart)
- [[share-via-power-bi-service-workspace-or-app.md]] — pattern (live-access counterpart)