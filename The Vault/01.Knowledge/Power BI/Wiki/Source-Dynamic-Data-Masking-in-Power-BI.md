---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic Data Masking in Power BI.md"
source_url: https://evaluationcontext.github.io/posts/data-masking/
note_type: source
tags: [power-bi, data-masking, security, rls, ols, object-level-security, row-level-security, tabular-model, jake-duddy]
---

# Dynamic Data Masking in Power BI (Jake Duddy)

> **Type:** article
> **Author:** Jake Duddy (evaluationcontext.github.io)
> **Published:** 2026-05-11
> **URL:** https://evaluationcontext.github.io/posts/data-masking/
> **Routed to:** Power BI

## Summary

**Critical security gotcha:** DAX-based column masking is NOT security — it only hides values in report visuals while the underlying column remains queryable in the semantic model. True data masking requires OLS (Object Level Security) on the source column, not DAX on top of it. RLS and OLS cannot be combined across different roles.

## Key Claims

### Why DAX Masking Is Not Security
- Common pattern: `IF([Can View PII], SELECTEDVALUE(Customer[Email]), "********")`
- Issue: unmasked column still exists in the semantic model
- Users with Build permission, Analyze in Excel, XMLA endpoint, or copied reports can query the original column
- Obscurity ≠ security

### OLS as Proper Data Masking
- Object Level Security restricts access to tables and columns at the model level
- RLS filters rows; OLS restricts tables/columns
- A secured column cannot be queried through any route — not visuals, not XMLA, not Excel

### RLS + OLS Restriction
- RLS and OLS cannot be combined in different roles on the same model
- Query-time error for users who are members of such mixed roles
- Both security mechanisms must be in the same role

### DirectQuery Note
- Not covered in this article
- Masking in DirectQuery scenarios can often be applied in the source (Lakehouse/Warehouse)
- Different considerations for SSO passthrough and gateways

## References
- [MS: Row Level Security](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security)
- [MS: Object Level Security](https://learn.microsoft.com/en-us/fabric/security/service-admin-object-level-security)
- [SQLBI: Security in Tabular Models](https://www.sqlbi.com/whitepapers/security-in-tabular-semantic-models/)

## Metadata

| Field | Value |
|-------|-------|
| Source file | Dynamic Data Masking in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
