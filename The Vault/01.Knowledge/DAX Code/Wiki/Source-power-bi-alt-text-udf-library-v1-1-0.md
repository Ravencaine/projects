---
created: 2026-08-08
source: Power BI Alt Text UDF Library
source_url: https://github.com/Juls-BI/powerbi-alttext-udfs
note_type: source
tags: [dax, accessibility, udf, power-bi, alt-text]
---

# Power BI Alt Text UDF Library v1.1.0 — Source

Six new DAX User-Defined Functions generating structured, screen-reader-friendly alt text for KPI visual patterns. Parameter-driven, visual-agnostic, no internal model references.

> **Type:** article
> **Author:** Juls
> **Published:** 2026-07-11
> **URL:** https://github.com/Juls-BI/powerbi-alttext-udfs
> **Routed to:** DAX Code

## Summary

Library ships as .dax files (one for patterns, one for demo measures). Functions take only parameters (context + values) and output clean narrative strings. Inspired by Alena Shkel's SVG KPI patterns, but generic — works across any visual type. Built using DAX FUNCTION syntax in DAX Query View or TMDL.

## Extracted Notes

- [[juls-bi]] — author
- [[progressbaralttext]] — function — alt text for progress bar visuals
- [[bulletchartalttext]] — function — alt text for bullet/target charts
- [[sparkbarsalttext]] — function — alt text for sparkline bar patterns
- [[ratingdotsalttext]] — function — alt text for star/dot ratings
- [[statuspillalttext]] — function — alt text for status indicator pills
- [[variancechipalttext]] — function — alt text for variance chips
- [[alt-text-udf-workflow]] — pattern — how to use the library files

## Metadata

| Field | Value |
|-------|-------|
| Source file | Power BI Alt Text UDF Library |
| Ingestion date | 2026-08-11 |
| PBIX attachment | [[Attachments/UDF for SVG Pills.pbix]] |
