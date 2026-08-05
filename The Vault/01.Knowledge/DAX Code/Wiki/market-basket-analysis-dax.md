---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, customers, market-basket, cross-sell, recommendation]
---

# Market Basket Analysis in DAX

Identifies which products are purchased together in the same order. Enables cross-sell recommendations and store layout optimization.

## Purpose

For each product, find all other products that appear in orders containing that product. Use CONCATENATEX + DISTINCT to list co-purchased items per order, then count co-occurrences.

## Formula

```dax
Better Together 2 =
    VAR __Items = DISTINCT( 'Better Together 1'[Item_Name] )
    VAR __Table = FILTER(
        GENERATE(
            SELECTCOLUMNS( __Items, "__Item1", [Item_Name] ),
            SELECTCOLUMNS( __Items, "__Item2", [Item_Name] )
        ),
        [__Item1] <> [__Item2]
    )
    VAR __Result = ADDCOLUMNS(
        __Table,
        "Bought Together",
        VAR __T = SUMMARIZE(
            FILTER(
                'Better Together 1',
                [Item_Name] = [__Item1] | [Item_Name] = [__Item2]
            ),
            [Order_ID],
            "__Count", COUNTROWS( 'Better Together 1' )
        )
        VAR __R = COUNTROWS( FILTER( __T, [__Count] > 1 ) ) + 0
        RETURN __R
    )
    RETURN __Result
```

## Step-by-Step Breakdown

1. **DISTINCT items**: get all unique product names
2. **GENERATE Cartesian product**: every item paired with every other item (all combinations)
3. **Filter `<>`**: remove self-pairs (Kettle with Kettle)
4. **Filter `<`**: prevent duplicate reversed pairs (Iron/Kettle only once, not Kettle/Iron)
5. **ADDCOLUMNS**: for each pair, count orders where both items appear
6. **COUNTROWS > 1**: count only orders with both items together

## Example Output

| Item 1 | Item 2 | Bought Together |
|--------|--------|-----------------|
| Kettle | Iron | 3 |
| Kettle | Cucumber | 2 |
| Kettle | Tomatoes | 1 |
| Iron | Cucumber | 2 |
| Iron | Tomatoes | 1 |
| Cucumber | Tomatoes | 2 |

## Notes

- **GENERATE**: creates a Cartesian product of two tables (all combinations)
- **`<` vs `<=`**: using `<` on item names removes both self-pairs and reversed duplicates
- **SUMMARIZE grouping**: groups orders by Order_ID, counts items per order, then counts orders where count > 1 (both items present)
- Use with TOPN to find strongest associations

## Related

- [[customer-lifetime-value-ltv-dax]] — customer value
- [[customer-churn-rate-dax]] — retention
