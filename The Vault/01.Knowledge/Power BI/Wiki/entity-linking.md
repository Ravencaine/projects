---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [cognitive-services, entity-linking, disambiguation, api, knowledge-base]
---

# Entity Linking — Disambiguate Entity Meanings

Resolves entity mentions to a canonical knowledge base entry — distinguishing between different meanings of the same term.

## Definition

"Apple" could mean the fruit, the record label, or Apple Inc. Entity Linking resolves ambiguous mentions to their correct canonical entry.

## API Details

| Field | Value |
|-------|-------|
| Service | Azure Text Analytics |
| Endpoint | `https://<resource>.cognitiveservices.azure.com/text/analytics/v3.1/entities/linking` |
| Method | POST |
| Input | `{ "documents": [{ "id": "...", "language": "en", "text": "..." }] }` |
| Output | `{ "documents": [{ "entities": [{ "name", "bingId", "matches": [{ "text", "score" }] }] }] }` |

## Output Fields

| Field | Description |
|-------|-------------|
| name | Canonical entity name |
| bingId | Unique identifier in Bing's knowledge base |
| matches | All occurrences in the document with match score |

## Use Cases

- Disambiguate company names in financial news
- Resolve person names that map to multiple individuals
- Build a knowledge graph from text

## Related

- [[named-entity-recognition-ner]]
- [[azure-cognitive-services-overview]]
