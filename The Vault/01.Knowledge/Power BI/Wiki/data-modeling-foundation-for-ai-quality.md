---
created: 2026-07-29
updated: 2026-08-02
source: AI in Power BI (2025) — Full Tutorial (Tejwani)
note_type: atomic
tags: [data-modeling, ai, copilot, quality, star-schema]
---

# Data Modeling Is the Foundation for AI Quality

AI features in Power BI — Copilot, Q&A, Key Influencers — read your data model directly. Garbage column names and poor relationships produce garbage AI outputs.

## Definition

AI quality in Power BI is a function of data model quality. Clean, human-readable table and column names, a proper star schema, and explicit relationships are prerequisites — not nice-to-haves.

## Key Points

- AI reads **column names as vocabulary**. "Total Revenue" is interpretable; "Rev_Amt_Sum" is not
- **Star schema** (fact + dimensions) gives AI clear paths to follow through the model
- **Plain-English naming** is the interface between the analyst and the AI
- **Dedicated date table** is required for time intelligence and forecasting to work correctly
- A properly modelled semantic layer is the AI's only window into the data — there is no second chance

## Examples

**Poor model:**
```
tbl_tx_001 | col_rev_amt_sum | fk_date_001 | tbl_str_23
```

**Good model:**
```
Sales | Total Revenue | OrderDate | Store
```

Copilot working with the good model can answer: *"Why did total revenue drop at Store 23 in March?"* — using the actual column names as semantic anchors.

## Related

- [[build-ai-powered-power-bi-dashboard]] — workflow
- [[power-bi-ai-feature-comparison]] — reference
- [[garbage-in-garbage-out]] — Diepeveen 2022 gotcha
