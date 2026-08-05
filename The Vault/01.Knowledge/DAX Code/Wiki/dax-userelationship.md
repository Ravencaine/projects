---


title: "USERELATIONSHIP"
created: 2026-07-28
updated: 2026-08-02
tags: [dax, function, relationships]
note_type: function
description: "USERELATIONSHIP — temporarily activates an inactive relationship in a DAX expression. Used when a fact table has multiple date keys. From DAX Index (Dunlop)."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# USERELATIONSHIP

Temporarily overrides the default active relationship between two tables and activates a specified inactive relationship for the duration of the calculation.

## Syntax

```
USERELATIONSHIP( <column1>, <column2> )
```

## Arguments

| Argument | Description |
|----------|-------------|
| `column1` | The foreign key column in the "many" side |
| `column2` | The primary key column in the "one" side |

## When to Use

- A fact table has **multiple date columns** (e.g., OrderDate, ShipDate, DueDate) each referencing a date dimension
- The active relationship defaults to one (e.g., OrderDate), but you need to calculate something using another (e.g., ShipDate)
- Wrap `USERELATIONSHIP()` inside `CALCULATE()` to activate it for specific measures

## Example

```dax
-- Average days to ship (using inactive ShipDate relationship)
Avg Days to Ship :=
CALCULATE(
    AVERAGE( 'Sales'[DaysToShip] ),
    USERELATIONSHIP( 'Sales'[ShipDate], 'Date'[Date] )
)
```

## Key Rules

- Can only be used as a filter argument inside `CALCULATE`
- Both columns must be from tables that have an inactive relationship defined in the model
- Only one USERELATIONSHIP can be active at a time within the same CALCULATE
- The relationship must exist in the model diagram — it doesn't create a new relationship

## Related Functions

- `CALCULATE` — required wrapper for USERELATIONSHIP
- `RELATED` — retrieves a value from the "one" side of a relationship
- `LOOKUPVALUE` — similar but no relationship required

## Source Reference

Listed in the DAX Index of *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
