---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["binary", "m-function"]
---


# Binary.Range

Returns a subset of the binary value beginning at the offset binary. An optional parameter, offset, sets the maximum length of the subset.

## Signature

```m
Binary.Range(
binary as binary,
offset as number,
optional count as nullable number
) as binary
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| binary | binary | |
| offset | number | |
| optional count | nullable number | |

## Returns

binary

### Example 1

Returns a subset of the binary value starting at offset 6.

```m
Binary.Range(#binary({0..10}), 6)
```

// Output
```
#binary({6, 7, 8, 9, 10})
```

### Example 2

Returns a subset of length 2 from offset 6 of the binary value.

```m
Binary.Range(#binary({0..10}), 6, 2)
```

// Output
```
#binary({6, 7})
```

