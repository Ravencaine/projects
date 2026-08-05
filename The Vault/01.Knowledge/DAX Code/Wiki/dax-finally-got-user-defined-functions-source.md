---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
source_url: https://medium.com/@t.gulab/dax-finally-got-user-defined-functions-d58e022379ca
note_type: source
tags: [dax, user-defined-function, udf, ga, june-2026, val, expr, tmdl, daxlib]
---

# DAX Finally Got User-Defined Functions (source note)

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2026-07-06
> **URL:** https://medium.com/@t.gulab/dax-finally-got-user-defined-functions-d58e022379ca
> **Routed to:** DAX Code

## Summary

Honest practitioner account of DAX user-defined functions going generally available in the June 2026 Power BI release. Evaluates what the feature actually solves (copy-paste duplication disease, organizational maintainability), what it doesn't (model quality, performance, time intelligence), and the critical VAL/EXPR evaluation mode trap that will generate production incidents.

## Key Claims

- DAX UDFs GA in June 2026; requires compatibility level 1702
- ~15–40% of measures in mature models are near-duplicates of each other
- ~25% of a mature DAX corpus genuinely wants to become functions; time intelligence mostly stays as-is
- VAL is the default evaluation mode — the wrong choice silently produces wrong numbers
- daxlib (SQLBI) provides the first community library infrastructure for DAX
- UDFs are an organizational feature more than a calculation feature

## Notable Details

- VAL: argument evaluated immediately, value passed in — cannot re-evaluate under changed context
- EXPR: expression passed in, function controls evaluation context — required when function body uses CALCULATE
- functions.tmdl in PBIP format makes UDFs first-class version-controlled objects
- Community naming: PascalCase with dots for namespacing (e.g., `Sales.NetRevenue`)
- The VAL/EXPR class of error is the SUM-vs-SUMX equivalent for UDFs — invisible until context changes

## Extracted Notes

Links to notes derived from this source:

- [[dax-user-defined-functions-udfs]] — `function` — Named, parameterized first-class functions in the DAX model
- [[val-vs-expr-parameter-evaluation]] — `gotcha` — Wrong evaluation mode silently produces wrong numbers
- [[dax-udf-adoption-workflow]] — `workflow` — 4-step workflow for adopting UDFs in a production model
- [[dax-udf-define-function-pattern]] — `pattern` — DEFINE FUNCTION syntax with doc comment, typed params, EXPR/VAL
- [[daxlib-sqlbi-open-source-dax-library]] — `pattern` — SQLBI's community DAX function library
- [[udfs-vs-calculation-groups]] — `comparison` — When to use UDFs vs calculation groups
- [[udfs-vs-copy-paste-pattern]] — `comparison` — How UDFs eliminate copy-paste duplication
- [[dax-udf-boilerplate-define-function]] — `snippet` — Ready-to-use UDF definition boilerplates
- [[test-dax-udf-multiple-calling-contexts]] — `snippet` — Minimum test cases before production
- [[udfs-dont-fix-the-model]] — `atomic` — UDFs cannot compensate for broken semantic models
- [[udfs-dont-automatically-improve-performance]] — `atomic` — Shared functions multiply inefficiency by number of callers

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Finally Got User-Defined Functions… (Tejwani) |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-29 |
| Word count | ~2,200 |
