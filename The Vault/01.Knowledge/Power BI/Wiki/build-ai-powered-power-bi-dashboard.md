---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: workflow
tags: [ai, copilot, python, power-bi, machine-learning]
---

# Build an AI-Powered Power BI Dashboard

A 4-phase workflow for building an AI-first Power BI dashboard using Copilot, Q&A, Key Influencers, anomaly detection, Smart Narratives, and Python ML integration.

## Prerequisites

- Power BI Desktop (latest version — November 2025 or later)
- Power BI Premium or Premium Per User (PPU) license — required for Copilot, Q&A, Key Influencers
- 30-day PPU trial available at app.powerbi.com
- A dataset with clean star-schema data model
- 2–3 hours of focused time

## Phase 1: Set Up AI-Enabled Power BI Environment

### Step 1 — Enable AI Features

1. Open Power BI Desktop
2. File → Options and Settings → Options
3. Preview Features → Enable all AI-related features
4. Restart Power BI Desktop
5. Copilot pane appears on the right side

> **Note:** Copilot and most AI features require Premium/PPU. Free Pro licenses have limited access.

### Step 2 — Verify License (Power BI Service)

1. Sign in at app.powerbi.com
2. Confirm workspace is assigned to Premium or PPU capacity
3. Publish report to that workspace

## Phase 2: Data Preparation for AI Analysis

### Step 3 — Import and Model Data

1. Import data (SQL Server, Excel, CSV, SharePoint, etc.)
2. Open Model View
3. Create star-schema layout: fact table + dimension tables
4. Name tables and columns in plain English (e.g., "Total Revenue", not "Rev_Amt_Sum")
5. Remove special characters from names — AI tools read column names directly

### Step 4 — Create Dedicated Date Table

Create a date table using DAX. This is required for time intelligence and AI forecasting features:

```dax
DateTable = CALENDAR(MIN(Sales[OrderDate]), MAX(Sales[OrderDate]))
```

Add calculated columns as needed: Year, Month, Quarter, Day of Week.

### Step 5 — Establish Relationships

In Model View, create one-to-many relationships from dimension tables to the fact table. Clear, unambiguous relationships improve AI feature accuracy.

## Phase 3: Implement Power BI AI Features

Stack multiple AI features on a single dashboard for maximum coverage.

### Feature 1 — Copilot Integration

1. Click the Copilot icon in the ribbon
2. Start with simple questions: "Show me total sales by month"
3. Graduate to complex: "Why did sales drop in March?"
4. Be specific: "Create a line chart showing total sales by month for 2024 and 2025" works better than "show sales"

> Copilot generates DAX, creates visuals, and cross-references tables. Works best with clean model names.

### Feature 2 — Q&A Visual

1. Insert → Q&A visual (search-box visual)
2. Test: type "top products by revenue"
3. Customise: Settings → Teach Q&A → Add synonyms for industry terms
4. Add featured questions for common queries
5. Review failed Q&A interpretations and correct them over time

**Synonym example:** Add "revenue" → "sales", "income", "earnings"

### Feature 3 — Key Influencers Visual

1. Visualizations → Key Influencers icon
2. Set "Analyze" to the primary metric (e.g., Sales Revenue)
3. Set "Explain by" to relevant dimensions (Store Location, Product Category, Promotion Active, Employee Count)
4. Let AI analyze (5–10 seconds)
5. Explore the AI-generated explanations

**Output:** Rankings like "Sales are 2.3× higher when PromotionActive = Yes"

### Feature 4 — Anomaly Detection

1. Select a line chart visual (e.g., sales over time)
2. Format → Analytics → Enable "Anomaly detection"
3. Set sensitivity (70–80% is a good starting point)
4. AI automatically flags unusual data points with explanations

### Feature 5 — Smart Narratives

1. Insert → Smart Narrative
2. Automatically generates text summaries of visuals
3. Updates dynamically when filters change
4. Useful for executive one-pagers

### Feature 6 — Python Visual for Predictive Analytics

Enable Python scripting, add a Python visual, and write forecasting code. See [[python-forecasting-in-power-bi-sklearn]] for the full pattern.

## Phase 4: Deploy and Govern

### Step 6 — Publish to Power BI Service

1. Publish to a Premium/PPU workspace
2. Configure row-level security (RLS) if needed
3. Set up scheduled refresh for the dataset

### Step 7 — Set Up Automated Alerts

1. In Power BI Service, pin the dashboard
2. Enable alerts on anomaly detection and threshold-crossing metrics
3. Configure email or Teams notifications

### Step 8 — Document and Iterate

Create an "AI Insights Log" page in the report:

| Date | AI Insight | Action Taken | Result |
|------|-----------|--------------|--------|
| YYYY-MM-DD | Insight description | What was done | Outcome |

This builds trust in AI recommendations over time.

## Common Errors

- **Copilot gives wrong answers** → Clean up table/column names; check relationships
- **Q&A misinterprets questions** → Add synonyms via Teach Q&A
- **Key Influencers shows meaningless correlations** → Validate with domain knowledge (see [[ai-shows-correlations-not-causations]])
- **Python visual fails to run** → Enable Python scripting in Options → Preview Features

## Related

- [[ai-shows-correlations-not-causations]] — gotcha
- [[copilot-requires-premium-licensing]] — gotcha
- [[data-modeling-foundation-for-ai-quality]] — atomic
- [[python-forecasting-in-power-bi-sklearn]] — pattern
- [[power-bi-ai-feature-comparison]] — reference
