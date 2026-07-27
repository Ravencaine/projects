Yes — I checked the v1.1 plan. This is **significantly stronger** than the earlier versions. It has moved from “good architecture document” to a mostly **executable blueprint**: it now includes schema versioning, stable note IDs, chunk IDs, access-level policy, idempotency, failure handling, test requirements, CLI commands, ADRs, observability, conflict rules, and a definition of done [1].

My overall verdict:

```text
Architecture:        9 / 10
Build readiness:     8.5 / 10
Schema consistency:  8 / 10
Operational safety:  9 / 10
MVP clarity:         8 / 10
```

It is now close to buildable, but there are still several inconsistencies that should be fixed before implementation.

---

# Executive verdict

The plan is now **very strong**, but not quite 10/10 yet.

The main remaining issues are:

1. **Schema examples still conflict with the universal schema.**
2. **`id` is accidentally defined twice in the universal schema.**
3. **Some templates omit required universal fields.**
4. **Tag conventions conflict between earlier and later sections.**
5. **Access-level rules are inconsistent.**
6. **The implementation phases are still too compressed.**
7. **SQLite/Qdrant schema does not fully match the frontmatter and chunk metadata model.**
8. **Some folder/file manifests are inconsistent with the newer skill naming scheme.**

These are fixable. The core architecture is sound.

---

# What is excellent now

## 1. The plan now has a real executable structure

The document now includes:

- definition of done,
- test requirements,
- schema migration policy,
- CLI command reference,
- ADRs,
- observability reports,
- conflict behaviour,
- prompt templates,
- cloud LLM data boundary,
- idempotency rules,
- failure handling [1].

That is a major improvement. This is no longer just conceptual architecture.

## 2. Stable note IDs and chunk IDs are a big improvement

The plan now defines stable note IDs:

```yaml
id: note_<ulid>
```

and deterministic chunk IDs:

```text
note_<ulid>#chunk-0007
```

This is exactly the right direction. It makes retrieval, citation, indexing, and future migrations much safer [1].

## 3. The Cloud LLM Data Boundary is strong

The plan now clearly states that cloud LLMs may receive selected retrieval chunks, source excerpts, draft context, citation metadata, and tag/link proposals, but may not receive full raw files, full vault exports, private logs, restricted chunks, credentials, or maintenance output [1].

That is a very good operational safety boundary.

## 4. The no-silent-mutation rule is excellent

The plan now explicitly says automation may create drafts, reports, logs, and proposal blocks, but may not silently modify published note bodies, delete notes, merge duplicates, rewrite source text, or remove evidence blocks without approval [1].

That is exactly the kind of invariant this system needs.

## 5. The rebuildability goal is now explicit

The definition of done requires that the full retrieval index can be rebuilt from the Markdown vault and `requirements.txt` [1]. This supports the local-first design.

---

# Remaining problems to fix

## 1. Universal schema has two conflicting `id` definitions

In Section 4, the universal schema first says:

```yaml
id: note_<ulid>
```

Then later, under atomic-note compatibility, it says:

```yaml
id: <technical_language>-<kebab-case-id>
```

This is a serious schema conflict.

You should not overload `id`.

Recommended fix:

```yaml
id: note_<ulid>
legacy_id: <technical_language>-<kebab-case-id>
```

Use:

```yaml
id
```

for the universal stable identifier.

Use:

```yaml
legacy_id
```

only when importing older atomic notes.

Update the validation rules accordingly:

```text
id: required, format note_<ulid>
legacy_id: optional, string
```

---

## 2. Generated answer template is missing required universal fields

The universal schema requires:

```yaml
schema_version
id
name
title
status
created
updated
tags
```

But the Generated Answer Template currently lacks:

```yaml
schema_version
id
retrieval_run_id
generation_model
generated_by
```

The plan later says generated-answer notes should include `retrieval_run_id`, `generation_model`, and `generated_by`, but the actual template does not include them [1].

