---
created: 2026-07-27
updated: 2026-08-02
source: "RELATIONSHIP in DAX: Unlocking Role-Playing Dimensions"
note_type: function
tags: [dax, userelationship, function, inactive-relationship, role-playing]
---

# USERELATIONSHIP Function

Activates an existing inactive relationship between two tables for the duration of a CALCULATE expression — enabling role-playing dimensions without duplicating tables.

## Signature

```dax
USERELATIONSHIP ( <Column1>, <Column2> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<Column1>` | column | Foreign key column in one table (typically the fact table) |
| `<Column2>` | column | Primary key column in the related table (typically the dimension table) |

## Returns

A boolean. The relationship must already exist (inactive) between the two columns. USERELATIONSHIP does NOT create a new relationship.

## Examples

```dax
-- Sales by Invoice Date (uses default active relationship)
Sales by Invoice Date = SUM ( Sales[SalesAmount] )

-- Sales by Ship Date (activates inactive relationship)
Sales by Ship Date =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
)
```

## Notes

- Only works with **inactive** relationships that already exist in the model
- Cannot be used with non-existent relationships — use TREATAS for that case
- Does not permanently change the model; the activation is scoped to the enclosing CALCULATE
- For dynamic switching between multiple date roles, combine with SWITCH + SELECTEDVALUE

## Related

- [[role-playing-dimensions-pattern]]
- [[treatas-vs-userelationship-comparison]]
- [[calculate]]
