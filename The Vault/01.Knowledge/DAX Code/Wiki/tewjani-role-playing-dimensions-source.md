---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
source_url: "https://medium.com/write-your-world/relationship-in-dax-unlocking-role-playing-dimensions-ac67667d2618"
note_type: source
tags: [dax, power-bi, relationships, role-playing-dimensions, uselationship, beginner]
---

# Role-Playing Dimensions in DAX — Gulab Chand Tejwani

> **Type:** pattern guide / beginner
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-12-07
> **URL:** https://medium.com/write-your-world/relationship-in-dax-unlocking-role-playing-dimensions-ac67667d2618
> **Routed to:** DAX Code
> **KB:** DAX Code

## Summary

How to handle multiple date columns in a fact table (e.g., InvoiceDate, ShipDate) that each need their own relationship to a single Date dimension. Power BI allows only one active relationship between two tables — all others are inactive by default. The solution is USERELATIONSHIP(), which temporarily activates an inactive relationship within CALCULATE. Covers: the role-playing problem, USERELATIONSHIP mechanics, why not to duplicate date tables, dynamic date switching with SWITCH + SELECTEDVALUE, common mistakes, and best practices.

## Extracted Notes

- [[uselationship-function]] — `atomic` — Temporarily activates an inactive relationship inside CALCULATE; does not create relationships
- [[role-playing-dimensions-pattern]] — `atomic` — Single Date dimension + inactive relationships vs duplicated date tables; one Date table keeps filters unified
- [[dynamic-date-switching-with-switch]] — `atomic` — SWITCH + SELECTEDVALUE + parameter table for dynamic date type switching via slicer
- [[uselationship-common-mistakes]] — `atomic` — Top mistakes: using on active relationships, forgetting CALCULATE wrapper, cross-filter direction errors
- [[shipping-delay-dax]] — `atomic` — AVERAGEX + DATEDIFF across InvoiceDate/ShipDate pair; real-world example of role-playing in practice

## Metadata

| Field | Value |
|-------|-------|
| Source file | RELATIONSHIP in DAX — Unlocking Role-Playing Dimensions.md |
| Ingestion date | 2026-08-01 |
| Word count | ~850 |
| Level | Beginner |
| Category | Patterns / Relationships |
