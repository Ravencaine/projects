I reaudit-read the revised Lillith build plan. This version is **materially improved** from the previous one. Most of the earlier structural/schema issues have been fixed: `pipeline_status` is now separated from lifecycle `status`, `template_source.md` is included in the phase manifest, the wikilink convention is explicit, and `gotcha` is now represented in the template index [1].

My verdict: **this is now a strong v1 architecture, but it still needs a few corrections before implementation.**

---

## Executive verdict

**Buildability:** High  
**Architecture quality:** Strong  
**Implementation risk:** Medium  
**Main remaining issue:** The plan is still slightly inconsistent between the “universal schema,” specific templates, and Phase 1 checklist.

The plan is now suitable to start **Phase 1 foundation work**, but I would make the cleanup edits below before writing ingestion/indexing scripts.

---

# What improved since the previous audit

## 1. `status` vs ingestion state is now fixed

You now distinguish:

```yaml
status: <draft|review|published|archived>
pipeline_status: <raw|chunked|indexed|done>
```

This is the right fix. The plan also explicitly says what `status` is **not** used for, avoiding cases like `status: processed` or `status: transcript` [1].

This is a major improvement.

---

## 2. Wikilink convention is much clearer

The revised plan now says all wikilinks should use full vault paths, e.g.:

```markdown
[[20 Sources/PDFs/example-report]]
[[30 Concepts/Wiki/Hybrid-Retrieval]]
[[70 Generated Answers/Wiki/question-slug]]
```

and specifically forbids abbreviated forms like:

```markdown
[[Sources/PDF/example]]
```

That removes ambiguity for automation and link validation [1].

Good decision.

---

## 3. `template_source.md` is now included

The Phase 1 file manifest includes:

```text
template_source.md
```

This fixes one of the earlier gaps [1].

---

## 4. The architecture still has the right core

The strongest parts remain:

- local-first Obsidian vault,
- immutable source notes,
- hybrid retrieval with SQLite FTS5 + Qdrant,
- cloud LLM for synthesis/drafting,
- local Ollama for validation and maintenance,
- Git branch review workflow,
- never-delete archival model [1].

Those are all solid architectural choices.

---

# Remaining issues to fix

## 1. Phase 1 still says “Copy all 10 templates”

In Section 14, Phase 1 says:

```text
Copy all 10 templates to 30 Concepts/Templates/
```

But the plan now lists **12 templates**:

1. `template_atomic.md`
2. `template_function.md`
3. `template_pattern.md`
4. `template_comparison.md`
5. `template_error.md`
6. `template_workflow.md`
7. `template_reference.md`
8. `template_snippet.md`
9. `template_gotcha.md`
10. `template_generated_answer.md`
11. `template_transcript.md`
12. `template_source.md`

Change:

```text
Copy all 10 templates
```

to:

```text
Copy/create all 12 templates
```

or better:

```text
Copy the 9 existing canonical templates and create the 3 Lillith-specific templates:
template_generated_answer.md, template_transcript.md, template_source.md.
```

This is a small but important implementation clarity fix.

---

## 2. Universal `note_type` enum still omits `gotcha`

In Section 4, the universal schema says:

```yaml
note_type: <atomic|function|pattern|comparison|error|
            workflow|reference|snippet|generated-answer|
            transcript|source>
```

But Section 5 includes:

```text
gotcha
```

as a valid note type [1].

Add `gotcha` to the universal enum:

```yaml
note_type: <atomic|function|pattern|comparison|error|
            workflow|reference|snippet|gotcha|generated-answer|
            transcript|source>
```

This is important because your validator will likely depend on that enum.

---

## 3. `language` is listed as universal, but source notes do not include it

The universal frontmatter says all notes have:

```yaml
language: <DAX|M|Python|Excel|VBA|SQL|CSS|HTML|General>
```

But the Source Note Template does **not** include `language` [1].

You have two options.

### Option A: Make `language` truly universal

Add this to source notes:

```yaml
language: General
```

or, better:

```yaml
language: <en|fr|de|...>
```

But this creates ambiguity because your `language` field currently mixes programming languages with natural language.

### Option B: Make `language` conditional

I recommend this. Rename the field for programming/topic language:

```yaml
technical_language: <DAX|M|Python|Excel|VBA|SQL|CSS|HTML|General>
```

Then add a separate natural-language field for source/transcript notes:

```yaml
content_language: <en|fr|de|es|...>
```

For example:

```yaml
note_type: source
source_type: pdf
content_language: en
```

and:

```yaml
note_type: function
technical_language: Python
content_language: en
```

This will prevent confusion later.

---

## 4. `name`, `title`, `key_insight`, and `answers` are universal but missing from generated/source/transcript templates

The universal schema says all notes have:

```yaml
name:
title:
key_insight:
answers:
```

But the specific templates do not consistently include them.

For example, the generated answer template only includes:

```yaml
note_type:
created:
updated:
status:
confidence:
source_notes:
tags:
```

