To make the Lillith plan closer to **10/10 across architecture, build readiness, schema consistency, operational safety, and MVP clarity**, I would improve it in five major ways:

1. **Separate the architecture spec from the build spec**
2. **Finalize a strict schema contract**
3. **Define hard operational boundaries**
4. **Make retrieval/indexing fully reproducible**
5. **Add test criteria for every phase**

Right now, the plan is very good, but it still reads partly like a vision document and partly like an implementation document. A 10/10 plan should be executable by you, Hermes, Claude, or another agent with minimal interpretation.

Below is how I would improve it.

---

# 1. Split the document into four documents

The current plan tries to be everything at once:

- architecture overview,
- folder manifest,
- schema reference,
- pipeline spec,
- implementation plan,
- operations guide,
- safety policy.

That makes it harder to build from.

I would split it into:

```text
Lillith/
├── ARCHITECTURE.md
├── BUILD_PLAN.md
├── SCHEMA.md
├── OPERATIONS.md
└── SECURITY_AND_PRIVACY.md
```

## `ARCHITECTURE.md`

Purpose: explain the system.

Contains:

- what Lillith is,
- local-first philosophy,
- memory layers,
- system overview,
- high-level pipeline,
- technology choices,
- major design decisions.

## `BUILD_PLAN.md`

Purpose: tell an implementer exactly what to build.

Contains:

- phases,
- tasks,
- acceptance criteria,
- dependencies,
- implementation order,
- what is explicitly out of scope.

## `SCHEMA.md`

Purpose: define the contract all scripts must obey.

Contains:

- universal frontmatter fields,
- per-note-type schemas,
- allowed enums,
- tag rules,
- filename rules,
- wikilink rules,
- SQLite schema,
- Qdrant payload schema,
- validation rules.

## `OPERATIONS.md`

Purpose: explain recurring behavior.

Contains:

- ingestion workflow,
- retrieval workflow,
- generated answer workflow,
- maintenance schedule,
- Git workflow,
- backup/rebuild procedure,
- archive procedure.

## `SECURITY_AND_PRIVACY.md`

Purpose: define hard boundaries.

Contains:

- cloud LLM data boundary,
- local-only data classes,
- allowed/forbidden payloads,
- `access_level` enforcement,
- redaction policy,
- credential handling,
- audit logging.

This would immediately raise the plan’s build readiness.

---

# 2. Define a strict universal schema

The biggest remaining issue is schema ambiguity. A 10/10 build plan needs a schema that is not just descriptive, but enforceable.

I would define a minimal universal schema that every note must have.

## Recommended universal frontmatter

```yaml
---
schema_version: 1

note_type: <atomic|function|pattern|comparison|error|workflow|reference|snippet|gotcha|generated-answer|transcript|source>

name: <unique-kebab-case-name>
title: <Human-readable title>

status: <draft|review|published|archived>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/<note_type>
  - status/<status>
---
```

That is the true universal contract.

Everything else should be type-specific.

---

# 3. Add `schema_version`

Add this to every note:

```yaml
schema_version: 1
```

This is extremely important.

Eventually you will change the schema. If you do not version notes, migration becomes painful. With versioning, you can later write:

```bash
lillith migrate-schema --from 1 --to 2
```

This is a simple field, but it makes the system much more future-proof.

---

# 4. Separate `technical_language` from `content_language`

The current `language` field is ambiguous because it can mean either:

- programming/query language: Python, DAX, SQL, M, VBA,
- natural language: English, French, German.

Use two fields instead:

```yaml
technical_language: <Python|DAX|M|Excel|VBA|SQL|CSS|HTML|General>
content_language: <en|fr|de|es|unknown>
```

For source notes:

```yaml
technical_language: General
content_language: en
```

For Python notes:

```yaml
technical_language: Python
content_language: en
```

For a transcript in French:

```yaml
technical_language: General
content_language: fr
```

This prevents confusion during filtering, retrieval, and generation.

---

# 5. Create per-type schemas

Do not rely only on prose descriptions. Define each note type clearly.

Example:

## Source note schema

