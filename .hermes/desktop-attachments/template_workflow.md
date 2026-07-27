# SKILL TEMPLATE: workflow

<!--
SKILL INSTRUCTIONS
==================
This file defines the canonical structure for note_type: workflow.
A workflow documents an ordered sequence of steps to accomplish a task.
It describes a PROCESS, not a code composition. If the note is primarily
about combining functions to compute a result, use note_type: pattern.

DISTINCTION GUIDE:
  - Use note_type: pattern   → code-level composition of functions
  - Use note_type: workflow  → process-level sequence of actions
                               (may include code in individual steps,
                               but the structure is the sequence itself)

Examples of workflows:
  - Steps to connect Power Query to a REST API
  - Process for deploying a DAX model to the service
  - How to set up a Python virtual environment
  - Steps to profile and optimise a slow SQL query

When a user asks you to create a workflow note, you MUST populate every
section below. Do not skip sections. Do not rename headings.
Replace all <placeholder> tokens with real content.
Remove all HTML comments before saving the final note.
-->

---
note_type: workflow
language: <DAX | M | Python | Excel | VBA | SQL | CSS | HTML | General>
name: <Action-oriented name, e.g. "Connect Power Query to a REST API">
tags: [<tag1>, <tag2>]
complexity: <beginner | intermediate | advanced>
estimated_time: <e.g. 10 minutes | 1 hour>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Goal

<!--
State in 1-3 sentences what the reader will have achieved by the
end of this workflow. Be specific about the end state.
-->

<What the reader will have built, configured, or produced when
they complete all steps.>

## Prerequisites

<!--
List what must be in place before starting. Be specific.
Write as short plain English statements.
-->

<Prerequisite 1: software, access, data, or knowledge required.>

<Prerequisite 2: software, access, data, or knowledge required.>

## Steps

<!--
Document each step as a numbered section.
Each step must have:
  - A ### heading with the step number and a short action title
  - A plain English description of what to do and why
  - A code block IF a specific command or expression is required
  - A verification note IF there is something to check before moving on
Keep steps atomic — one action per step.
-->

### Step 1 — <Action title>

<What to do and why. Write in the imperative voice ("Open...", "Click...",
"Enter..."). Explain any decision points the user will encounter.>

```<language>
<!-- Only include this block if a specific command or code is required -->
<command or code>
```

**Verify:** <What to check to confirm this step succeeded before proceeding.>

### Step 2 — <Action title>

<What to do and why.>

```<language>
<!-- Only include this block if a specific command or code is required -->
<command or code>
```

**Verify:** <What to check to confirm this step succeeded before proceeding.>

### Step 3 — <Action title>

<What to do and why.>

**Verify:** <What to check to confirm this step succeeded before proceeding.>

<!-- Add or remove steps as needed -->

## Troubleshooting

<!--
Document 1-3 common failure points specific to this workflow.
For each: name the symptom and the fix.
-->

**<Symptom 1>:** <What to do when this happens.>

**<Symptom 2>:** <What to do when this happens.>

## Related Notes

See also: <RelatedNoteName1>, <RelatedNoteName2>
