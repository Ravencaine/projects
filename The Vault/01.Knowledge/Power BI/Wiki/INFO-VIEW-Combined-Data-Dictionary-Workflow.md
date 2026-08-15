---
created: 2026-08-09
updated: 2026-08-09
source: "Data Dictionary in Power BI Create One with INFO.VIEW.md"
note_type: pattern
tags: [power-bi, data-dictionary, metadata, info.view, selectcolumns, union, documentation, model]
---

# INFO.VIEW Combined Data Dictionary Workflow

Combine all four INFO.VIEW outputs into a single unified, filterable data dictionary table using SELECTCOLUMNS + UNION.

## Four INFO.VIEW Building Blocks

```dax
ModelMeasures      = INFO.VIEW.MEASURES()
ModelTables        = INFO.VIEW.TABLES()
ModelColumns       = INFO.VIEW.COLUMNS()
ModelRelationships  = INFO.VIEW.RELATIONSHIPS()
```

## Combined Data Dictionary Pattern

```dax
DataDictionary =
VAR MeasuresTable =
    SELECTCOLUMNS(
        ModelMeasures,
        "Name",     [Name],
        "Type",     "Measure",
        "Expression", IFERROR([Expression], ""),
        "Description", IFERROR([Description], "")
    )
VAR TablesTable =
    SELECTCOLUMNS(
        ModelTables,
        "Name",     [Name],
        "Type",     "Table",
        "Expression", "",
        "Description", IFERROR([Description], "")
    )
VAR ColumnsTable =
    SELECTCOLUMNS(
        ModelColumns,
        "Name",     [Name],
        "Type",     "Column",
        "Expression", "",
        "Description", IFERROR([Description], "")
    )
VAR RelationshipsTable =
    SELECTCOLUMNS(
        ModelRelationships,
        "Name",     [From Table] & " → " & [To Table],
        "Type",     "Relationship",
        "Expression", [Cross Filter Direction] & " | " & [Cardinality],
        "Description", ""
    )
RETURN
    UNION(MeasuresTable, TablesTable, ColumnsTable, RelationshipsTable)
```

## How It Works

1. Each INFO.VIEW output is shaped with SELECTCOLUMNS to extract only the relevant fields
2. A synthetic `Type` column is added to each sub-table to identify the source (Measure, Table, Column, Relationship)
3. IFERROR wraps Description/Expression to handle blanks gracefully
4. UNION stacks all four sub-tables into one flat table
5. The `Type` column enables a slicer to filter by category

## Enriching the Dictionary

**Add measure descriptions** in Model view (select measure → Properties pane → Description). Refresh the ModelMeasures table and the description propagates into the union automatically.

**Add table/column descriptions** the same way — available via the Description column in INFO.VIEW.TABLES and INFO.VIEW.COLUMNS.

## Interactive Report Page

Build a dedicated report page exposing the DataDictionary table:

- Table visual: Name, Type, Description, Expression columns
- Text slicer on Name: search by keyword
- Slicer on Type: filter to Measure, Table, Column, or Relationship only

This gives non-technical users a self-service way to explore the model's documentation without opening Model view.

## Why Not Keep Separate Tables?

Separate INFO.VIEW tables are easier to maintain but harder to explore. A single combined table enables cross-filtering between types (e.g., "show all components where Description is blank") and a unified search experience. Trade-off: the combined UNION approach requires DAX knowledge to maintain; separate tables are simpler but siloed.

## Related

- [[info.view.tables]] — INFO.VIEW.TABLES reference
- [[info.view.columns]] — INFO.VIEW.COLUMNS reference
- [[info.view.relationships]] — INFO.VIEW.RELATIONSHIPS reference
- [[Source-Data-Dictionary-in-Power-BI-INFO-VIEW]] — source note
