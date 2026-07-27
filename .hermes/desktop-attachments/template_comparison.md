# SKILL TEMPLATE: comparison

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: comparison.
A comparison note directly contrasts two or more things to help the
reader build accurate mental models and make correct choices.

RULES FOR COMPARISON NOTES:
  - Compare exactly 2 or 3 things. More than 3 becomes a reference note.
  - The recommendation section MUST give clear guidance on when to use each.
    Do not write "it depends" without explaining what it depends on.
  - The comparison table is mandatory. It is the most scannable part.
  - Both subjects must be documented with equal depth — no bias toward
    one being the "correct" choice unless that is genuinely the case.

When a user asks you to create a comparison note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.

SUPPORTED LANGUAGES (use exactly as shown in the language field):
  DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General
-->

---
note_type: comparison
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General>
name: <SubjectA> vs <SubjectB>
subjects: [<SubjectA>, <SubjectB>]
key_insight: <One sentence — what is the most important distinction to know when choosing between these two?>
answers: [<Question pattern this note answers 1>, <Question pattern this note answers 2>]
tags: [<tag1>, <tag2>]
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Overview

<!--
In 3-5 sentences, set up the comparison.
Explain what both subjects are and why the distinction matters.
Do not favour one over the other here — that comes in the Recommendation.
-->

<Neutral overview of both subjects and why developers need to understand
the difference between them.>

## Questions This Note Answers

<!--
List the specific question patterns this note addresses.
Write them as questions a developer would actually ask —
"when should I use X vs Y...", "what is the difference between...", "which is faster for...".
Include at least 2. These feed the `answers` frontmatter field.
-->
- <Question 1?>
- <Question 2?>

## <SubjectA>

<!--
Describe Subject A in plain English: what it does, how it works,
and what it is optimised for. 3-5 sentences.
-->

<Description of Subject A.>

```<language>
<!-- Example usage of Subject A -->
<code>
```

## <SubjectB>

<!--
Describe Subject B in plain English: what it does, how it works,
and what it is optimised for. 3-5 sentences.
-->

<Description of Subject B.>

```<language>
<!-- Example usage of Subject B -->
<code>
```

## Side-by-Side Comparison

<!--
Fill in the table. Add or remove rows as appropriate for the subjects.
Common rows: Performance, Syntax, Use Case, Limitations, Returns, Context.
-->

| Dimension | <SubjectA> | <SubjectB> |
|-----------|-----------|-----------|
| <Dimension 1> | <SubjectA value> | <SubjectB value> |
| <Dimension 2> | <SubjectA value> | <SubjectB value> |
| <Dimension 3> | <SubjectA value> | <SubjectB value> |
| <Dimension 4> | <SubjectA value> | <SubjectB value> |

## Recommendation

<!--
Give clear, actionable guidance.
Structure as: Use <SubjectA> when... Use <SubjectB> when...
Do not be vague. Specify the conditions that determine the right choice.
-->

**Use <SubjectA> when** <specific condition that favours SubjectA>.

**Use <SubjectB> when** <specific condition that favours SubjectB>.

<Any additional nuance, e.g. cases where either works or where a third
option should be considered instead.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
