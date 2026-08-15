---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [table, m-function]
---


# Table.Schema

Returns a table describing the columns of table. Each row in the table describes the properties of a column of table: ﾉ Expand table Column Name Description Name The name of the column. Position The 0-based position of the column in table. TypeName The name of the type of the column. Kind The kind of the type of the column. IsNullable Whether the column can contain null values. NumericPrecisionBase The numeric base (for example, base-2 or base-10) of the NumericPrecision and NumericScale fields. NumericPrecision The precision of a numeric column in the base specified by NumericPrecisionBase. This is the maximum number of digits that can be represented by a value of this type (including fractional digits). NumericScale The scale of a numeric column in the base specified by NumericPrecisionBase. This is the number of digits in the fractional part of a value of this type. A value of 0 indicates a fixed scale with no fractional digits. A value of null indicates the scale is not known (either because it is floating or not defined). DateTimePrecision The maximum number of fractional digits supported in the seconds portion of a date or time value. MaxLength The maximum number of characters permitted in a text column, or the maximum number of bytes permitted in a binary column. --- PAGE 1111 --- Column Name Description IsVariableLength Indicates whether this column can vary in length (up to MaxLength) or if it is of fixed size. NativeTypeName The name of the type of the column in the native type system of the source (for example, nvarchar for SQL Server). NativeDefaultExpression The default expression for a value of this column in the native expression language of the source (for example, 42 or newid() for SQL Server). Description The description of the column. --- PAGE 1112 ---

## Signature

```m
Table.Schema(table as table) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | |

## Returns

table

