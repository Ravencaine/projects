---
created: 2026-08-09
updated: 2026-08-09
source: "Creating functions for the like-for-like DAX pattern.md"
source_url: https://www.sqlbi.com/articles/creating-functions-for-the-like-for-like-dax-pattern/
note_type: source
tags: [dax, user-defined-function, like-for-like, pattern, sqlbi, Marco-Russo, Alberto-Ferrari, library]
---

# Creating Functions for the Like-for-Like DAX Pattern

Transform the like-for-like comparison pattern into model-independent DAX user-defined functions, enabling reuse across any semantic model.

> **Type:** article
> **Authors:** Marco Russo & Alberto Ferrari
> **Published:** 2026-03-09
> **URL:** https://www.sqlbi.com/articles/creating-functions-for-the-like-for-like-dax-pattern/
> **Routed to:** DAX Code

## Summary

The article demonstrates converting the DAX Like-for-Like comparison pattern into reusable user-defined functions. The key insight is the distinction between **model-dependent** functions (hard-coded to a specific model's tables and columns) and **model-independent** functions (fully parametric, agnostic to model structure). By separating these concerns, the pattern's business logic is centralized in a library function that can be deployed to any model with a thin Local.* wrapper for model-specific column mapping.

The final library (`DaxPatterns.LikeForLike`) handles stores, products, or any comparable entity — Active/Inactive replaces the domain-specific Open/Closed terminology.

## Key Claims

- DAX UDFs enable model-independent logic that benefits all models using the library
- Model-independent functions must receive every table and column as a parameter
- The `Local.*` prefix marks model-dependent wrapper functions
- Generalizing from Store to Entity broadens the function to any comparable dimension
- Centralizing logic in one place means a single optimization benefits every calling measure

## Pattern Stages (Article Walkthrough)

| Stage | Description |
|-------|-------------|
| 1 | Copy-paste pattern code into `Local.StoreStatus` and `Local.SameStoreSales` (model-dependent) |
| 2 | Replace column/table names with parameters → `DaxPatterns.LikeForLike.StoreStatus` (model-independent) |
| 3 | Further generalize from Store to Entity → `DaxPatterns.LikeForLike.EntityStatus` + `ComputeForSameEntity` |
| 4 | Instantiate for Product → `Local.ProductStatus` + `Local.ComputeForSameProduct` |

## Extracted Notes

- [[Model-Dependent-vs-Model-Independent-UDFs]] — `atomic` — the core distinction between model-aware and fully parametric UDFs
- [[DaxPatterns-LikeForLike-Library]] — `pattern` — the full three-function library (EntityStatus, ComputeForSameEntity, ComputeForSameStore)
- [[Local-Wrapper-UDF-Pattern]] — `atomic` — the `Local.*` naming pattern for model-dependent wrapper functions
- [[UDF-Generalization-Workflow]] — `workflow` — step-by-step: from pattern to model-independent library function

## Metadata

| Field | Value |
|-------|-------|
| Source file | Creating functions for the like-for-like DAX pattern.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~1,500 |
| Download links | 3 article URLs (SQLBI/DaxPatterns) — no files |
