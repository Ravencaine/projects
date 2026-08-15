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
| `entity` | A named person, tool, or organization referenced by one or more articles in the KB but lacking a dedicated wiki note. Used by `extract-implicit-knowledge` skill. |
| `claim` | A specific assertion or thesis attributed to one or more articles in the KB. The assertion itself, not the topic — can be cited, contradicted, or built upon. Used by `extract-implicit-knowledge` skill. |
| `relationship` | A typed edge between two notes (builds_on, exemplifies, cites, contradicts) with quoted evidence. Used by `extract-implicit-knowledge` skill. |

---

## Section 2 — Two-Pass Protocol

### Pass 1 — Discovery & Inventory

**MANDATORY: Check for video sources FIRST.**

Before anything else, scan the source for embedded YouTube/video URLs:
- Does the file contain `youtube.com/watch?v=`, `youtu.be/`, or other video URLs in frontmatter or body?
- Does the source `note_type` or metadata indicate it is a video?

If **YES** — the source is a video or contains a video link:
1. Load `video-transcriber-skill` and invoke it on the URL first
2. Wait for the transcript note to be written to `00.Inbox/`
3. **Then ingest the transcript note** (not the original article link) using this same protocol
4. This ensures full transcripts — not captions — are the authoritative ingested source
5. **Wikilink the video file in the transcript source note body** — embed with `![[filename.ext]]`
   at the top of the body, and add `video_file: 99.System/Attachments/Video/<filename>` to frontmatter.
   Also add a `transcript:` frontmatter field pointing to the transcript note.

If **NO** — proceed to the inventory scan below.

---

**MANDATORY: Check for downloadable file attachments.**

After the video check, run `scan_for_downloads.py` on the source:

```bash
python 99.System/Scripts/scan_for_downloads.py --verbose <source_file>
```

Focus on high-confidence detections — `.pbix`, `.xlsx`, `.pbip`, `.pqx`, `.zip`, `.csv`,
`.py`, `.ipynb`, `.sql`, `.dax`, `.m` files — not inline images served from CDNs
(images on `lwfiles.mycourse.app`, `cdn-images-*.medium.com`, `cloudinary.com`,
`community.powerbi.com`, etc. are content, not attachments).

For any real downloadable asset found:
1. Download it to `99.System/Attachments/` (use a subfolder that matches the file type:
   `PowerBI/`, `Excel/`, `Data/`, `Code/`)
2. Add `download_file: 99.System/Attachments/<type>/<filename>` to the source note frontmatter
3. **Wikilink the file in the source note body** — add `[[99.System/Attachments/<type>/<filename>]]`
   in the **Notable Details** section and in the **Metadata table** (Attachments row). This is
   required, not optional. Files without wikilinks in the body are invisible to Obsidian's
   backlink graph and cannot be opened from the note.
4. If the asset is a `.pbix`/`.pbip` or `.xlsx`/`.xlsm`/`.xlsb` that contains reusable
   DAX/M code or techniques, ingest that file as a separate note (see Section 4 for split rules)
5. If the asset is a compressed archive, extract it and scan for nested content notes

---

**CRITICAL: Scan across ALL note types for every source — never default to source-only.**

Every source contains multiple extractable concepts. At minimum, always ask for each source:
- Is there a named **function** (DAX, M, Python)?
- Is there a named **pattern** (recipe, technique)?
- Is there a **gotcha** (counterintuitive behaviour)?
- Is there a **workflow** (step-by-step process)?
- Is there a **comparison** (A vs B)?
- Is there a distinct **atomic** (principle, mental model)?

**Default to extract, not skip.** If unsure, extract it. You can merge later; you cannot recover missed extraction after archiving.

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
| `template_entity.md` | entity |
| `template_claim.md` | claim |
| `template_relationship.md` | relationship |

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

### Implicit-Knowledge Extension Rules (extract-implicit-knowledge skill)

These rules apply only to notes created by the `extract-implicit-knowledge` skill:

- **Entity notes**: if the skill proposes an entity whose slug already exists in the KB's `Wiki/Implicit/` folder or in `merge-state.json`, extend the existing note's `## Sources in the Vault` list with the new article citation rather than creating a duplicate.
- **Claim notes**: if the skill proposes a claim whose slug already exists, add the new `## Evidence` bullet (with the new article citation) rather than creating a duplicate. Do not overwrite the existing claim body.
- **Relationship notes**: if the skill proposes a relationship whose slug already exists, skip it silently — the existing note is preserved.

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

## Section 5b — Tags Format (Obsidian-Required)

Every `tags:` field in frontmatter must use Obsidian's native format — **unquoted lowercase hyphenated tags inside a bare YAML list**:

```yaml
tags: [power-bi, data-modeling, dax]
```

**Never use YAML-quoted strings inside tags:**

```yaml
# WRONG — Obsidian will not render these as tags
tags: ["power-bi", "data-modeling"]
tags: ['power-bi', 'data-modeling']
tags: ["power-bi", 'data-modeling']
```

