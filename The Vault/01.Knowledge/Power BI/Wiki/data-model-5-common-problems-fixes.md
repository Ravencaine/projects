---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling (Part 2).md"
note_type: atomic
tags: [power-bi, data-modeling, beginner, troubleshooting, many-to-many, bidirectional-filter]
---

# Data Model: 5 Common Problems and Fixes

Five problems that catch every beginner. Recognise the symptom, apply the fix.

## Problem 1: Numbers 10x Too High

**Symptom:** Expected total $2.6M. Actual: $26M.

**Cause:** Many-to-many relationship duplicating rows. Or two relationship paths between tables creating a loop.

**Diagnosis:**
1. Go to Model view
2. Look for relationships with "*" on both sides
3. Check for multiple paths between the same two tables

**Fix:** Delete the extra relationship. Keep only the single clean one-to-many path from dimension to fact.

## Problem 2: Slicers Don't Filter Visuals

**Symptom:** Select "Enterprise" in Customer Segment slicer. Nothing changes.

**Cause:** No relationship exists, or filter direction points the wrong way.

**Fix:**
- If no relationship line: create it (CustomerID in Customers → CustomerID in Orders)
- If line exists but wrong direction: click the relationship → Properties → Cross filter direction → Single, pointing from Customers to Orders

## Problem 3: (Blank) Rows Everywhere

**Symptom:** Customer Name with Revenue shows "(Blank): $120,000"

**Cause:** Orders table has a CustomerID (e.g., "C999") that doesn't exist in the Customers table. The key in the fact table has no match in the dimension.

**Fix:**
1. Option 1: Add the missing customer to the dimension table
2. Option 2: Fix the invalid key in the source data
3. Option 3: Exclude blanks in the measure:
```dax
Revenue (Excl Blanks) =
CALCULATE(
    [Total Revenue],
    NOT(ISBLANK(Customers[CustomerName]))
)
```

## Problem 4: Can't Create Second Date Relationship

**Symptom:** Connect Orders[ShipDate] to Date[Date]. Power BI says "A relationship already exists."

**Cause:** Only one active relationship between two tables is allowed. OrderDate already uses the relationship to Date.

**Fix:**
1. Create the ShipDate relationship (it will appear as inactive, dashed line)
2. Use USERELATIONSHIP in a measure:
```dax
Revenue by Ship Date =
CALCULATE(
    [Total Revenue],
    USERELATIONSHIP(Orders[ShipDate], Date[Date])
)
```

## Problem 5: Bidirectional Filter Causing Duplication

**Symptom:** Enabling bidirectional relationships causes numbers to inflate again.

**Cause:** Bidirectional filter propagation makes the same row visible through multiple paths, doubling or tripling the count.

**Fix:** Revert to single-direction filter. Only use bidirectional filters with explicit bridge tables for genuine many-to-many scenarios.

## The Diagnostic Process

1. **Check Model view first**: broken relationships show red exclamation marks
2. **Create a simple test visual**: table with dimension + measure. Does it show correct data?
3. **Add one slicer at a time**: isolate which relationship is the problem
4. **Compare to source totals**: difference = relationship issue
5. **Remove and re-add relationships**: clean start often fixes subtle loop problems

## Related

- [[role-playing-date-calculated-columns]] — handling multiple date columns
- [[data-model-5-testing-checks]] — systematic testing before troubleshooting
- [[relationship-types-one-to-many-many-to-many]] — the cardinality choices that cause these problems
