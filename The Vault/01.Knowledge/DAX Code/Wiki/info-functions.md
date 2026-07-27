---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, information-functions, metadata, dmv, model-introspection]
---

# INFO Functions (Model Introspection)

DAX INFO functions return metadata about the data model. They are useful for documentation, auditing, and model documentation.

## Table / Column Metadata

### INFO.VIEW.COLUMNS

```dax
INFO.VIEW.COLUMNS(<table_name>)
```

Returns information about columns in a table: names, data types, visibility, etc.

### INFO.VIEW.MEASURES

```dax
INFO.VIEW.MEASURES(<table_name>)
```

Returns information about measures in a table: names, expressions, format strings.

### INFO.VIEW.RELATIONSHIPS

```dax
INFO.VIEW.RELATIONSHIPS()
```

Returns all relationships in the model: columns, cross-filter directions, cardinality.

### INFO.VIEW.TABLES

Returns information about all tables in the model.

## Storage Metadata

### INFO.STORAGETABLES

```dax
INFO.STORAGETABLES()
```

Returns information about storage tables: row counts, partitions, data sizes.

### INFO.STORAGEFOLDERS

Returns information about storage folder structure.

## Model Metadata

### INFO.VARIATIONS

```dax
INFO.VARIATIONS(<table_name>)
```

Returns all variations defined for a table (used in composite models).

### INFO.CSDLMETADATA

```dax
INFO.CSDLMETADATA()
```

Returns the CSDL (Conceptual Schema Definition Language) metadata for the model — the full model schema in XML format.

### INFO.DATACOVERAGEDEFINITIONS

Returns data coverage definitions for the model.

## Function Discovery

### INFO.FUNCTIONS

```dax
INFO.FUNCTIONS(<category>)
```

Returns all DAX functions in a given category. Categories: Math, Trig, Math, Financial, DateTime, TimeIntelligence, Filter, Information, Logical, Statistical, Table, Text.

```dax
INFO.FUNCTIONS("Math")
INFO.FUNCTIONS("Text")
```

## Use Cases

- **Documentation**: Generate model documentation automatically
- **Auditing**: Check column data types and measure expressions
- **Comparison**: Compare two versions of a model
- **Governance**: Enforce naming conventions and standards

## Example: Document All Measures

```dax
EVALUATE INFO.VIEW.MEASURES("Sales")
```

## Related

- [[information-functions-overview]]
