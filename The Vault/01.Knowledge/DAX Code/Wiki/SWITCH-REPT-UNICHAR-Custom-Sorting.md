---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: atomic
tags: [dax, rept, unichar, zero-width, sort, custom-sort, switch]
---

# `SWITCH + REPT(UNICHAR(8203))` Custom Measure Sorting

Using `REPT(UNICHAR(8203), n)` — a zero-width space — to create a non-numeric sort key that allows Power BI to order text categories by their underlying numeric value. Enables sorting of "Positive / Neutral / Negative" labels in the correct severity order without displaying the number.

## The Problem

Power BI can only sort text columns alphabetically or by a related numeric column. If you have a sentiment column with values like "Very Positive", "Neutral", "Very Negative", alphabetical sort puts them in the wrong order: Neutral → Negative → Positive → Very Negative → Very Positive.

## The Solution

Prepend a number of `UNICHAR(8203)` characters (zero-width space) equal to the sort rank, then wrap it in the measure:

```dax
Sentiment value =
    SWITCH(
        TRUE(),
        [Sentiment score] > 4,
            REPT(UNICHAR(8203), 5) & "Positive",
        [Sentiment score] > 3.2,
            REPT(UNICHAR(8203), 4) & "Slightly Positive",
        [Sentiment score] > 2.8,
            REPT(UNICHAR(8203), 3) & "Neutral",
        [Sentiment score] > 1.5,
            REPT(UNICHAR(8203), 2) & "Slightly Negative",
        REPT(UNICHAR(8203), 1) & "Negative"
    )
```

`UNICHAR(8203)` = U+200B (zero-width space) — invisible character that occupies no visual space but is still a character Power BI can sort on.

## Resulting Sort Order

| SWITCH output | Characters | Sort key |
|---------------|-----------|---------|
| Very Positive | `Positive` (5 ZWSPs) | sorts highest |
| Slightly Positive | `Slightly Positive` (4 ZWSPs) | ↓ |
| Neutral | `Neutral` (3 ZWSPs) | ↓ |
| Slightly Negative | `Slightly Negative` (2 ZWSPs) | ↓ |
| Negative | `Negative` (1 ZWSP) | sorts lowest |

Power BI sorts alphabetically on the string — but the zero-width spaces mean higher-ranked labels come first alphabetically.

## Why UNICHAR(8203) Specifically

UNICHAR(8203) = U+200B is the zero-width space. Unlike a regular space (UNICHAR(32)), it:
- Takes up no visual width
- Is still a sortable character
- Does not affect readability when prepended to text

## Usage in a Power BI Visual

1. Create the `Sentiment value` measure above
2. Add a **Matrix** or **Table** visual
3. Put `Theme` on rows
4. Put `Sentiment value` in the values — it will display as text but sort by severity
5. Sort the `Sentiment value` column **A→Z** (ascending) so the most-positive sentiment appears at the top

## Alternative: Sort by a Separate Numeric Column

If you have a separate numeric sort column in your dataset, Power BI's native "Sort by Column" feature handles this without the REPT trick. The REPT approach is preferred when:
- The sort order is derived from a measure (not a static column)
- You don't want to add an extra numeric column to the model

## Related

- [[Survey-Sentiment-Scorecard]]
- [[REPT-UNICHAR-Measure-Sorting-Isabelle]]
- [[Author-Isabelle-Bittar]]
