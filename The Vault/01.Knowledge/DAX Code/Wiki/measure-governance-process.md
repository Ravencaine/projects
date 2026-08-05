---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: workflow
tags: [dax, measure-library, governance, process, review, library-champion, sustainability]
---

# Measure Governance Process

The recurring operational cadence that keeps a DAX measure library organized after the initial reorganization. Three time-scales: weekly review, monthly audit, quarterly cleanup.

## Purpose

Folder structures and naming conventions decay without a process to maintain them. New analysts who don't know the conventions, deadline pressure, and accumulated technical debt will restore chaos within 3 months without governance.

## The 3-Step Addition Process

Every new measure follows this before entering the library:

### Step 1: Measure Proposal

Before building, the analyst answers:
- What business question does this answer?
- Does a similar measure already exist? (search first)
- Where will it fit in the folder structure?
- What should it be named? (naming convention test)

### Step 2: Peer Review

Another analyst reviews:
- Is the logic correct?
- Does it follow naming conventions?
- Is it properly documented?
- Is it in the right folder?

### Step 3: Library Addition

Only after peer review, the measure enters the shared library with its documentation.

## Exploration Exception

For deadlines, analysts can work in `📁 _Exploration` with a `#` prefix:
- `#` prefix = temporary measure
- Personal folder = won't affect shared library yet
- When proven: clean up, move to proper folder, remove `#` prefix, add documentation

This allows fast iteration without breaking the library.

## Cadence

### Weekly Measure Review (15 minutes, Friday 4 PM)

- Quick scan of new measures added that week
- Check for naming convention violations
- Flag `#` prefixed measures older than 2 weeks
- Celebrate good examples

### Monthly Library Audit (30 minutes, first Monday)

- Search for `#` prefixed measures (orphaned exploration)
- Review Utilities folder for measures that should move
- Check for duplicate measures
- Update documentation for modified measures

### Quarterly Cleanup Sprint (2 hours, quarterly)

- Delete deprecated measures (confirm no visuals reference them)
- Consolidate similar measures
- Update folder structure if business needs changed
- Train new team members on conventions

## Library Champion Role

Rotates monthly. Responsibilities:
- Lead the weekly review
- Answer questions about conventions
- Update the style guide when patterns emerge
- Advocate for good practices

**Not a policeman — a coach.** The goal is enablement, not enforcement.

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Governance without flexibility | People work around rigid processes | Allow exploration + require cleanup before sharing |
| Inconsistent enforcement | One person breaking conventions → chaos in 3 months | Make it part of code review. No exceptions. |
| Building architecture, then abandoning | Weekly review is optional → measures drift | Schedule it. Treat it as real work. |
| Over-organizing too early | 50 folders for 20 measures → complexity without value | Start with 3–5 folders. Add when category hits 10+. |

## Rule for Deprecated Measures

When someone finds `[DO_NOT_USE_OLD]`, what's the process?
- Delete? Deprecate? Document why it's still there?
- Agree on this before it happens.

## Related

- [[implement-dax-measure-library-architecture]] — full implementation plan
- [[dax-measure-naming-convention-framework]] — naming conventions
- [[dax-measure-documentation-template]] — documentation template
