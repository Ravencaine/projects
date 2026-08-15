---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# StatusPillAltText

DAX UDF generating screen-reader-friendly alt text for a status indicator pill/badge visual in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context and status value as parameters. Returns a plain-language description of the status — e.g., "Status: On Track. The project is within schedule and budget."

## Design Principles

- Parameter-driven, no internal model references
- Avoids naming chart types or colours
- WCAG accessibility compliant
- Generic: works with any status pill/badge visual

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[progressbaralttext]], [[bulletchartalttext]], [[sparkbarsalttext]], [[ratingdotsalttext]], [[variancechipalttext]]
