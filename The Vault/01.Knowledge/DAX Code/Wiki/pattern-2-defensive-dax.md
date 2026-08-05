---
created: 2026-07-27
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use"
note_type: pattern
tags: [dax, defensive-dax, error-handling, blank, divide, safety]
---

# Pattern 2: Defensive DAX

Every measure that performs division, references a measure that might be BLANK, or depends on external data includes explicit defensive logic. This prevents "weird numbers" in visuals and broken KPIs.

## Purpose

Prevent division-by-zero, null propagation, and BLANK coalescing from creating misleading or error-producing results in visuals.

## Components

- DIVIDE() with third argument for zero-handling (preferred over plain `/`)
- IF() / IFERROR() for explicit branch handling
- ISBLANK() for checking intermediate results
- COALESCE() (if available) for null replacement

## Structure

```dax
-- Step 1: Calculate the numerator
Numerator := [Revenue] - [Cost]

-- Step 2: Defensive check before division
Margin % :=
VAR Profit = [Numerator]
RETURN
    IF (
        OR ( ISBLANK ( Profit ), Profit = 0 ),
        BLANK (),
        DIVIDE ( Profit, [Revenue], 0 )
    )
```

## Examples

**Division-by-zero protection:**

```dax
-- Anti-pattern: plain division breaks if denominator is 0
Margin % := [Profit] / [Revenue]

-- Defensive: DIVIDE with zero replacement
Margin % := DIVIDE ( [Profit], [Revenue], BLANK() )
```

**BLANK propagation protection:**

```dax
-- Check numerator is not BLANK before using
Safe Conversion Rate :=
VAR Visits      = SUM(Sessions[Visits])
VAR Conversions = SUM(Sessions[Conversions])
VAR HasData    = NOT ISBLANK(Visits) && Visits > 0
RETURN
    IF ( HasData, DIVIDE(Conversions, Visits, 0), BLANK() )
```

**ISERROR() for external data dependencies:**

```dax
Safe Revenue :=
IFERROR ( [Revenue], 0 )
```

## Related

- [[var-in-dax]] — VAR enables clean defensive checks
- [[divide]] — DIVIDE function
- [[sumx]] — SUMX iterators are another common site for division; wrap the SUMX result in DIVIDE
