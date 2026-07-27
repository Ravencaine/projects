# SKILL TEMPLATE: function

<!-- 
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: function.
When a user asks you to create a function note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.

SUPPORTED LANGUAGES (use exactly as shown in the language field):
  DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General

COMPLEXITY VALUES: beginner | intermediate | advanced
-->

---
note_type: function
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General>
name: <FunctionName>
syntax: <FunctionName(param1, param2, ...)>
key_insight: <One sentence — what is the single most important thing to know about this function?>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
complexity: <beginner | intermediate | advanced>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## What It Does

<!-- 
WRITE IN PLAIN ENGLISH. No jargon unless explained.
Answer two questions:
  1. What does this function do in a single sentence?
  2. Why would someone reach for it — what problem does it solve?
Aim for 3-5 sentences. Avoid repeating the syntax.
-->

<Plain English explanation of what the function does and why it is useful.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask —
"how do I...", "what does X return when...", "can X do Y...".
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## Syntax Breakdown

<!-- 
Document every parameter. Use the table below.
For optional parameters add (optional) after the description.
-->

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| <param1> | <type> | Yes / No | <What this parameter controls> |
| <param2> | <type> | Yes / No | <What this parameter controls> |

## Template

<!-- 
Provide a clean blank-variable template the user can copy and fill in.
Use the exact language syntax. No example values here — only placeholders.
-->

```<language>
<FunctionName>(
    <param1>,
    <param2>
)
```

## Examples

<!-- 
Provide at least 3 examples. If more exist in the source, include all of them.
Each example must:
  - Have a descriptive ### heading explaining the scenario
  - Show a complete, working code block
  - Have a plain English explanation AFTER the code block (2-4 sentences)
  - Progress in complexity: simple → moderate → advanced/composed
-->

### Example 1 — <Short scenario title>

```<language>
<working code for example 1>
```

<Plain English explanation of what this example does and why it is written this way.>

### Example 2 — <Short scenario title>

```<language>
<working code for example 2>
```

<Plain English explanation of what this example does and why it is written this way.>

### Example 3 — <Short scenario title>

```<language>
<working code for example 3>
```

<Plain English explanation of what this example does and why it is written this way.>

## Gotchas

<!-- 
List 2-4 known pitfalls, edge cases, or counterintuitive behaviours.
Write each as a short paragraph or a single sentence. No bullet points.
Focus on what trips people up in real use, not theoretical edge cases.
-->

<Gotcha 1: describe the pitfall and how to avoid or work around it.>

<Gotcha 2: describe the pitfall and how to avoid or work around it.>

## Related Notes

<!-- 
Link to other notes in the knowledge base that are directly relevant.
Use the note name as it appears in the frontmatter name field.
List as comma-separated values on a single line.
-->

See also: <RelatedNoteName1>, <RelatedNoteName2>
