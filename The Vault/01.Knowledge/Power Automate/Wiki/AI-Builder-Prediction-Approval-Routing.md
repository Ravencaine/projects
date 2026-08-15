---
created: 2026-08-10
updated: 2026-08-10
source: Build a Smart Approval System with Prediction Model in Power Automate
source_url: https://medium.com/@tamilarasu-arunachalam/smart-approval-system-with-prediction-model-in-power-automate-e6ec7995d50b
note_type: workflow
tags: [power-automate, ai-builder, prediction, approval, dataverse, automation, confidence-threshold]
---

# AI Builder Prediction Approval Flow

Combine AI Builder prediction models with Power Automate to automate conditional approval routing based on prediction confidence scores.

## Architecture

```
New ApprovalRequest (Dataverse)
    → AI Builder Predict action
    → Confidence Score branch:
          > 0.7  → Auto-approve
          0.4–0.7 → Send to manager
          < 0.4  → Escalate to senior manager
```

## Prerequisites

1. **Dataverse table** — e.g. `ApprovalRequests` with fields: `Amount`, `Department`, `Priority`, `Request Type`, `AI Decision`
2. **AI Builder prediction model** — trained on historical outcomes table
   - Select Dataverse table as data source
   - Select target column (e.g. `AI Decision`)
   - Select features: `Amount`, `Department`, `Priority`, `Request Type`
   - Train and publish before using in flow
3. **AI Builder license** — required for Predict action

## Trigger

Dataverse trigger: **When a row is added** on `ApprovalRequests` table

## AI Builder Action

Power Automate action: **Predict** — select the trained/published model, map inputs from trigger outputs.

## Confidence Threshold Routing

| Confidence | Action | Power Automate Step |
|------------|--------|-------------------|
| > 0.7 | Auto-approve | Condition: `predictionResult > 0.7` → Approve |
| 0.4–0.7 | Manager approval | Condition: `predictionResult >= 0.4 && <= 0.7` → Send approval request |
| < 0.4 | Senior manager escalation | Condition: `predictionResult < 0.4` → Escalate |

## Implementation Notes

- AI Builder model must be **published** before the flow can use it
- The **Predict** action in Power Automate maps trigger outputs to model input columns
- Prediction outcome includes both the predicted label and a confidence score
- This is a prototype pattern — extend by adding error handling, logging, and email notifications

## References

- [Use predict action in Power Automate — AI Builder | Microsoft Learn](https://learn.microsoft.com/en-us/ai-builder/predict-action-pwr-automate)
- [A simple predictive AI Builder model in Power Automate — ExcelTown](https://exceltown.com/en/tutorials/power-automate/a-simple-predictive-ai-builder-model-in-power-automate/)

## Related

- [[Power-Automate-Flow-Design-Principles]] — flow design guidance
- [[Failed-Flow-Monitoring-Alerting]] — monitoring for flow failures
