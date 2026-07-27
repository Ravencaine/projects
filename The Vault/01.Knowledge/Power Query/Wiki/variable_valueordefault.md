---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["variable", "m-function"]
---


# Variable.ValueOrDefault

Returns the value of the specified variable identifier defined by the current evaluation environment. If the variable is not defined, the optional defaultValue is returned. --- PAGE 1338 --- Enumerations 09/16/2025 The Power Query M formula language includes these enumerations. List of enumerations ﾉ Expand table Name Description AccessControlKind.Type Specifies the kind of access control. BinaryEncoding.Type Specifies the type of binary encoding. BinaryOccurrence.Type Specifies how many times the item is expected to appear in the group. BufferMode.Type Describes the type of buffering to be performed. ByteOrder.Type Specifies the byte order. Compression.Type Specifies the type of compression. CsvStyle.Type Specifies the significance of quotes in a CSV document. Day.Type Represents the day of the week. ExtraValues.Type Specifies the expected action for extra values in a row that contains columns less than expected. GroupKind.Type Specifies the kind of grouping. JoinAlgorithm.Type Specifies the join algorithm to be used in the join operation. JoinKind.Type Specifies the kind of join operation. JoinSide.Type Specifies the left or right table of a join. LimitClauseKind.Type Indicates the features that the specific SQL dialect supports. MissingField.Type Specifies the expected action for missing values in a row that contains columns less than expected. Occurrence.Type Specifies the occurrence of an element in a sequence. ODataOmitValues.Type Specifies the kinds of values an OData service can omit. --- PAGE 1339 --- Name Description Order.Type Specifies the direction of sorting. PercentileMode.Type Specifies the percentile mode type. Precision.Type Specifies the precision of comparison. QuoteStyle.Type Specifies the quote style. RankKind.Type Specifies the precise ranking method. RelativePosition.Type Indicates whether indexing should be done from the start or end of the input. RoundingMode.Type Specifies rounding direction when there is a tie between the possible numbers to round to. SapBusinessWarehouseExecutionMode.Type Specifies valid options for SAP Business Warehouse execution mode option. SapHanaDistribution.Type Specifies valid options for SAP HANA distribution option. SapHanaRangeOperator.Type Specifies a range operator for SAP HANA range input parameters. TextEncoding.Type Specifies the text encoding type. TraceLevel.Type Specifies the trace level. WebMethod.Type Specifies an HTTP method. --- PAGE 1340 ---

## Signature

```m
Variable.ValueOrDefault(identifier as text, optional defaultValue as any) as any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| identifier | text | |
| optional defaultValue | any | |

## Returns

any

