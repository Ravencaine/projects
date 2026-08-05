---
created: 2026-07-27
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use"
note_type: pattern
tags: [dax, test-measures, validation, quality-assurance]
---

# Pattern 5: Validation Loop

Test measures are created for every base measure to verify the calculation is correct before building dependent measures on top of it. Tests are never deleted — they serve as ongoing regression guards.

## Purpose

A broken base measure silently corrupts every dependent KPI measure. The validation loop catches broken base measures immediately by comparing them against independently verifiable totals.

## Components

- TEST measures (prefixed with TEST) — simple independent calculations
- Hard-coded total comparisons — verify TEST measure against a known total
- Delta measures — confirm TEST and base measure agree

## Structure

```dax
-- Base measure (hidden from business users)
_Revenue = SUMX(Sales, Sales[Qty] * Sales[Price])

-- TEST measure (visible, verified independently)
TEST Revenue Raw := SUM(Sales[Revenue])   -- direct column sum as verification

-- Validation measure
TEST Revenue Delta := [TEST Revenue Raw] - [_Revenue]
-- Expected value: 0 (or very small due to rounding)
```

## Example Validation Set

```dax
-- Base measure
Gross Profit = [Revenue] - [Total Cost]

-- Independent test: manually verify a known total
TEST Gross Profit Check :=
CALCULATE (
    SUM ( FactSales[GrossProfit] ),
    DAXUnitTests[IsVerifiedTotal] = TRUE
)

-- Delta check
Gross Profit Validation :=
IF ( ABS ( [Gross Profit] - [TEST Gross Profit Check] ) > 0.01,
    "ERROR: Base measure mismatch",
    "OK"
)
```

## When to Run Validation

- After any data model change
- After adding new base measures
- After updating business logic in existing measures
- Before publishing a new version of the PBIX

## Rule

> Never build a KPI measure on top of a base measure until the TEST measure for that base measure returns the expected value. One broken base measure silently corrupts every KPI that depends on it.

## Related

- [[measure-branching-pattern]] — what to build on top of validated base measures
- [[pattern-2-defensive-dax]] — defensive checks within base measures
