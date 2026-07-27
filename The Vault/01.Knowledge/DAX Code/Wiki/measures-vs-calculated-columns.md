---
created: 2026-07-26
source: dax.pdf
note_type: atomic
tags: [dax, fundamentals, measures, calculated-columns]
---

# Measures vs Calculated Columns

Measures and calculated columns are both DAX formulas, but they differ fundamentally in when and how they evaluate.

## Definition

- **Calculated Column**: evaluated once per row when the model processes or refreshes. Results are stored in the model.
- **Measure**: evaluated dynamically at query time for each cell in a report, based on the current filter context.

## Key Points

| | Calculated Column | Measure |
|---|---|---|
| Evaluation | Row-level, at refresh time | Cell-level, at query time |
| Storage | Stored in the model | Not stored — recalculated each query |
| Context | Row context only | Filter context only |
| Updates | Only when model is refreshed | Updates with every user interaction |
| Use for | Pre-computing values per row | Dynamic aggregations |
| Performance | Can improve query performance | Can slow queries if complex |

### Calculated Column Rules

- A formula like `[Column1] + [Column2]` adds the two columns' values for each row
- Must be re-calculated on model refresh
- Can be used as relationship keys
- Row-level security formulas can reference calculated columns

### Measure Rules

- Syntax: `MeasureName := <expression>` (name before the formula, unlike calculated columns)
- Result cannot be determined without filter context
- Appears in the Fields pane associated with a table (home table)
- Measures can be passed as arguments to other measures

### When to Use Each

- Use calculated columns when the value is constant per row and used for relationships, sorting, or row-level security
- Use measures when the value depends on the current report context

## Related

- [[dax-overview]] — atomic
- [[dax-context]] — atomic
- [[sum]] — function
- [[sumx]] — function
