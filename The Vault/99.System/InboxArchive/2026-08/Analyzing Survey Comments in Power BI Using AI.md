---
title: "✨ Analyzing Survey Comments in Power BI Using AI"
source: "https://medium.com/the-bi-corner/analyzing-survey-comments-in-power-bi-using-ai-ea0ca35ff98b"
author:
  - "[[Isabelle Bittar]]"
published: 2025-07-12
created: 2026-08-04
description: "How I used GPT-4 to extract themes, score sentiment, and build an interactive dashboard in Power BI"
Processed: "Unprocessed"
---
## How I used GPT-4 to extract themes, score sentiment, and build an interactive dashboard in Power BI

![By Isabelle Bittar for KI Data Science](99.System/Attachments/By_Isabelle_Bittar_for_KI_Data_Science.webp)

By Isabelle Bittar for KI Data Science

🎁 *PBIX included at the end of this article!*

### Introduction

Organizations have access to an increasing amount of text data — which is super exciting as there is as well a growing number of ways for us to analyze and of course, visualize it😎!

However, I always find it alarming when all I see in someone’s report is a word cloud. Don’t get me wrong, world clouds can be fun and have their purpose, but we can do WAY better. This is not a high school project (I don’t even know what people are learning in high school anymore, but I like picturing a bunch of students completing some of their first coding projects and sharing their first “video games” or “world clouds” with their friends😅).

Let’s be real: if a CEO is expecting an executive summary of survey responses, we’re not going to share with them a line chart with response rates and a world cloud.

![Line chart with a wordcloud in Power BI — let’s not do that 😅](99.System/Attachments/Line_chart_with_a_wordcloud_in_Power_BI_—_let’s_not_do_that_😅.webp)

Line chart and a word cloud in Power BI… let’s not do that 😅

OK, enough about world clouds, in the following article, I’ll walk you through some of my ideas in visualizing survey comments in Power BI. You can also view this quick demo showcasing the key highlights of the reports I built:

### Part 1: The Key is Going Beyond Power BI

My starting point was a CSV file containing a collection of open-ended survey responses, each associated with a submission date. No additional context was provided — these were free-text fields at the end of a survey where respondents could share any feedback they wanted.

![](99.System/Attachments/1!T2Sqznpgc6XREYTqRYID4w.png.webp)

Starting Point to Survey Text Answers Analysis

In my case, I created the following Python script to extract key themes from survey comments, assign each comment a theme label, and score sentiment on a scale from 1 (very negative) to 5 (very positive). The script was executed in Google Colab and uses the GPT-4 API.

