---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# RatingDotsAltText

DAX UDF generating screen-reader-friendly alt text for a star/dot rating visual in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context and rating value(s) as parameters. Returns a plain-language narrative describing the rating — e.g., "Customer rating: 4 out of 5 stars. 80% positive."

## Design Principles

- Parameter-driven, no internal model references
- Avoids naming chart types or colours
- WCAG accessibility compliant
- Works with any rating configuration (stars, dots, hearts, etc.)

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[progressbaralttext]], [[bulletchartalttext]], [[sparkbarsalttext]], [[statuspillalttext]], [[variancechipalttext]]
