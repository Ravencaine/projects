---
created: 2026-08-05
updated: 2026-08-05
source: Analyzing Survey Comments in Power BI Using AI (Isabelle Bittar)
note_type: atomic
tags: [python, gpt-4, openai, survey, colab, sentiment, themes, tagging]
---

# Python + GPT-4 Survey Enrichment Workflow

8-step Colab notebook that takes a CSV of open-ended survey comments and enriches them with GPT-4: extracted themes, per-comment theme tags, and 1–5 sentiment scores. Output is a CSV ready for Power BI.

## Prerequisites

```bash
!pip install openai pandas openpyxl --quiet
```

Packages: `openai>=1.0` (uses new `client.chat.completions.create` API), `pandas`, `openpyxl`, `tqdm` (progress bars).

## Step 1–2: Load Data

```python
from google.colab import files
import pandas as pd

uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name) if file_name.endswith(".csv") else pd.read_excel(file_name)
df.head()
```

Input CSV expected columns: at minimum `Comment` (free-text survey response). Optional: `SubmissionDate` or other metadata.

## Step 3: Authenticate

```python
import openai
from openai import OpenAI
import getpass

api_key = getpass.getpass("Enter your OpenAI API key: ")
client = OpenAI(api_key=api_key)
```

Uses `getpass.getpass` so the API key is not stored in the notebook history.

## Step 4: Extract Themes (Batch)

```python
sample_comments = df["Comment"].tolist()
prompt = (
    "Here are open-ended customer feedback comments:\n\n"
    + "\n".join(f"- {c}" for c in sample_comments)
    + "\n\nPlease extract 12 to 15 concise, professional themes that reflect "
    "the key topics customers are discussing. Take into account the current "
    "economic climate (e.g., pricing sensitivity, value, speed, ethics). "
    "Return only a clean bullet list of theme names."
)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3
)
themes_text = response.choices[0].message.content
```

Temperature 0.3: deterministic enough for consistency, creative enough to find nuanced themes. Batch call (all comments at once) — only 1 GPT-4 call for theme extraction.

## Step 5: Parse Themes to List

```python
theme_list = [
    t.strip("- ").strip()
    for t in themes_text.split("\n")
    if t.strip()
]
```

## Step 6: Tag Each Comment with a Theme (Per-Comment Call)

```python
from tqdm import tqdm
tqdm.pandas()

def tag_comment(comment, theme_list):
    prompt = (
        f"Choose the most appropriate theme from the list for:\n\n"
        f"Comment: \"{comment}\"\n\nAvailable themes:\n"
        + "\n".join(f"- {t}" for t in theme_list)
        + "\n\nReturn only the best-matching theme."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Error"

df["Theme"] = df["Comment"].progress_apply(lambda c: tag_comment(c, theme_list))
```

One GPT-4 call per comment. `tqdm.pandas()` shows a progress bar. Wrap in try/except to handle API errors gracefully.

## Step 7: Score Sentiment Per Comment

```python
def score_sentiment(comment):
    prompt = (
        f"On a scale from 1 to 5, rate the sentiment of:\n\n"
        f"Comment: \"{comment}\"\n\n"
        f"Use this scale:\n1 = Very Negative\n2 = Negative\n3 = Neutral\n4 = Positive\n5 = Very Positive\n\nReturn only the number (1 to 5)."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0  # Fully deterministic for sentiment
        )
        return int(response.choices[0].message.content.strip())
    except:
        return None

df["SentimentScore"] = df["Comment"].progress_apply(score_sentiment)
```

Temperature 0: identical prompts must return identical scores. Returns integer 1–5.

## Step 8: Export and Download

```python
output_file = "tagged_survey_comments.csv"
df.to_csv(output_file, index=False)
files.download(output_file)
```

Final CSV columns: `Comment`, `Theme`, `SentimentScore` (+ any original columns).

## Output Schema

| Column | Type | Description |
|--------|------|-------------|
| Comment | string | Original survey response |
| Theme | string | GPT-4-assigned theme label |
| SentimentScore | int (1–5) | GPT-4-assigned sentiment |

## Cost Estimate

| Step | GPT-4 calls | Input tokens | Output tokens |
|------|------------|-------------|---------------|
| Extract themes | 1 | ~10 × N comments | ~200–400 |
| Tag themes | N | ~50–100 each | ~5–15 |
| Score sentiment | N | ~30–50 each | ~1–2 |

For ~500 comments: approximately **$2.99 total** via ChatGPT API.

## Related

- [[Analyzing-Survey-Comments-AI-Power-BI-Isabelle-Bittar-source]]
- [[Survey-Sentiment-Scorecard]]
- [[Survey-AI-Dashboard-Components]]
