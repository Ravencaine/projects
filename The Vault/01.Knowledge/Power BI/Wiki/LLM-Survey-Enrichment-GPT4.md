---
created: 2026-08-04
updated: 2026-08-05
source: "Analyzing Survey Comments in Power BI Using AI.md"
note_type: pattern
tags: [llm, gpt-4, openai, python, survey-enrichment, theme-tagging, sentiment-scoring, google-colab, pandas, tqdm, hybrid-pipeline]
related: [GPT-4-Thematic-Coding, OpenAI-API-Cost-Audit, Survey-Comments-Dashboard, sentiment-analysis-api, ai-insights-text-analytics-power-bi]
---

# LLM Survey Enrichment (GPT-4 Two-Pass Pipeline)

Process a corpus of free-text survey comments through an LLM (GPT-4) to produce a **structured CSV** of `{Comment, Theme, SentimentScore}` — ready to be loaded into Power BI as a model-driven dashboard. The pipeline runs in Google Colab or any Python host, exports the enriched CSV, and Power BI consumes it like any other data source.

## Purpose

Open-ended survey responses are rich but unstructured. Manual thematic coding is slow and inconsistent. Pure Power BI tools (built-in AI Insights, Azure Cognitive Services) cover sentiment and key-phrase extraction but cannot perform *taxonomy induction* — discovering the relevant themes from the corpus itself. This pattern lets GPT-4 do the taxonomy induction + tagging + scoring in one short script, then hands the structured output to Power BI for visualisation.

## Components

- **OpenAI Python client:** `openai.OpenAI(api_key=...)`, model `gpt-4`.
- **Pandas DataFrame** of comments (`df["Comment"]`).
- **Two distinct LLM calls per comment** (theme tag + sentiment score), plus **one shared call** that runs once over the whole corpus (theme extraction).
- **`tqdm.pandas()`** for the per-comment iterations so progress is visible on long runs.
- **Robustness wrapper:** every per-comment call lives inside `try/except` returning `"Error"` or `None` on failure — single bad inputs don't kill the run.
- **CSV export** at the end (`df.to_csv("tagged_survey_comments.csv", index=False)`) — this is the handoff to Power BI.

## Structure

```python
# STEP 1: Setup
!pip install openai pandas openpyxl --quiet
from google.colab import files
import pandas as pd
import openai
from openai import OpenAI
import getpass

# STEP 2: Upload + load
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name) if file_name.endswith(".csv") else pd.read_excel(file_name)

# STEP 3: Authenticate
client = OpenAI(api_key=getpass.getpass("API key: "))

# STEP 4 (corpus-wide, runs once): extract themes
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": THEME_EXTRACTION_PROMPT}],
    temperature=0.3,
)
themes_text = response.choices[0].message.content
theme_list = [t.strip("- ").strip() for t in themes_text.split("\n") if t.strip()]

# STEP 5 (per-comment): tag with theme
from tqdm import tqdm
tqdm.pandas()
df["Theme"] = df["Comment"].progress_apply(lambda c: tag_comment(c, theme_list))

# STEP 6 (per-comment): score sentiment
df["SentimentScore"] = df["Comment"].progress_apply(score_sentiment)

# STEP 7: Export enriched CSV for Power BI
df.to_csv("tagged_survey_comments.csv", index=False)
files.download("tagged_survey_comments.csv")
```

`THEME_EXTRACTION_PROMPT` is shown in [[GPT-4-Thematic-Coding]].

`tag_comment` and `score_sentiment` are wrappers around `client.chat.completions.create(...)` calls, each with its own prompt and a `try/except` returning `"Error"` / `None` on failure.

## Example

In the Bittar article's example run (a survey of unspecified size), the entire pipeline took a few minutes and cost **$2.99 USD**. Output:

```text
Comment, Theme, SentimentScore
"The app crashes when I open the menu.", "App Stability & Bugs", 1
"Customer service was super helpful!", "Customer Support Quality", 5
"Pricing feels fair for what you get.", "Pricing & Value Perception", 4
```

## Variations

- **Swap the LLM.** Any instruction-following model works — `gpt-4o`, `claude-3-5-sonnet`, `llama-3` via Ollama, etc. Smaller/weaker models may need more explicit JSON-output instructions to keep tagging structured.
- **Run locally.** The script runs anywhere Python + an OpenAI key runs. Google Colab is convenient (free GPU + ephemeral file storage) but you can also run it on a laptop or a serverless job.
- **Add more enrichment columns.** GPT-4 can extract named entities, urgency flags, actionable vs non-actionable, etc. — each as its own per-comment column. Treat the script as a per-comment function and add columns as needed.
- **Streaming for live updates.** Replace `progress_apply` with a streaming pipeline that writes rows incrementally — useful for ongoing survey feeds where new comments arrive continuously.
- **Bias controls.** The "current economic climate" instruction in Bittar's theme-extraction prompt is an *intentional framing* to steer GPT-4 toward economy-relevant themes. Swap or remove it for other corpora.

## Notes

- **Don't ask GPT-4 to tag freely.** The two-pass approach (closed theme list then per-comment tag) produces consistent, comparable tags. Letting GPT-4 invent a theme per comment gives unbounded cardinality and breaks aggregations downstream.
- **Temperature choices matter.** Theme extraction at 0.3 (creative but stable); per-comment tagging at 0.3 (consistency matters, but you want some room for disambiguation); sentiment scoring at 0 (deterministic numeric scale).
- **Cost is not free.** See [[OpenAI-API-Cost-Audit]] — the example was $2.99; thousands of comments can run into tens of dollars. Plan for it.
- **Privacy.** Customer feedback sent to OpenAI is subject to OpenAI's data-use policy (typically retained for 30 days for abuse monitoring, not used for training for API customers). For PII or regulated data, use Azure OpenAI with a BAA, or run a local model.
- **Different from Azure Cognitive Services.** Built-in Power BI AI Insights and Azure Text Analytics return a fixed shape (sentiment label, key phrases, entities) — they cannot perform the closed-set theme induction this pipeline does. Use this pattern when taxonomy must be corpus-driven.

## Related

- [[GPT-4-Thematic-Coding]] — the prompt-engineering pattern this pipeline wraps
- [[OpenAI-API-Cost-Audit]] — concrete cost datum + ROI framing
- [[Survey-Comments-Dashboard]] — the Power BI visualisation layer that consumes the pipeline output
- [[sentiment-analysis-api]] — Azure alternative (label-based, not numeric; can't induce themes)
- [[ai-insights-text-analytics-power-bi]] — built-in Power BI AI Insights (limited; no theme induction)
