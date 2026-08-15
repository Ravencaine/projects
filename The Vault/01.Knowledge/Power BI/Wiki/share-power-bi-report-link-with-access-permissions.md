---
created: 2026-08-15
source: "7 Powerful Ways to Share Your Power BI Reports Effectively.md"
source_url: https://medium.com/write-a-catalyst/7-powerful-ways-to-share-your-power-bi-reports-effectively-bbb33afe301f
note_type: pattern
tags: [power-bi, sharing, permissions, access-control]
---

# Share Power BI Report Link with Access Permissions

<!-- Send a report link to specific people and control what they can do with it -->

## Purpose

Distribute a Power BI report directly to named colleagues with per-user access controls — instead of (or in addition to) bundling the report into a Workspace App. This is the lightweight channel for ad-hoc sharing when you don't want to set up an App.

## Components

- The published report in a Power BI workspace
- The recipient's email address (must be a recognised identity in the tenant, or a B2B guest — see [[share-power-bi-report-external-users-b2b.md]])
- Permission flags: **Allow reshare** and **Build permission**

## Structure

```
Report → Share → enter email(s) → choose permissions → Send
                                              ↓
                                   recipient receives link
                                              ↓
                                   click → opens in Service
```

## Workflow

1. Open the report in Power BI Service.
2. Click **Share** in the toolbar.
3. Enter the email addresses of the recipients (one or many).
4. Configure permissions:
   - **Allow recipients to share this report** — toggles whether viewers can re-share.
   - **Build permission** — lets recipients create their own reports on top of the underlying dataset.
5. Optionally add a message and click **Send**.
6. Recipients get a notification + email with a link that opens the report in the Service.

## Example

A sales manager wants the regional leads to see (but not reshare) the latest pipeline report:

- Open `Pipeline.pbix` report in the Service.
- **Share** → enter four regional-lead emails.
- Uncheck **Allow reshare** so leads cannot forward the link internally.
- Leave **Build permission** off — they should only consume, not author new reports on the dataset.
- Send.

## Variations

- **Share with the whole tenant** — leave the email field empty and the report becomes discoverable by anyone in the org with link + appropriate license. Use sparingly; prefer Apps for broad distribution.
- **Reshare + Build** — common when handing a dataset to an analytics team that will author downstream reports.
- **Read-only reshare** — most common; balances reach with control.

## License

- Sender: **Power BI Pro**.
- Viewer: **Power BI Pro**, OR the workspace must be backed by **Premium capacity** (in which case Pro is required only on the sharer).

## Related

- [[power-bi-sharing-methods-compared.md]] — comparison
- [[share-via-power-bi-service-workspace-or-app.md]] — pattern (App-based distribution)
- [[share-power-bi-report-external-users-b2b.md]] — pattern (for recipients outside the tenant)