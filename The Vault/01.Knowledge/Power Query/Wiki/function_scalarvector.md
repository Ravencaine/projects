---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["function", "m-function"]
---


# Function.ScalarVector

Returns a scalar function of type scalarFunctionType that invokes vectorFunction with a single row of arguments and returns its single output. Additionally, when the scalar function is repeatedly applied for each row of a table of inputs, such as in Table.AddColumn, instead vectorFunction will be applied once for all inputs. vectorFunction will be passed a table whose columns match in name and position the parameters of scalarFunctionType. Each row of this table contains the arguments for one call to the scalar function, with the columns corresponding to the parameters of scalarFunctionType. vectorFunction must return a list of the same length as the input table, whose item at each position must be the same result as evaluating the scalar function on the input row of the same position. The input table is expected to be streamed in, so vectorFunction is expected to stream its output as input comes in, only working with one chunk of input at a time. In particular, vectorFunction must not enumerate its input table more than once.

## Signature

```m
Function.ScalarVector(scalarFunctionType as type, vectorFunction as function) as
function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| scalarFunctionType | type | |
| vectorFunction | function | |

## Returns

function

### Example 1

Multiply two columns of the input table by processing the inputs in batches of 100.

```m
let
Compute.ScoreScalar = (left, right) => left * right,
// When Function.ScalarVector batching kicks in, we'll receive all
// of the inputs for the entire table here at once.
Compute.ScoreVector = (input) => let
chunks = Table.Split(input, 100),
scoreChunk = (chunk) => Table.TransformRows(chunk, each
Compute.ScoreScalar([left], [right]))
in
List.Combine(List.Transform(chunks, scoreChunk)),
Compute.Score = Function.ScalarVector(
type function (left as number, right as number) as number,
Compute.ScoreVector
),
Final = Table.AddColumn(
Table.FromRecords({
[a = 1, b = 2],
[a = 3, b = 4]
}),
"Result",
each Compute.Score([a], [b])
)
in
Final
```

// Output
```
Table.FromRecords({
[a = 1, b = 2, Result = 2],
[a = 3, b = 4, Result = 12]
})
```

### Example 2

Compute test scores in batches of two, and populate a batch ID field that can be used to verify that batching is working as expected.

```m
let
_GradeTest = (right, total) => Number.Round(right / total, 2),
_GradeTests = (inputs as table) as list => let
batches = Table.Split(inputs, 2),
gradeBatch = (batch as table) as list =>
let
batchId = Text.NewGuid()
in
Table.TransformRows(batch, each [Grade = _GradeTest([right], [total]),
BatchId = batchId])
in
List.Combine(List.Transform(batches, gradeBatch)),
GradeTest = Function.ScalarVector(type function (right as number, total as number)
as number, _GradeTests),
Tests = #table(type table [Test Name = text, Right = number, Total = number],
{
{"Quiz 1", 3, 4},
{"Test 1", 17, 22},
{"Quiz 2", 10, 10}
}),
// To break batching, replace [Right] with {[Right]}{0}.
TestsWithGrades = Table.AddColumn(Tests, "Grade Info", each GradeTest([Right],
[Total]), type record),
// To verify batching, also expand BatchId.
Final = Table.ExpandRecordColumn(TestsWithGrades, "Grade Info", {"Grade"})
in
Final
```

// Output
```
#table(
type table [Test Name = text, Right = number, Total = number, Grade = number],
{
{"Quiz 1", 3, 4, 0.75},
{"Test 1", 17, 22, 0.77},
{"Quiz 2", 10, 10, 1}
}
)
Last updated on 11/05/2025
Lines functions
Article • 08/04/2022
These functions convert lists of text to and from binary and single text values.
Name Description
Lines.FromBinary Converts a binary value to a list of text values split at lines breaks.
Lines.FromText Converts a text value to a list of text values split at lines breaks.
Lines.ToBinary Converts a list of text into a binary value using the specified encoding and
lineSeparator.The specified lineSeparator is appended to each line. If not
specified then the carriage return and line feed characters are used.
Lines.ToText Converts a list of text into a single text. The specified lineSeparator is
appended to each line. If not specified then the carriage return and line feed
characters are used.
Feedback
Was this page helpful? ﾂ Yes ﾄ No
Get help at Microsoft Q&A
```

