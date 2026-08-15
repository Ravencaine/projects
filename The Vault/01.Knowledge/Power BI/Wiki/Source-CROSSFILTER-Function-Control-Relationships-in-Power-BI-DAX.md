---
created: 2026-08-09
updated: 2026-08-09
source: "CROSSFILTER Function Control Relationships in Power BI DAX.md"
source_url: https://databear.com/crossfilter-function-in-dax/
note_type: source
tags: [dax, crossfilter, relationship, bidirectional, databear, boniface-muchendu]
---

# CROSSFILTER Function: Control Relationships in Power BI DAX

Use CROSSFILTER in DAX to override relationship filter direction within a CALCULATE — useful for ad-hoc bidirectional filtering without permanently changing the model.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2022-10-15
> **URL:** https://databear.com/crossfilter-function-in-dax/
> **Routed to:** Power BI

## Summary

CROSSFILTER is not a scalar or table function — it is a relationship-control function that changes how filters propagate between tables for the duration of a single CALCULATE. It requires an existing physical relationship and only works inside CALCULATE. The article demonstrates bridging a gap where Customer filters Internet Sales, but Internet Sales also needs to filter back through Product to Reseller Sales — a case where CROSSFILTER with `BOTH` enables a measure that would otherwise return wrong results.

## Key Claims

- CROSSFILTER only works with an existing relationship (cannot create a new one)
- CROSSFILTER is a CALCULATE-only function
- The `BOTH` direction makes a one-directional relationship bidirectional for that calculation only
- Prefer CROSSFILTER over permanently changing model relationships when bidirectional filtering is needed only for specific measures
- The `Oneway_LeftFiltersRight` and `Oneway_RightFiltersLeft` options apply to one-to-one relationships where you want directional control in a single direction without full bidirectionality

## Example: Reseller Sales of Products Purchased by a Customer

```dax
Reseller Sales of products purchased by a particular customer =
CALCULATE(
    SUM(FactResellerSales[Reseller Sales]),
    CROSSFILTER(
        DimProduct[ProductKey],
        FactInternetSales[ProductKey],
        BOTH
    )
)
```

This bridges: DimCustomer → FactInternetSales → DimProduct → FactResellerSales. Without CROSSFILTER, the relationship from DimProduct to FactInternetSales is one-directional and the measure returns nothing meaningful.

## Direction Options

| Direction | Effect |
|-----------|--------|
| `NONE` | Disables cross-filtering entirely for this relationship |
| `BOTH` | Bidirectional — filter propagates both ways |
| `ONEWAY` | Standard one-directional (many-to-one, one filters many) |
| `ONEWAY_LEFTFILTERSRIGHT` | One-to-one: left table filters right table |
| `ONEWAY_RIGHTFILTERSLEFT` | One-to-one: right table filters left table |

## Extracted Notes

- [[CROSSFILTER-Oneway-Directional-Options]] — `atomic` — `ONEWAY_LEFTFILTERSRIGHT` and `ONEWAY_RIGHTFILTERSLEFT` for one-to-one relationships

## Metadata

| Field | Value |
|-------|-------|
| Source file | CROSSFILTER Function Control Relationships in Power BI DAX.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~550 |
