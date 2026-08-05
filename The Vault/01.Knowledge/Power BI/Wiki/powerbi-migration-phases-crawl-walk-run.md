---
created: 2026-08-01
updated: 2026-08-02
source: "We Replaced 47 Excel Files With One Power BI Model. Here's What Actually Happened.md"
note_type: atomic
tags: [power-bi, migration, phases, crawl-walk-run, incremental, star-schema]
---

# Power BI Migration Phases — Crawl, Walk, Run

## The 21-Week Migration Timeline

| Phase | Weeks | Focus |
|-------|-------|-------|
| Audit + Priority Matrix | 1–2 | Catalog, interviews, prioritization |
| Data Warehouse Foundation | 3–4 | Star schema, ETL, validation layer |
| Quick Wins | 5–8 | 3 high-impact / low-effort files |
| Big Projects | 9–14 | P&L, commission calcs, executive deck |
| Easy Wins | 15–18 | 6 files per week |
| Parallel Run | 19–20 | Both systems, survey trust |
| Cutover | 21 | Excel → read-only, Power BI only |

Total: 90 days. Extended when needed — don't rush.

## Foundation First (Weeks 3–4)

Most people skip this. Don't.

### Star Schema Design

Fact Tables:
- FactSales (every sales transaction)
- FactInventory (daily inventory snapshots)
- FactFinancials (monthly financial entries)

Dimension Tables:
- DimDate (every day 2020–2030)
- DimProduct, DimCustomer, DimEmployee, DimRegion, DimAccount

### ETL with Validation

Extract:
- ERP sales: every hour
- Warehouse inventory: every 4 hours
- Financial data: nightly

Transform:
- Standardize names ("Widget A" vs "WidgetA" vs "WIDGET-A")
- Validate dates (catch future dates, nulls, invalid formats)
- Calculate derived fields (profit margin, days in inventory)
- Flag anomalies (sales over $100K, negative inventory)

### Incremental Refresh (Critical for Large Datasets)

- Historical (>2 years): load once, never refresh
- Recent (last 2 years): refresh nightly
- Current month: refresh hourly

Result: 3-hour load → 12 minutes.

### Validation Checks Before Load

```sql
-- Row count shouldn't drop more than 10%
-- No future dates
-- Sales total within expected range (flag >3x historical avg)
```

6 data quality issues caught in first month.

## Migration Factory Pattern (Weeks 15–18)

6 files migrated per week:

**Monday:** Audit Excel file, interview owner, document workflow, identify sources

**Tuesday–Wednesday:** Build data model, create basic report, validate calculations

**Thursday:** User testing, fix discrepancies, refine based on feedback

**Friday:** Deploy to test, schedule training

**Next week:** Parallel run, document issues, prepare cutover

## Phase-by-Phase Anti-Patterns

| Mistake | What Actually Happened |
|---------|----------------------|
| "Looks the same as Excel" | User workflow ≠ Excel visual layout |
| "Do everything at once" | Overwhelmed Finance; had to restart with crawl-walk-run |
| "Migrate first, document later" | 47 manual adjustments discovered in P&L — nearly ended the project |
| "Skip parallel run" | Would've missed 17 discrepancies in first week |

## Critical Rule: Rebuild the Workflow, Not the Visuals

Excel file shows: pipeline by stage, conditional formatting, drill-down

User's actual workflow:
1. Which stage has most deals? → Summary pivot
2. Which deals stuck 30+ days? → Drill into detail
3. Filter by rep vs last month? → Compare performance
4. Add notes for at-risk deals? → Annotate directly
5. Export snapshot to VP? → Email Friday subscription

**Don't rebuild what Excel looks like. Rebuild what Excel does.**
