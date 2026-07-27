# SKILL TEMPLATE: atomic

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: atomic.
An atomic note captures ONE idea, concept, rule, or mental model.
It must be self-contained — a reader should fully understand the idea
without needing to read another note first.

RULES FOR ATOMIC NOTES:
  - One idea only. If you find yourself writing "and also...", split the note.
  - No code examples unless a tiny inline snippet genuinely aids understanding.
  - No step-by-step instructions — use note_type: workflow for that.
  - No function documentation — use note_type: function for that.
  - The body should be 3-7 sentences. If longer, the idea is not atomic.

When a user asks you to create an atomic note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.
-->

---
note_type: atomic
id: <language>-<short-kebab-case-id>
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General>
title: <Short title stating the idea as a noun phrase or rule>
key_insight: <One sentence — what does this note teach? Write it as a standalone statement, as if answering a question. No hedging.>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Idea

<!--
State the single idea clearly and concisely in plain English.
Write 3-7 sentences. The first sentence must be a direct statement
of the idea — do not build up to it.
If the idea has a contrast or a common misconception, address it here.
No bullet points. No headers inside this section.
-->

<Direct statement of the single idea. Expand with context, contrast,
or clarification in the following sentences. Keep to 3-7 sentences total.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask —
"how do I...", "why does...", "when should...", "what is the difference between...".
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## Why It Matters

<!--
Explain in 1-3 sentences why understanding this idea changes how
someone writes code, builds models, or solves problems.
This should make the reader feel the practical consequence of the idea.
-->

<Why this idea is worth knowing. What goes wrong if you misunderstand it?>

## Related Notes

<!--
Link to notes that provide more detail, contrast, or context.
Use the note name or id as it appears in the frontmatter.
-->

See also: <RelatedNoteName1>, <RelatedNoteName2>
