---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: [m-language, metadata]
---


# Metadata in M

Every M value can carry metadata — additional information stored in a metadata record. Metadata is accessed with `Value.Metadata(value)` and attached using `value meta [field = value]`. Metadata does not affect the value itself.

## Key Points

- Every value has an empty metadata record by default
- Metadata is attached with the `meta` operator: `value meta [Key = "data"]`
- Multiple meta calls are merged (record merge semantics)
- Access metadata with `Value.Metadata(value)`
- Metadata is preserved through most operations but some functions strip it

## Examples

```m
// Attach metadata
"Masterpiece" meta [Rating = 5, Genre = "Classical"]
// Result: text value with metadata Rating=5, Genre="Classical"

// Access metadata
Composer = "Mozart" meta [Rating = 5, Tags = {"Classical"}],
Rating = Value.Metadata(Composer)[Rating]  // 5

// Merging metadata
("Mozart" meta [Rating = 5]) meta [Tags = {"Classical"}]
// Equivalent to:
"Mozart" meta [Rating = 5, Tags = {"Classical"}]
```

## Related

- [[value_removemetadata]] — replaceMetadata
- [[value_removemetadata]] — removeMetadata
