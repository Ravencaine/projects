---
name: extract-implicit-knowledge
description: "Extract implicit knowledge (entities, claims, and semantic relationships) from a KB wiki. Writes native Obsidian notes into the KB under Wiki/Implicit/. Use when: the user asks to mine implicit relationships, find hidden connections between notes, extract unnamed entities, or surface claims and contradictions in a knowledge base."
argument-hint: "<kb-name-or-path> [scope-glob]"
---

# extract-implicit-knowledge

Extracts implicit knowledge — **entities**, **claims**, and **semantic relationships** — from a knowledge base's wiki notes, and writes the results as first-class Obsidian notes inside the same KB.

## When NOT to Use

- **New source ingestion** → use `note-ingestion` skill
- **Audit or auto-fix existing notes** → use `knowledge-base-health-check` skill
- **Interactive graph dashboard** → use Understand-Anything's `/understand-knowledge` (code repos, one-off exploration)
- **All 7 KBs at once** → run this skill once per KB

## Supported KBs

This skill runs on a single KB at a time. Supported KBs:

- `Data Modeling` · `DAX Code` · `Excel` · `Power Automate` · `Power BI` · `Power Query` · `VBA`

If the user supplies an invalid KB name, refuse and list the valid KBs.

## Pipeline

### Phase 1 — Discover

Run the deterministic discovery script:

```
py 99.System/Vault Guides/extract-implicit-knowledge/discover-and-batch.py "<kb-path>" [scope-glob]
```

The script:
1. Locates the KB's Wiki folder
2. Reads `INDEX.md` for category mapping
3. Loads `merge-state.json` to skip already-extracted articles
4. Extracts from each note: H1, frontmatter, first 3000 chars, wikilinks, category
5. Groups into batches of ~12 articles (same-category co-location)
6. Writes `batch-<N>.json` + `scan.json` to the extraction cache

Report to the user:
- "Found N articles across N batches"
- "N articles already extracted (skipping)"
- "Scope: [scope or 'all Wiki/*.md']"

### Phase 2 — Extract (LLM)

For each batch file, dispatch a subagent to perform the LLM analysis.

**Analyst role** (embed this prompt for each subagent):

```
You are a knowledge graph extraction expert. Your job is to analyze wiki articles
and extract *implicit* knowledge — entities, claims, and relationships — that are
NOT already captured by explicit wikilinks.

## Input
Read the batch JSON at <batch-path>. It contains:
- batch number, KB slug
- articles: [{id, name, summary, wikilinks, category, content}]
- all_node_ids: full list of existing node IDs in the KB
- already_extracted: article IDs already processed (do not re-analyze)

## Task
For each article in the batch, extract:

### Entities (people, tools, papers, organizations)
Named things mentioned in the text that do NOT already have a node in all_node_ids.
- id: "entity:<normalized-name>" (lowercase, hyphens for spaces)
- type: "entity"
- name: proper name as written
- summary: one-line description from context
- tags: ["entity", "<category>", "<kb-name>"]
- articles: [list of article IDs that mention this entity]

### Claims (assertions, architectural decisions, key insights)
Specific assertions stated in the articles.
- id: "claim:<article-stem>:<short-slug>"
- type: "claim"
- name: short claim title
- summary: the assertion itself (1-2 sentences)
- tags: ["claim", "<category>", "<kb-name>"]
- evidence: [{article: "...", section: "..."}]
- first_article: article ID where the claim first appears

### Implicit Relationships
Only emit with clear textual evidence:
- **builds_on** (weight 0.8): Article A explicitly extends or refines Article B
- **contradicts** (weight 0.9): Article A conflicts with Article B's position
- **exemplifies** (weight 0.7): Entity or article is a concrete example of a concept
- **cites** (weight 0.7): Article references a raw source document
- **authored_by** (weight 0.6): Article attributed to a specific entity

Edge format:
{
  "source": "article:...",
  "target": "article:...",
  "type": "builds_on",
  "direction": "forward",
  "weight": 0.8,
  "description": "Brief reason for this relationship"
}

## Rules
1. Do NOT duplicate wikilink edges — wikilinks are already captured as "related" edges
2. Be conservative — only create edges with clear textual evidence
3. Deduplicate entities across articles within this batch
4. Use exact node IDs from all_node_ids when creating edges
5. Skip any article in already_extracted
6. Keep it proportional: ~5-15 entities, ~5-10 claims, ~10-15 edges per 10 articles
7. Do NOT include existing article or topic nodes in output — only new entities, claims, implicit edges

## Output
Write a JSON file to <batch-path-parent>/analysis-batch-<N>.json:
{
  "nodes": [
    { "id": "...", "type": "entity", "name": "...", "summary": "...", "tags": [...], "articles": [...] },
    { "id": "...", "type": "claim", "name": "...", "summary": "...", "tags": [...], "evidence": [...] }
  ],
  "edges": [
    { "source": "...", "target": "...", "type": "...", "direction": "forward", "weight": 0.8, "description": "..." }
  ]
}
```

Dispatch up to 3 subagents concurrently. Wait for all batches before proceeding.

Report: "Analyzed N batches. Extracted ~N entities, ~N claims, ~N implicit edges."

### Phase 3 — Persist

Run the deterministic persistence script:

```
py 99.System/Vault Guides/extract-implicit-knowledge/persist-as-notes.py "<kb-path>"
```

The script:
1. Reads all `analysis-batch-*.json` files from the cache
2. Loads `merge-state.json` for deduplication
3. Writes each new entity to `Wiki/Implicit/Entities/<slug>.md`
4. Writes each new claim to `Wiki/Implicit/Claims/<slug>.md`
5. Writes each implicit edge to `Wiki/Implicit/Edges/<type>/<slug>.md`
6. Updates `merge-state.json`
7. Appends new notes to the KB's `INDEX.md` under `## Implicit Knowledge`
8. Writes a report to `Outputs/<YYYY-MM-DD>_implicit-extraction-<kb>.md`

Existing notes are never overwritten. Duplicates are skipped silently.

### Phase 4 — Verify

Run the orphan check:

```
py 99.System/Scripts/find_orphans.py --verbose
```

Fix any orphans found before declaring the session complete.

Append to the KB's `CHANGELOG.md`:

```
## <YYYY-MM-DD> — Implicit-knowledge extraction
- Created: <N> entities, <M> claims, <K> relationship notes
- Source: extract-implicit-knowledge
- Scope: <scope-glob or "all Wiki/*.md">
```

### Phase 5 — Cleanup

Delete `The Vault/.extraction_cache/<kb>/` after Phase 3 completes.
The cache is per-run; `merge-state.json` is the durable cross-run record.

## Trigger Phrases

This skill activates on any of:
- "extract implicit knowledge from Power BI"
- "find implicit relationships in Power BI"
- "run implicit extraction on Power BI"
- "mine implicit edges from Power BI wiki"
- "what implicit relationships exist in Power BI?"
- Replace "Power BI" with any valid KB name

## Behaviours This Skill Must Never Do

1. Edit any existing wiki note. The skill is additive only.
2. Run on more than one KB in a single invocation.
3. Emit implicit edges without clear textual evidence in the source article.
4. Re-create an entity or claim whose slug already exists in `merge-state.json` or in the KB.
5. Write a note longer than 600 words.
6. Skip the `find_orphans.py` verification step.
7. Write notes outside the seven defined KBs.
8. Add a `created_by:` field to frontmatter.
9. Alter existing `INDEX.md` sections — only append `## Implicit Knowledge`.
10. Run without first confirming the target KB with the user.
