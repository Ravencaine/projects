---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# SparkBarsAltText

DAX UDF generating screen-reader-friendly alt text for a sparkline bar pattern in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context and array of values as parameters and returns a plain-language narrative describing the trend shown by the spark bar — e.g., "Sales trend over the last 6 months: 10k, 12k, 11k, 15k, 14k, 18k. Overall upward trend."

## Design Principles

- Parameter-driven, no internal model references
- Avoids naming chart types or colours
- WCAG accessibility compliant
- Generic: works with any spark bar configuration

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[progressbaralttext]], [[bulletchartalttext]], [[ratingdotsalttext]], [[statuspillalttext]], [[variancechipalttext]]
