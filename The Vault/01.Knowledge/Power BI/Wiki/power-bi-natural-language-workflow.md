---
created: 2026-07-27
updated: 2026-08-02
source: "Natural Language Analytics: Instant Dashboard Answers"
note_type: workflow
tags: [power-bi, natural-language, q-and-a, smart-narrative, synonyms, copilot]
---

# Power BI Natural Language Workflow

Step-by-step guide for setting up and using Q&A visual, Smart Narrative, and Copilot in Power BI reports.

## Q&A Visual Setup

### 1. Prepare the Semantic Model

Q&A uses synonyms to map business terms to model objects. Good synonym coverage = accurate question interpretation.

1. Open the semantic model in Power BI Service
2. Navigate to Model > Manage > Synonyms
3. For each business term, map it to the correct table/column

| Business Term | Model Object | Alternative Terms |
|--------------|-------------|-----------------|
| Revenue | Sales[RevenueAmount] | Sales, Total Sales, Income |
| Customer Count | Customers[CustomerKey] | Customers, # Customers, Unique Customers |
| Year | Calendar[Year] | Fiscal Year, CY, Year |
| Product Category | Products[Category] | Category, Product Type |

### 2. Configure Q&A Visual Defaults

1. Click the Q&A visual
2. Set **Suggested questions** for common starting points
3. Set **Default visual type** (table, card, column chart)
4. Set **Restrict to certain models** if multiple models exist

### 3. Common Q&A Questions and Expected DAX

```
"Total revenue by product category"
-> SUM(Sales[RevenueAmount]) GROUP BY Products[Category]

"Revenue vs last year"
-> [Total Revenue] vs SAMEPERIODLASTYEAR measure

"Top 5 customers by sales"
-> TOPN(5, Customers, [Total Revenue], DESC)
```

## Smart Narrative Setup

### 1. Add Smart Narrative Visual

1. Insert > Smart Narrative
2. Drag fields onto the visual
3. The narrative updates with each visual refresh

### 2. Customize the Narrative Template

1. Click the narrative visual > Format pane
2. Set Narrative tone: formal, casual, executive
3. Set which metrics to include in the summary
4. Add custom narrative phrases

## Copilot for DAX Generation

```
Prompt examples:
"Create a measure for gross margin %"
"Build a visual showing revenue by region for this year"
"Add a KPI card for customer count"
```

## Limitations

| Tool | Limitation |
|------|------------|
| Q&A | Requires good synonyms; complex multi-step questions fail |
| Smart Narrative | Updates only on visual refresh; not real-time |
| Copilot | Requires Pro/Premium; edit permissions on workspace |

## Related

- [[ai-copilot-power-bi-workflow]]
