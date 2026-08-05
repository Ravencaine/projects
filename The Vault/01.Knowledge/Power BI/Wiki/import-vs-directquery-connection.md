---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Connecting to Your First Data Source.md"
note_type: atomic
tags: [power-bi, import-mode, directquery, data-source, performance, beginner]
---

# Import vs DirectQuery Connection

When connecting to most data sources, Power BI asks you to choose a connection mode. This choice has permanent consequences for performance, features, and refresh behaviour.

## Import Mode

Power BI pulls a snapshot of the data from the source and stores it in compressed format inside the .pbix file.

| Characteristic | Detail |
|---------------|--------|
| Performance | Fast — data is local, no network latency |
| Feature support | Full — all DAX, calculated tables, and modelling features available |
| Data freshness | Snapshot only — stale after next refresh |
| File size | Grows with data volume; large imports can produce multi-GB .pbix files |
| Best for | Data that changes infrequently; smaller-to-medium datasets; full feature access |

## DirectQuery Mode

Power BI leaves the data in the source and queries it at runtime whenever a visual needs to render.

| Characteristic | Detail |
|---------------|--------|
| Performance | Depends on source query speed and network; can be slow for complex queries |
| Feature support | Restricted — some DAX functions, calculated tables, and data transformations unavailable |
| Data freshness | Always current — queries run against live source |
| File size | Small — no data stored in .pbix |
| Best for | Large datasets that can't be imported; situations where data freshness is critical |

## The Critical Rule

> **You cannot switch a published data source from Import to DirectQuery (or vice versa) after setup.**

The choice is made at connection time. If you publish a model with Import and later realise you need DirectQuery, you must remove the data source and reconnect from scratch — losing any transformations, relationships, and measures built on the original connection.

## Which to Choose

| Scenario | Mode |
|----------|------|
| Data under 1 GB, changes daily or weekly | Import |
| Data changes in real time and must always reflect source | DirectQuery |
| Need calculated tables or full DAX features | Import |
| Dataset larger than Power BI Service capacity | DirectQuery or Aggregations |
| On-premises database with large data volume | DirectQuery |
| Unknown or mixed refresh requirements | Import (more flexible) |

When in doubt, Import is the safer default. The irreversibility of DirectQuery makes it a commitment.

## Related

- [[load-vs-transform-data]] — what happens before this choice
- [[file-based-data-sources-power-bi]] — Import applies to all file-based sources
