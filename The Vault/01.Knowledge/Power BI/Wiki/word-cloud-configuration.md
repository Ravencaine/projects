---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [word-cloud, configuration, stop-words, min-frequency, rotation, scale]
---

# Word Cloud Configuration — Options at a Glance

Five settings that control the output of a Word Cloud visual.

## Quick Reference

| Setting | Effect | Recommended value |
|---------|--------|------------------|
| **Stop Words** | Exclude common words (the, a, is) | Always include English stop words |
| **Min Frequency** | Words below this count are excluded | 3–5 for small datasets, 10+ for large |
| **Max Words** | Total words displayed | 50–100; too many = noise |
| **Rotation** | How much words rotate | 0° for clean layout, 45° for variety |
| **Scale** | Size mapping function | sqrt for moderate differentiation |

## Common Configurations

| Dataset size | Min Frequency | Max Words | Scale |
|------------|--------------|----------|-------|
| <1,000 rows | 2–3 | 50 | sqrt |
| 1,000–10,000 | 5–10 | 75 | sqrt |
| >10,000 | 10–20 | 100 | log |

## Pre-processing Tips

- Use [[key-phrase-extraction-api]] to extract key phrases before word cloud — single words miss multi-word topics
- Remove URLs, HTML tags, and special characters in Power Query before feeding to the Word Cloud
- Aggregate reviews to a single text field per category to avoid duplicate counting

## Related

- [[word-cloud-visual]]
- [[key-phrase-extraction-api]]
