---
created: 2026-08-09
updated: 2026-08-09
source: "Creating functions for the like-for-like DAX pattern.md"
note_type: atomic
tags: [dax, user-defined-function, naming-convention, model-dependent, wrapper, local]
---

# Local.* UDF Wrapper Pattern

Use the `Local.` prefix for model-dependent wrapper functions that call model-independent library functions. This separates the model-specific column mapping from the reusable business logic.

## Pattern

```
Local.<EntityName>  →  calls library function with model-specific arguments
```

```dax
-- Thin model-dependent wrapper — just maps columns to library parameters
DEFINE
FUNCTION Local.StoreStatus = () =>
    DaxPatterns.LikeForLike.EntityStatus(
        'Date'[Year],
        Store[StoreKey],
        Sales
    )

DEFINE
FUNCTION Local.ComputeForSameStore = (
    formulaExpr : ANYREF
) =>
    DaxPatterns.LikeForLike.ComputeForSameEntity(
        StoreStatus[StoreKey],
        StoreStatus[Status],
        Store[StoreKey],
        'Date',
        formulaExpr
    )
```

## Why the Local. Prefix

- **Scope clarity:** `Local.*` functions are scoped to the current model; they cannot be shared
- **Collision avoidance:** multiple models can all have a `Local.StoreStatus` without conflicts
- **Discoverability:** Model Explorer shows Local.* functions as model-specific, separating them from shared library functions
- **Upgrade path:** when the library function is updated, only the Local.* wrapper may need adjustment

## When Local.* Is Required

Use a Local.* wrapper whenever the model-independent function requires model-specific objects as parameters. The wrapper performs the mapping, not the business logic.

```dax
-- Calling from a measure — the Local.* wrapper hides the parameter mapping
Same Store Sales = Local.ComputeForSameStore([Sales Amount])
```

Without the Local.* pattern, every measure would need to pass all 5 parameters. The Local.* pattern reduces the measure to one parameter: the expression.

## Contrast: No Local.* Pattern

```dax
-- Without Local.*: the measure carries all the column references
-- Every measure using this pattern must specify all 5 parameters
Same Store Sales =
    DaxPatterns.LikeForLike.ComputeForSameEntity(
        StoreStatus[StoreKey],       -- model-specific
        StoreStatus[Status],         -- model-specific
        Store[StoreKey],             -- model-specific
        'Date',                       -- model-specific
        [Sales Amount]               -- the only model-independent part
    )
```

With Local.*, the measure is just:

```dax
Same Store Sales = Local.ComputeForSameStore([Sales Amount])
```

## Multiple Local.* Instances Per Model

One model can have multiple Local.* wrappers for different entity types:

```dax
Local.StoreStatus        → DaxPatterns.LikeForLike.EntityStatus(Store keys)
Local.ProductStatus      → DaxPatterns.LikeForLike.EntityStatus(Product keys)
Local.CustomerStatus     → DaxPatterns.LikeForLike.EntityStatus(Customer keys)
```

Each wrapper creates its own status calculated table and its own Compute wrapper.

## Related

- [[Model-Dependent-vs-Model-Independent-UDFs]] — the conceptual foundation
- [[DaxPatterns-LikeForLike-Library]] — the library functions Local.* wraps
- [[dax-udf-define-function-pattern]] — DEFINE FUNCTION syntax
