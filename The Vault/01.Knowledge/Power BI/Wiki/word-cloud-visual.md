---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [word-cloud, power-bi, marketplace-visual, text-visualisation]
---

# Word Cloud Visual (Power BI Marketplace)

A marketplace visual that generates a word cloud from text data — word size proportional to frequency.

## Signature

Power BI Marketplace → install "Word Cloud" visual → add to report canvas

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Text | text column | Column containing the text to analyse |
| Stop Words | text column or list | Common words to exclude (e.g., "the", "a", "is") |
| Min Frequency | integer | Minimum times a word must appear to appear in the cloud |
| Max Words | integer | Maximum number of words in the cloud |
| Word Rotation | slider 0–90° | Rotation angle for words |
| Scale | dropdown | linear / sqrt / log — affects size distribution |

## Returns

A visual where each word's font size is proportional to its frequency in the text column.

## Steps

1. Install Word Cloud from Marketplace
2. Drag the text column to the "Text" field
3. Add a stop words list (or use the built-in English stop words)
4. Adjust Max Words to keep the cloud readable (50–100 is typical)
5. Use a Power Query custom function to pre-process: extract key phrases or remove unwanted characters first

## Related

- [[word-cloud-configuration]]
- [[key-phrase-extraction-api]]