Recommended generated-answer template:

```yaml
---
schema_version: 1
id: note_<ulid>
note_type: generated-answer
name: <question-as-slug>
title: <Question as heading>
status: draft
confidence: <low|medium|high>

retrieval_run_id: <run_id>
generation_model: <model-name>
generated_by: Hermes

source_notes:
  - "[[20 Sources/PDFs/example-report]]"

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/generated-answer
  - status/draft
  - generated
  - topic/<topic>
---
```

This would align the template with the schema.

---

## 3. Source note template is missing `schema_version` and `id`

The Source Note Template also omits required universal fields:

```yaml
schema_version
id
```

Add them:

```yaml
---
schema_version: 1
id: note_<ulid>
note_type: source
name: <source-slug>
title: <Document title>
...
---
```

Also consider adding:

```yaml
access_level: <public|internal|private|restricted>
```

at the note level, even if chunk-level access is the enforcement layer. This gives the ingestion pipeline a default access level for all chunks created from that note.

---

## 4. Transcript template is missing `schema_version`, `id`, `source_hash`, and `transcription_model`

The universal/type-specific schema says transcript notes should include:

```yaml
id
source_hash
transcription_model
```

But the Transcript Note Template lacks these fields [1].

Recommended transcript frontmatter:

```yaml
---
schema_version: 1
id: note_<ulid>
note_type: transcript
name: <transcript-slug>
title: "Transcript: <Title>"

source_type: <video|audio>
source_hash: <sha256>
content_language: <en|fr|de|es|unknown>
duration: "<HH:MM:SS>"
transcription_model: <faster-whisper-model>

pipeline_status: done
status: published

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

video_file: "90 System/Attachments/Video/<filename>"

tags:
  - note_type/transcript
  - source/transcript
  - status/published
  - machine_transcribed
---
```

Also, prefer forward slashes in stored vault paths:

```yaml
video_file: "90 System/Attachments/Video/<filename>"
```

rather than:

```yaml
video_file: "90 System\\Attachments\\Video\\<filename>"
```

Even on Windows, Python can usually resolve forward-slash paths, and Obsidian-style vault paths are more portable with `/`.

---

## 5. `generated` appears as a bare field in the universal schema

In Section 4, generated answers include:

```yaml
generated
```

under the generated-answer conditional fields.

That is invalid YAML as a key/value field unless written as:

```yaml
generated: true
```

But the plan treats `generated` as a tag, not a field.

Fix by removing this from the frontmatter fields and keeping it only under tags:

```yaml
tags:
  - generated
```

---

## 6. Tag conventions conflict at the end of the document

Earlier, the plan says:

- `generated` is for LLM-synthesised derived notes,
- `machine_transcribed` is for transcript notes,
- they are mutually exclusive [1].

That is good.

But in Section 24, “Tag Conventions Applied to Templates,” it says:

```text
generated | All generated-answer and transcript notes
```

That contradicts the earlier rule.

Fix this row to:

```text
generated | Generated-answer and LLM-drafted derived notes only
machine_transcribed | Transcript notes only
```

Also, Section 24 uses:

```text
language/<lang>
```

but earlier the plan replaced this with:

```text
technical_language/<lang>
```

Fix that row too.

Recommended corrected table rows:

```text
technical_language/<lang> | Code/technical notes only
generated | LLM-synthesised notes only
machine_transcribed | Transcript notes only
```

---

## 7. Access-level policy is inconsistent

The Cloud LLM Data Boundary says:

```json
"access_level": "private"   // default — eligible for retrieval
"access_level": "restricted" // excluded from all cloud-bound retrieval queries
```

But earlier the access-level policy says:

```text
private — cloud LLM only with per-run manual approval
restricted — never sent to cloud LLM
```

These conflict.

If `private` requires manual approval, it should not be the default eligible-for-cloud setting.

Recommended policy:

```text
public:
  May be sent to cloud.

internal:
  May be sent to cloud if cloud synthesis is enabled.

private:
  Must be excluded from cloud evidence unless per-run approval is given.

restricted:
  Must never be sent to cloud.
```

Recommended default:

```yaml
access_level: internal
```

or safer:

```yaml
access_level: private
```

But if default is private, retrieval must exclude private from cloud-bound evidence unless manually approved.

So the enforcement section should say:

```json
"access_level": "internal"   // default — eligible if cloud synthesis enabled
"access_level": "private"    // requires per-run approval
"access_level": "restricted" // never cloud-bound
```

---

## 8. Retrieval access filter currently allows private by default

The retrieval output example shows:

```json
"access_level": ["public", "internal", "private"]
```

That conflicts with the stricter policy where private requires manual approval [1].

Change default cloud-bound retrieval filters to:

```json
"access_level": ["public", "internal"]
```

Then allow private only with an explicit flag:

```bash
lillith retrieve "query" --allow-private
```

or:

```bash
lillith generate-answer "query" --approve-private
```

Restricted should never be allowed.

---

## 9. Qdrant access-level enum omits `internal`

The Qdrant payload schema says:

```text
access_level: keyword (private | restricted | public)
```

But the rest of the document uses:

```text
public | internal | private | restricted
```

Add `internal` to Qdrant payload schema:

```text
access_level: keyword (public | internal | private | restricted)
```

---

## 10. SQLite schema does not include `note_id`

The plan’s chunk metadata uses:

```json
"note_id": "note_..."
```

and the chunk ID depends on it [1].

But the SQLite `chunks` table has:

```sql
chunk_id
source_id
note_name
vault_path
...
```

It does not include:

```sql
note_id
```

Add it:

```sql
note_id TEXT NOT NULL
```

Also add `note_id` to the `notes` table:

```sql
note_id TEXT NOT NULL UNIQUE
```

Recommended `notes` table:

```sql
CREATE TABLE notes (
  note_id      TEXT NOT NULL UNIQUE,
  note_path    TEXT PRIMARY KEY,
  note_type    TEXT NOT NULL,
  name         TEXT NOT NULL UNIQUE,
  title        TEXT NOT NULL,
  status       TEXT NOT NULL,
  confidence   TEXT,
  created_at   TEXT NOT NULL,
  updated_at   TEXT NOT NULL,
  valid_from   TEXT,
  valid_until  TEXT
);
```

---

## 11. SQLite `pipeline_status` enum omits `failed`

The frontmatter schema allows:

```yaml
pipeline_status: <raw|chunked|indexed|done|failed>
```

But the SQLite schema comment says:

```sql
pipeline_status TEXT DEFAULT 'raw',  -- raw | chunked | indexed | done
```

Add `failed`.

```sql
pipeline_status TEXT DEFAULT 'raw',  -- raw | chunked | indexed | done | failed
```

---

## 12. SQLite `chunks` table uses `language`, but schema uses `content_language` / `technical_language`

The SQLite chunk table currently has:

```sql
language TEXT DEFAULT 'en'
```

But the plan now distinguishes:

```yaml
content_language
technical_language
```

Recommended fields:

```sql
content_language TEXT DEFAULT 'unknown',
technical_language TEXT DEFAULT 'General'
```

Or for chunks, use only:

```sql
content_language TEXT DEFAULT 'unknown'
```

and keep `technical_language` on notes only.

---

## 13. Qdrant payload uses `language`, but schema uses `content_language`

Same issue in Qdrant:

```text
language: keyword
```

Change to:

```text
content_language: keyword
technical_language: keyword
```

or at least:

```text
content_language: keyword
```

---

## 14. Skill file names are inconsistent across sections

Section 3 lists:

```text
SKILL_lillith_ingestion.md
SKILL_lillith_retrieve.md
...
```

Section 13 lists skills like:

