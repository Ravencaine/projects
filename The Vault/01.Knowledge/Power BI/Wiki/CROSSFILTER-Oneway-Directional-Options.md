---
created: 2026-08-09
updated: 2026-08-09
source: "CROSSFILTER Function Control Relationships in Power BI DAX.md"
note_type: atomic
tags: [dax, crossfilter, relationship, one-to-one, unidirectional]
---

# CROSSFILTER Oneway Directional Options for One-to-One Relationships

`ONEWAY_LEFTFILTERSRIGHT` and `ONEWAY_RIGHTFILTERSLEFT` are CROSSFILTER directions for one-to-one relationships where you need control over filter direction without enabling full bidirectionality.

## When These Exist

In a one-to-one relationship, both tables are the "one" side. The model must choose a default direction. The `Oneway_*` options give explicit control:

```dax
-- Left table filters right table (only)
CALCULATE(
    [Measure],
    CROSSFILTER(
        TableA[Key],
        TableB[Key],
        ONEWAY_LEFTFILTERSRIGHT
    )
)

-- Right table filters left table (only)
CALCULATE(
    [Measure],
    CROSSFILTER(
        TableA[Key],
        TableB[Key],
        ONEWAY_RIGHTFILTERSLEFT
    )
)
```

## Why Not Just BOTH?

| Direction | Use when |
|-----------|----------|
| `BOTH` | Both tables need to filter each other — creates full bidirectionality |
| `ONEWAY_LEFTFILTERSRIGHT` | Only TableA filters TableB; TableB must NOT filter TableA |
| `ONEWAY_RIGHTFILTERSLEFT` | Only TableB filters TableA; TableA must NOT filter TableB |

Use the directional variants when:
- One direction is semantically correct (e.g., Order → Invoice) but the other creates ambiguity
- You want the same granularity relationship but with explicit directional enforcement per measure
- Preventing accidental cross-filtering that `BOTH` would allow

## Contrast with ONEWAY

`ONEWAY` (without the suffix) is the standard one-directional setting — filter propagates from the one side to the many side. `ONEWAY_*_FILTERS_*` specifically targets one-to-one relationships where there is no many side, so the direction must be explicitly stated.

## Related

- [[crossfilter]] — CROSSFILTER function reference (signature, BOTH, NONE, ONEWAY)
- [[treatas-uselationship-crossfilter]] — TREATAS vs USERELATIONSHIP vs CROSSFILTER comparison
