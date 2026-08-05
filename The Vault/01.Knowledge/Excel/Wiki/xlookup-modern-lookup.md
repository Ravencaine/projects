---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: function
tags: [excel, function, lookup, dynamic]
---

# XLOOKUP — Modern Dynamic Lookup

A versatile replacement for VLOOKUP and INDEX/MATCH that searches horizontally or vertically, supports approximate and exact matches, and returns arrays.

## Signature

```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `lookup_value` | Value | The value to search for |
| `lookup_array` | Range | The range to search in |
| `return_array` | Range | The range to return a value from |
| `if_not_found` | Value | Optional — value to return if no match |
| `match_mode` | Number | Optional — 0 (exact, default), -1 (exact or next smallest), 1 (exact or next largest), 2 (wildcard) |
| `search_mode` | Number | Optional — 1 (first-to-last, default), -1 (last-to-first), 2 (binary search) |

## Returns

The corresponding value from `return_array` at the matched position in `lookup_array`, or `if_not_found` if no match.

## Examples

```excel
=XLOOKUP(A2, TaskID, TaskName)                    ' Basic lookup: task ID → task name
=XLOOKUP(A2, TaskID, Owner, "Unknown")           ' With fallback for missing IDs
=XLOOKUP(2, PriorityCode, PriorityLabel, , -1)  ' Approximate match for priority bands
=XLOOKUP(A2, TaskID, DueDate, , , -1)            ' Search last-to-first for most recent match
```

Use in a project dashboard: look up task owner, status label, or due date from a task ID — replacing multiple nested VLOOKUPs or INDEX/MATCH chains.

## Notes

- XLOOKUP replaces VLOOKUP (vertical lookup) and HLOOKUP (horizontal lookup) with a single function.
- `lookup_array` and `return_array` do not need to be adjacent or in the same order.
- Default `match_mode` is exact match (like MATCH with `0`), not the approximate match that VLOOKUP defaults to.
- Not available in older Excel versions (pre-2019). Use INDEX/MATCH as a fallback for legacy compatibility.

## Related

- [[dynamic-status-dashboard]] — `pattern`
- [[countif-project-progress]] — `function`
- [[sumifs-conditional-project-sums]] — `function`
