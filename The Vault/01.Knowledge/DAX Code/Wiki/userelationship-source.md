---
created: 2026-07-27
updated: 2026-08-02
source: "RELATIONSHIP in DAX: Unlocking Role-Playing Dimensions"
source_url: "https://medium.com/write-your-world/relationship-in-dax-unlocking-role-playing-dimensions-ac67667d2618"
note_type: source
tags: [dax, userelationship, role-playing-dimensions, inactive-relationships]
---

# RELATIONSHIP in DAX: Unlocking Role-Playing Dimensions

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-12-07
> **URL:** https://medium.com/write-your-world/relationship-in-dax-unlocking-role-playing-dimensions-ac67667d2618
> **Routed to:** DAX Code

## Summary

USERELATIONSHIP() activates an existing inactive relationship between two tables for the scope of a CALCULATE expression. This enables role-playing dimensions (e.g., Invoice Date and Ship Date both filtering the same Date table) without duplicating the Date dimension.

## Key Claims

- Power BI allows only ONE active relationship between two tables; inactive relationships exist but are dormant
- USERELATIONSHIP activates an inactive relationship temporarily within CALCULATE
- Never duplicate Date tables for role-playing — use USERELATIONSHIP with a single Date table
- SWITCH + SELECTEDVALUE enables dynamic switching between role-playing dimensions via slicer

## Extracted Notes

- [[userelationship-function]] — function
- [[role-playing-dimensions-pattern]] — pattern
- [[treatas-vs-userelationship-comparison]] — comparison

## Metadata

| Field | Value |
|-------|-------|
| Source file | RELATIONSHIP in DAX — Unlocking Role-Playing Dimensions.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~820 |
