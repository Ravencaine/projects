---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Row-level Security in Power BI.md"
source_url: https://databear.com/dynamic-row-level-security-in-power-bi/
note_type: source
tags: [power-bi, rls, row-level-security, dynamic-rls, security, databear, boniface-muchendu]
---

# Dynamic Row-level Security in Power BI (Data Bear)

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2022-10-30
> **URL:** https://databear.com/dynamic-row-level-security-in-power-bi/
> **Routed to:** Power BI

## Summary

Dynamic RLS: users' report access depends on login credentials (USERPRINCIPALNAME()). More secure than static RLS; supports one user → multiple roles and many users → many roles. Implementation: create sales rep table (with Power BI usernames), create transactions table (with sales rep column), establish relationship, create role with USERPRINCIPALNAME() DAX filter, assign roles in Power BI Service after publish.

## Key Claims

- Dynamic RLS: access controlled by USERPRINCIPALNAME() — matches logged-in user's credentials
- Two tables required: user table (with Power BI account usernames) + transactions table (with owner/role column)
- Create relationship between user table and data table
- In Power BI Desktop: Modeling tab → Manage Roles → create role → DAX filter using USERPRINCIPALNAME()
- Add users in Power BI Service (post-publish): Security tab → dataset → Members → add by email
- Verify roles: "Other users" box in Power BI Desktop → enter username → view permissions
- DAX filter example: `USERPRINCIPALNAME()` replaces username value in filter expression

## Metadata

| Field | Value |
|-------|-------|
| Source file | Dynamic Row-level Security in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
