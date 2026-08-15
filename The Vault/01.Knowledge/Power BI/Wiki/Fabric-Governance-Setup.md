---
created: 2026-08-13
source: 5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)
note_type: workflow
tags: [governance, rls, microsoft-fabric, security, role-based-access, sensitivity-labels, workspace]
---

# Fabric Governance Setup

<!-- Source: Anurodh Kumar, "5 Mistakes Beginners Make in Microsoft Fabric", 2026-05-03 -->

## Prerequisites

- Microsoft Fabric capacity (Premium per capacity or Fabric capacity)
- Fabric workspace created
- Admin access to Microsoft Purview (for sensitivity labels)
- Identified data owners and consumer roles

## Steps

1. **Define roles** — map business roles to Fabric workspace roles (Admin, Member, Contributor, Viewer)

2. **Create workspace structure** — one workspace per domain/project; do not mix unrelated workloads

3. **Apply Row-Level Security (RLS)** — in the semantic model, define DAX filter roles that restrict data by user principal:
   ```dax
   -- Role: SalesRegion
   [Region] = USERNAME()
   ```
   Assign users to roles in the Power BI service.

4. **Apply sensitivity labels** — use Microsoft Purview compliance centre to label semantic models and lakehouse items:
   - `Confidential` — restricted to named groups
   - `Highly Confidential` — encryption + no export
   - `General` — org-wide

5. **Document workspace ownership** — assign an owner to each workspace; owners are responsible for access grants and retention policies.

## Variations

**Hierarchical RLS:** Finance sees all regions; Regional Managers see only their region; Analysts see only their team.

**Column-level security:** Restrict access to sensitive columns (salary, PII) even within a role — add filter on the column itself.

## Common Errors

- Giving full dataset access instead of RLS → data leaks
- No workspace owner assigned → nobody accountable for access decisions
- Skipping sensitivity labels → compliance audit failures

## Related

- [[Source-Dynamic-Row-level-Security-in-Power-BI]] — RLS vs CLS in Power BI
- [[End-to-End-Fabric-Pipeline]] — pipeline that governance protects
- [[Medallion-Architecture-Fabric]] — layers that governance secures
