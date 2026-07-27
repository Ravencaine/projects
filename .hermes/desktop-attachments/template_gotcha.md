# SKILL TEMPLATE: gotcha

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: gotcha.
A gotcha documents a known footgun, counterintuitive behaviour, or
silent failure. The focus is on what trips people up in practice,
not on explaining how a feature is supposed to work.

DISTINCTION GUIDE:
  - Use note_type: atomic   → to explain a concept or mental model
  - Use note_type: error    → to document a specific error message
  - Use note_type: gotcha   → for behaviour that is technically correct
                               but surprises developers (no error raised,
                               wrong result produced silently, or common
                               misuse that compiles/runs fine but is wrong)

When a user asks you to create a gotcha note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.
-->

---
note_type: gotcha
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML>
name: <Short title that names the trap, e.g. "VLOOKUP defaults to approximate match">
key_insight: <One sentence — what is the counterintuitive behaviour that catches developers off guard?>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
severity: <low | medium | high>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

<!--
SEVERITY GUIDE:
  low    → mildly confusing but easy to spot once you know
  medium → produces wrong results silently or wastes significant debugging time
  high   → causes data errors or production failures that are hard to detect
-->

## The Trap

<!--
Describe the counterintuitive behaviour in plain English.
Be specific: what does the developer expect to happen, and what
actually happens instead? Do not assume the reader knows it is a trap.
Aim for 3-5 sentences.
-->

<What the developer expects to happen. What actually happens instead.
Why the behaviour exists — briefly. Whether it produces an error or
fails silently.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask —
"why does X behave like...", "how do I avoid...", "what happens when...".
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## Example — The Trap in Action

<!--
Show code that demonstrates the gotcha.
Add an inline comment marking the line that causes the problem.
If the output is non-obvious, include a commented expected vs actual block.
-->

```<language>
<Code that demonstrates the gotcha>

<!-- Expected: <what the developer expected> -->
<!-- Actual:   <what actually happens> -->
```

## The Fix

<!--
Show the corrected code and explain in 2-4 sentences why it works.
-->

```<language>
<Corrected code>
```

<Plain English explanation of why the fix works and what it changes.>

## How to Avoid It

<!--
Give 1-3 practical rules or habits that prevent this trap.
Write as short plain English statements, not bullet points.
-->

<Rule or habit 1 that prevents this trap.>

<Rule or habit 2 that prevents this trap.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
