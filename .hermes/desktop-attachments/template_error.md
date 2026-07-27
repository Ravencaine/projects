# SKILL TEMPLATE: error

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: error.
An error note documents a specific error message, what causes it,
and how to resolve it. It is tied to a real error that surfaces
during development, not a theoretical failure mode.

RULES FOR ERROR NOTES:
  - The error_message field must be the exact text of the error,
    copied verbatim, so it is searchable.
  - Causes and fixes must be concrete — avoid vague advice like
    "check your data" without saying what to check and why.
  - If an error has multiple distinct causes, each gets its own
    Cause/Fix pair under the Resolution section.

When a user asks you to create an error note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.
-->

---
note_type: error
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML>
name: <Short human-readable error name>
error_message: "<Exact error message text as it appears in the tool/IDE>"
key_insight: <One sentence — what is the root cause or the key lesson from this error?>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## What This Error Means

<!--
Explain in plain English what the error is telling you.
Do not restate the error message — translate it.
Aim for 2-4 sentences. A developer who has never seen this error
before should understand the nature of the problem after reading this.
-->

<Plain English translation of what the error means and the general
category of problem it represents.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask.
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## Resolution

<!--
Document each distinct cause and its fix as a pair.
If there is only one cause, use a single pair.
For each pair:
  - Cause: what specific condition triggers this error
  - Fix: the exact action to resolve it, with a code block if needed
-->

### Cause 1 — <Short description of this cause>

**Why this happens:**
<Explain the specific condition that produces the error.>

**Fix:**
<Explain the resolution in plain English.>

```<language>
<!-- Before (broken) -->
<code that produces the error>

<!-- After (fixed) -->
<code that resolves the error>
```

### Cause 2 — <Short description of this cause>

**Why this happens:**
<Explain the specific condition that produces the error.>

**Fix:**
<Explain the resolution in plain English.>

```<language>
<!-- Before (broken) -->
<code that produces the error>

<!-- After (fixed) -->
<code that resolves the error>
```

<!-- Add or remove Cause/Fix pairs as needed -->

## How to Diagnose

<!--
Describe the diagnostic steps someone should follow to identify
which cause applies to their situation. Keep it practical.
Write as short plain English paragraphs, not a checklist.
-->

<Step 1: what to check first and what the result tells you.>

<Step 2: what to check next if step 1 does not identify the problem.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
