---
created: 2026-08-13
source: "5 Mistakes Beginners Make in Microsoft Fabric (And How to Avoid Them)"
source_url: "https://medium.com/powerbi-microsoft-fabric/5-mistakes-beginners-make-in-microsoft-fabric-and-how-to-avoid-them-269ac1739472"
note_type: atomic
tags: [microsoft-fabric, governance, security, rls, workspace]
---

# Governance Cannot Be an Afterthought in Fabric

Fabric makes it easy to build and share — but that ease creates data governance debt if you do not plan for control from the start.

## Definition

Fabric governance covers three layers: **access control** (who can see what), **data sensitivity** (how sensitive is the data), and **workspace structure** (how workspaces map to business units and projects).

## Key Points

**The risk:** Fabric workspaces are easy to create and share broadly. Without governance:

- **Data leaks** — sensitive data accessible to people who should not see it
- **Report confusion** — multiple versions of the same metric across unorganized workspaces
- **Loss of trust** — users stop trusting reports because they do not know which is authoritative

**The solution is three-pronged:**

1. **Role-based access control** — assign roles (Admin, Member, Contributor, Viewer) at the workspace level
2. **Row-Level Security (RLS)** — restrict data visibility by user role within the semantic model
3. **Sensitivity labels** — apply Microsoft Purview sensitivity labels to datasets and reports

**Workspace structure matters.** Group related items (Lakehouse, datasets, reports) in the same workspace and assign access at the workspace level rather than per-item.

## Common Beginner Mistake

Granting full dataset access to all report consumers instead of using RLS. This is the fastest way to expose data that should be restricted.

## Related

- [[skipping-lakehouse-causes-problems]] — the modeling consequences of skipping governance planning
- [[power-bi-subscription-workflow]] — sharing and distribution patterns that need governance
- [[pii-detection]] — identifying sensitive data before applying labels
