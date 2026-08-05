---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: gotcha
tags: [copilot, licensing, premium, power-bi, ai]
---

# Copilot Requires Premium Licensing

Copilot in Power BI is gated behind Power BI Premium or Premium Per User (PPU). A standard Pro license will not enable it.

## Expected Behaviour

You enable Copilot in Power BI Desktop (File → Options → Preview Features → Copilot), expecting it to work.

## Actual Behaviour

The Copilot pane may appear but returns errors, or the Copilot button is greyed out. The feature is only functional when the report is published to a workspace assigned to a Premium capacity (P1–P3) or PPU license.

## Why It Happens

Microsoft tiers AI features by license level:

| Feature | Free | Pro | Premium/PPU |
|---------|------|-----|-------------|
| Copilot | ✗ | ✗ | ✓ |
| Key Influencers | ✗ | ✗ | ✓ |
| Q&A Visual | ✗ | ✓ | ✓ |
| Anomaly Detection | ✗ | ✓ | ✓ |
| Smart Narratives | ✗ | ✓ | ✓ |
| Python Visual | ✗ | ✓ | ✓ |

Copilot is the most resource-intensive AI feature and is reserved for Premium capacities.

## How to Handle It

1. **Check your license:** Power BI Service → Workspace settings → Premium capacity status
2. **Start a PPU trial:** 60-day free trial at app.powerbi.com — assign to a workspace
3. **Scope the feature:** If budget is a concern, use Q&A Visual + Anomaly Detection (Pro-licensed) instead
4. **Communicate to clients:** Present the ROI of Copilot vs. licensing cost before scoping it into a project
5. **Use 30-day trial for evaluation:** Power BI Premium trial gives 30 days of full access

## Related

- [[power-bi-ai-feature-comparison]] — reference
- [[build-ai-powered-power-bi-dashboard]] — workflow
