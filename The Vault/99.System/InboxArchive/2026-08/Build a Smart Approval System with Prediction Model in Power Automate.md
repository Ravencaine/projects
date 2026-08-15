---
title: "Build a Smart Approval System with Prediction Model in Power Automate"
source: "https://medium.com/@tamilarasu-arunachalam/smart-approval-system-with-prediction-model-in-power-automate-e6ec7995d50b"
author:
  - "[[Tamilarasu Arunachalam]]"
published: 2026-06-15
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*RTOXeCd1mjgbEgMl.png)

In this AI era, traditional approvals no longer make sense. Approvals play a major role everywhere, but they often require follow-ups and reminders to get things sorted. To address this, I planned to build a smart approval system using Dataverse, AI Builder, and Power Automate. This is a small prototype, but it can be extended to a larger solution.

The agenda is simple: when a new approval request is created, AI Builder will predict the outcome using a trained model. If the prediction likelihood is greater than 0.7, it will be auto-approved. If it is between 0.4 and 0.7, it will be sent to the manager for approval. If it is less than 0.4, it will be escalated to the senior manager.

To accomplish this, I created a Dataverse table named **ApprovalRequests** with the required fields and data types.

![](https://miro.medium.com/v2/format:webp/1*6XA3-7MnAYdQQwqdol9S4g.png)

Next, navigate to [https://make.powerautomate.com](https://make.powerautomate.com/) and select the **AI Models** menu. From there, choose **Predict future outcomes from historical data** under the Prediction section and create a custom model. Select the table as **ApprovalRequests** and the column as **AI Decision**.

![AI Builder prediction model configuration screen in Power Automate](https://miro.medium.com/v2/format:webp/1*csZ51WUlc0jzrFOvvw8LcQ.png)

AI Builder prediction model configuration screen in Power Automate

On the next page, select the columns **Amount**, **Department**, **Priority**, and **Request Type** from the historical outcomes table.

![AI Builder prediction model configuration screen in Power Automate](https://miro.medium.com/v2/format:webp/1*ZJK-XG0M_m_8AEChBoB1DA.png)

AI Builder prediction model configuration screen in Power Automate

Train the model and publish it so that it can be used in Power Automate. Make sure the model is successfully trained and published.

Then, create an instant flow with the Dataverse trigger **“When a record is added”** for the **ApprovalRequests** table. Add the next action as AI Builder, select the trained model, and map the required inputs from the trigger outputs.

You can refer to the workflow diagram below to implement the Power Automate flow.

![](https://miro.medium.com/v2/format:webp/1*vKmT70O6noC7q8zapKtDiQ.png)

Your flow will be looking like the below screenshot

![Approval flow structure](https://miro.medium.com/v2/format:webp/1*uJUWmR3dMirV33fMxCP7WQ.png)

Approval flow structure

### References

- [Use predict action in Power Automate — AI Builder | Microsoft Learn](https://learn.microsoft.com/en-us/ai-builder/predict-action-pwr-automate)
- [A simple predictive AI Builder model in Power Automate](https://exceltown.com/en/tutorials/power-automate/a-simple-predictive-ai-builder-model-in-power-automate/)

Have a great day!