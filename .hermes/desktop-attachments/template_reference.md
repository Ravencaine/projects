# SKILL TEMPLATE: reference

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: reference.
A reference note is a lookup table or quick-reference sheet.
It is structured data, not an explanation. The reader scans it,
they do not read it top to bottom.

DISTINCTION GUIDE:
  - Use note_type: atomic      → to explain a concept
  - Use note_type: comparison  → to contrast two specific things
  - Use note_type: reference   → for a structured lookup table covering
                                  multiple items of the same kind
                                  (e.g. all SQL data types, all CSS units,
                                  all DAX operator precedence rules,
                                  all VBA error codes)

RULES FOR REFERENCE NOTES:
  - The table is the primary content. Everything else supports it.
  - Rows must be consistent — every row uses the same columns.
  - Values in cells must be brief. If a cell needs more than one sentence,
    the information belongs in a function or atomic note instead.
  - Omit the Examples section entirely if examples would be redundant.

When a user asks you to create a reference note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.
-->

---
note_type: reference
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General>
name: <Descriptive title, e.g. "SQL Aggregate Functions", "CSS Length Units">
tags: [<tag1>, <tag2>]
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## What This Covers

<!--
One or two sentences only. State what set of things this table covers
and what the reader will use it to look up.
-->

<One sentence stating what this reference covers and when to use it.>

## Reference Table

<!--
Design the columns to fit the subject matter.
Common column patterns:
  Functions:    | Name | Syntax | Returns | Notes |
  Data types:   | Type | Description | Range/Size | Example |
  Operators:    | Operator | Precedence | Description | Example |
  Keywords:     | Keyword | Context | Description |
  CSS units:    | Unit | Type | Relative To | Best Used For |
  Error codes:  | Code | Name | Meaning | Common Cause |
Choose the columns that make the table maximally useful for scanning.
-->

| <Column 1> | <Column 2> | <Column 3> | <Column 4> |
|------------|------------|------------|------------|
| <value> | <value> | <value> | <value> |
| <value> | <value> | <value> | <value> |
| <value> | <value> | <value> | <value> |

## Notes

<!--
Optional. Use only for information that applies to the table as a whole
or that cannot fit cleanly in a cell. Keep to 3 sentences or fewer.
If there is nothing meaningful to add, remove this section.
-->

<Any table-wide caveats, version notes, or context that helps the reader
use the table correctly.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
