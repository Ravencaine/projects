# SKILL_note_ingestion.md — Note Ingestion Protocol

## Section 1 — Supported Note Types

Every note has exactly one type. Pick the most specific fit.

| note_type | When to use |
|-----------|-------------|
| `author` | A person who has contributed one or more sources to the vault. Tracks their background, expertise, and all their sources in one place. |
| `source` | The complete, clean source document — all content, no noise. Archived as the authoritative record. A source note is filed in its target KB alongside its extracted notes. |
| `atomic` | A single mental model, concept, or principle. Something you understand once and apply repeatedly. |
| `function` | A single callable: a DAX function, M function, Python function, SQL query, etc. One signature, one purpose. |
| `pattern` | A named composition of two or more functions or steps. Reusable recipe, not a one-off. |
| `error` | An error message, code, or symptom paired with its cause and resolution. |
| `snippet` | A copy-paste boilerplate: import statements, config blocks, boilerplate code, boilerplate text. |
| `gotcha` | A counterintuitive behaviour or silent failure that surprises experienced users. |
| `comparison` | A vs B analysis: two approaches, tools, or concepts evaluated side by side. |
| `workflow` | A step-by-step process with ordered, conditional, or branching steps. |
| `reference` | A lookup table, cheatsheet, cheat sheet, or quick-reference card. |

---

## Section 2 — Two-Pass Protocol

### Pass 1 — Discovery & Inventory

Scan the source across ALL 9 note types BEFORE writing anything. Produce an inventory table:

```
| # | Type | Name | Location | Status |
|---|------|------|----------|--------|
| 1 | atomic | Name here | 01.Knowledge/<KB>/Wiki/ | pending |
...
```

**The inventory is a contract.** Every item must be written or extended. Do not skip items because they seem minor. Do not add items not in the source. Ask the user to confirm the inventory before starting Pass 2.

If the source is small (fewer than 5 notes), the inventory can be brief. If the source is large (chaptered article, book, video series), produce a full inventory per chapter.

### Pass 2 — Extraction

Work through the inventory systematically. For each item:
1. Run the merge/extend check (see Section 4b).
2. Write using the appropriate template.
3. Update the Status column to `done`.

---

The canonical note templates live alongside the skill in `99.System/Vault Guides/`:

| Template file | note_type |
|---------------|-----------|
| `template_author.md` | author |
| `template_source.md` | source |
| `template_atomic.md` | atomic |
| `template_comparison.md` | comparison |
| `template_error.md` | error |
| `template_function.md` | function |
| `template_gotcha.md` | gotcha |
| `template_pattern.md` | pattern |
| `template_reference.md` | reference |
| `template_snippet.md` | snippet |
| `template_workflow.md` | workflow |

---

## Section 3 — Classification Decision Tree

```
Is it a single callable with a name and a signature?
  YES → function
  NO
  Is it a named recipe combining 2+ callables?
    YES → pattern
    NO
    Is it an error message + cause + fix?
      YES → error
      NO
      Is it a counterintuitive or silent failure?
        YES → gotcha
        NO
        Is it a copy-paste boilerplate?
          YES → snippet
          NO
          Is it a lookup table or cheatsheet?
            YES → reference
            NO
            Is it a named person with sources in the vault?
              YES → author
            NO
            Is it a copy of a complete source document with all content preserved and noise stripped?
              YES → source
            NO
            Is it a vs B comparison?
              YES → comparison
              NO
              Is it an ordered, step-by-step process?
                YES → workflow
                NO
                → atomic
```

---

## Section 4 — Split Rules

Split aggressively. Every distinct concept in the source gets its own note. Common split signals:

- A new function or formula
- A new concept or principle
- A new error or edge case
- A new step in a process
- A new comparison axis

When NOT to split:
- Minor variations of the same function (one note per function, not one per overload)
- Inline examples that illustrate a single concept
- Throwaway code used once in the source

When to write an `author` note:
- The author has contributed two or more sources to the vault
- Their background or expertise is relevant to understanding their contributions
- One source is sufficient only if the author's identity is notable (e.g., a recognised expert in the field)

When to write a `source` note:
- The source is more than ~500 words of substantive content
- It has enough depth that keeping the clean, complete record is worth the file
- A source note is the authoritative verbatim record; extracted notes are the synthesised derivatives
- Strip noise (author CTAs, promotional sections, dead links, image tags) from the source note but preserve all substantive content

---

## Section 4b — Merge / Extend Protocol

Before writing, check if a similar note exists in the target KB:

1. Search the KB's Wiki folder for notes with the same name or subject.
2. If found, open the existing note and the source side by side.
3. If the source adds genuinely new information (new parameters, new edge cases, new context), extend the existing note. Append new sections; do not overwrite existing content.
4. If the source repeats the existing note verbatim or near-verbatim, skip writing — mark inventory item as `skipped (duplicate)`.
5. If the source contradicts the existing note, flag it in the report and mark the inventory item as `conflict — see report`.
6. If no similar note exists, write a new one.

---

## Section 5 — Mandatory Frontmatter

Every note requires this frontmatter block at the very top:

```yaml
---
created: YYYY-MM-DD
source: <source name or URL>
source_url: <url or empty>
note_type: <type from table above>
tags: [optional, tags, here]
---
```

The `source` field must be quoted if it contains a colon (e.g., `source: "Article Title: Subtitle"`).

The frontmatter must be valid YAML. Do not add custom fields outside this block without a documented reason.

---

## Section 5b — Unicode Filename Normalization

