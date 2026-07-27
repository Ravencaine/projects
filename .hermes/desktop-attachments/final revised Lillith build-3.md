Final check complete. This v1.2 plan is **very close to implementation-ready**. It is now a strong executable blueprint rather than just an architecture concept. Most previous issues are fixed: schema versioning is present, `id: note_<ulid>` is now universal, `legacy_id` replaces the conflicting old ID pattern, access-level policy is coherent, Phase 2 is split, Ollama setup is moved earlier, chunk size is standardized, SQLite/Qdrant schemas now include `note_id`, and templates are much better aligned [1].

My final rating:

```text
Architecture:        9.5 / 10
Build readiness:     9 / 10
Schema consistency:  8.8 / 10
Operational safety:  9.5 / 10
MVP clarity:         9 / 10
Overall:             9.2 / 10
```

I would approve this for **Phase 1A and Phase 1B implementation**, with a few small cleanup edits before coding ingestion.

---

## Final verdict

**Yes — this is ready to start building.**

The remaining issues are not fundamental architecture problems. They are mostly cleanup inconsistencies in the appendices/templates. The system design is now mature: local-first vault, source immutability, hybrid retrieval, Git-reviewed agent writes, chunk-level evidence, cloud privacy boundaries, idempotency, failure handling, validation, test requirements, and rebuildability are all represented [1].

Do **not** keep revising the architecture forever. I would make the fixes below, then start implementation.

---

# What is now strong

## 1. Architecture is coherent

The system has a clear pipeline:

```text
Raw Source → Source Note → Chunk + Index → Retrieve → Generate Draft → Validate → Human Review → Publish
```

The separation between source notes, concept notes, generated answers, system files, indexes, logs, and ADRs is clean [1].

## 2. The frontmatter schema is much better

The universal required fields are now clear:

```yaml
schema_version
note_type
id
name
title
status
created
updated
tags
```

That is exactly the right minimum contract [1].

## 3. The privacy model is now operationally meaningful

The access levels are now clear:

```text
public     → cloud allowed
internal   → cloud allowed by default
private    → cloud only with --approve-private
restricted → never cloud
```

This is good enough to build around [1].

## 4. Chunking and retrieval are now specific

The chunk size is standardized:

```text
Target: 700 tokens
Range: 350–850
Overlap: 120
```

The retrieval pipeline now specifies SQLite FTS5, Qdrant, RRF, access filtering, optional reranking, deduplication, and adaptive evidence chunk selection [1].

## 5. Operational safety is strong

The no-silent-mutation rule, source immutability guarantee, idempotency table, failure handling, structured audit logs, maintenance never-do list, and Git branch workflow are all appropriate [1].

This is one of the strongest parts of the current plan.

---

# Remaining cleanup issues before build

## 1. Transcript template is missing `schema_version`

The transcript template currently starts:

```yaml
---
note_type: transcript
id: note_<ulid>
...
```

But universal schema requires:

```yaml
schema_version: 1
```

Fix:

```yaml
---
schema_version: 1
note_type: transcript
id: note_<ulid>
...
```

This is the most obvious remaining schema mismatch.

---

## 2. `template_source.md` is missing from the main folder tree

In Section 3, under `30 Concepts/Templates/`, the list includes:

```text
template_generated_answer.md
template_transcript.md
```

but does **not** include:

```text
template_source.md
```

Later sections correctly mention all 12 templates, including `template_source.md` [1].

Fix Section 3 to include:

```text
├── template_generated_answer.md
├── template_transcript.md
└── template_source.md
```

---

## 3. ADR path still conflicts in Section 20

Section 3 correctly uses:

```text
90 System/ADRs/
```

But Section 20 says:

```text
Architecture decisions are documented as ADRs in 90 System/Decisions/
```

and shows:

```text
90 System/Decisions/
```

Fix Section 20 to:

```text
Architecture decisions are documented as ADRs in 90 System/ADRs/
```

and:

```text
90 System/ADRs/
├── ADR-001-markdown-as-source-of-truth.md
...
```

This is a small but important manifest consistency issue.

---

## 4. Appendix D skill manifest is outdated

Section 3 and Phase 1C correctly list one skill per file:

```text
SKILL_lillith_ingest_pdf.md
SKILL_lillith_ingest_video.md
SKILL_lillith_ingest_web.md
...
```

But Appendix D still lists:

```text
SKILL_lillith_ingestion.md
SKILL_lillith_retrieve.md
...
```

inside `90 System/Skills/` [1].

Fix Appendix D to match Section 3:

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

Then keep the root-level aliases:

```text
SKILL_lillith_ingestion.md
SKILL_lillith_maintenance.md
```

---

## 5. Appendix D is missing `90 System/Reports/`, `90 System/Prompts/`, and `90 System/ADRs/`

The main plan introduces:

```text
90 System/Reports/
90 System/Prompts/
90 System/ADRs/
```

But the Phase 1 manifest in Appendix D does not include all of them [1].

Either add them to Phase 1 deliverables, or clearly mark them as Phase 3/4 deliverables.

I recommend adding empty folders with `.gitkeep` during Phase 1A:

