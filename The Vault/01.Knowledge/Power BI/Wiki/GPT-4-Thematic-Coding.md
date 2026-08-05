---
created: 2026-08-04
source: "Analyzing Survey Comments in Power BI Using AI.md"
note_type: pattern
tags: [llm, gpt-4, openai, prompt-engineering, thematic-coding, theme-extraction, sentiment-scoring, closed-set-classification]
related: [LLM-Survey-Enrichment-GPT4, sentiment-analysis-api]
---

# GPT-4 Thematic Coding (Two-Pass Prompt Pattern)

A prompt-engineering pattern for inductively tagging free-text with an LLM: **first** ask the LLM to extract a closed set of themes from the corpus, **then** ask it to classify every comment against that closed set. Plus a strict, low-temperature numeric sentiment-scoring prompt.

## Purpose

You want every comment tagged with a theme so you can aggregate, filter, and visualise — but the relevant themes are *inside the corpus itself*, not predefined. The naive approach ("ask GPT-4 to tag freely per comment") produces unbounded cardinality, inconsistent labels ("Customer Support" vs "Support Quality" vs "Helpful Support"), and downstream aggregations that don't line up. The two-pass approach forces the LLM to commit to a closed vocabulary first, then pick from it.

## Components

1. **Pass 1 prompt — Theme extraction (one call over the full corpus).** Asks the LLM to extract 12–15 concise professional themes; returns a clean bullet list. Runs **once** for the whole survey.
2. **Pass 2 prompt — Per-comment theme tag (one call per comment).** Closes the tag choice to the extracted theme list. Runs **per row**.
3. **Pass 3 prompt — Per-comment sentiment score (one call per comment).** Numeric 1–5 scale with locked definitions. Runs **per row**.

## Structure

### Pass 1 — Extract themes (one call, all comments)

```python
sample_comments = df["Comment"].tolist()
prompt = (
    "Here are open-ended customer feedback comments:\n\n"
    + "\n".join(f"- {c}" for c in sample_comments)
    + "\n\nPlease extract 12 to 15 concise, professional themes that reflect "
      "the key topics customers are discussing. "
      "Take into account the current economic climate (e.g., pricing sensitivity, "
      "value, speed, ethics). "
      "Return only a clean bullet list of theme names."
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3,
)

themes_text = response.choices[0].message.content
theme_list  = [t.strip("- ").strip() for t in themes_text.split("\n") if t.strip()]
```

Convert the bullet list to a Python list with `str.strip("- ").strip()` per line, filtering empty lines.

### Pass 2 — Tag each comment (one call per comment)

```python
def tag_comment(comment, theme_list):
    prompt = (
        "Choose the most appropriate theme from the list for the following survey comment:\n\n"
        f"Comment: \"{comment}\"\n\n"
        "Available themes:\n"
        + "\n".join(f"- {t}" for t in theme_list)
        + "\n\nReturn only the best-matching theme."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Error"

df["Theme"] = df["Comment"].progress_apply(lambda c: tag_comment(c, theme_list))
```

### Pass 3 — Sentiment score (one call per comment)

```python
def score_sentiment(comment):
    prompt = (
        "On a scale from 1 to 5, rate the sentiment of the following comment:\n\n"
        f"Comment: \"{comment}\"\n\n"
        "Use this scale:\n"
        "1 = Very Negative\n"
        "2 = Negative\n"
        "3 = Neutral\n"
        "4 = Positive\n"
        "5 = Very Positive\n\n"
        "Return only the number (1 to 5)."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,                       # numeric scale → max determinism
        )
        return int(response.choices[0].message.content.strip())
    except Exception:
        return None

df["SentimentScore"] = df["Comment"].progress_apply(score_sentiment)
```

## Example

A health-insurance survey with ~400 free-text responses. Pass 1 produces 13 themes such as *"Claim Reimbursement Speed"*, *"Agent Responsiveness"*, *"Premium Affordability"*, *"Online Portal Usability"*, *"Coverage Clarity"*. Pass 2 tags every comment against these 13 — downstream aggregations are valid (`COUNTROWS`, `DISTINCTCOUNT`, bar charts, etc.) because every row carries a label from the same vocabulary.

## Variations

- **JSON-mode outputs.** Add `"response_format": {"type": "json_object"}` and ask for `{"theme": "...", "sentiment": N}` in one combined call — halves the API cost at the cost of more fragile parsing.
- **Few-shot examples.** For ambiguous categories (sarcasm, multilingual comments, very short comments), append 3–5 hand-labelled examples to the prompt.
- **Multi-label tagging.** Allow a comment to belong to more than one theme by asking for a comma-separated list and `split(",")` post-processing.
- **Tiered themes (parent → child).** Pass 1 extracts top-level themes; a second pass extracts sub-themes per top-level theme; pass 3 tags comments against `{top_theme, sub_theme}`. Useful for fine-grained drill-downs.
- **No-corpus extraction.** If you *do* have a predefined taxonomy (e.g., from a prior survey), skip Pass 1 and inject the list directly.

## Notes

- **Temperature = 0 for numeric scales.** The sentiment prompt is `temperature=0` because the rating is a 5-bucket deterministic decision — any randomness here is just noise. Tagging and theme *generation* tolerate 0.3.
- **Robustness.** Wrap every per-comment call in `try/except` returning `"Error"` or `None`. Bad inputs (rate limits, API hiccups, malformed outputs) should leave a blank row in the CSV — not crash the entire run.
- **Tag drift.** Two runs of Pass 1 against the same corpus can produce slightly different theme names. If you re-run enrichment, freeze the resulting `theme_list` and reuse it.
- **Token economics.** Sending the full comment list to Pass 1 costs prompt tokens proportional to corpus size. For very large corpora (10k+ comments), chunk the corpus and merge theme lists in a final consolidation call.
- **Privacy.** Customer feedback is sent to OpenAI's API. Subject to data-use policy; for PII or regulated data use Azure OpenAI with a BAA or a local model.

## Related

- [[LLM-Survey-Enrichment-GPT4]] — the wider pipeline that wraps these three prompts
- [[sentiment-analysis-api]] — Azure alternative (no theme induction, label-based)
- [[OpenAI-API-Cost-Audit]] — cost and ROI framing