The source note template also does not include `name`, `title`, `key_insight`, or `answers` [1].

This matters because your SQLite `notes` table has:

```sql
name TEXT NOT NULL
```

So if source or generated-answer notes omit `name`, the indexing script will fail unless it derives `name` from the filename or heading.

You should decide one of two approaches.

### Recommended approach

Define a **minimal universal schema**:

```yaml
note_type:
name:
title:
status:
created:
updated:
tags:
```

Then make everything else conditional.

For source notes:

```yaml
note_type: source
name: example-report
title: Example Report
status: published
source_type: pdf
source_hash: <sha256>
vault_path: 20 Sources/PDFs/example-report
pipeline_status: done
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags:
  - source/pdf
  - note_type/source
  - status/published
```

For generated answers:

```yaml
note_type: generated-answer
name: question-slug
title: <Question as heading>
status: draft
confidence: medium
source_notes:
  - "[[20 Sources/PDFs/example-report]]"
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags:
  - note_type/generated-answer
  - generated
  - topic/<topic>
  - status/draft
```

This will make validation much easier.

---

## 5. Generated answer tags do not follow your own tag convention

The Generated Answer Template currently uses:

```yaml
tags:
  - generated-answer
  - topic/<topic>
```

But your tag convention says all notes should use:

```yaml
note_type/<type>
status/<status>
```

and generated outputs should use:

```yaml
generated
```

So change generated-answer tags to:

```yaml
tags:
  - note_type/generated-answer
  - topic/<topic>
  - status/draft
  - generated
```

This keeps tag logic consistent.

---

## 6. Source and transcript tags should include `status/published`

The source template currently has:

```yaml
tags:
  - source/pdf
  - note_type/source
```

The transcript template has:

```yaml
tags:
  - source/transcript
  - note_type/transcript
```

But your tag convention includes `status/<status>` [1].

Add:

```yaml
- status/published
```

to both.

---

## 7. `generated` tag on transcripts is debatable

The tag convention says:

```text
generated applies to all generated-answer and transcript notes
```

That is understandable because transcripts are machine-generated, but it may create confusion between:

- LLM-generated synthesis,
- machine-transcribed source material.

I recommend separating them:

```yaml
generated
```

for LLM-generated derived notes.

```yaml
machine_transcribed
```

for transcripts.

So transcript tags become:

```yaml
tags:
  - source/transcript
  - note_type/transcript
  - status/published
  - machine_transcribed
```

This will help later when filtering generated synthesis vs raw machine-generated evidence.

---

## 8. Source note template says “full text preserved” but template shows excerpts

The PDF pipeline says source notes contain:

```text
Full text of each page preserved
```

But the source template section is named:

```markdown
## Source Excerpts
```

and shows selected quote blocks [1].

You need to decide which source notes are supposed to contain.

There are three possible models:

### Option A: Full text inside Markdown source notes

Pros:
- Fully portable.
- Git-readable.
- Rebuild indexes entirely from Markdown.

Cons:
- Huge Markdown files.
- Obsidian may become slow for long PDFs.
- Git diffs become noisy.

### Option B: Excerpts only in Markdown, full text in SQLite

Pros:
- Cleaner notes.
- Better Obsidian usability.

Cons:
- Index is no longer fully rebuildable from Markdown.
- Contradicts the “rebuildable from Markdown” principle.

### Option C: Full text in source note, but structured by page with collapsible sections

Recommended if portability matters.

Example:

```markdown
## Page 1

> [!quote] Page 1 canonical text
> Full extracted text here...

## Page 2

> [!quote] Page 2 canonical text
> Full extracted text here...
```

If you only want selected excerpts, then change the ingestion pipeline wording from:

```text
Full text of each page preserved
```

to:

```text
Representative page-level excerpts preserved; full text indexed in SQLite/Qdrant.
```

But that weakens the rebuildable-from-Markdown promise.

---

## 9. File URL for video is likely not portable

Transcript template uses:

```markdown
[Open video file](file:///90 System/Attachments/Video/<filename>)
```

That probably will not resolve correctly on Windows or macOS because it is not an absolute path.

Better options:

```markdown
[Open video file](../../90%20System/Attachments/Video/<filename>)
```

or simply:

```markdown
Video file: [[90 System/Attachments/Video/<filename>]]
```

However, Obsidian does not always handle binary file wikilinks consistently depending on settings.

I recommend this:

```markdown
video_file: "90 System/Attachments/Video/<filename>"
```

and in body:

```markdown
- **Local file:** `90 System/Attachments/Video/<filename>`
```

Let scripts resolve the path instead of relying on `file:///`.

---

## 10. Git branch naming is slightly ambiguous

You write:

```text
main/
agent/
```

But Git branches are usually referred to without slashes unless they are hierarchical branch names.

If the branch is literally named `agent/`, that is unusual and may be invalid or awkward. If you mean branch prefix, say:

```text
main
agent/drafts
```

or:

```text
agent
```

