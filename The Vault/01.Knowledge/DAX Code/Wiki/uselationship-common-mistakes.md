---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
note_type: atomic
tags: [dax, uselationship, errors, gotcha, beginner]
---

# USERELATIONSHIP: Common Mistakes

USERELATIONSHIP is powerful but has sharp edges. These are the most frequent errors — both from the source article and from wider DAX practice.

## Mistake 1: Using USERELATIONSHIP on an Already-Active Relationship

```dax
-- ERROR: fails because InvoiceDate relationship is already active
Sales Error =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[InvoiceDate], 'Date'[Date] )
)
```

**Fix:** Remove USERELATIONSHIP when using the active relationship. Use it only for inactive ones.

## Mistake 2: Calling USERELATIONSHIP Without CALCULATE

```dax
-- WRONG: USERELATIONSHIP outside CALCULATE has no effect
Total Sales = SUM ( Sales[SalesAmount] )
             + USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
```

**Fix:** USERELATIONSHIP must be inside CALCULATE as a filter argument.

## Mistake 3: Wrong Column Polarity (Many-Side First)

```dax
-- WRONG: column order matters — fact column first
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( 'Date'[Date], Sales[ShipDate] )  -- reversed
)
```

**Fix:** Pass the fact table column first, then the dimension column.

## Mistake 4: Cross-Filter Direction Conflicts

If the relationship's cross-filter direction is set to one direction only (e.g., Date → Sales but not Sales → Date), USERELATIONSHIP may not filter correctly in the expected direction.

**Fix:** Verify the relationship's cross-filter direction in the model view. For role-playing dates, bidirectional filtering may be needed, or consider `CROSSFILTER()` instead.

## Mistake 5: Unexpected Blanks in Results

Inactive relationships may not have all rows connected — some fact rows might have NULL date values. When USERELATIONSHIP activates the relationship, those NULL rows can cause unexpected blank results depending on the filter context.

**Fix:** Use `COALESCE()` or `IF()` to handle NULL dates in the fact table, or add a default row to the Date dimension.

## Mistake 6: Multiple USERELATIONSHIP in One CALCULATE

```dax
-- AMBIGUOUS: Power BI cannot activate two relationships simultaneously
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[InvoiceDate], 'Date'[Date] ),
    USERELATIONSHIP ( Sales[ShipDate],    'Date'[Date] )  -- conflict
)
```

**Fix:** Use separate CALCULATE calls for each relationship. Combine results with `+` or use a different approach.

## Related

- [[uselationship-function]] — correct usage and mechanics
- [[role-playing-dimensions-pattern]] — alternative approaches to role-playing dates
