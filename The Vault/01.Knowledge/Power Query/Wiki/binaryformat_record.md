---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: [binaryformat, m-function]
---


# BinaryFormat.Record

Returns a binary format that reads a record. The record parameter specifies the format of the record. Each field in the record can have a different binary format. If a field contains a value that is not a binary format value, then no data is read for that field, and the field value is echoed to the result.

## Signature

```m
BinaryFormat.Record(record as record) as function
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| record | record | |

## Returns

function

### Example 1

Read a record containing one 16-bit integer and one 32-bit integer.

```m
let
binaryData = #binary({
0x00, 0x01,
0x00, 0x00, 0x00, 0x02
}),
recordFormat = BinaryFormat.Record([
A = BinaryFormat.UnsignedInteger16,
B = BinaryFormat.UnsignedInteger32
])
in
recordFormat(binaryData)
```

// Output
```
[A = 1, B = 2]
```

