---
created: 2026-07-26
source: dax.pdf
note_type: reference
tags: [dax, reference, glossary]
---

# DAX Glossary

A quick reference for DAX terminology.

## Terms

**BLANK** — The DAX equivalent of an empty cell. Not zero, not an empty string. Propagates through scalar expressions.

**CALCULATE** — Evaluates an expression in a modified filter context. The most important DAX function.

**Context** — The environment in which a DAX expression evaluates. Two types: **row context** (current row) and **filter context** (active filters).

**Filter Context** — The set of filters (slicers, visual filters, CALCULATE arguments) that determines which rows contribute to a calculation.

**Row Context** — The current row in an iterated table. Created by iterator functions (SUMX, FILTER, etc.) and calculated columns.

**Measure** — A calculation defined in the model that evaluates in the filter context. Returns a scalar value.

**Calculated Column** — A column defined by a DAX expression that is evaluated for each row in a table. Creates row context.

**Iterator Function** — A function that loops over a table row by row, creating row context (e.g., SUMX, AVERAGEX, FILTER).

**DAX Query** — A query expression starting with EVALUATE that returns a table. Used in DAX Studio, SSMS, and Power BI.

**Date Table** — A table of dates marked as a date table in the model. Required for time intelligence functions.

**Filter Argument** — A parameter in CALCULATE that modifies the filter context. Can be a Boolean expression, table expression, or modifier function.

**Modifier Function** — A function that changes how filters are applied without creating a new table (e.g., ALL, KEEPFILTERS, USERELATIONSHIP).

**Lineage** — The link between a column in a virtual table and its source column in the model. Affects how filters propagate.

**Auto-exist** — A DAX optimization where mutually existing filter combinations are automatically handled to reduce query complexity.

## Related

- [[dax-context]]
- [[dax-syntax]]
- [[dax-operators]]
