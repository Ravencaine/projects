---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-bi, dax, power-query, data-modeling, best-practice]
---

# Calculate Upstream vs DAX

Use DAX for filter-context-dependent calculations; push static row-level business rules to SQL, Power Query, or the data warehouse instead.

## Definition

Not every calculation belongs in DAX. Static row-level business rules — revenue calculations that always add the same columns, classifications that never depend on filter context — are better calculated upstream in SQL, Power Query (M), or the warehouse. DAX measures (aggregations, ratios, context-dependent logic) stay in the semantic model.

## Key Points

- **DAX belongs to**: measures, ratios, aggregations that depend on filter context, time intelligence
- **Upstream belongs to**: row-level business rules that are static, repeatable, and filter-context-independent
- Upstream calculation example: `Net Revenue = Room Revenue + Experience Revenue + Other Revenue - Discount Amount`
- After pushing upstream: a DAX measure becomes trivially `SUM(Net Revenue)` — no row-level logic needed
- **Trade-off**: upstream calculations are faster (computed once at load), DAX calculations are computed at query time
- Row-level calculations that use filter context (e.g., conditional on another column) still belong in DAX
- Roach's maxim: know which layer each type of logic belongs to

## Examples

**Upstream in SQL (computed column):**
```sql
NetRevenue = RoomRevenue + ExperienceRevenue + OtherRevenue - DiscountAmount
```

**Upstream in Power Query (M):**
```
Net Revenue = [Room Revenue] + [Experience Revenue] + [Other Revenue] - [Discount Amount]
```

**DAX after upstream:**
```dax
Total Net Revenue = SUM(Fact_Booking[Net Revenue])
```

## Related

- [[calculate]] — CALCULATE for filter-context-dependent DAX
- [[Measure-Table-Dedicated]] — organizing DAX measures
