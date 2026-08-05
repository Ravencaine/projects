---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "conversion", "data-type"]
note_type: function

---

# CONVERT — Data Type Conversion

Converts a value from one data type to another.

## Signature

```dax
CONVERT( <Expression>, <Type> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Expression | Any | Value to convert. |
| Type | Type keyword | Target data type: INTEGER, DOUBLE, STRING, BOOLEAN, DATETIME |

## Examples

```dax
As Integer := CONVERT( 3.7, INTEGER )     -- returns 3
As String  := CONVERT( 123, STRING )      -- returns "123"
As Boolean := CONVERT( 1, BOOLEAN )       -- returns TRUE
```

## Notes

- Returns an error if conversion is not possible
- For datetime, use DATE(), TIME(), or DATETIME() constructors
- VALUE() converts strings to numbers

## Related

- [[data-modeling-bi-trustworthy-analytics]]
