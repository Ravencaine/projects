---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: reference
tags: [data-warehouse, methodology, inmon, kimball, data-vault, dimensional-modeling]
---

# Inmon vs Kimball vs Data Vault — Decision Framework

Three established data warehouse modeling methodologies. No single approach is universally "best" — fit depends on team size, speed requirements, source system volatility, and regulatory environment.

## Quick Reference

| Approach | Creator | Structure | Direction | Best for |
|----------|---------|-----------|----------|----------|
| **Inmon / EDW** | Bill Inmon | 3NF central warehouse → departmental marts | Top-down | Large orgs, enterprise consistency, long-term strategy |
| **Kimball / Dimensional** | Ralph Kimball | Fact + dimension tables per subject area, unified via conformed dimensions | Bottom-up | Fast delivery, single subject area first, BI-friendly output |
| **Data Vault** | Dan Linstedt | Hubs (keys) + Links (relationships) + Satellites (attributes/history) | Middle-out | Frequently-changing sources, high audit requirements, long-term history |

## Key Decision Questions

- **How large is your team and how quickly do you need value?** Small team, fast results → Kimball. Large team, long runway → Inmon.
- **How many source systems and how often do they change?** Many volatile sources → Data Vault. Stable sources → Kimball or Inmon.
- **Single subject area first or enterprise-wide?** Subject area first → Kimball bottom-up. Whole org at once → Inmon top-down.
- **Regulatory/audit pressure?** High (finance, healthcare) → Data Vault for auditability. Low → Kimball.
- **What does the BI tool expect?** Most BI tools work naturally with dimensional models — even Inmon and Data Vault typically need a Kimball presentation layer.

## Notes

- All three can be blended with modern practices (medallion architecture, ELT) — pure methodology adherence is less important than fit
- Data Vault always requires a dimensional view on top — it is not a layer for direct business user consumption
- Kimball without discipline risks subject-area silos; use the bus matrix to maintain cross-subject-area consistency

## Related

- [[medallion-architecture-raw-cleansed-dimensional]] — raw/cleansed/dimensional layering
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source` — real-world project using Kimball
