---
created: 2026-08-01
updated: 2026-08-02
source: "Natural Language Analytics Instant Dashboard Answers.md"
note_type: atomic
tags: [power-bi, natural-language, nla, nlp, ai, beginner]
---

# How Natural Language Analytics Works: 4-Step Pipeline

The user experience is simple — type a question, get an answer. Under the hood, four stages convert plain English into a formatted insight.

## Step 1: Understanding the Question (NLP Parsing)

Natural Language Processing analyses what you typed to identify:
- **The metric**: what you want to measure (revenue, churn rate, conversion)
- **The time frame**: when (last quarter, this month, YTD)
- **The dimension**: how to slice it (by region, product, channel)

**Example:** "Show quarterly revenue by region" → Metric: revenue, Time frame: quarterly, Dimension: region.

NLP handles free-form phrasing: "how did we do in the northeast" and "revenue northeast last quarter" both map to the same components.

## Step 2: Mapping to Real Data (Schema Translation)

The system translates the parsed question into an actual query against the data source — matching your phrasing to correct field names, table relationships, and the underlying schema.

You don't need to know column names, table structure, or SQL. The translation layer handles it.

This is also where **synonym handling** kicks in: "revenue" and "sales" both map to the same field if the model has been set up with synonyms.

## Step 3: Running the Analysis

The platform retrieves the data and performs the required operation:
- Aggregating totals (sum, average, count)
- Comparing periods (this quarter vs last quarter)
- Calculating trends (month-over-month growth)
- Measuring variance against a target

## Step 4: Delivering the Answer (Automated Formatting)

Results are returned in the format that best fits the question:
- **Chart**: when a visual comparison makes sense
- **KPI card**: for a single metric vs a target
- **Table**: when detail rows are needed
- **Plain-language explanation**: AI-generated summary of what the data shows and why it's notable

The system picks the format automatically rather than always returning a raw table.

## Related

- [[nla-vs-nlq-distinction]] — NLQ vs NLA depth of capability
- [[natural-language-analytics-platform-capabilities]] — capabilities that separate real NLA from keyword matching
- [[bold-bi-ai-features]] — how Bold BI implements this pipeline
