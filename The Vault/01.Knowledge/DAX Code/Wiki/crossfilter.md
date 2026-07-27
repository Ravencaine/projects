---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, relationship]
---

# CROSSFILTER

## Signature

```dax
CROSSFILTER(<columnName1>, <columnName2>, <crossFilterType>)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `<columnName1>` | First column from the relationship to modify. |
| `<columnName2>` | Second column from the relationship to modify. |
| `<crossFilterType>` | Direction: `ONEWAY`, `BOTH`, or `NONE`. |

## Returns

Modifies the filter direction for the current calculation only — does not persist beyond the enclosing expression.

## Examples

```dax
-- Enable bidirectional filtering for a specific calculation
CALCULATE([Sales], CROSSFILTER('Sales'[ProductKey], 'Product'[ProductKey], BOTH))

-- Disable cross-filtering entirely for a specific calculation
CALCULATE([Sales], CROSSFILTER('Sales'[ProductKey], 'Product'[ProductKey], NONE))
```

## Notes

- Overrides the cross-filter direction for a specific calculation **without permanently changing** the model's relationship settings.
- `NONE` disables cross-filtering entirely for that relationship during the calculation.
- `BOTH` makes the filter bidirectional — useful when a calculation requires filtering in both directions but the model is configured as one-way.
- Prefer `CROSSFILTER` over manually changing relationship settings when bidirectional filtering is only needed for one specific measure.

## Related

- [[userexplicitrelationship]] — activates an inactive relationship (different use case)
- [[calculate]] — the only context where CROSSFILTER is valid