```text
lillith_ingest_pdf
lillith_ingest_video
lillith_ingest_web
```

Phase 1C says the actual files should be:

```text
SKILL_lillith_ingest_pdf.md
SKILL_lillith_ingest_video.md
SKILL_lillith_ingest_web.md
...
```

Appendix D still lists:

```text
SKILL_lillith_ingestion.md
```

inside `90 System/Skills/`.

Pick one convention.

I recommend this as the canonical skill folder:

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

Then at project root:

```text
SKILL_lillith_ingestion.md
SKILL_lillith_maintenance.md
```

as aliases or overview files.

Update Section 3 and Appendix D accordingly.

---

## 15. `90 System/Decisions/` conflicts with `60 Decisions/`

The main folder structure defines:

```text
60 Decisions/
```

for decision notes.

But ADRs are placed in:

```text
90 System/Decisions/
```

This is okay if you intentionally separate system ADRs from knowledge decisions, but it should be explicit.

Recommended structure:

```text
60 Decisions/Wiki/        # user/domain decisions
90 System/ADRs/           # architecture decision records
```

I would rename:

```text
90 System/Decisions/
```

to:

```text
90 System/ADRs/
```

to avoid confusion.

---

## 16. The source note `vault_path` omits `.md`, while chunk metadata includes `.md`

Source template:

```yaml
vault_path: 20 Sources/<Type>/<slug>
```

Chunk metadata:

```json
"vault_path": "20 Sources/PDFs/example-report.md"
```

Wikilinks omit `.md`, but filesystem paths usually include `.md`.

You need two separate concepts:

```yaml
vault_path: "20 Sources/PDFs/example-report.md"
wikilink: "[[20 Sources/PDFs/example-report]]"
```

Or define that `vault_path` always excludes `.md`. But for scripts and SQLite, including `.md` is usually clearer.

Recommended:

```yaml
vault_path: "20 Sources/PDFs/example-report.md"
```

Wikilinks remain:

```markdown
[[20 Sources/PDFs/example-report]]
```

---

## 17. Chunk size is inconsistent

Section 2 says:

```text
350–700 tokens
```

Section 7.3 says:

```text
Default chunk size: 800 tokens
Overlap: 120 tokens
```

Appendix C says:

```text
Chunk size: 350–700 tokens
```

Pick one.

Recommended:

```text
Target chunk size: 700 tokens
Allowed range: 350–850 tokens
Overlap: 120 tokens
```

Then explain:

- chunks should aim for 700,
- they may be smaller/larger to preserve headings/pages/quotes,
- hard max maybe 900 or 1,000 tokens.

---

## 18. Phase 2 is too large

Phase 2 currently includes PDFs, videos, chunking, embeddings, SQLite, Qdrant, and end-to-end testing in 2–3 days [1].

That is ambitious and risky.

I strongly recommend splitting Phase 2:

```text
Phase 2A: PDF ingestion + source note creation
Phase 2B: SQLite FTS5 indexing
Phase 2C: Qdrant embeddings
Phase 2D: Video/audio transcription
```

Suggested order:

1. PDF ingestion to Markdown.
2. Chunking.
3. SQLite FTS5.
4. Rebuild command.
5. Qdrant.
6. Hybrid retrieval.
7. Generated answers.
8. Video/audio.

This would improve MVP clarity and reduce integration risk.

---

## 19. Phase 5 should happen earlier

Local Ollama validation is currently Phase 5, after generation and maintenance [1].

But Phase 3 depends on:

```text
lillith_validate_note: Ollama validation before write
```

So Ollama cannot wait until Phase 5 if validation is required in Phase 3.

Move basic Ollama setup earlier:

```text
Phase 1E: Local LLM endpoint setup
```

or make Phase 3 validation initially script-only, with Ollama optional.

Recommended:

```text
Phase 1E: Configure local validation backend
Phase 3: Generated-answer validation uses script validator first, Ollama second
```