**Why it matters:** YAML parses `["foo"]` as a list containing a single quoted string — Obsidian's tag parser expects raw unquoted identifiers. Quoted tags render as plain text, not clickable tags.

**Rule:** `replace_all: true` for the entire `tags:` field in every template and skill file so newly written notes always use the correct format.

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
9. Tags are lowercase and hyphenated if multi-word, and **unquoted** (no `"..."` or `'...'` inside the brackets).
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

After all notes are written, run the post-ingest audit:

```bash
python 99.System/Scripts/find_orphans.py
```

- **Exit 0 (clean):** Archive the source immediately. No exceptions — clean means ready.
- **Exit 1 (orphans found):** Fix the `source:` frontmatter on each orphan note, re-run until clean, then archive.

**Archive order is fixed — do not deviate.** The correct sequence is:

1. Write all notes.
2. Update each note's KB `INDEX.md`.
3. Run `find_orphans.py` until exit 0.
4. **If the registry row in `00.Inbox/_INGESTED.md` does not yet exist for this source**, add it now with `status: pending` (the script reads the row but does not require it pre-exist).
5. **If the registry row already exists with `status: archived`, change it back to `pending` before running `safe_archive.py`.** The script short-circuits on `status: archived` and skips the file move.
6. Run `safe_archive.py` with just the filename (no path):
   ```bash
   python 99.System/Scripts/safe_archive.py "<filename.md>"
   ```
   The script's final step is what writes `status: archived` to the registry and moves the file into `99.System/InboxArchive/YYYY-MM/`.
7. **Verify the file actually moved.** Confirm `00.Inbox/<filename>.md` no longer exists and `99.System/InboxArchive/YYYY-MM/<filename>.md` exists. A success message from `safe_archive.py` is necessary but not sufficient — the script can print success on a `status: archived` short-circuit without ever touching the file.
8. **Verify the registry row** now reads `status: archived` (script writes this as step 5 of its own run).

**Failure-mode table:**

| Symptom | Cause | Fix |
|---------|-------|-----|
| `safe_archive.py` prints "INFO: Source already marked 'archived' in registry" and the file stays in Inbox | Registry row was set to `archived` before the script ran | Edit `_INGESTED.md` row back to `pending`, re-run `safe_archive.py` |
| `safe_archive.py` prints "BLOCKED: No notes found" | No note's `source:` frontmatter matches the filename exactly (including Unicode normalisation — see Section 5b) | If the source was rejected: archive manually (see below). If genuinely no notes: add `source:` to at least one note's frontmatter, re-run |
| `safe_archive.py` errors with `Source not found in Inbox` | Passed a path (`00.Inbox/foo.md`) instead of just the filename | Pass `foo.md` only |

**Rejected sources (no notes to reference):** `safe_archive.py` blocks because it requires at least one note's `source:` field to match. Archive manually:

```bash
PYTHONIOENCODING=utf-8 py -3 -c "
import shutil, pathlib
src = pathlib.Path('00.Inbox/<filename.md>')
dest = pathlib.Path('99.System/InboxArchive/YYYY-MM/<filename.md>')
shutil.move(str(src), str(dest))
print('Moved to', dest)
"
```

After archiving, verify the file is gone from Inbox and exists in the archive folder.
| `safe_archive.py` errors with `Source not found in Inbox` | Passed a path (`00.Inbox/foo.md`) instead of just the filename | Pass `foo.md` only |
| File moved but registry row still says `pending` | Race / partial failure | Re-run `safe_archive.py`; it will move nothing (file gone) but will still update the registry row |
| `status: archived` row exists but archive folder is empty | The pre-fix bug above — short-circuit on already-archived row | Reset row to `pending`, re-run |

After archiving, delete any temporary extracted files (e.g., `*_extracted.txt`) from the Inbox.

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
17. Ingest a video source (YouTube, local video) without running `video-transcriber-skill` first — always transcribe, never ingest captions as the authoritative source.
18. Skip the downloadable-attachments check — always run `scan_for_downloads.py --verbose` on every source before starting the inventory scan.
19. Leave downloaded files unwikilinked in the source note body — every downloaded file must appear as `[[path]]` in both the Notable Details section and the Metadata table.
20. Pre-mark the `_INGESTED.md` row for the source as `status: archived` before running `safe_archive.py` — the script short-circuits on that status and skips the file move. Set `pending` first; let the script set `archived`.
21. Trust `safe_archive.py`'s success message without verifying the file actually left Inbox — the script can print success on a `status: archived` short-circuit without ever moving the file. Verify `00.Inbox/<filename>.md` is gone and `99.System/InboxArchive/YYYY-MM/<filename>.md` exists.
22. Run `safe_archive.py` with a path (`00.Inbox/foo.md`) — pass the filename only (`foo.md`).
23. Skip the post-archive verification step — always check Inbox → Archive movement AND registry status, in that order.

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
