---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# VarianceChipAltText

DAX UDF generating screen-reader-friendly alt text for a variance chip/badge visual in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context, actual value, and budget/plan value as parameters. Returns a plain-language narrative describing the variance — e.g., "Variance: +$2,000 ahead of plan. Actual $52,000 vs. plan $50,000."

## Design Principles

- Parameter-driven, no internal model references
- Avoids naming chart types or colours
- WCAG accessibility compliant
- Works with any variance chip configuration (absolute or percentage)

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[progressbaralttext]], [[bulletchartalttext]], [[sparkbarsalttext]], [[ratingdotsalttext]], [[statuspillalttext]]
