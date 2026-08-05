---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: snippet
tags: [ai, setup, copilot, checklist, power-bi-desktop, premium]
---

# AI Feature Setup Checklist (Power BI Desktop)

Pre-flight checklist before enabling any AI feature in a new Power BI project.

## Code / Steps

### Step 1 — Update Power BI Desktop

- Download the latest version from microsoft.com/powerbi
- Requires November 2025 release or later for full Copilot support

### Step 2 — Enable Preview Features

```
File → Options and Settings → Options → Preview Features
```
Enable:
- [ ] Copilot
- [ ] Python scripting
- [ ] Anomaly Detection (usually on by default)

### Step 3 — Restart Power BI Desktop

Required for preview features to activate.

### Step 4 — Verify Python Runtime (if using Python Visual)

```
File → Options and Settings → Python scripting
```
Confirm:
- Python home directory is set
- Required packages installed: `pandas`, `scikit-learn`, `numpy`, `matplotlib`

### Step 5 — Verify Premium / PPU License (before publishing)

In Power BI Service:
- Workspace → Settings → Premium capacity
- Confirm assigned to Premium or PPU (required for Copilot, Key Influencers)

### Step 6 — Check Data Model Quality

Before adding AI features, confirm:
- [ ] Star schema: fact table + dimension tables
- [ ] Table names in plain English
- [ ] Column names descriptive (no special characters)
- [ ] Relationships established in Model View
- [ ] Date table created and marked as date table

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[power-bi-ai-feature-comparison]] — reference
- [[data-modeling-foundation-for-ai-quality]] — atomic