If the Inbox source filename contains any non-ASCII character (em-dash, curly quotes, emoji, mathematical Unicode, etc.), **normalize it to ASCII before writing it into any `source:` field or any `source` column in `_INGESTED.md`**.

Normalize the Inbox source file's name FIRST (rename it in-place before ingestion), then use that normalized name in all frontmatter and registry entries. This ensures the `source:` field and the archived filename always match exactly — enabling `find_orphans.py` to correctly link notes back to their sources.

**Normalization rules** (apply in order):

| Unicode | Replace with |
|---------|-------------|
| Em-dash `—`, en-dash `–`, hyphen-dash `‐` | `-` (hyphen) |
| Left/right double curly quotes `"` `"` | ` ` (stripped) |
| Left/right single curly quotes `'` `'` | `'` (straight apostrophe) |
| Ellipsis `…` | `...` |
| Emoji and decorative Unicode (`📊🚀💻🧙⚡🏛️🔄✨`, etc.) | stripped |
| Mathematical bold/script/italic letters (`𝐒𝐮𝐩𝐞𝐫…`) | stripped |
| Other non-ASCII | stripped via NFKD + ASCII replace |

**Procedure when ingesting a Unicode filename:**
1. Rename the file in `00.Inbox/` using the rules above — e.g. `"🧙 Power Query Trick…"` → `"Power Query Trick Add Leading Zeros Only When You Should.md"`
2. Use the renamed filename in all `source:` frontmatter fields
3. Use the renamed filename in `_INGESTED.md`
4. The archived file in `InboxArchive/YYYY-MM/` will also have the ASCII name

**Do not use the original Unicode filename anywhere** — even if the Inbox file has emoji or em-dashes in its name, the `source:` field must use the ASCII-normalized form.

---

## Section 6 — Quality Checks

Run these before delivering any note:

1. Frontmatter is present and valid YAML.
2. `note_type` matches the selected template.
3. No `created_by` field in frontmatter.
4. Body has at least one content section below the frontmatter.
5. No Lorem Ipsum or placeholder text.
6. No truncated code blocks (blocks should be complete and runnable).
7. No links to non-existent files or notes.
8. File name matches the note's subject (snake_case for the filename).
9. Tags are lowercase and hyphenated if multi-word.
10. No duplicate headings in the same note.
11. Note is filed under the correct KB.
12. Note was added to the target KB's INDEX.md under the correct section.
13. `source:` field is present in frontmatter with the exact source filename. **Normalize Unicode to ASCII** before writing it — see Section 5b (below). This field is what links notes back to their source and enables orphan detection via `find_orphans.py`. Using a normalized form ensures notes always match their archived source even if the Inbox file had Unicode in its name.

---

## Section 7 — INGESTION COMPLETE Summary Block

After all notes are written, output this block exactly:

```
INGESTION COMPLETE

Notes       : <comma-separated list of filenames>
Note types  : <comma-separated types>
Language    : <e.g., DAX, M, Python, etc.>
Tags        : [<comma-separated tags>]
KB routing  : <KB name> (<N> notes)
Extracted   : <N>
Extended    : <N>
Source note : <yes|no — write one if source is >500 words>
Author note : <yes|no — write one if author has 2+ sources or is a recognised expert>
Saturation  : <M items found | clean>
```

**After the summary block**, run `find_orphans.py` to verify no notes were left as orphans:

```
python 99.System/Scripts/find_orphans.py
```

Exit 0 = clean. Exit 1 = orphans found — fix the `source:` frontmatter on each orphan note to match the actual Inbox/Archive filename, then re-run until clean.

**The source file stays in `00.Inbox/` after the summary block.** Archive is a separate, optional step — not a completion gate. Nothing is lost if a source stays in the Inbox.

### Manual Archive (Optional)

When you want to clean up the Inbox, run `99.System/Scripts/safe_archive.py` — never use raw `mv` or shutil.move directly. The script verifies that notes exist before archiving and refuses to move the source if they don't.

Archive triggers (any of these):
- User says "archive" or "clean up inbox"
- Batch ingest is complete and the user requests cleanup
- The Inbox exceeds 50 files and you proactively offer to archive

When archiving:
1. Call `safe_archive.py` — it exits non-zero if notes are missing
2. `safe_archive.py` moves the source file and updates `_INGESTED.md` status to `archived` atomically
3. Delete any temporary extracted files (e.g., `*_extracted.txt`) from the Inbox after archiving

---

## Section 8 — Behaviours the Skill Must Never Do

1. Skip the inventory phase.
2. Write notes before the inventory is confirmed.
3. Invent `note_type` values not in Section 1.
4. Add `created_by` to frontmatter.
5. Overwrite an existing note without running the merge check first.
6. Declare ingestion done before all inventory items are resolved.
7. Create notes outside the 7 defined KBs without asking.
8. Copy-paste source content verbatim as a note.
9. Write a note longer than 800 words without splitting it.
10. Leave frontmatter blank or incomplete.
11. Use the wrong template for the selected `note_type`.
12. Move a source from the Inbox without running `safe_archive.py` first.
13. Skip the quality checks before delivering.
14. File a note in the wrong KB.
15. Leave notes without adding them to INDEX.md.
16. Ignore contradictions between new source content and existing notes.

---

## Section 9 — Trigger Phrases

This skill activates on any of:
- "ingest this"
- "add to knowledge base"
- "create a note from this"
- "document this"
- "save this as a note"
- "run ingestion on"
- "process this source"

On activation, begin Phase 1 immediately. Do not ask permission to start.
