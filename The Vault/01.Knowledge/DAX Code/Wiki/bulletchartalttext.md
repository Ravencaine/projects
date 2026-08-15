---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# BulletChartAltText

DAX UDF generating screen-reader-friendly alt text for a bullet/target chart visual in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context, actual value, target value, and optional range values as parameters. Returns a plain-language narrative describing the performance against target — e.g., "Sales of $48,000 achieved 96% of the $50,000 target."

## Design Principles

- Parameter-driven (context + values only), no internal model references
- Avoids naming chart types or colours
- WCAG accessibility compliant
- Visual-agnostic: works across any bullet chart configuration

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[progressbaralttext]], [[sparkbarsalttext]], [[ratingdotsalttext]], [[statuspillalttext]], [[variancechipalttext]]
