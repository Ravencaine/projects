---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, database, authentication, security, beginner]
---

# Database Authentication Types

Connecting Power BI to SQL Server, MySQL, PostgreSQL, or other databases requires credentials. Getting authentication wrong is the most common reason database connections fail.

## Authentication Methods by Database Type

### SQL Server

Two primary options in the connection dialog:

| Method | When to use |
|--------|-------------|
| **Windows Authentication** (current Windows user) | When your Windows login has database read access; simplest for individual machines |
| **Database Authentication** (username + password) | When database access is managed separately from Windows logins; required for shared or enterprise databases |
| **Microsoft Account** | For SQL Server in Azure or Azure SQL Database |

### MySQL and PostgreSQL

Always use **Database Authentication** (username + password) — these databases do not integrate with Windows authentication. Credentials are created when the database user is provisioned and are independent of Windows.

### Cloud Databases (Azure SQL, Snowflake, etc.)

Typically use:
- **Azure Active Directory** authentication (preferred for Azure services)
- **Username + password** (legacy)
- **Service principal** or managed identity (for automated/scheduled refresh in Power BI Service)

## What to Have Ready Before Connecting

1. **Server name**: e.g., `company-db.database.windows.net` or `sqlserver01.internal.company.com`
2. **Database name**: the specific database you need (optional in some connectors — you can browse)
3. **Credentials**: username and password; for Windows auth, just ensure you're logged into the correct Windows account
4. **Permission confirmation**: IT/DBA must confirm your account has read access to the target tables

## Common Failure Mode

> **"Login failed or user does not have access"** almost always means one of three things: wrong username, wrong password, or insufficient database permissions. Contact IT before spending time on connection settings.

IT departments control database access separately from Windows file access. Having a valid Windows login does not automatically grant database read permissions.

## Related

- [[on-premises-gateway-requirement]] — required when publishing to Power BI Service
- [[data-source-troubleshooting-quick-reference]] — full troubleshooting matrix
- [[import-vs-directquery-connection]] — the mode choice alongside authentication
