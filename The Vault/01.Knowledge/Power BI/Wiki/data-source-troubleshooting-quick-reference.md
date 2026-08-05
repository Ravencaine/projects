---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, troubleshooting, data-sources, beginner, quick-reference]
---

# Data Source Troubleshooting Quick Reference

Four canonical connection problems and their root causes. Most failures fall into one of these four categories.

## 1. Authentication / Permission Failures

**Symptoms:** "Login failed", "User does not have permission", "Access denied", connection dialog repeatedly prompting for credentials.

**Root cause:** Credentials are wrong, expired, or the database/folder account doesn't have read access.

**Fixes:**
- Verify username and password with IT
- Confirm the account has read permission on the specific table, file, or site
- For cloud services, check that appropriate licenses are assigned (e.g., Power BI Pro licence needed for SharePoint connections)
- For Windows auth, confirm you're logged into the correct Windows account on the Power BI machine

## 2. Network / Connectivity Failures

**Symptoms:** Connection times out, "unable to connect", extremely slow initial load, connection works on one machine but not another.

**Root causes:** Firewall blocking the port, VPN not connected, source server down, network routing issue.

**Fixes:**
- Test basic connectivity (ping, telnet) to the server or URL
- Check firewall rules with IT for the specific port (e.g., 1433 for SQL Server)
- For on-premises databases: ensure the Power BI Gateway is running and the machine has network access
- For cloud sources: confirm internet access and that the service is operational (check status pages for Azure, SharePoint, OneDrive)

## 3. Data Type Recognition Failures

**Symptoms:** Numbers showing as text, dates formatted as serial numbers, columns appearing blank after import, unexpected "Error" cells.

**Root causes:** Power BI auto-detected the wrong type, source data has hidden characters or formatting, inconsistent data formats in the source.

**Fixes:**
- Use **Transform Data** to open Power Query Editor before loading
- Change data types using the type icon next to each column header
- Check for hidden characters: use View → Show Whitespace in Power Query Editor
- For dates: ensure consistent date format across the entire source column before importing

## 4. Performance / Slow Load

**Symptoms:** Data loads slowly or times out, visual rendering is sluggish after load.

**Root causes:** Dataset too large for Import mode, complex source query, network latency, insufficient RAM on the machine.

**Fixes:**
- Consider **DirectQuery** for very large datasets (but note the feature restrictions)
- Check that Power BI is using the correct data types — numeric columns stored as text consume far more memory
- For databases: ask IT if the source tables have indexes on the columns used for filtering
- Reduce the number of columns imported — import only what's needed for the report

## Related

- [[database-authentication-types]] — root cause of category 1 failures
- [[on-premises-gateway-requirement]] — required for category 2 failures with on-premises databases
- [[load-vs-transform-data]] — fix for category 3 failures