Do not make Phase 3 depend on a Phase 5 component.

---

## 20. “Source notes do not require human review” may be too strong

The plan says source notes are auto-generated and do not require human review because the pipeline itself is the review [1].

That is acceptable for text extraction, but OCR and transcripts can be wrong. I would soften this:

```text
Source notes are published automatically as machine-generated records,
but extraction_quality/transcription_quality indicates confidence.
Low-quality extraction creates status: review or pipeline_status: done_with_warnings.
```

Recommended:

```yaml
pipeline_status: done
status: published
extraction_quality: low
review_required: true
```

or:

```yaml
status: review
pipeline_status: done
```

for low-quality OCR/transcripts.

This gives you a safer evidence layer.

---

# Highest-priority fixes

If you want to make this plan implementation-ready, fix these first:

1. Replace the second `id` field with `legacy_id`.
2. Add `schema_version` and `id` to all templates.
3. Add `source_hash` and `transcription_model` to transcript template.
4. Remove bare `generated` from frontmatter fields; keep it as a tag only.
5. Fix tag convention conflicts: transcripts use `machine_transcribed`, not `generated`.
6. Make access-level behavior consistent, especially `private`.
7. Add `internal` to Qdrant access-level enum.
8. Add `note_id` to SQLite `notes` and `chunks` tables.
9. Fix `pipeline_status` enum in SQLite to include `failed`.
10. Standardize `vault_path` with or without `.md`.
11. Standardize chunk size policy.
12. Split Phase 2 into smaller phases.
13. Move Ollama/basic validation earlier or make validation script-only at first.

---

# Suggested corrected mini-schema

Here is the core schema I would lock before coding:

```yaml
---
schema_version: 1
id: note_<ulid>

note_type: <atomic|function|pattern|comparison|error|workflow|reference|snippet|gotcha|generated-answer|transcript|source>

name: <kebab-case-unique-name>
title: <Human-readable title>

status: <draft|review|published|archived>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/<note_type>
  - status/<status>
---
```

Then optional compatibility field:

```yaml
legacy_id: <old-template-id>
```

Source note:

```yaml
source_type: <pdf|web>
source_hash: <sha256>
vault_path: "20 Sources/PDFs/<name>.md"
content_language: <en|fr|de|es|unknown>
page_count: <N>
extraction_quality: <high|medium|low>
access_level: <public|internal|private|restricted>
pipeline_status: <raw|chunked|indexed|done|failed>
```

Transcript:

```yaml
source_type: <video|audio>
source_hash: <sha256>
vault_path: "20 Sources/Transcripts/<name>.md"
content_language: <en|fr|de|es|unknown>
duration: "<HH:MM:SS>"
transcription_model: <faster-whisper-model>
transcription_quality: <high|medium|low>
access_level: <public|internal|private|restricted>
pipeline_status: <raw|chunked|indexed|done|failed>
video_file: "90 System/Attachments/Video/<filename>"
```

Generated answer:

```yaml
confidence: <low|medium|high>
retrieval_run_id: <run_id>
generation_model: <model-name>
generated_by: Hermes
source_notes:
  - "[[20 Sources/PDFs/example-report]]"
```

---

# Final assessment

This is now a **very good plan**. The architecture is mature, and the additions around safety, testing, rebuildability, observability, cloud boundaries, and CLI commands are exactly what was needed [1].

The remaining work is mostly **consistency cleanup**, not fundamental redesign.

Once you fix the schema/template mismatches, access-level contradictions, SQLite/Qdrant schema drift, and phase sequencing, I would rate it close to:

```text
Architecture:        9.5 / 10
Build readiness:     9 / 10
Schema consistency:  9.5 / 10
Operational safety:  9.5 / 10
MVP clarity:         9 / 10
```

In short: **yes, this plan is now strong enough to proceed to Phase 1A and Phase 1B**, but I would not start scripting ingestion until the schema and template inconsistencies above are corrected.