---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: function
tags: [dax, udf, abc-classification, banding, tiering, switch, parameter]
---

# dwp.ABCBand — Parameterized ABC Classification UDF

Converts a cumulative percentage to an ABC classification tier. Replaces hardcoded SWITCH statements scattered across measures with a single parameterized function.

## Signature

```
dwp.ABCBand(CumulativePercent: NUMERIC, TierA: NUMERIC = 0.8, TierB: NUMERIC = 0.95): STRING
```

## Definition

```dax
DEFINE
    /// Classifies an item into A/B/C tier based on cumulative percentage.
    /// @param {NUMERIC} CumulativePercent — cumulative % of total (0–1)
    /// @param {NUMERIC} TierA — upper bound for A tier (default 0.80)
    /// @param {NUMERIC} TierB — upper bound for B tier (default 0.95)
    /// @returns "A", "B", or "C"
    FUNCTION dwp.ABCBand = (
        CumulativePercent: NUMERIC,
        TierA: NUMERIC = 0.8,
        TierB: NUMERIC = 0.95
    ) =>
        SWITCH (
            TRUE,
            CumulativePercent <= TierA, "A",
            CumulativePercent <= TierB, "B",
            "C"
        )

EVALUATE
{ dwp.ABCBand ( [CumulativePct] ) }
```

## Usage

```dax
// Standard 80/15/5 split (uses defaults)
[ABC Tier] := dwp.ABCBand ( [CumulativePct] )

// Stricter 70/20/10 split
[ABC Tier Strict] := dwp.ABCBand ( [CumulativePct], TierA:=0.70, TierB:=0.90 )
```

## Key Design Points

- Default parameter values (`TierA:=0.8`, `TierB:=0.95`) mean existing call sites don't break when the UDF is deployed
- Named parameter syntax (`TierA:=`) allows overriding only the needed threshold without positional arguments
- All parameters are `NUMERIC` — no expression evaluation needed

## Migration Impact

Before: ABC banding logic with hardcoded 80/15/5 thresholds existed as duplicate SWITCH statements in multiple models. After: one function, threshold-overridable per-model.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[Value-vs-Expression-Parameter-Types]] — both NUMERIC (value type); no expression needed here
