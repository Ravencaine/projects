# SKILL TEMPLATE: snippet

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: snippet.
A snippet is a reusable block of boilerplate code that is copied
and adapted rather than called like a function. It is more reusable
than a one-off example but less conceptual than a pattern.

DISTINCTION GUIDE:
  - Use note_type: function  → if documenting a single callable function
  - Use note_type: pattern   → if documenting composed functions with logic
  - Use note_type: snippet   → if documenting boilerplate scaffold code
                               that is copied and filled in (e.g. a CTE
                               scaffold, a Python class skeleton, an HTML
                               meta block, a standard import block)

When a user asks you to create a snippet note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.

SUPPORTED LANGUAGES (use exactly as shown in the language field):
  DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General
-->

---
note_type: snippet
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML>
name: <Descriptive name for this snippet>
tags: [<tag1>, <tag2>]
complexity: <beginner | intermediate | advanced>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## What It Is

<!--
Describe what this snippet is and what situation it is used in.
Answer: what do you paste this into, and what does it give you?
Aim for 2-4 sentences. No jargon without explanation.
-->

<Plain English description of what this snippet is, when to use it,
and what it provides to the developer.>

## Snippet

<!--
The ready-to-copy code block.
Use FILL_IN as the placeholder token for parts the user must replace.
Add inline comments inside the code to explain non-obvious sections.
This is the primary content of a snippet note.
-->

```<language>
<Full boilerplate snippet with FILL_IN placeholders and inline comments>
```

## Customisation Guide

<!--
Document each FILL_IN placeholder and what the user should put there.
Use the table format below. Add rows as needed.
-->

| Placeholder | What to Replace It With |
|-------------|-------------------------|
| FILL_IN_1 | <Description of what goes here> |
| FILL_IN_2 | <Description of what goes here> |

## Example — Filled In

<!--
Show the snippet filled in with a realistic, concrete example.
This helps the user verify they have used the snippet correctly.
One example only — this is not a function note.
-->

```<language>
<The snippet with all FILL_IN values replaced with realistic example values>
```

<Brief plain English description of what this filled-in example produces.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
