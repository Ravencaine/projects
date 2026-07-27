# SKILL TEMPLATE: pattern

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: pattern.
A pattern is a named, reusable combination of functions that together
solve a specific problem. It is NOT a single function — if only one
function is involved, use note_type: function instead.

When a user asks you to create a pattern note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.

SUPPORTED LANGUAGES (use exactly as shown in the language field):
  DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General

COMPLEXITY VALUES: beginner | intermediate | advanced
-->

---
note_type: pattern
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML>
name: <Descriptive Pattern Name>
components: [<Function1>, <Function2>, <Function3>]
key_insight: <One sentence — what problem does this pattern solve and why is this combination the right approach?>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
complexity: <beginner | intermediate | advanced>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## What It Does

<!--
WRITE IN PLAIN ENGLISH. This section carries more weight than in a
function note because the reader needs to understand WHY these functions
are combined, not just what each one does individually.
Answer three questions:
  1. What problem does this pattern solve?
  2. How do the components work together at a high level?
  3. When should someone reach for this pattern over alternatives?
Aim for 4-6 sentences.
-->

<Plain English explanation of the pattern, the problem it solves,
and why the components are combined this way.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask —
"how do I...", "what is the best way to...", "when should I use X instead of Y...".
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## How It Works

<!--
Break down the pattern step by step in plain English.
Describe the role of each component and the order in which
things happen. Do not show code here — this is conceptual.
Use short paragraphs, one per step.
-->

**Step 1 — <Component or action name>:**
<Explain what happens at this step and why.>

**Step 2 — <Component or action name>:**
<Explain what happens at this step and why.>

**Step 3 — <Component or action name>:**
<Explain what happens at this step and why.>

<!-- Add or remove steps as needed -->

## Template

<!--
Provide a clean blank-variable template the user can copy and fill in.
Show the full composed structure, not each function individually.
Use placeholders that make the role of each argument obvious.
No example values here — only placeholders.
-->

```<language>
<PatternStructure(
    <role_description_param1>,
    <NestedFunction>(
        <role_description_param2>,
        <role_description_param3>
    )
)>
```

## Examples

<!--
Provide at least 3 examples (or all if the source has more).
Each example must:
  - Have a descriptive ### heading explaining the scenario
  - Show the FULL composed pattern as a working code block
  - Have a plain English explanation AFTER the code block (3-5 sentences)
    explaining what is happening and why it is structured this way
  - Progress in complexity: direct use → variation → advanced composition
-->

### Example 1 — <Short scenario title>

```<language>
<Full working pattern for example 1>
```

<Plain English explanation of what this example achieves, how the
components interact, and any decisions worth noting.>

### Example 2 — <Short scenario title>

```<language>
<Full working pattern for example 2>
```

<Plain English explanation of what this example achieves, how the
components interact, and any decisions worth noting.>

### Example 3 — <Short scenario title>

```<language>
<Full working pattern for example 3>
```

<Plain English explanation of what this example achieves, how the
components interact, and any decisions worth noting.>

## Gotchas

<!--
List 2-4 known pitfalls specific to this pattern.
Focus on INTERACTION EFFECTS between the components, not
individual function quirks (those belong in function notes).
Write each as a short paragraph.
-->

<Gotcha 1: describe the interaction pitfall and how to avoid it.>

<Gotcha 2: describe the interaction pitfall and how to avoid it.>

## Prerequisites

<!--
List any conditions that must be true for this pattern to work correctly.
Examples: a marked Date table, a specific column type, a library import.
Write as short plain English statements.
-->

<Prerequisite 1>

<Prerequisite 2>

## Related Notes

<!--
Link to function notes for the individual components and any
related patterns. Use the note name as it appears in the
frontmatter name field.
-->

See also: <RelatedNoteName1>, <RelatedNoteName2>
