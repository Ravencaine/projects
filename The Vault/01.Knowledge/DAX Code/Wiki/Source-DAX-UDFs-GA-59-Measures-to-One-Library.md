---
created: 2026-08-09
updated: 2026-08-09
source: "From 59 Copy Pasted Measures to One Library What Migrating to GA DAX UDFs Actually Taught Me"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/From-59-Copy-Pasted-Measures-to-One-Library-What-Migrating-to-GA/ba-p/5259384"
published: 2026-07-01
note_type: source
tags: [dax, udf, power-bi, fabric, library, refactor, tmdl, xmla]
---

# DAX UDFs GA — 59 Measures to One Library

Source: Fabric Community Blog / powerbiweekly newsletter. Published 2026-07-01. Author: unlisted (no individual attribution in frontmatter; not in vault).

## The Core Problem

DAX had no reusable functions — only measures, calculated columns, and calculation groups. Every reusable pattern was copy-paste with a naming convention. This causes:
- Duplicate logic across models (same pattern written N times slightly differently)
- Bug drift: fix a bug in Model A, Model B still has it
- No way to enforce a single source of truth

## The Solution: DAX User-Defined Functions

GA in Power BI June 2026 release. A UDF is a **first-class model object:** visible in Model Explorer, storable in TMDL, callable from measures, calculated columns, visual calculations, and other UDFs.

Syntax:
```dax
DEFINE
    /// @param {NUMERIC} Numerator — value to divide
    /// @param {NUMERIC} Denominator — value to divide by
    /// @returns division result, or BLANK if denominator is zero
    FUNCTION dwp.SafeDivide = (
        Numerator: NUMERIC,
        Denominator: NUMERIC
    ) =>
        IF ( Denominator = 0, BLANK(), DIVIDE ( Numerator, Denominator ) )

EVALUATE
{ dwp.SafeDivide ( [Total Sales], [Total Cost] ) }
```

## Key Concepts Extracted

### Typed Parameters: Two Passing Modes

- **Value types** (Scalar, Table, AnyVal) — evaluate eagerly when the function is called
- **Expression types** (AnyRef, CalendarRef) — pass an unevaluated expression; the function controls evaluation context. Used when a function needs to reference a measure and force its own CALCULATE context transition.

Getting this wrong is the single most common UDF migration bug.

### IntelliSense Documentation

The `///` XML-comment block is not decoration. Typing the function name anywhere in the model surfaces the description, parameter list, and return type via IntelliSense.

### DevOps / Version Control

UDFs live in TMDL text files (`functions.tmdl`) — checkable into Git. Multiple models can pull from the same source of truth, collapsing bug-fix cycles from "fix in every model" to "fix in one file."

## Three Real Refactors

1. **Safe division:** 6 near-identical "safe divide" measures across models → 1 `dwp.SafeDivide` UDF
2. **ABC classification:** hardcoded 80/15/5 thresholds → `dwp.ABCBand(CumulativePercent, TierA:=0.8, TierB:=0.95)` with optional overrides
3. **Currency-aware growth:** measure passed as value param caused silent context bug; switched to AnyRef expression type + explicit CALCULATE wrapper inside function

## UDF Development Entry Points

| Entry Point | Best For |
|------------|---------|
| DAX Query View | Interactive testing; right-click → Quick Queries ("Define and evaluate") |
| TMDL View | Code-first editing; Git versioning |
| Model Explorer | Create/edit via formula bar; Functions node |
| XMLA endpoint / SSMS 22.5+ | Programmatic or DevOps deployment |
| Semantic Link Labs (Fabric notebooks) | Script entire library deployment in one cell |

## Prerequisite

UDFs require **database compatibility level 1702 or higher**. Silent failure — FUNCTION block fails with no obvious error if the model is on an older compatibility level.

## Honest Limitations

- UDFs do NOT replace calculation groups — different problems solved
- Calculation group: changes *which* measure is calculated based on slicer selection
- UDF: changes *how* a piece of logic is computed wherever it's called
- Dependency chains (UDFs calling UDFs) can become elegant to write and painful to performance-tune
- UDFs enable AI copilots and junior teammates to use logic correctly without reverse-engineering nested DAX

## Five-Minute UDF Audit

Count in your model:
1. Measures with identical `IF(... = 0, BLANK(), DIVIDE(...))` pattern → candidate: `SafeDivide`
2. Banding/tiering SWITCH statements with hardcoded thresholds → candidate: parameterized UDF
3. Measures that would all break if a business rule changed → candidate: UDF with that rule in one place

## Notes Extracted From This Source

- [[DAX-UDFs-vs-Calculation-Groups]] — `atomic` — UDFs change how logic is computed; calculation groups change which measure is selected
- [[Value-vs-Expression-Parameter-Types]] — `atomic` — Value (NUMERIC etc.) evaluates eagerly; AnyRef passes unevaluated expression for CALCULATE control
- [[DAX-UDFs-Require-Compatibility-1702]] — `atomic` — silent blocker: FUNCTION fails on compatibility < 1702
- [[dwp.SafeDivide]] — `function` — parameterized safe division with BLANK-on-zero
- [[dwp.ABCBand]] — `function` — ABC classification with optional TierA/TierB overrides
- [[dwp.CurrencyAwareGrowth]] — `function` — AnyRef expression param for context-correct growth%
- [[Measure-Library-to-UDF-Migration]] — `pattern` — refactoring strategy: audit → extract → parameterize → deploy
- [[DAX-UDF-Development-Environments]] — `workflow` — entry points: DAX Query View, TMDL, Model Explorer, XMLA/SSMS, Semantic Link Labs
- [[Five-Minute-UDF-Audit]] — `workflow` — count copy-paste patterns to find UDF candidates
- [[DAX-UDFs-Dont-Replace-Calculation-Groups]] — `gotcha` — UDFs and calculation groups solve different problems
- [[AnyRef-Expression-Parameter-Bug]] — `gotcha` — wrong parameter type causes silent context bug in UDF
- [[DAX-UDFs-Enable-AI-Copilot-Adoption]] — `atomic` — typed documented UDFs are the contract AI needs to use models safely