```yaml
---
schema_version: 1
note_type: source

name: <unique-source-slug>
title: <Human-readable source title>

status: published
source_type: <pdf|web|audio|video|manual>
pipeline_status: <raw|extracted|chunked|indexed|done|failed>

source_hash: <sha256>
source_uri: <original-path-or-url>
vault_path: <vault-relative-path>

content_language: <en|fr|de|es|unknown>
extraction_quality: <high|medium|low>
access_level: <public|internal|private|restricted>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/source
  - source/<source_type>
  - status/published
---
```

## Transcript note schema

```yaml
---
schema_version: 1
note_type: transcript

name: <unique-transcript-slug>
title: <Human-readable transcript title>

status: published
source_type: video
pipeline_status: done

source_hash: <sha256>
source_uri: <local-video-path>
vault_path: <vault-relative-path>

transcription_model: <faster-whisper-model>
transcription_quality: <high|medium|low>
content_language: <en|fr|de|es|unknown>
access_level: <public|internal|private|restricted>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

tags:
  - note_type/transcript
  - source/transcript
  - status/published
  - machine_transcribed
---
```

## Generated answer schema

```yaml
---
schema_version: 1
note_type: generated-answer

name: <question-slug>
title: <Question or answer title>

status: draft
confidence: <low|medium|high>

created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>

source_notes:
  - "[[20 Sources/PDFs/example-source]]"

retrieval_run_id: <uuid>
generation_model: <model-name>
generated_by: Hermes

tags:
  - note_type/generated-answer
  - status/draft
  - generated
  - topic/<topic>
---
```

This makes it very clear what each note requires.

---

# 6. Add field-level validation rules

A 10/10 plan should define what counts as valid.

Example:

```text
name:
  - required
  - unique across vault
  - lowercase kebab-case
  - no spaces
  - no slashes
  - max 80 characters

title:
  - required
  - human-readable
  - may contain spaces
  - max 150 characters

status:
  - required
  - enum: draft, review, published, archived

note_type:
  - required
  - enum: atomic, function, pattern, comparison, error, workflow, reference, snippet, gotcha, generated-answer, transcript, source

source_hash:
  - required for source/transcript notes
  - sha256 hex string
  - 64 characters

created/updated:
  - required
  - ISO date: YYYY-MM-DD

tags:
  - must include note_type/<note_type>
  - must include status/<status>
```

This lets you build a validator with no guesswork.

---

# 7. Define filename and path rules

The plan should explicitly say how filenames are generated.

Example:

```text
Filename rule:
  <name>.md

Name normalization:
  - lowercase
  - trim whitespace
  - replace spaces with hyphens
  - remove punctuation except hyphen
  - collapse repeated hyphens
  - if duplicate, append short hash

Examples:
  "Hybrid Retrieval" → hybrid-retrieval.md
  "Power BI: CALCULATE Gotcha" → power-bi-calculate-gotcha.md
  "Q2 Report.pdf" → q2-report-a1b2c3.md
```

And path rules:

```text
Source notes:
  20 Sources/PDFs/<name>.md
  20 Sources/Web/<name>.md
  20 Sources/Transcripts/<name>.md

Concept notes:
  30 Concepts/Wiki/<name>.md

Generated answers:
  70 Generated Answers/Wiki/<name>.md
```

This prevents link and indexing bugs.

---

# 8. Make wikilink rules fully deterministic

The plan already improved this, but for 10/10 clarity I would add exact rules.

```text
All wikilinks must use full vault-relative paths without file extension.

Correct:
  [[30 Concepts/Wiki/hybrid-retrieval]]
  [[20 Sources/PDFs/example-report]]

Incorrect:
  [[Hybrid Retrieval]]
  [[Sources/PDF/example-report]]
  [[20 Sources/PDFs/example-report.md]]
```

Then define aliases:

```markdown
[[30 Concepts/Wiki/hybrid-retrieval|Hybrid Retrieval]]
```

This gives humans readable links while preserving scriptability.

---

# 9. Decide full-text vs excerpt source notes

This is one of the most important architectural decisions.

If Lillith is truly local-first and Markdown-backed, I recommend:

## Store full extracted text in Markdown source notes

For PDFs:

```markdown
# Example Report

## Source Metadata

- Source type: PDF
- SHA256: ...
- Extraction quality: high

## Full Extracted Text

### Page 1

> Extracted page text here.

### Page 2

> Extracted page text here.
```

For transcripts:

```markdown
# Video Title

## Transcript

### 00:00:00

Speaker/text...

### 00:01:30

Speaker/text...
```

This makes the system rebuildable from the vault.

If you do not want huge notes, use sidecar Markdown files:

```text
20 Sources/PDFs/example-report.md
20 Sources/PDFs/example-report.fulltext.md
```

But I would not make SQLite the only place full text exists. That weakens the local-first claim.

---

# 10. Add a rebuild-from-scratch guarantee

A 10/10 local-first system should be rebuildable.

Add a section:

```markdown
## Rebuild Guarantee

Given only:
- the Markdown vault,
- files inside 90 System/Attachments/,
- the Python scripts,
- requirements.txt,

the system must be able to rebuild:
- SQLite metadata tables,
- SQLite FTS5 index,
- Qdrant collection,
- chunk metadata,
- backlinks report,
- validation report.
```

Then define command:

```bash
lillith rebuild --all
```

Expected outputs:

```text
90 System/Indexes/lillith.db
90 System/Indexes/qdrant_storage/
90 System/Logs/rebuild-YYYY-MM-DD.md
```

This is a major architecture-quality upgrade.

---

# 11. Add immutable IDs

Relying only on file paths is fragile. Notes may move. Titles may change. Add stable IDs.

```yaml
id: note_<uuid-or-ulid>
```

Example:

```yaml
id: note_01J4Z7Y2M8W7KJQG9F8K6D1P3A
```

Then your database can track notes even if files move.

Recommended universal schema becomes:

```yaml
---
schema_version: 1
id: note_<ulid>
note_type: ...
name: ...
title: ...
...
---
```

This makes Lillith more durable.

---

# 12. Add chunk IDs

For retrieval, every chunk should have a stable ID.

```text
chunk_id = note_id + "#chunk-" + zero_padded_index
```

Example:

```text
note_01J4Z7Y2M8W7KJQG9F8K6D1P3A#chunk-0007
```

Chunk metadata:

```json
{
  "chunk_id": "note_01J...#chunk-0007",
  "note_id": "note_01J...",
  "vault_path": "20 Sources/PDFs/example-report.md",
  "heading_path": ["Full Extracted Text", "Page 7"],
  "start_char": 12340,
  "end_char": 13820,
  "access_level": "internal",
  "source_type": "pdf"
}
```

This makes citations, reranking, and generated evidence much cleaner.

---

# 13. Define chunking policy

Right now, the plan says chunking happens, but a 10/10 version should define the policy.

Example:

```text
Default chunk size:
  800 tokens

Overlap:
  120 tokens

Chunk boundaries:
  Prefer Markdown headings.
  Prefer page boundaries for PDFs.
  Prefer timestamp boundaries for transcripts.
  Never split YAML frontmatter.
  Never split code blocks unless block exceeds max chunk size.

Chunk metadata must include:
  - chunk_id
  - note_id
  - source_path
  - heading_path
  - page_number, if PDF
  - timestamp_start/timestamp_end, if transcript
  - token_count
  - access_level
```

This prevents inconsistent indexing later.

---

# 14. Define retrieval algorithm precisely

The retrieval pipeline is conceptually good, but I would make it exact.

Example:

```text
Input:
  user_query
  filters

Steps:
  1. Normalize query.
  2. Run SQLite FTS5 BM25 search, top_k=50.
  3. Run Qdrant dense vector search, top_k=50.
  4. Apply access_level filter before cloud use.
  5. Merge using Reciprocal Rank Fusion.
  6. Optional local reranker, top_k=20.
  7. Deduplicate by note_id and chunk_id.
  8. Return top_n evidence chunks.
```

RRF formula:

```text
score(d) = Σ 1 / (k + rank_i(d))
where k = 60
```

Then define output:

```json
{
  "query": "...",
  "retrieval_run_id": "...",
  "results": [
    {
      "rank": 1,
      "chunk_id": "...",
      "note_id": "...",
      "vault_path": "...",
      "score": 0.083,
      "retrieval_sources": ["fts5", "qdrant"],
      "excerpt": "..."
    }
  ]
}
```

This raises implementation readiness a lot.

---

# 15. Define generated-answer evidence format

A generated answer should cite exact source chunks.

Example:

```markdown
# Why use hybrid retrieval?

## Answer

Hybrid retrieval combines exact lexical matching with semantic search...

## Evidence

### Evidence 1

- Source: [[20 Sources/PDFs/vector-search-notes]]
- Chunk: `note_01J...#chunk-0004`
- Retrieval score: 0.083
- Page: 7

> Quoted evidence here.

### Evidence 2

- Source: [[30 Concepts/Wiki/sqlite-fts5]]
- Chunk: `note_01J...#chunk-0002`

> Quoted evidence here.

## Limitations

- This answer is based only on indexed vault content.
- Source coverage may be incomplete.

## Follow-up Questions

- ...
```

This gives generated answers provenance and auditability.

---

# 16. Add quality gates

Every phase should have acceptance criteria.

Example:

## Phase 1 acceptance criteria

```text
Phase 1 is complete when:
  - all required folders exist,
  - all 12 templates exist,
  - every template passes schema validation,
  - .gitignore excludes indexes and logs,
  - main and agent/drafts branches exist,
  - README explains basic vault layout.
```

## Phase 2 acceptance criteria

```text
PDF ingestion is complete when:
  - a PDF can be hashed,
  - duplicate PDFs are detected,
  - text is extracted,
  - a source note is created,
  - chunks are created,
  - SQLite FTS5 index is updated,
  - ingestion log is written,
  - the process can be rerun idempotently.
```

## Phase 3 acceptance criteria

```text
Retrieval is complete when:
  - exact search works,
  - semantic search works,
  - rank fusion returns stable results,
  - access_level filters are enforced,
  - retrieval output includes chunk IDs,
  - failed Qdrant does not break FTS5-only fallback.
```

This is one of the biggest differences between an 8/10 plan and a 10/10 build plan.

---

# 17. Add idempotency rules

Automation must be safe to rerun.

Define:

```text
All ingestion jobs must be idempotent.

If a source_hash already exists:
  - do not duplicate the source note,
  - do not duplicate chunks,
  - update pipeline_status only if progressing,
  - log duplicate detection.

If an index already contains a chunk_id:
  - update only if source note updated timestamp changed,
  - otherwise skip.

If a generated answer name already exists:
  - create a revision note or append suffix,
  - never overwrite without explicit approval.
```

This is critical for operational safety.

---

# 18. Add failure handling

The plan needs explicit failure states.

Example:

```yaml
pipeline_status: failed
failure_reason: OCR timeout
failure_stage: text_extraction
last_attempted: 2026-07-25
```

And retry rules:

```text
Failed ingestion:
  - may be retried manually,
  - must not be retried indefinitely,
  - must preserve error logs,
  - must not produce partial published notes.
```

Add a failed folder or report:

```text
90 System/Logs/failed_ingestions.md
```

This will make the system easier to debug.

---

# 19. Add audit logs as structured Markdown

Instead of only freeform logs, define log format.

```markdown
# Activity Log

## 2026-07-25 14:32:10 — PDF Ingestion

- Run ID: `run_01J...`
- Input: `example.pdf`
- SHA256: `...`
- Result: success
- Source note: [[20 Sources/PDFs/example-report]]
- Chunks created: 42
- Indexed in SQLite: yes
- Indexed in Qdrant: yes
- Duration: 14.2s
```

For generated answers:

```markdown
## 2026-07-25 15:11:04 — Generated Answer

- Run ID: `run_01J...`
- Query: "How does hybrid retrieval work?"
- Model: `claude-sonnet-x`
- Retrieval run: `retrieval_01J...`
- Output: [[70 Generated Answers/Wiki/how-hybrid-retrieval-works]]
- Status: draft
```

This makes the system inspectable.

---

# 20. Add a formal Cloud LLM Data Boundary

This is necessary for a 10/10 operational safety score.

Add:

```markdown
## Cloud LLM Data Boundary