I recommend:

```text
main
agent/drafts
```

Then generated work lands in:

```bash
git checkout -B agent/drafts
```

This is cleaner and supports future branches like:

```text
agent/maintenance
agent/revisions
```

---

## 11. Hermes skill naming is inconsistent

The skills inventory lists:

```text
lillith_ingest_pdf
lillith_ingest_video
lillith_ingest_web
```

But the file structure lists:

```text
SKILL_lillith_ingestion.md
```

and Phase 1 creates:

```text
SKILL_lillith_ingestion.md
SKILL_lillith_retrieve.md
SKILL_lillith_generate_note.md
...
```

This is not necessarily wrong, but you should define whether:

- `SKILL_lillith_ingestion.md` is a parent protocol containing multiple skills, or
- each skill gets its own file.

Recommended file layout:

```text
90 System/Skills/
├── SKILL_lillith_ingest_pdf.md
├── SKILL_lillith_ingest_video.md
├── SKILL_lillith_ingest_web.md
├── SKILL_lillith_retrieve.md
├── SKILL_lillith_generate_note.md
├── SKILL_lillith_validate_note.md
├── SKILL_lillith_maintenance_daily.md
├── SKILL_lillith_maintenance_weekly.md
└── SKILL_lillith_archive.md
```

Then the root aliases can point to the most common entrypoints.

---

## 12. Cloud LLM privacy policy still needs a formal section

The plan says maintenance never sends raw vault content to cloud [1]. It also says cloud LLM handles structured extraction and note drafting from evidence chunks [1].

That is acceptable, but the policy needs to be explicit.

Add a short section:

```markdown
## Cloud LLM Data Boundary

Cloud LLM may receive:
- selected retrieval chunks required for synthesis
- source excerpts explicitly selected by retrieval
- generated draft context
- metadata needed for citations and wikilinks

Cloud LLM may not receive:
- entire raw source files
- entire vault exports
- private logs
- files/chunks tagged access_level: restricted unless manually approved
- credentials, personal secrets, or unredacted private data
```

Because you already have `access_level` in chunk metadata, this should become an enforceable retrieval filter [1].

---

# Suggested corrected universal schema

I would revise the universal schema to this:

```yaml
---
note_type: <atomic|function|pattern|comparison|error|workflow|reference|snippet|gotcha|generated-answer|transcript|source>

name: <unique-kebab-or-title-safe-name>
title: <Human-readable title>

status: <draft|review|published|archived>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/<type>
  - status/<status>
---
```

Then conditional fields:

```yaml
# Code/technical notes
technical_language: <DAX|M|Python|Excel|VBA|SQL|CSS|HTML|General>
complexity: <beginner|intermediate|advanced>

# Natural language content
content_language: <en|fr|de|es|...>

# Source notes only
source_type: <pdf|transcript|web>
source_hash: <sha256>
vault_path: <vault-relative-path>
pipeline_status: <raw|chunked|indexed|done>
extraction_quality: <high|medium|low>

# Generated answers only
confidence: <low|medium|high>
source_notes:
  - "[[20 Sources/PDFs/example-report]]"

# Temporal notes
valid_from: <YYYY-MM-DD>
valid_until: <YYYY-MM-DD>

# Type-specific fields
subjects: []
components: []
syntax: ""
severity: <low|medium|high>
estimated_time: ""
key_insight: ""
answers: []
```

This will be much easier to validate.

---

# Recommended implementation order

The current phases are good, but I would slightly modify them.

## Phase 1A: Vault skeleton only

Do:

- folder structure,
- `.gitignore`,
- `CLAUDE.md`,
- `_INGESTED.md`,
- `_Index_Schema.md`,
- empty `activity.md`,
- Git init,
- branch setup.

## Phase 1B: Schema and templates

Do:

- finalize universal schema,
- create all 12 templates,
- create schema validator,
- run validator against templates.

This should happen **before** ingestion scripts.

## Phase 2A: PDF-only ingestion

Start with PDFs only:

- checksum,
- source note creation,
- chunking,
- SQLite indexing.


## Phase 2B: Qdrant embeddings

Add:

- BGE-M3 embedding,
- Qdrant collection,
- metadata payload,
- rebuild script.

## Phase 2C: Video ingestion

Add:

- FFmpeg,
- faster-whisper,
- transcript note generation,
- video storage.

## Phase 3: Retrieval-generated answer loop

Then implement:

- FTS5 + Qdrant retrieval,
- rank fusion,
- evidence section,
- generated answer note,
- validation,
- agent branch write.

## Phase 4: Maintenance

Add automation last.



## Final assessment

This is now a **credible implementation plan**. The architecture is coherent, the major lifecycle conflict has been fixed, and the system boundaries are much clearer [1].

I would rate it:

```text
Architecture:        8.5 / 10
Build readiness:     7.5 / 10
Schema consistency:  7 / 10
Operational safety:  8.5 / 10
MVP clarity:         7 / 10
```

