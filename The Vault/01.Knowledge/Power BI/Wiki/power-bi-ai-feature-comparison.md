---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: reference
tags: [ai, copilot, key-influencers, qa-visual, anomaly-detection, smart-narratives, python]
---

# Power BI AI Feature Comparison

Quick reference for the six core AI features in Power BI — what each does, when to use it, and what it requires.

## Quick Reference

| Feature | License | Input | Output | Best For |
|---------|---------|-------|--------|---------|
| Copilot | Premium/PPU | Natural language | DAX, visuals, hypotheses | Root-cause analysis, ad-hoc questions |
| Q&A Visual | Pro+ | Natural language | Auto-generated visuals | Self-service for non-technical users |
| Key Influencers | Premium/PPU | Metric + dimensions | Rankings + explanations | Discovering what drives a metric |
| Anomaly Detection | Pro+ | Time-series visual | Flagged outliers + attribution | Monitoring KPIs with seasonal variation |
| Smart Narratives | Pro+ | Any visual | Text summary | Executive one-pagers, report annotations |
| Python Visual | Pro+ | Dataset | Custom visuals, ML predictions | Forecasting, custom analytics |

## Feature Details

### Copilot

- Reads table and column names directly
- Generates DAX measures, creates visuals, runs cross-table analysis
- Requires plain-English naming convention
- Best for: "Why did sales drop 18% last month?"

### Q&A Visual

- Free-text search box on the dashboard
- Interprets business language → data model fields
- Teaches over time via synonym additions
- Best for: Non-technical users getting instant answers

### Key Influencers

- Runs regression analysis across specified dimensions
- Shows ranked factors driving a metric
- Output: "Sales are 2.3× higher when PromotionActive = Yes"
- Best for: Discovering hidden drivers not in existing reports

### Anomaly Detection

- Built into line chart via Analytics pane
- SR-CNN (Spectral Residual + Convolutional Neural Network) algorithm
- Sensitivity 70–80% is a good starting point
- Best for: KPI monitoring with known seasonal patterns

### Smart Narratives

- Generates natural-language summaries of any visual
- Updates dynamically with slicer/filter selections
- Best for: Annotating visuals on executive dashboards

### Python Visual

- Runs Python (pandas, scikit-learn) inside Power BI
- Data passed via `dataset` variable
- Supports any matplotlib visualisation or ML model
- Best for: Custom forecasting, advanced analytics not in native visuals

## License Requirements Summary

| Feature | Free | Pro | Premium/PPU |
|---------|------|-----|-------------|
| Copilot | ✗ | ✗ | ✓ |
| Q&A Visual | ✗ | ✓ | ✓ |
| Key Influencers | ✗ | ✗ | ✓ |
| Anomaly Detection | ✗ | ✓ | ✓ |
| Smart Narratives | ✗ | ✓ | ✓ |
| Python Visual | ✗ | ✓ | ✓ |

## When to Use Each

- **Ad-hoc root-cause question** → Copilot
- **Non-technical user self-service** → Q&A Visual
- **Discovering what drives a metric** → Key Influencers
- **Monitoring a KPI over time** → Anomaly Detection
- **Annotating an executive visual** → Smart Narratives
- **Predictive or custom analytics** → Python Visual

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[ai-shows-correlations-not-causations]] — gotcha
- [[python-forecasting-in-power-bi-sklearn]] — pattern
