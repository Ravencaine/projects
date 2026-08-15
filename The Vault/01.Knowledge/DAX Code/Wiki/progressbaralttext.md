---
created: 2026-08-11
source: Power BI Alt Text UDF Library
note_type: function
tags: [dax, udf, accessibility, alt-text, power-bi]
---

# ProgressBarAltText

DAX UDF generating screen-reader-friendly alt text for a progress bar visual in Power BI.

## Signature

> Fetch from: https://github.com/Juls-BI/powerbi-alttext-udfs
> File: AltText\_VisualPatterns.dax

## Purpose

Takes the visual context and numeric value(s) as parameters and returns a plain-language narrative describing the progress bar state — e.g., "Current progress is 75 out of 100, which is 75% complete."

## Design Principles

- Takes only parameters (context + values) — no references to internal model objects
- Avoids naming chart types or colours
- Follows WCAG accessibility best practices
- Generic: works with any progress bar regardless of visual configuration

## Related

- [[alt-text-udf-workflow]] — how to load and use UDF files from the library
- [[bulletchartalttext]], [[sparkbarsalttext]], [[ratingdotsalttext]], [[statuspillalttext]], [[variancechipalttext]] — other UDFs in the library
