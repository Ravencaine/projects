---
created: 2026-08-09
updated: 2026-08-09
source: "Fix Incorrect Totals in Power BI Tables.md"
note_type: workflow
tags: [power-bi, dax, totals, matrix, table, measure, workflow]
---

# Fix Incorrect Totals in Power BI Tables

Step-by-step process for diagnosing and correcting wrong total rows in table and matrix visuals.

## Step 1: Identify the Problem

The total row shows a number that doesn't equal the sum of visible row values. This commonly happens when a measure uses:

- `MAX()`
- `MIN()`
- `AVERAGE()`
- `MEDIAN()`

If the total looks wrong, one of these aggregations is likely the cause.

## Step 2: Write the Corrected Measure

Replace the naive aggregation with the SUMX + SUMMARIZE pattern.

**For MAX:**
```dax
Max Value Corrected :=
SUMX(
    SUMMARIZE(
        Categories,
        Categories[CategoryName],
        "MaxPer", CALCULATE( MAX( OrderDetails[UnitPrice] ) )
    ),
    [MaxPer]
)
```

**For AVERAGE:**
```dax
Avg Value Corrected :=
SUMX(
    SUMMARIZE(
        Calendar,
        Calendar[Year],
        Calendar[Month],
        "AvgPer", CALCULATE( AVERAGE( OrderDetails[Quantity] ) )
    ),
    [AvgPer]
)
```

## Step 3: Replace the Measure in the Visual

1. Open the **Fields** pane
2. Locate the original (wrong) measure in your data model
3. Drag the corrected measure onto the visual
4. Verify the total row now equals the sum of detail row values

## Step 4: Verify Subtotals

For matrix visuals with multiple levels (Year → Month), ensure each subtotal row is also correct. If subtotals are wrong, add the intermediate grouping column to `SUMMARIZE`.

## Key Takeaways

- Always check total rows when using MAX/MIN/AVERAGE measures
- The fix always follows: `SUMX(SUMMARIZE(... CALCULATE(...)), [alias])`
- `CALCULATE` is required for context transition inside `SUMMARIZE`

## Related

- [[Fix-Incorrect-Totals-SUMX-SUMMARIZE-Pattern]] — full pattern with variations
- [[Totals-Wrong-Row-Context-Missing]] — the atomic explanation of why totals go wrong
