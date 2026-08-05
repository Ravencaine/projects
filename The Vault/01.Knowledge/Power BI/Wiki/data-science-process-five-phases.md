---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [data-science-process, crisp-dm, phases, use-case, data, feature-engineering, model, integration]
---

# Data Science Process — Five Phases

The data science process is non-linear and iterative: use case → data → preparation → model → integration.

## Definition

A structured approach to building and deploying AI/ML solutions, typically framed as five phases that iterate:

1. **Define the Use Case**: what question are you answering? What does success look like?
2. **Acquire Data**: collect, connect, or pipeline data from source systems
3. **Prepare Data**: clean, transform, engineer features
4. **Train the Model**: select algorithm, train, evaluate
5. **Integrate the Model**: deploy to an endpoint and consume in an application or report

## Key Points

- The process is **non-linear**: expect to loop back from any phase
- Phase 1 (use case) is critical: a vague problem produces a useless model
- Azure ML and Power BI support each phase: data connectors (phase 2), Power Query + AI Insights (phase 3), AutoML/Designer (phase 4), endpoints (phase 5)
- Evaluation metrics must be defined *before* training — "how good is good enough?"

## Examples

- Tourism forecasting use case: predict monthly visitors → connect tourism CSV → Power Query clean → AutoML train → deploy ACI endpoint → Power BI score column
- Telecom churn: identify at-risk customers → customer data pipeline → feature engineering (tenure, usage) → classification model → Power BI score column

## Related

- [[feature-engineering-versus-selection-versus-importance]]
- [[automl-overview]]
- [[azure-ml-realtime-inference-pipeline]]