```text
90 System/ADRs/
90 System/Reports/
90 System/Prompts/
90 System/Schemas/
```

This makes the structure future-proof.

---

## 6. Universal schema example contains repeated `note_type` keys inside one YAML block

In Section 4, the universal schema block includes:

```yaml
note_type: <atomic|function|...>
...
# Source notes only
note_type: source
...
# Transcript notes only
note_type: transcript
...
# Generated answers only
note_type: generated-answer
...
```

This is understandable as documentation, but as YAML it is misleading because duplicate keys in YAML are invalid/ambiguous.

Better format:

```yaml
# Universal
note_type: <atomic|function|...|source|transcript|generated-answer>
```

Then for conditional sections, write comments only:

```yaml
# Required when note_type == source
source_type: <pdf|web>
...
```

Instead of repeating:

```yaml
note_type: source
```

This will prevent someone from copying the whole block and creating invalid YAML.

---

## 7. `vault_path` example still uses `<Type>` instead of actual folder names

In the source schema:

```yaml
vault_path: 20 Sources/<Type>/<slug>
```

But the actual source folders are:

```text
20 Sources/PDFs/
20 Sources/Transcripts/
20 Sources/Web/
```

Use concrete examples:

```yaml
vault_path: "20 Sources/PDFs/<slug>.md"
```

For source notes:

```yaml
vault_path: "20 Sources/PDFs/<name>.md"
```

For web:

```yaml
vault_path: "20 Sources/Web/<name>.md"
```

For transcript:

```yaml
vault_path: "20 Sources/Transcripts/<name>.md"
```

---

## 8. `_INGESTED.md` examples omit `.md` in vault path

Appendix A shows:

```text
20 Sources/PDFs/example-report
20 Sources/Transcripts/meeting
```

But the plan now standardizes filesystem `vault_path` with `.md`.

Fix to:

```text
20 Sources/PDFs/example-report.md
20 Sources/Transcripts/meeting.md
```

Wikilinks should still omit `.md`.

---

## 9. SQLite FTS5 external-content setup needs implementation caution

The SQLite schema says:

```sql
CREATE VIRTUAL TABLE chunks_fts USING fts5(
  ...
  content='chunks',
  content_rowid='rowid'
);
```

But the `chunks` table does not explicitly define `rowid` or include `content`. In SQLite, ordinary tables have implicit `rowid`, but the external-content FTS setup requires careful trigger or manual sync logic.

You have two options.

### Option A: Simpler MVP

Use a standalone FTS table:

```sql
CREATE VIRTUAL TABLE chunks_fts USING fts5(
  chunk_id,
  note_id,
  vault_path,
  heading,
  content
);
```

This is easier to build first.

### Option B: External-content FTS

Keep the current model, but add:

- `content TEXT NOT NULL` to `chunks`, or
- triggers to sync FTS rows,
- rebuild command for FTS index.

For MVP, I recommend **Option A** unless you specifically need external-content optimization.

---

## 10. `source_type: transcript` vs `source_type: video|audio` needs one final decision

In Section 4 source notes say:

```yaml
source_type: <pdf|transcript|web>
```

Transcript notes say:

```yaml
source_type: <video|audio>
```

The tag system uses:

```yaml
source/transcript
```

This is mostly okay, but the field is doing two related jobs.

Recommended final model:

For `note_type: source`:

```yaml
source_type: <pdf|web>
```

For `note_type: transcript`:

```yaml
source_type: <video|audio>
```

For tags:

```yaml
source/pdf
source/web
source/transcript
```

So remove `transcript` from the source-note `source_type` enum unless you intend transcripts to also be treated as source notes.

---

# Final recommended fixes list

Before starting scripts, make these edits:

1. Add `schema_version: 1` to the transcript template.
2. Add `template_source.md` to Section 3’s template tree.
3. Change Section 20 from `90 System/Decisions/` to `90 System/ADRs/`.
4. Update Appendix D skill names to match Section 3.
5. Add `90 System/Reports/`, `90 System/Prompts/`, and `90 System/ADRs/` to Appendix D or mark their phase.
6. Remove repeated `note_type: source/transcript/generated-answer` keys from the universal YAML example.
7. Standardize `vault_path` examples with `.md`.
8. Update `_INGESTED.md` examples to use `.md`.
9. Decide whether SQLite FTS5 is standalone or external-content.
10. Clarify `source_type` enum for source notes vs transcript notes.

---

# Go / no-go decision

## Phase 1A: Vault skeleton

**Go.**  
You can start immediately.

## Phase 1B: Templates and schema

**Go after small fixes.**  
Make the transcript/schema/template corrections first.

## Phase 2A: PDF ingestion

**Wait until schema is locked.**  
Do not start ingestion scripting until the universal schema, source template, transcript template, and path rules are final.

---

# Final assessment

This is a **high-quality plan** and very close to a 10/10 build blueprint.

The architecture itself is excellent. The remaining work is mostly editorial/schema consistency. Once the issues above are fixed, I would treat this as implementation-ready.

Final answer: **Approved for Phase 1A now; approved for full implementation after the 10 cleanup edits above.**