🔗You can access my [**Google Colab file here**](https://colab.research.google.com/drive/1Z59S89qWHEcy4JcqqSZRKXbzT_lrhM90?usp=sharing).

```c
# STEP 1: Install required packages
!pip install openai pandas openpyxl --quiet

# STEP 2: Upload your Excel or CSV file
from google.colab import files
import pandas as pd

# Upload file manually
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

# Load into DataFrame (auto-detect format)
if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
else:
    df = pd.read_excel(file_name)

df.head()

# STEP 3: Authenticate with OpenAI
import openai
from openai import OpenAI
import getpass

api_key = getpass.getpass("🔐 Enter your OpenAI API key: ")
client = OpenAI(api_key=api_key)

# STEP 4: Extract 12–15 key themes from comments using GPT-4
sample_comments = df["Comment"].tolist()

prompt = (
    "Here are open-ended customer feedback comments:\n\n" +
    "\n".join(f"- {c}" for c in sample_comments) +
    "\n\nPlease extract 12 to 15 concise, professional themes that reflect the key topics customers are discussing. "
    "Take into account the current economic climate (e.g., pricing sensitivity, value, speed, ethics). "
    "Return only a clean bullet list of theme names."
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3
)

themes_text = response.choices[0].message.content
print("🎯 Extracted Themes:\n", themes_text)

# STEP 5: Convert extracted bullet list to Python list
theme_list = [t.strip("- ").strip() for t in themes_text.split("\n") if t.strip()]
print("✅ Parsed Themes:", theme_list)

# STEP 6: Tag each comment with the best-matching theme using GPT-4
from tqdm import tqdm
tqdm.pandas()

def tag_comment(comment, theme_list):
    prompt = (
        f"Choose the most appropriate theme from the list for the following survey comment:\n\n"
        f"Comment: \"{comment}\"\n\n"
        f"Available themes:\n" + "\n".join(f"- {t}" for t in theme_list) +
        "\n\nReturn only the best-matching theme."
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

# Apply with progress bar
df["Theme"] = df["Comment"].progress_apply(lambda c: tag_comment(c, theme_list))

# STEP 7: Tag each comment with sentiment score using GPT-4
def score_sentiment(comment):
    prompt = (
        f"On a scale from 1 to 5, rate the sentiment of the following comment:\n\n"
        f"Comment: \"{comment}\"\n\n"
        f"Use this scale:\n"
        f"1 = Very Negative\n"
        f"2 = Negative\n"
        f"3 = Neutral\n"
        f"4 = Positive\n"
        f"5 = Very Positive\n\n"
        f"Return only the number (1 to 5)."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return int(response.choices[0].message.content.strip())
    except Exception as e:
        return None

df["SentimentScore"] = df["Comment"].progress_apply(score_sentiment)

# STEP 8: Download the tagged file
output_file = "tagged_survey_comments.csv"
df.to_csv(output_file, index=False)

from google.colab import files
files.download(output_file)
```

The workflow is as follows:

- Load the input file (CSV or Excel) containing open-ended comments.
- Send the full list of comments to GPT-4 to extract a list of 12–15 themes.
- For each comment, use GPT-4 to assign the most relevant theme from the extracted list.
- For each comment, request a sentiment score from GPT-4 based on a 5-point scale.
- Save the final dataset — including the original comment, theme, and sentiment score — as a CSV file for analysis in Power BI.

Here is what my CSV output looked like:

![](99.System/Attachments/1!kuvYQBlln74Ob7hZHiVI8g.png.webp)

CSV Output From Python Script

This output is GOLD. There are so many visualizations we can easily do in Power BI with it using some simple DAX and Power BI’s native visuals.

### Part 2: Building the Power BI Dashboard

Once the enriched dataset was exported from Python, I loaded it into Power BI to build an interactive dashboard that enables both high-level summaries and deep dives into individual comments.

### 1 — Theme Overview

![](99.System/Attachments/1!PF9Pe1R2C2tXBoE8yeKqbA.png.webp)

Theme Overview in Power BI

The **Theme Overview** table groups all comments by their assigned theme and displays both the number of responses and the average sentiment score for each. The sentiment score is calculated using a simple DAX measure:

```c
Sentiment score = AVERAGE(Comments[SentimentScore])
```

To make the scores easier to interpret, a second measure classifies them into categories using tiered thresholds and a `SWITCH` statement:

```c
Sentiment value = 
    SWITCH(
        TRUE(),
        [Sentiment score] > 4, REPT(UNICHAR(8203),5) & "Positive",
        [Sentiment score] > 3.2, REPT(UNICHAR(8203),4) & "Slightly Positive",
        [Sentiment score] > 2.8, REPT(UNICHAR(8203),3) & "Neutral",
        [Sentiment score] > 1.5, REPT(UNICHAR(8203),2) & "Slightly Negative",
        REPT(UNICHAR(8203),1) & "Negative"
    )
```

This logic allows for a more nuanced interpretation of sentiment beyond just positive/neutral/negative. The use of `REPT(UNICHAR(8203), n)` (a zero-width space repeated `n` times) is a Power BI trick that enables sorting by sentiment severity without displaying a numeric value—ensuring categories are ordered logically in visuals.

If you would like to learn more about this trick, you can view my article on this topic [**here**](https://medium.com/microsoft-power-bi/power-bi-elevating-data-visualization-with-custom-measure-sorting-b368fd382917):

## [Power BI: Elevating Data Visualization with Custom Measure Sorting](https://medium.com/microsoft-power-bi/power-bi-elevating-data-visualization-with-custom-measure-sorting-b368fd382917?source=post_page-----ea0ca35ff98b---------------------------------------)

### How to Implement Custom Sorting for Measures in a Power BI Visualization Table

medium.com

To the right of the Theme Overview, I included a few summary stats:

- Total number of comments
- Percentage of comments classified as positive
- Total number of unique themes identified by GPT-4

Together, these elements provide a quick but rich overview of the data that was processed from the survey file and enhance the report’s ability to surface insights at a glance.

### 2 — Sentiment Distribution and Theme Breakdown

![](99.System/Attachments/1!mpLLqlRzdpDtwe4to08dKg.png.webp)

Sentime Distribution and Theme Breakdown

To give users a high-level sense of sentiment balance, I created a **donut chart** that shows the breakdown of positive, neutral, and negative comments across all themes. Directly underneath, the **Theme Analysis** bar chart compares sentiment distribution per theme. This makes it easy to spot which themes are skewing negative (e.g., “Speed and Timeliness of Service”) and which are receiving more favorable feedback.

### 3 — Trend Analysis Over Time

![](99.System/Attachments/1!-p_9YIQ2QREkcVxlZFKe0A.png.webp)

Trend Analysis for Product Quality and Reliability in Power BI

The **Trend Analysis** chart tracks either the average sentiment or the number of comments over time, depending on the selected view. This lets users assess how feedback evolved month to month. For example, if the sentiment for “Product Quality and Reliability” dipped in November, that could prompt a deeper operational review.

### 4 — Search and Cross-Filtering

![](99.System/Attachments/1!4c5EcA6LDUUHhOyNNKao8Q.png.webp)

Cross-Filtering in Power BI

All visuals in the report are interactive. When a user clicks on a specific theme, all components on the page respond:

- The donut and bar charts update to reflect sentiment just for that theme.
- The trend line shows how that theme’s sentiment changed over time.
- The detailed comment table below is filtered to show only relevant responses.

Users can also type into the **search bar** at the top to filter themes dynamically. Typing a keyword like “product” will return any themes containing that term, update all associated visuals, and allow users to drill into specific areas of interest.

![](99.System/Attachments/1!YDoWGStyXr2bZzmKvpFHoQ.png.webp)

Text Search in Power BI

### 5 — Detailed Answers Table

![](99.System/Attachments/1!04lOe7hZT2A4bAvBr0GlYA.png.webp)

Detailed Answers Table

Finally, I included a **detailed table** at the bottom that shows each individual comment, its assigned theme, sentiment classification, and timestamp. A simple conditional format was added to show sentiment using color-coded icons using SVG.

If you would like to learn more about using SVGs in Power BI, here’s my article on the topic:

## [Step Up Your Power BI Game With SVGs 🔥](https://medium.com/the-bi-corner/step-up-your-power-bi-game-with-svgs-e0e255c1316d?source=post_page-----ea0ca35ff98b---------------------------------------)

### Building a Crypto Market Watch Dashboard in Power BI Using SVGs

medium.com

This view is especially useful for:

- Quality assurance (e.g., spot-checking tagging)
- Copy/pasting actual quotes into reports
- Identifying frequent wording patterns under specific themes
- Exporting to analyze in Excel 😅

### Wrapping Up

As you can see from this approach, I used other tools beyond Power BI to develop the end product. Power BI is amazing on it’s own, but I think it’s important to not shy away from other tools and platforms. Their synergy can really deliver game changing results at a fast speed.

Another consideration is cost — here I used the ChatGPT API. To run these survey comments in total it cost me 2.99 USD. So this approach was not free — but imagine the human time it would have taken to get something close to this result if themes were manually identified and tagged (without considering potential mistakes made in the process!).

**👉As promised,** [**here**](https://drive.google.com/file/d/1FCKWTT8KXWqYKSmPOLgIfZwpwy9ELnix/view?usp=sharing) **’s the PBIX file with the example visuals and tricks mentioned above.**

Enjoy using Python with Power BI? Here is one of my recent articles on how you can use Python directly in Power BI.

## [💡 My Favorite Way to Forecast in Power BI](https://medium.com/the-bi-corner/my-favorite-way-to-forecast-in-power-bi-634d1221df24?source=post_page-----ea0ca35ff98b---------------------------------------)

### How I used Power Query and Python to build a reusable, customizable forecasting model — no Premium needed

medium.com

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)