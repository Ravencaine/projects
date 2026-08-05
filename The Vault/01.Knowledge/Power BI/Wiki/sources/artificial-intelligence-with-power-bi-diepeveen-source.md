---
created: 2026-07-28
source: Artificial Intelligence with Power BI
source_url:
note_type: source
tags: [power-bi, artificial-intelligence, machine-learning, deep-learning, forecasting, anomaly-detection, cognitive-services, nlu, computer-vision, automl, responsible-ai]
---

# Artificial Intelligence with Power BI (Diepeveen)

Technical guide covering AI capabilities within Microsoft Power BI — from out-of-the-box features to custom model training.

> **Type:** book
> **Author:** Mary-Jo Diepeveen
> **Published:** 2022
> **Publisher:** Packt Publishing
> **Routed to:** Power BI

## Summary

A practical guide for data analysts who want to integrate AI into Power BI reports without a data science background. Covers the full spectrum: exploratory data analysis, built-in AI visuals (forecasting, anomaly detection, Q&A), Azure Cognitive Services integration (text analytics, computer vision), custom model training via Azure ML AutoML and Designer, and responsible AI principles. The book emphasises understanding what each AI feature does internally — not just clicking buttons.

## Key Claims

- Power BI democratises AI: citizen data scientists can use pretrained models without writing code
- Understanding the algorithm behind an AI feature is essential for knowing when NOT to use it
- Data quality and representativeness are prerequisites for reliable AI output — garbage in, garbage out
- The five-phase data science process (use case → data → preparation → model → integration) is non-linear and iterative
- AI features in Power BI sit on a trade-off spectrum: out-of-the-box speed versus custom model control
- Responsible AI requires examining privacy, transparency, fairness, and bias at every stage

## Book Structure

| Part | Chapters | Focus |
|------|---------|-------|
| Part 1: AI Fundamentals | 1–3 | AI concepts, EDA, data preparation |
| Part 2: Out-of-the-Box AI | 4–10 | Forecasting, anomaly detection, Q&A visual, Cognitive Services, NLU, CV, Q&A app |
| Part 3: Create Your Own Models | 11–13 | AutoML, Azure ML Designer, Responsible AI |

## Notable Details

- Tourism data (Netherlands monthly visitors) is the recurring dataset used across forecasting, anomaly detection, and AutoML chapters
- World Happiness Report (2018–2020) is used for EDA and Azure ML Designer regression examples
- Hotel reviews dataset used for text analytics and Word Cloud examples
- Clothing images dataset used for Custom Vision + image reel visualisation
- All sample datasets hosted on GitHub: `github.com/PacktPublishing/Artificial-Intelligence-with-Power-BI`
- Azure Cognitive Services requires an Azure subscription; Power BI Premium capacity is required for AI Insights in the service
- Custom Vision published model requires a prediction key and endpoint for Power BI integration
- AutoML in Azure ML supports Regression, Classification, and Time-Series Forecasting tasks

## Extracted Notes

Links to notes derived from this source:

- [[ai-as-umbrella-term]] — `atomic` — AI ⊇ ML ⊇ DL hierarchy
- [[machine-learning-algorithm-plus-data-equals-model]] — `atomic` — ML core concept
- [[deep-learning-artificial-neural-networks]] — `atomic` — DL explanation
- [[supervised-versus-unsupervised-learning]] — `atomic` — two fundamental ML paradigms
- [[regression-classification-clustering]] — `atomic` — three core ML task types
- [[data-science-process-five-phases]] — `atomic` — CRISP-DM / five-phase process
- [[data-analyst-responsibilities-ai-workflow]] — `atomic` — analyst role definition
- [[out-of-box-versus-custom-model-tradeoff]] — `atomic` — trade-off spectrum
- [[ai-democratisation-power-bi]] — `atomic` — why AI in Power BI matters
- [[exploratory-data-analysis-eda-workflow]] — `workflow` — EDA steps in Power BI
- [[data-profiling-column-quality-distribution-profile]] — `workflow` — three profiling tools
- [[column-profiling-default-1000-row-cap]] — `gotcha` — default cap misses real issues
- [[summary-statistics-power-bi]] — `atomic` — min/max/mean/median/count/distinct/unique
- [[high-cardinality-features-antipattern]] — `atomic` — model不喜欢高基数
- [[data-storytelling]] — `atomic` — humans need narrative not data
- [[line-chart-visual]] — `function` — Power BI line chart
- [[histogram-visual]] — `function` — histogram in Power BI
- [[histogram-versus-bar-chart]] — `pattern` — numerical vs categorical distinction
- [[scatter-plot-visual]] — `function` — scatter plot
- [[scatter-plot-trend-line-correlation]] — `pattern` — detecting correlations
- [[correlation-does-not-imply-causation]] — `gotcha` — critical caveat
- [[matplotlib-histogram-python-visual]] — `pattern` — histogram via matplotlib
- [[matplotlib-box-plot-python-visual]] — `pattern` — box plot via matplotlib
- [[box-plot-visual]] — `function` — box plot in Power BI
- [[box-plot-anatomy]] — `atomic` — min, Q1, mean, median, Q3, max, whiskers
- [[distribution-shapes-normal-right-skewed-left-skewed]] — `atomic` — three distribution shapes
- [[structured-versus-semi-structured-data]] — `pattern` — tabular vs JSON/NoSQL
- [[fixing-data-structure-pq]] — `pattern` — headers, delimiters, JSON expand
- [[power-query-expand-versus-extract]] — `function` — two key PQ operations
- [[power-query-unpivot-columns]] — `function` — Unpivot Column transform
- [[handling-missing-data-strategies]] — `pattern` — mean/median/mode/impute
- [[mitigating-bias-in-ml-datasets]] — `pattern` — resampling, algorithm choice
- [[bias-not-always-a-problem]] — `gotcha` — bias can be the signal
- [[outlier-detection-box-plot]] — `pattern` — box plot for outliers
- [[outlier-handling-strategies]] — `pattern` — delete vs train to recognise
- [[time-series-data-requirements]] — `atomic` — what forecasting needs
- [[trend-versus-seasonality]] — `atomic` — two time-series components
- [[ets-exponential-smoothing-model]] — `atomic` — Power BI's forecasting algorithm
- [[forecasting-visual-power-bi]] — `function` — line chart + Analytics pane
- [[forecasting-configuration-cheatsheet]] — `reference` — all four options at a glance
- [[forecasting-cannot-predict-unforeseen-events]] — `gotcha` — limitation of out-of-box forecasting
- [[validate-forecast-with-ignore-last]] — `pattern` — using Ignore Last for validation
- [[anomaly-detection-supervised-versus-unsupervised]] — `atomic` — two detection approaches
- [[sr-cnn-spectral-residual-convolutional-neural-network]] — `atomic` — Power BI's anomaly algorithm
- [[anomaly-detection-data-requirements]] — `atomic` — time-series + enough points
- [[anomaly-detection-visual]] — `function` — Find Anomalies in line chart
- [[anomalies-pane-explain-with-attributes]] — `function` — Anomalies pane usage
- [[anomaly-correlations-require-domain-expertise]] — `gotcha` — correlations need validation
- [[natural-language-processing-data-exploration]] — `atomic` — NLP for DBQA
- [[semantic-matching-qa-visual]] — `atomic` — how Q&A maps words to fields
- [[qa-visual-power-bi]] — `function` — Q&A visual setup
- [[qa-best-practices]] — `pattern` — column names, types, categories, relationships
- [[qa-field-synonyms]] — `pattern` — add/exclude terms for Q&A
- [[qa-review-questions-feedback-loop]] — `pattern` — review asked questions
- [[qa-feedback-thumbs-down]] — `pattern` — end-user correction workflow
- [[language-model-improves-over-time]] — `atomic` — child-learning analogy
- [[qa-underline-states]] — `reference` — single/dashed/wavy = understood/uncertain/unknown
- [[azure-cognitive-services-overview]] — `atomic` — service categories
- [[create-cognitive-services-resource-azure]] — `workflow` — Azure portal setup
- [[language-detection-api]] — `function` — Detect Language
- [[key-phrase-extraction-api]] — `function` — Extract Key Phrases
- [[sentiment-analysis-api]] — `function` — Detect Sentiment
- [[named-entity-recognition-ner]] — `function` — NER for entities
- [[entity-linking]] — `function` — disambiguate entity meanings
- [[pii-detection]] — `function` — flag PII in text
- [[azure-computer-vision-image-description]] — `function` — Describe Image
- [[azure-computer-vision-object-detection]] — `function` — Detect Objects
- [[azure-custom-vision]] — `function` — supervised image classification
- [[custom-vision-workflow]] — `pattern` — create → upload → tag → train → publish
- [[custom-vision-evaluation-metrics]] — `reference` — Precision, Recall, AP
- [[azure-face-api]] — `function` — age, emotion, glasses, hair, mask
- [[ai-insights-text-analytics-power-bi]] — `workflow` — AI Insights button workflow
- [[power-query-custom-function-text-analytics]] — `workflow` — Advanced Editor M function
- [[word-cloud-visual]] — `function` — Word Cloud marketplace visual
- [[word-cloud-configuration]] — `pattern` — stop words, min freq, max words, rotation
- [[privacy-risk-custom-function-public]] — `gotcha` — privacy-level risk with API calls
- [[azure-question-answering-knowledge-base]] — `workflow` — Language Studio Q&A
- [[power-apps-faq-app]] — `workflow` — Power Apps canvas app
- [[power-automate-http-request-qa-endpoint]] — `workflow` — Power Automate HTTP call
- [[power-apps-automate-qa-integration]] — `pattern` — full pipeline wiring
- [[anonymous-image-access-power-bi]] — `pattern` — Azure Blob SAS URL pattern
- [[improving-custom-vision-prediction-feedback]] — `pattern` — retrain from predictions
- [[ai-insights-vision-power-bi]] — `workflow` — AI Insights Vision workflow
- [[azure-blob-storage-sas-image-urls]] — `workflow` — SAS token generation
- [[image-reel-visualisation-matrix]] — `pattern` — matrix visual for images
- [[automl-overview]] — `atomic` — automating FE + model selection
- [[automl-tasks-regression-classification-forecasting]] — `atomic` — three supported tasks
- [[azure-ml-workspace-compute-cluster-dataset]] — `workflow` — Azure ML setup
- [[automl-run-configuration]] — `workflow` — target, horizon, frequency, CV settings
- [[deploy-automl-model-aci-endpoint]] — `workflow` — deploy to ACI
- [[azure-ml-model-integration-power-bi]] — `workflow` — Azure ML in Power BI
- [[azure-ml-designer]] — `atomic` — drag-and-drop ML pipeline
- [[azure-ml-designer-pipeline-components]] — `pattern` — component catalogue
- [[clean-missing-data-replace-median-designer]] — `pattern` — imputation in designer
- [[normalise-data-designer]] — `pattern` — normalisation transform
- [[split-data-train-test-designer]] — `pattern` — 75/25 split with seed
- [[train-evaluate-regression-model-designer]] — `pattern` — regression pipeline
- [[execute-python-script-designer]] — `pattern` — matplotlib scatter plot in designer
- [[azure-ml-realtime-inference-pipeline]] — `workflow` — real-time inference pipeline
- [[deploy-realtime-endpoint-designer]] — `workflow` — ACI deployment from designer
- [[integrate-azure-ml-endpoint-power-bi]] — `workflow` — real-time endpoint in PBI
- [[responsible-ai-six-principles]] — `atomic` — harm, fairness, transparency
- [[remove-pii-from-datasets]] — `pattern` — PII identification and removal
- [[differential-privacy-smartnoise]] — `atomic` — noise injection for privacy
- [[transparent-by-design-algorithms]] — `atomic` — linear models and decision trees
- [[explain-black-box-models]] — `pattern` — SHAP, Mimic, Feature Permutation
- [[feature-importance-aggregate-versus-individual]] — `atomic` — two importance views
- [[fair-models-identify-mitigate-unfairness]] — `pattern` — Fairlearn workflow
- [[fairlearn-toolkit]] — `reference` — fairness assessment reference
- [[automl-evaluation-metrics-cheatsheet]] — `reference` — AUC, AP, TN/FP/FN/TP
- [[batch-versus-realtime-inference]] — `atomic` — two inference patterns
- [[azure-ml-endpoints-aci-versus-aks]] — `atomic` — deployment targets
- [[ml-data-formats-csv-parquet-json]] — `atomic` — supported data formats
- [[feature-engineering-versus-selection-versus-importance]] — `atomic` — three FE concepts
- [[pytorch-deep-learning-framework]] — `reference` — PyTorch reference note
- [[azure-ml-data-orchestration]] — `reference` — Data Factory, Synapse reference
- [[garbage-in-garbage-out]] — `gotcha` — data quality > data quantity
- [[model-accuracy-plateau]] — `gotcha` — more data doesn't always help
- [[world-happiness-dataset-workflow]] — `workflow` — CSV import into Power BI
- [[auto-date-time-power-bi]] — `atomic` — built-in date table feature

## Metadata

| Field | Value |
|-------|-------|
| Source file | artificialintelligencewithpowerbi.pdf |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-28 |
| Word count | ~N (348-page technical book) |
