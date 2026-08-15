---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
note_type: pattern
tags: [dax, udf, library, migration, refactor, tmdl]
---

# Measure Library → UDF Library Migration

Systematic approach for refactoring a folder of copy-pasted measures into a typed UDF library.

## When to Migrate

- 3+ measures sharing an identical `IF(x=0, BLANK(), DIVIDE(...))` pattern
- Banding/tiering SWITCH statements with hardcoded thresholds that vary by model
- Business logic that would break identically across N models if a rule changed
- Measure library growing without a way to enforce a single source of truth

## The Migration Process

### Step 1: Audit

Count in your model:
1. `IF(... = 0, BLANK(), DIVIDE(...))` patterns → `SafeDivide` candidates
2. SWITCH statements with hardcoded thresholds → parameterized UDF candidates
3. Measures that would all break if one business rule changed → extract that rule into a UDF

### Step 2: Categorize Parameters

For each candidate:
- Arithmetic values / column references → `NUMERIC` (value type)
- Measures that need CALCULATE context inside the function → `AnyRef` (expression type)
- Date references → `CalendarRef`

### Step 3: Define with Defaults

Use default parameter values so existing call sites don't break on deployment:
```dax
FUNCTION dwp.ABCBand = (
    CumulativePercent: NUMERIC,
    TierA: NUMERIC = 0.8,
    TierB: NUMERIC = 0.95
) => ...
```

### Step 4: Document

Add `///` XML comments above every function. IntelliSense reads them — this is how users discover and use the library correctly.

### Step 5: Version Control

UDFs live in `functions.tmdl`. Check into Git. Multiple models pull from the same source → one fix propagates everywhere.

### Step 6: Deploy

| Method | Tool |
|--------|------|
| Manual | Model Explorer / DAX Query View |
| CI/CD | XMLA endpoint / SSMS 22.5+ |
| Fabric | Semantic Link Labs (`sempy.links.tom.*`) |

## What Doesn't Belong in a UDF

- Logic that is genuinely different per visual (keep as individual measures)
- Calculation groups (different problem — use calculation groups)
- Performance-critical paths that would become harder to trace with function-call overhead

## Expected Outcome

59 measures → ~20 distinct UDFs. Bug fixes collapse to one location. IntelliSense replaces wiki documentation.

## Related

- [[Source-DAX-UDFs-GA-59-Measures-to-One-Library]] — source
- [[dwp.SafeDivide]] — example: SafeDivide consolidation
- [[dwp.ABCBand]] — example: parameterized ABC with defaults
- [[dwp.CurrencyAwareGrowth]] — example: AnyRef parameter
- [[Value-vs-Expression-Parameter-Types]] — parameter type selection guide
