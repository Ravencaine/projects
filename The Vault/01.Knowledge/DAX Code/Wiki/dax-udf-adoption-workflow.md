---
created: 2026-07-29
updated: 2026-08-02
source: "DAX Finally Got User - Defined Functions. After 20 Years of Copy - Pasting Measures, Here's What Actually Changes - and What Doesn't.md"
note_type: workflow
tags: [dax, user-defined-function, adoption, inventory, governance, production]
---

# Adopt DAX UDFs in a Production Model

A four-move workflow for safely introducing DAX user-defined functions into an existing production semantic model without disrupting existing reports.

## Prerequisites

- Power BI Desktop (June 2026 release or later)
- Database compatibility level 1702 or higher
- Model Explorer accessible (DAX query view or TMDL view)
- Existing semantic model with 15+ measures (where duplication is likely)

## Steps

### Step 1 — Inventory: Find Near-Duplicate Measures

Do not write a single function before counting what exists.

**Automated:** Use DAX query view with INFO functions:
```dax
EVALUATE INFO.USERDEFINEDFUNCTIONS()
```

**Manual:** Open Model Explorer. For each measure, ask:
- Does this measure share logic with another measure?
- Has this business rule been implemented slightly differently across the model?
- Has the rule changed in one place but not in the others?

Document the top candidates: business rules where the definition has changed at least once in the past year.

### Step 2 — Convert Top Three Duplicated Rules First

Start small. Three functions, not thirty.

**Priority order:**
1. Business rules that have drifted across copies (highest risk of inconsistency)
2. Rules with parameters (margin rates, tax rates, currency codes)
3. Rules with safety logic (DIVIDE with default, SWITCH with fallback)

**Do not convert yet:**
- Time intelligence patterns (use [[info.calculationgroups]] instead)
- Grain-dependent logic (what the model assumes about fact table grain)
- One-off measures unlikely to be reused

### Step 3 — Write the Doc Comment Before the Body

```dax
DEFINE
/// <one clear sentence describing what this does>
/// <if there is a non-obvious edge case, document it here>
FUNCTION <Name> = (
    <param1> : <Type>,
    <param2> : <Type> [VAL | EXPR]
) =>
    <expression>
```

If you cannot write the description in one sentence, the function is doing too much — split it.

The `///` comment is the only documentation in Model Explorer. It is the primary interface to the next analyst.

### Step 4 — Test from Two Calling Contexts Minimum

| Context | Why It Matters |
|---------|---------------|
| Measure | Standard evaluation; filter context from the visual |
| Calculated column | Row context + context transition |
| Iterator (e.g., SUMX) | Different evaluation order |

```dax
-- Test 1: as a measure
MEASURE Sales[TestNetRevenue] = Finance.NetRevenue( SUM(Sales[Amount]) )

-- Test 2: as a calculated column on Sales
-- Column formula:
-- = Finance.NetRevenue( Sales[Amount] )

-- Test 3: in an iterator
-- MEASURE TestIterator = SUMX( Sales, Finance.NetRevenue( Sales[Amount] ) )
```

If numbers differ between Test 1 and Test 2, the function has a VAL/EXPR issue — see [[val-vs-expr-parameter-evaluation]].

## Variations

### Naming Convention for a Team Library

```
<Team>.<Domain>.<Action>
Finance.Revenue.NetWithTax
Operations.Inventory.SafeDivide
HR.Headcount.ActiveFTE
```

### When to Use EXPR vs VAL

| Scenario | Mode | Reason |
|----------|------|--------|
| Simple arithmetic with scalar inputs | VAL | No context dependency |
| CALCULATE inside function body | EXPR | Must defer evaluation |
| FILTER/CALCULATETABLE inside function | EXPR | Must apply filters at call site |
| Text manipulation | VAL | No context dependency |

## Common Errors

- **Wrong numbers in production** → VAL/EXPR mismatch (see [[val-vs-expr-parameter-evaluation]])
- **Function not found** → Compatibility level below 1702
- **Circular reference error** → Function calls itself or another function that calls it

## Related

- [[dax-user-defined-functions-udfs]] — function reference
- [[val-vs-expr-parameter-evaluation]] — gotcha
- [[udfs-vs-calculation-groups]] — comparison
- [[dax-udf-define-function-pattern]] — pattern: DEFINE FUNCTION syntax
