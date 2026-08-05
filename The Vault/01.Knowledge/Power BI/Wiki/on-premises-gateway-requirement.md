---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, gateway, on-premises, data-refresh, power-bi-service, beginner]
---

# On-Premises Gateway Requirement

The Power BI Gateway is the bridge between on-premises data sources (databases, file shares, on-premises SharePoint) and Power BI Service. Without it, scheduled and automatic refresh of on-premises data in the cloud is not possible.

## When the Gateway Is Required

The gateway is needed when **all three conditions are true**:
1. Your data source is on-premises (not cloud-hosted)
2. You have published a Power BI report to Power BI Service
3. You want the report to refresh on a schedule or trigger a manual refresh from the cloud

## What It Does

| Function | Detail |
|---------|--------|
| Secure channel | Encrypts credentials and maintains a secure connection from Power BI Service to your on-premises network |
| Credential storage | Stores database credentials in the gateway (not in Power BI Service directly) |
| Scheduled refresh | Enables automatic refresh schedules set in Power BI Service |
| Multiple sources | One gateway can serve multiple reports and multiple on-premises data sources |

## Gateway Types

| Type | Best for |
|------|----------|
| **On-premises data gateway (standard mode)** | Enterprise: multiple users, multiple data sources, IT-managed |
| **On-premises data gateway (personal mode)** | Individual: single user, personal reports; simpler setup but less manageability |

## What Does NOT Require a Gateway

- Excel/CSV/JSON files stored in OneDrive or SharePoint Online
- Cloud databases (Azure SQL, Snowflake, Databricks)
- Web data sources
- Power BI datasets and dataflows
- Any source already accessible from the internet

## Setup Requirement

The gateway must be installed on a machine that stays powered on and connected to the internet during scheduled refresh times. A laptop that sleeps or shuts down cannot run scheduled refresh.

## Related

- [[database-authentication-types]] — gateway stores credentials, not just connection strings
- [[cloud-data-sources-onedrive-sharepoint]] — cloud sources that don't need the gateway
- [[data-source-documentation-practice]] — document gateway requirements alongside connection details
