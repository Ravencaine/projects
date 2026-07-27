---
created: 2026-07-26
source: dax.pdf
note_type: atomic
tags: [dax, fundamentals, relationships]
---

# Table Relationships in DAX

Tabular data models support relationships between tables that DAX can traverse to retrieve related values.

## Definition

A relationship connects two tables on a key column (typically a foreign key relationship). DAX can automatically follow relationships in filter context to propagate filters and retrieve values across tables.

## Key Points

### Relationship Types

- **One-to-many**: most common. The lookup (one) side contains unique keys; the fact (many) side contains repeated keys.
- **One-to-one**: both sides have unique keys.
- **Many-to-many**: both sides can have duplicate keys. Requires careful handling to avoid ambiguity.

### Active vs Inactive Relationships

- Only one relationship between two tables is **active** at a time
- Inactive relationships are not followed automatically in filter context
- Use `USERELATIONSHIP()` inside CALCULATE to activate a specific relationship

### Relationship Direction

- **Single direction**: filter flows from the one side to the many side only
- **Both directions**: filter flows both ways (requires bidirectional cross-filtering)

### RELATED vs RELATEDTABLE

- `RELATED(Column)` — fetches a scalar value from the related table across the active relationship (requires row context)
- `RELATEDTABLE(Table)` — returns all related rows from the related table as a table

### Relationship Functions

- `CROSSFILTER()` — overrides the cross-filter direction in a specific calculation
- `USERELATIONSHIP()` — activates a specific inactive relationship for a calculation
- `TREATAS()` — maps column values from one table to another without a physical relationship

### Referential Integrity

- DAX does not enforce referential integrity (non-matching key values are allowed)
- Blank or non-matching values can cause unexpected results
- `LOOKUPVALUE()` can find values when a relationship does not exist or is inactive

## Related

- [[dax-overview]] — atomic
- [[dax-context]] — atomic
- [[related]] — function
- [[relatedtable]] — function
- [[relatedtable]] — access related rows from the many side of a relationship
- [[userexplicitrelationship]] — function (spells USERELATIONSHIP)
- [[treatas]] — function
- [[crossfilter]] — function
- [[lookupvalue]] — function
