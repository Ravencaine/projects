---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["xml", "m-function"]
---


# Xml.Tables

Returns the contents of the XML document as a nested collection of flattened tables.

## Signature

```m
Xml.Tables(
contents as any,
optional options as nullable record,
optional encoding as nullable number
) as table
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| contents | any | |
| optional options | nullable record | |
| optional encoding | nullable number | |

## Returns

table

### Example 1

Retrieve the contents of a local XML file.

```m
Xml.Tables(File.Contents("C:\invoices.xml"))
```

// Output
```
table
Binary functions
Article • 02/21/2023
These functions create and manipulate binary data.
Binary Formats
Reading numbers
Name Description
BinaryFormat.7BitEncodedSignedInteger A binary format that reads a 64-bit signed integer
that was encoded using a 7-bit variable-length
encoding.
BinaryFormat.7BitEncodedUnsignedInteger A binary format that reads a 64-bit unsigned integer
that was encoded using a 7-bit variable-length
encoding.
BinaryFormat.Binary Returns a binary format that reads a binary value.
BinaryFormat.Byte A binary format that reads an 8-bit unsigned
integer.
BinaryFormat.Choice Returns a binary format that chooses the next binary
format based on a value that has already been read.
BinaryFormat.Decimal A binary format that reads a .NET 16-byte decimal
value.
BinaryFormat.Double A binary format that reads an 8-byte IEEE double-
precision floating point value.
BinaryFormat.Group Returns a binary format that reads a group of items.
Each item value is preceded by a unique key value.
The result is a list of item values.
BinaryFormat.Length Returns a binary format that limits the amount of
data that can be read. Both BinaryFormat.List and
BinaryFormat.Binary can be used to read until end of
the data. BinaryFormat.Length can be used to limit
the number of bytes that are read.
BinaryFormat.List Returns a binary format that reads a sequence of
items and returns a list.
Name Description
BinaryFormat.Null A binary format that reads zero bytes and returns
null.
BinaryFormat.Record Returns a binary format that reads a record. Each
field in the record can have a different binary
format.
BinaryFormat.SignedInteger16 A binary format that reads a 16-bit signed integer.
BinaryFormat.SignedInteger32 A binary format that reads a 32-bit signed integer.
BinaryFormat.SignedInteger64 A binary format that reads a 64-bit signed integer.
BinaryFormat.Single A binary format that reads a 4-byte IEEE single-
precision floating point value.
BinaryFormat.Text Returns a binary format that reads a text value. The
optional encoding value specifies the encoding of
the text.
BinaryFormat.Transform Returns a binary format that will transform the
values read by another binary format.
BinaryFormat.UnsignedInteger16 A binary format that reads a 16-bit unsigned
integer.
BinaryFormat.UnsignedInteger32 A binary format that reads a 32-bit unsigned
integer.
BinaryFormat.UnsignedInteger64 A binary format that reads a 64-bit unsigned
integer.
Controlling byte order
Name Description
BinaryFormat.ByteOrder Returns a binary format with the byte order specified by a function.
Table.PartitionValues Returns information about how a table is partitioned.
Binary data
Name Description
Binary.ApproximateLength Returns the approximate length of the binary.
Name Description
Binary.Buffer Buffers the binary value in memory. The result of this call is a stable
binary value, which means it will have a deterministic length and
order of bytes.
Binary.Combine Combines a list of binaries into a single binary.
Binary.Compress Compresses a binary value using the given compression type.
Binary.Decompress Decompresses a binary value using the given compression type.
Binary.From Returns a binary value from the given value.
Binary.FromList Converts a list of numbers into a binary value
Binary.FromText Decodes data from a text form into binary.
Binary.InferContentType Returns a record with field Content.Type that contains the inferred
MIME-type.
Binary.Length Returns the length of binary values.
Binary.Range Returns a subset of the binary value beginning at an offset.
Binary.Split Splits the specified binary into a list of binaries using the specified
page size.
Binary.ToList Converts a binary value into a list of numbers
Binary.ToText Encodes binary data into a text form.
Binary.View Creates or extends a binary with user-defined handlers for query and
action operations.
Binary.ViewError Creates a modified error record which won't trigger a fallback when
thrown by a handler defined on a view (via Binary.View).
Binary.ViewFunction Creates a function that can be intercepted by a handler defined on a
view (via Binary.View).
#binary Creates a binary value from numbers or text.
Feedback
Was this page helpful? ﾂ Yes ﾄ No
Get help at Microsoft Q&A
```