### Cloud LLM may receive

- selected evidence chunks returned by retrieval,
- source excerpts required for a user-requested generated note,
- note titles, paths, and metadata required for citations,
- user query and task instructions.

### Cloud LLM may not receive

- entire vault exports,
- entire raw source files unless manually approved,
- private logs,
- credentials or secrets,
- files tagged `access_level: restricted`,
- chunks tagged `access_level: restricted`,
- unredacted personal data unless manually approved.

### Local-only operations

The following must be handled by local scripts or local LLM only:

- duplicate detection across entire vault,
- stale-note review,
- broken wikilink detection,
- frontmatter validation,
- sensitive content scan,
- private/restricted source summarization.
```

And enforce it:

```text
Retrieval must apply access_level filtering before any cloud generation step.
```

---

# 21. Add access-level policy

Define:

```yaml
access_level: <public|internal|private|restricted>
```

Rules:

```text
public:
  May be sent to cloud.

internal:
  May be sent to cloud if user has not disabled cloud synthesis.

private:
  May not be sent to cloud unless manually approved per run.

restricted:
  Never sent to cloud.
```

Then retrieval/generation should respect this.

---

# 22. Add secrets policy

Explicitly state:

```text
No API keys, tokens, credentials, passwords, or private environment values may be written into notes, logs, generated answers, or prompts.

Secrets must live only in:
  - .env
  - OS keychain
  - external secret manager

