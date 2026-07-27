---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, relationship]
---

# USERELATIONSHIP

## Signature

```dax
USERELATIONSHIP(<column1>, <column2>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<column1>` | Typically the many-side column of the relationship. |
| `<column2>` | Typically the one-side column of the relationship. |

## Returns

Activates the specified relationship for the duration of the enclosing `CALCULATE` or `CALCULATETABLE`.

## Examples

```dax
-- Use ShipDate instead of OrderDate to calculate shipping-based metrics
CALCULATE([Sales], USERELATIONSHIP('Sales'[ShipDate], 'Date'[Date]))
```

## Notes

- Only works **inside `CALCULATE` or `CALCULATETABLE`** — cannot be used standalone.
- Activates a relationship that is marked as **inactive** in the data model.
- Useful when you need to filter by a different date (e.g., ship date vs. order date) than the active date relationship.
- The relationship must already exist in the model; this function only toggles its active state for the current calculation.

## Related

- [[related]] — fetches values across the active relationship
- [[calculate]] — the only context where USERELATIONSHIP is valid
- [[crossfilter]] — modifies filter direction instead of activating a different relationship
