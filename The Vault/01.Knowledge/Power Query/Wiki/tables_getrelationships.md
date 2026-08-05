---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["tables", "m-function"]
---


# Tables.GetRelationships

Gets the relationships among a set of tables. The set tables is assumed to have a structure similar to that of a navigation table. The column defined by dataColumn contains the actual data tables. --- PAGE 1160 --- #table Syntax #table(columns as any, rows as any) as any About Creates a table value from columns and rows. The columns value can be a list of column names, a table type, a number of columns, or null. The rows value is a list of lists, where each element contains the column values for a single row.

## Signature

```m
Tables.GetRelationships(tables as table, optional dataColumn as nullable text) as
table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| tables | table | |
| optional dataColumn | nullable text | |

## Returns

table

### Example 1

Create an empty table.

```m
#table({}, {})
```

// Output
```
#table({}, {})
```

### Example 2

Create a table by inferring the number of columns from the first row.

```m
#table(null, {{"Betty", 90.3}, {"Carl", 89.5}})
```

// Output
```
#table({"Column1", "Column2"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

### Example 3

Create a table by specifying the number of columns.

```m
#table(2, {{"Betty", 90.3}, {"Carl", 89.5}})
```

// Output
```
#table({"Column1", "Column2"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

### Example 4

Create a table by providing a list of column names.

```m
#table({"Name", "Score"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

// Output
```
#table({"Name", "Score"}, {{"Betty", 90.3}, {"Carl", 89.5}})
```

### Example 5

Create a table with an explicit type.

```m
#table(type table [Name = text, Score = number], {{"Betty", 90.3}, {"Carl", 89.5}})
```

// Output
```
#table(type table [Name = text, Score = number], {{"Betty", 90.3}, {"Carl", 89.5}})
```

## Related

[[type_functions]]
[[text_functions]]

[[these_functions_create_and_manipulate_text_values]]
[[information]]
[[table_expandrecordcolumn]]
[[name_description]]
[[text_infernumbertype_infers_the_granular_number_type_int64type_doubletype_and_so_on_of_a]]
[[number_encoded_in_text]]

