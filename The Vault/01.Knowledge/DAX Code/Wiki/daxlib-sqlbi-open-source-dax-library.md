---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: pattern
tags: [dax, user-defined-function, library, open-source, daxlib, sqlbi, community]
---

# daxlib: SQLBI Open-Source DAX Function Library

daxlib is an open-source repository of model-independent DAX user-defined functions, published by SQLBI, that can be imported directly into any Power BI semantic model.

## Purpose

Provides battle-tested, professionally reviewed DAX functions as importable building blocks — equivalent to Python's `pip install numpy`. Teams no longer need to write common business logic from scratch; they can import, review, and use community functions with full visibility into the implementation.

## Key Points

- **Repository:** SQLBI / daxlib (public GitHub)
- **Model-independent:** functions carry their own context assumptions; review before importing
- **Reviewed by professionals:** SQLBI team reviewed each function for correctness and performance
- **TMDL-format:** importable into PBIP projects via `functions.tmdl`
- **Coverage:** common business logic patterns: safe divide, currency conversion, tiered pricing, margin calculations

## Usage Pattern

1. Clone or download the daxlib repository
2. Review each function's documentation and implementation
3. Copy the `DEFINE FUNCTION` blocks into your model's `functions.tmdl`
4. Test from multiple calling contexts (see [[val-vs-expr-parameter-evaluation]])

## Why It Matters

Before daxlib, every team wrote the same ten helper functions independently — SafeDivide, ApplyTax, CurrencyConvert. With daxlib:
- Functions are reviewed by DAX experts rather than written by practitioners under time pressure
- Bugs are caught once and fixed across all models simultaneously
- Teams build on shared, proven logic rather than reinventing

This is the package-ecosystem moment DAX has lacked. The next generation of Power BI developers will `import daxlib` the way Python developers `import pandas`.

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[dax-udf-define-function-pattern]] — pattern
- [[dax-udf-adoption-workflow]] — workflow
- [[val-vs-expr-parameter-evaluation]] — gotcha