.env must be excluded from Git.
```

Add `.gitignore`:

```gitignore
.env
*.key
*.pem
*.sqlite-wal
*.sqlite-shm
90 System/Indexes/
90 System/Logs/*.log
```

---

# 23. Add backup and disaster recovery

A mature local-first system needs recovery rules.

```markdown
## Backup Policy

The following must be backed up:
- Markdown vault,
- 90 System/Attachments/,
- Git repository.

The following may be regenerated:
- 90 System/Indexes/lillith.db,
- 90 System/Indexes/qdrant_storage/,
- retrieval caches,
- temporary logs.

Recommended backup frequency:
- vault: daily,
- attachments: daily,
- Git remote push: after each reviewed merge.
```

And restore:

```bash
git clone <repo>
lillith rebuild --all
```

---

# 24. Add dependency and environment specification

For build readiness, add:

```text
Python: 3.11+
OS targets:
  - Windows 11
  - macOS 14+
  - Linux

Required tools:
  - Git
  - SQLite with FTS5
  - Qdrant local
  - FFmpeg
  - Tesseract OCR, optional
  - Ollama
  - Python packages listed in requirements.txt
```

Also define:

```text
requirements.txt
.env.example
config.yaml
```

Example config:

```yaml
vault_root: "/path/to/Lillith"
sqlite_path: "90 System/Indexes/lillith.db"
qdrant_path: "90 System/Indexes/qdrant_storage"
embedding_model: "BAAI/bge-m3"
local_llm: "llama3.1"
cloud_llm: "claude-sonnet"
cloud_allowed_default: false
```

This makes deployment much clearer.

---

# 25. Add CLI command design

A 10/10 build plan should define the interface.

Example:

```bash
lillith init
lillith validate
lillith ingest pdf path/to/file.pdf
lillith ingest video path/to/file.mp4
lillith retrieve "query text"
lillith generate-answer "question text"
lillith rebuild --all
lillith maintenance daily
lillith maintenance weekly
lillith archive path/to/note.md
```

Each command should have expected behavior and output.

Example:

```bash
lillith ingest pdf ./papers/example.pdf
```

Expected output:

```text
✓ Hash calculated
✓ No duplicate found
✓ Text extracted: 18 pages
✓ Source note created
✓ Chunks created: 47
✓ SQLite index updated
✓ Qdrant index updated
✓ Log written
```

This turns the plan into something directly buildable.

---

# 26. Add test suite requirements

Add a section:

```markdown
## Test Requirements
```

Minimum tests:

```text
Schema tests:
  - valid source note passes
  - missing name fails
  - invalid status fails
  - missing status tag fails
  - duplicate name fails

Ingestion tests:
  - PDF ingestion creates source note
  - duplicate PDF is detected
  - failed extraction logs failure
  - rerun does not duplicate chunks

Retrieval tests:
  - FTS5 search returns exact matches
  - Qdrant search returns semantic matches
  - rank fusion merges results
  - restricted chunks excluded from cloud generation

Generation tests:
  - generated answer includes source_notes
  - generated answer includes evidence section
  - generated answer is draft
  - generated answer is written to agent/drafts branch

Maintenance tests:
  - broken wikilinks are reported
  - stale notes are flagged, not rewritten
  - duplicates are suggested, not merged
```

This would push build readiness close to 10/10.

---

# 27. Add “definition of done” for the whole system

Example:

```markdown
## Definition of Done

Lillith v1 is complete when:

1. A new PDF can be ingested into the vault.
2. A source note is created with valid frontmatter.
3. The note is chunked and indexed in SQLite FTS5.
4. The note is embedded and indexed in Qdrant.
5. A user query retrieves relevant chunks from both indexes.
6. A generated answer note can be created with cited evidence.
7. The generated answer is saved as draft on agent/drafts.
8. Validation catches malformed notes.
9. Daily maintenance reports broken links and stale notes.
10. The full retrieval index can be rebuilt from Markdown and attachments.
11. Restricted notes are never sent to a cloud LLM.
12. Git review workflow protects published content.
```

This makes success measurable.

---

# 28. Add “non-goals”

This helps prevent scope creep.

```markdown
## Non-Goals for v1

Lillith v1 will not:
- provide a chat UI,
- replace Obsidian,
- auto-publish generated notes,
- auto-delete notes,
- auto-merge duplicates,
- expose a network service,
- sync private vault data to cloud,
- support multi-user permissions,
- support real-time collaborative editing.
```

This improves MVP clarity.

---

# 29. Add design decision records

Use ADRs:

```text
90 System/Decisions/
├── ADR-001-markdown-as-source-of-truth.md
├── ADR-002-sqlite-plus-qdrant.md
├── ADR-003-cloud-local-llm-boundary.md
├── ADR-004-full-path-wikilinks.md
├── ADR-005-agent-branch-workflow.md
```

Example ADR:

```markdown
# ADR-002: Use SQLite FTS5 and Qdrant for Hybrid Retrieval

## Status

Accepted

## Context

Exact keyword search and semantic similarity serve different retrieval needs.

## Decision

Lillith will use SQLite FTS5 for exact/BM25 retrieval and Qdrant for dense-vector semantic retrieval.

## Consequences

This adds operational complexity but provides more robust retrieval than either method alone.
```

This makes the architecture easier to maintain.

---

# 30. Refine the implementation phases

I would rewrite the phases like this.

## Phase 0 — Finalize contracts

Output:

```text
SCHEMA.md
SECURITY_AND_PRIVACY.md
config.yaml.example
requirements.txt
```

Acceptance:

```text
Schemas are complete.
Enums are final for v1.
All note templates validate.
```

## Phase 1 — Vault skeleton

Output:

```text
Folder structure
Templates
Logs
Git branches
.gitignore
CLAUDE.md
```

Acceptance:

```text
lillith validate --templates passes.
```

## Phase 2 — PDF ingestion with SQLite only

Output:

```text
PDF source notes
Chunks
SQLite tables
FTS5 search
```

Acceptance:

```text
One sample PDF can be ingested and searched.
```

## Phase 3 — Qdrant semantic search

Output:

```text
Embeddings
Qdrant collection
Hybrid retrieval
RRF merge
```

Acceptance:

```text
Query returns fused lexical and semantic results.
```

## Phase 4 — Generated answer notes

Output:

```text
Generated-answer template
Evidence section
Draft note creation
Git agent/drafts workflow
```

Acceptance:

```text
A question creates a cited draft answer note.
```

## Phase 5 — Video/transcript ingestion

Output:

```text
FFmpeg extraction
faster-whisper transcript
Transcript note
Transcript indexing
```

Acceptance:

```text
One video creates a searchable transcript note.
```

## Phase 6 — Maintenance

Output:

```text
Validation
Broken link report
Duplicate suggestions
Stale note report
Archive helper
```

Acceptance:

```text
Maintenance creates reports only; it does not silently rewrite published notes.
```

This is much cleaner than trying to do too much early.

---

# 31. Add a machine-readable schema

For a true 10/10, add a machine-readable schema file:

```text
90 System/Schemas/frontmatter.schema.json
```

or:

```text
90 System/Schemas/schema.yaml
```

Example:

```yaml
note_type:
  type: enum
  values:
    - atomic
    - function
    - pattern
    - comparison
    - error
    - workflow
    - reference
    - snippet
    - gotcha
    - generated-answer
    - transcript
    - source

status:
  type: enum
  values:
    - draft
    - review
    - published
    - archived
```

Then your validator uses the schema, not hardcoded assumptions.

---

# 32. Add migration policy

Eventually, schema changes will happen.

Add:

```markdown
## Schema Migration Policy

When schema_version changes:
1. A migration script must be created.
2. The migration must be idempotent.
3. The migration must create a Git commit.
4. The migration must write a log entry.
5. No migration may delete user content.
```

Example:

```bash
lillith migrate schema --from 1 --to 2
```

---

# 33. Add performance targets

Not mandatory, but helpful.

Example:

```text
For a vault of 10,000 notes:
  - validation should complete under 60 seconds,
  - FTS5 query should return under 500 ms,
  - Qdrant query should return under 1 second,
  - generated answer retrieval context should be prepared under 5 seconds.

For ingestion:
  - PDF text extraction should process at least 20 pages/minute without OCR.
  - OCR fallback may be slower.
```

This gives you objective scaling targets.

---

# 34. Add observability

Define reports:

```text
90 System/Reports/
├── validation_report.md
├── broken_links.md
├── duplicate_candidates.md
├── stale_notes.md
├── restricted_content_audit.md
└── index_health.md
```

Index health report:

```markdown
# Index Health

- Notes in vault: 1,240
- Notes in SQLite: 1,240
- Chunks in SQLite: 18,420
- Chunks in Qdrant: 18,420
- Missing embeddings: 0
- Broken source paths: 0
- Last rebuild: 2026-07-25
```

This makes maintenance transparent.

---

# 35. Define conflict behavior

When scripts and humans both edit files, what happens?

Add:

```text
If a note has uncommitted human edits:
  - automation must not overwrite it.
  - automation should write a proposed patch or report.

If generated output conflicts with existing file:
  - create a new revision file.
  - never silently overwrite.

If Git working tree is dirty:
  - ingestion may proceed only if writing new source notes.
  - maintenance rewrites must stop.
```

This matters a lot for safety.

---

# 36. Add review workflow for generated notes

Generated answer lifecycle:

```text
draft:
  Created by Hermes.

review:
  Human or local validator has reviewed structure.

published:
  Human-approved and merged into main.

archived:
  Superseded or no longer useful.
```

Promotion command:

```bash
lillith promote 70 Generated\ Answers/Wiki/example.md
```

Promotion checks:

```text
- valid frontmatter,
- at least one source note,
- all wikilinks valid,
- no restricted evidence used improperly,
- confidence is not low unless manually allowed.
```

---

# 37. Add “no silent mutation” rule

For 10/10 safety:

```text
No automation may silently rewrite published notes.

Allowed:
  - create draft notes,
  - create reports,
  - append logs,
  - propose patches.

Not allowed without explicit approval:
  - modify published note body,
  - delete notes,
  - merge duplicates,
  - rewrite source notes,
  - remove evidence blocks.
```

The current plan already leans this way, but I would make it a formal invariant.

---

# 38. Add source immutability guarantee

Define:

```text
Source notes are append-only after publication.

Allowed changes:
  - correction notes linked from source,
  - metadata updates through reviewed migration,
  - pipeline_status changes during initial ingestion.

Not allowed:
  - rewriting extracted source text,
  - deleting source sections,
  - replacing original evidence.
```

This protects provenance.

---

# 39. Add prompt templates

For LLM use, add actual prompt contracts.

Example:

```text
90 System/Prompts/
├── generate_answer.md
├── extract_concepts.md
├── propose_wikilinks.md
├── validate_note.md
└── summarize_source.md
```

Generated answer prompt should require:

```text
- answer only from supplied evidence,
- cite every substantive claim,
- include limitations,
- do not invent sources,
- if evidence is insufficient, say so.
```

This improves output reliability.

---

# 40. Add hallucination controls

For generated notes:

```text
Generated answers must:
  - include an Evidence section,
  - cite source_notes,
  - cite chunk IDs,
  - include Limitations,
  - mark unsupported claims as assumptions,
  - use confidence: low if evidence is incomplete.
```

Validator should fail generated answers that lack evidence.

---

# Target 10/10 version: compact checklist

If you want the shortest path to 10/10, make these changes:

## Architecture: 10/10

Add:

- rebuild-from-scratch guarantee,
- stable note IDs,
- chunk IDs,
- ADRs,
- explicit source-text storage decision.

## Build readiness: 10/10

Add:

- CLI command spec,
- phase acceptance criteria,
- dependency list,
- config file,
- test plan,
- definition of done.

## Schema consistency: 10/10

Add:

- `schema_version`,
- universal minimal schema,
- per-type schemas,
- field validation rules,
- machine-readable schema,
- consistent tags.

## Operational safety: 10/10

Add:

- cloud LLM data boundary,
- access-level enforcement,
- no-silent-mutation rule,
- idempotency rules,
- failure states,
- backup/recovery policy.

## MVP clarity: 10/10

Add:

- Phase 0 contract-finalization phase,
- PDF-only first ingestion,
- SQLite-only before Qdrant,
- explicit non-goals,
- “done” criteria per phase.

---

# My recommended “perfected” Lillith v1 structure

I would restructure the repo/vault like this:

```text
Lillith/
├── ARCHITECTURE.md
├── BUILD_PLAN.md
├── SCHEMA.md
├── OPERATIONS.md
├── SECURITY_AND_PRIVACY.md
├── README.md
├── requirements.txt
├── config.example.yaml
├── .env.example
├── .gitignore
│
├── 00 Inbox/
├── 10 Notes/
│   └── _INGESTED.md
├── 20 Sources/
│   ├── PDFs/
│   ├── Web/
│   └── Transcripts/
├── 30 Concepts/
│   ├── Wiki/
│   └── Templates/
├── 40 Projects/
│   └── Wiki/
├── 50 People/
│   └── Wiki/
├── 60 Decisions/
│   ├── Wiki/
│   └── ADRs/
├── 70 Generated Answers/
│   └── Wiki/
├── 80 Outputs/
├── 90 System/
│   ├── Attachments/
│   │   ├── PDF/
│   │   ├── Video/
│   │   ├── Audio/
│   │   └── Images/
│   ├── Indexes/
│   │   ├── lillith.db
│   │   └── qdrant_storage/
│   ├── Logs/
│   ├── Reports/
│   ├── Schemas/
│   │   └── frontmatter.schema.yaml
│   ├── Prompts/
│   ├── Scripts/
│   └── Skills/
└── CLAUDE.md
```

---

# Final recommendation

Your current plan is already strong. To push it to 10/10, do not add more features. Instead, add **contracts, validation, safety rules, and acceptance criteria**.

The most important changes are:

1. Add `schema_version`, stable note IDs, and chunk IDs.
2. Move from prose schema to strict per-type schemas.
3. Add a machine-readable schema and validator.
4. Define CLI commands and phase acceptance criteria.
5. Add cloud/privacy/access-level enforcement.
6. Define idempotency, failure handling, and no-silent-mutation rules.
7. Add rebuild-from-Markdown guarantee.
8. Make MVP smaller: PDF → SQLite → Qdrant → generated answers → video → maintenance.

If you make those changes, the plan becomes not just a good architecture document, but a highly reliable implementation blueprint.