---
title: "Power Up Your Automation: Triggering Flows with Conditions in Power Automate"
source: "https://medium.com/@michealogbeide19/power-up-your-automation-triggering-flows-with-conditions-in-power-automate-229c1317b1de"
author:
  - "[[Oluwamayowa Ogbeide]]"
published: 2023-05-01
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
Are you ready to discover the secret of triggering a flow based on a condition in Power Automate? Get excited, because we’re about to dive into the thrilling world of automation!

The Steps to achieving this would be

1. Creating an automated Flow

> Navigate to [**https://make.powerautomate.com/**](https://make.powerautomate.com/), Click on **New Flows and select Autmoated cloud flow**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JwJsRXVvFtqow4ZHerURyw.png)

2\. Input a Flow name, Select the trigger (When an item or a file is modified), and create.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*gcxz-RrspsGPcwI0Rqy1OA.png)

3\. Next is to generate an expression that'll be placed in the trigger card settings.

> Click on **New step** and add a **Do until card/action.**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*e_cHatGak_cBX09kbWDrLw.png)

> Input a value, select an expression and a condition value

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mKWuYkP1JQq_nEWX8m8J8g.png)

The martial status value is based on my choice column in SharePoint, and ill like my flow to trigger only when the value is equal to Married(the third selection).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*LsbtFi7vENIMv2eJ5TT7VA.png)

*NB: The third selection is case sensitive, only put in what match was on your SharePoint.Married does not equal married*

4\. Click **“Edit in advanced mode”**, this should show you an expression as shown below. Copy that expression and delete the Do until card.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UUcRhv8FML6WcHTNVK4UMw.png)

5\. Go to your trigger card, click on the ellipsis, and select settings.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I_aQMvxkvCDVXddELcmk7w.png)

Scroll down to Trigger actions, Click on Add, paste the expression that you copied previously, and click on Done.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*p1ak50pD9sCTM76U7xDY0g.png)

Add a new card, probably send an email and test your flow.

But here’s the kicker: this flow will only kick into action if the marital status in your SharePoint is set to “married”. It’s an amazing feature that will help you automate with precision and ease. And if you found this tip helpful, don’t forget to share, subscribe, and turn on notifications for more top-notch Power Platform tricks!